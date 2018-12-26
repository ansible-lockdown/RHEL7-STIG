#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016, Rackspace US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Build documentation from Benchmark files and Ansible tasks."""
from __future__ import print_function, unicode_literals
import os
import re
import glob

from collections import defaultdict

import jinja2
import yaml

try:
    from elementtree.ElementTree import parse, XMLParser, fromstring
except ImportError:
    from xml.etree.ElementTree import parse, XMLParser, fromstring

DOC_SOURCE_DIR = "{0}/..".format(os.path.dirname(os.path.abspath(__file__)))


def split_at_linelen(line, length):
    """Split a line at specific length for code blocks or 
       other formatted RST sections.
    """
    # Get number of splits we should have in line
    i = int(len(line)/length)
    p = 0

    while i > 0:
        p = p+length
        # If position in string is not a space
        # walk backwards until we hit a space
        while line[p] != ' ':
            p -= 1

        # Split the line
        line = line[:p] + '\n' + line[p+1:]
        i -= 1

    return line


def add_monospace(text):
    """Add monospace formatting to RST."""
    paragraphs = text.split('\n\n')

    for key, value in enumerate(paragraphs):

        # Replace all quotes "" with backticks `` for monospacing
        paragraphs[key] = re.sub(u'\u201c(.*?)\u201d',
                                 r'``\1``',
                                 value)

        # If our paragraph starts with a " and it wasn't handled
        # by the backtick substitution it probably means it
        # does not end with a " and is a special block of text
        if value.startswith('"'):
            paragraphs[key] = '.. code-block:: text\n\n    ' + '\n    '.join(split_at_linelen(value.lstrip('"'), 66).split('\n'))

            i = key+1

            # Loop through all the following paragraphs to format
            # and look for the last one
            while i < len(paragraphs):
                last_line = paragraphs[i].endswith('"')
                # Indent this paragraph
                paragraphs[i] = '    ' + '\n    '.join(split_at_linelen(paragraphs[i].rstrip('"'), 66).split('\n'))

                i += 1
                # Break the loop if we found the last paragraph
                if last_line:
                    break

        # If our paragraph ends with a colon and the next line isn't a special
        # note, let's make sure the next paragraph is monospaced.
        # if value.endswith(":"):

        #     if paragraphs[key + 1].startswith('Note:'):

        #         # Indent the paragraph AFTER the note.
        #         paragraphs[key + 2] = '::\n\n    ' + '\n    '.join(
        #             paragraphs[key + 2].split('\n')
        #         )

        #     else:
        #         # Ensure the paragraph ends with double colon (::).
        #         # paragraphs[key] = re.sub(r':$', '::', value)

        #         # Indent the next paragraph.
        #         paragraphs[key + 1] = '::\n\n    ' + '\n    '.join(
        #             paragraphs[key + 1].split('\n')
        #         )

        # If we found a note in the description, let's format it like a note.
        if value.startswith('Note:'):
            paragraphs[key] = ".. note::\n\n    {0}".format(value[6:])

        # If we have a line that starts with a pound sign, this probably needs
        # to be pre-formatted as well.
        if value.startswith('#'):
            paragraphs[key] = '::\n\n    ' + '\n    '.join(value.split('\n'))

        # If there's a command on a line by itself, we probably need to merge
        # it with the next line. The STIG has terrible formatting in some
        # places.
        monospace_strings = ['grep', 'more']
        if (
            key + 1 < len(paragraphs) and
            any(x in value for x in monospace_strings) and
            '\n' not in value and
            not paragraphs[key + 1].startswith('Password')
        ):
            value = "{0}\n{1}".format(
                value,
                '\n    '.join(paragraphs[key + 1].split('\n'))
            )
            del(paragraphs[key + 1])

    return '\n\n'.join(paragraphs)


def get_deployer_notes(path, stig_id):
    """Read deployer notes based on the Benchmark ID."""
    filename = "{0}/{1}.rst".format(path, stig_id)

    # Does this deployer note exist?
    if not os.path.isfile(filename):
        return 'Nothing to report\n'

    # Read the note and parse it with YAML
    with open(filename, 'r') as f:
        rst_file = f.read()

    return rst_file


def read_xml(path, filename):
    """Read XCCDF XML file and parse it into an etree."""
    with open("{0}/{1}".format(path, filename), 'r') as f:
        tree = parse(f)
    return tree


def render_all(jinja_env, stig_ids, all_rules):
    """Generate documentation RST for each STIG configuration."""
    template = jinja_env.get_template('template_all.j2')
    return template.render(
        stig_ids=stig_ids,
        all_rules=all_rules,
    )


def render_doc(jinja_env, stig_rule, deployer_notes):
    """Generate documentation RST for each STIG configuration."""
    template = jinja_env.get_template('template_doc.j2')
    return template.render(
        rule=stig_rule,
        notes=deployer_notes
    )


def render_toc(jinja_env, toc_type, stig_dict, all_rules, sort_order):
    """Generate documentation RST for each STIG configuration."""
    template = jinja_env.get_template('template_toc.j2')
    sorted_stig_items = sorted(stig_dict.items(), key=lambda t: sort_order.get(t[0]))
    return template.render(
        toc_type=toc_type,
        stig_items=sorted_stig_items,
        all_rules=all_rules,
    )

def write_file(filename, content):
    """Write contents to files."""
    file_path = "{0}/{1}".format(DOC_SOURCE_DIR, filename)

    if not os.path.isdir(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'wb') as f:
        f.write(content.encode('utf-8'))

    return True

def parse_ansible_tasks(path, filenames, with_items=[]):
    """Read and parse Ansible task files"""
    tasks = defaultdict(list)
    yaml_content = list()

    for fn in filenames:
        with open("{0}/tasks/{1}".format(path, fn), 'r') as stream:
            yaml_content += yaml.load(stream)

    for item in yaml_content:
        if item.get('name'):
            name_content = item['name'].rstrip('\n').lstrip('\n').split('\n')

            for k in name_content:
                item_id = k.split(' | ')[1]
                # see if this tasks includes some other tasks
                include = item.get('include_tasks')
                if include:
                    inc_tasks = parse_ansible_tasks(path, [include], with_items=item.get('with_items', []))
                    tasks.update(inc_tasks)
                elif item_id.endswith("{{ item.id }}"):
                    for i in with_items:
                        tasks[item_id.replace("{{ item.id }}", i['id'])].append(item)
                else:
                    tasks[item_id].append(item)

    return tasks


def generate_docs(app, config):
    """The main function."""
    metadata_dir = "{0}/{1}".format(DOC_SOURCE_DIR, config.stig_metadata_dir)
    ansible_dir = "{0}/{1}".format(DOC_SOURCE_DIR, config.stig_ansible_dir)
    ansible_task_filenames = config.stig_ansible_task_filenames
    xccdf_file = config.stig_xccdf_file
    xccdf_namespace = config.stig_xccdf_namespace
    control_statuses = config.stig_control_statuses
    control_statuses_order = config.stig_control_statuses_order
    control_severities = config.stig_control_severities

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(metadata_dir),
        trim_blocks=True,
        keep_trailing_newline=False,
    )
    jinja_env.filters['addmonospace'] = add_monospace

    tree = read_xml(metadata_dir, xccdf_file)

    # Read in control implementations from Ansible task files
    tasks = parse_ansible_tasks(ansible_dir, ansible_task_filenames)

    # Create a simple list to capture all of the STIGs
    stig_ids = []

    # Create defaultdicts to hold information to build our table of
    # contents files for sphinx.
    all_rules = defaultdict(list)

    # Prepopulate with control severities
    severity = defaultdict(list)
    [severity[s] for s in control_severities]

    # Prepopulate possible control statuses
    status = defaultdict(list)
    [status[v] for k, v in control_statuses.items() if k != 'missing']

    # Loop through the groups and extract rules
    group_elements = tree.findall(".//{}Group".format(xccdf_namespace))
    for group_element in group_elements:
        rule_element = group_element.find("{}Rule".format(xccdf_namespace))

        # Build a dictionary with all of our rule data.
        rule = {
            'id': rule_element.find("{}version".format(xccdf_namespace)).text,
            'vuln_id': group_element.attrib['id'],
            'title': rule_element.find("{}title".format(xccdf_namespace)).text,
            'severity': rule_element.attrib['severity'],
            'fix': rule_element.find("{}fixtext".format(xccdf_namespace)).text,
            'check': rule_element.find("{0}check/{0}check-content".format(xccdf_namespace)).text,
            'ident': [x.text for x in rule_element.findall("{}ident".format(xccdf_namespace))],
        }

        rule_tasks = tasks[rule['id']]
        rule['status'] = control_statuses['default']
        rule['vars'] = []
        rule['tags'] = []

        if not rule_tasks:
            rule['status'] = control_statuses['missing']

        for item in rule_tasks:
            tags = item.get('tags')
            conditionals = item.get('when')

            # All controls have an on/off var named after the STIG ID in form
            # rhel_07_###### so we add that here without relying on parser.
            # rule['vars'].append({'key': rule['id'].lower().replace('-','_'), 'value': 'true'})
            if conditionals is None:
                rule['vars'].append(rule['id'].lower().replace('-','_'))
            else:
                if type(conditionals) is str:
                    conditionals = [conditionals]

                for c in conditionals:
                    rule['vars'].append(c)
            
            # Implementation status parsing
            for key, value in control_statuses.items():
                if key in str(item.get('when')):
                    rule['status'] = value

            # Grab the tags
            if tags:
                rule['tags'] = tags
                # Check if notimplemented is in tags and update status
                if 'notimplemented' in tags:
                    rule['status'] = control_statuses['missing']

        # The description has badly formed XML in it, so we need to hack it up
        # and turn those tags into a dictionary.
        description = rule_element.find("{}description".format(xccdf_namespace)).text
        parser = XMLParser()
        temp = fromstring("<root>{0}</root>".format(description), parser)
        rule['description'] = {x.tag: x.text for x in temp.iter()}

        # Get the deployer notes
        deployer_notes = get_deployer_notes(metadata_dir + '/notes', rule['id'])
        rule['deployer_notes'] = deployer_notes

        all_rules[rule['id']] = rule
        stig_ids.append(rule['id'])
        severity[rule['severity']].append(rule['id'])
        status[rule['status']].append(rule['id'])

    sev_sort_order = {s: i for i, s in enumerate(control_severities)}
    status_sort_order = {s: i for i, s in enumerate(control_statuses_order)}

    all_toc = render_all(jinja_env, stig_ids, all_rules)
    severity_toc = render_toc(jinja_env, 'severity', severity, all_rules, sev_sort_order)
    status_toc = render_toc(jinja_env, 'status', status, all_rules, status_sort_order)

    write_file("auto_controls-all.rst", all_toc)
    write_file("auto_controls-by-severity.rst", severity_toc)
    write_file("auto_controls-by-status.rst", status_toc)


def setup(app):
    """Set up the Sphinx extension."""
    app.add_config_value('stig_metadata_dir', 'metadata', 'html')
    app.add_config_value('stig_ansible_dir', '../', 'html')
    app.add_config_value('stig_ansible_task_filenames', list(), 'html')
    app.add_config_value('stig_xccdf_file', '', 'html')
    app.add_config_value('stig_xccdf_namespace', "", 'html')
    app.add_config_value('stig_control_statuses', dict(), 'html')
    app.add_config_value('stig_control_statuses_order', list(), 'html')
    app.add_config_value('stig_control_severities', list(), 'html')

    print("Generating Role documentation...")
    app.connect('config-inited', generate_docs)

    return {'version': '0.1'}
