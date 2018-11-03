#!/usr/bin/env python
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
"""Generate deployer notes placeholders from STIG XCCDF"""
import os

try:
    from elementtree.ElementTree import parse, XMLParser
except ImportError:
    from xml.etree.ElementTree import parse, XMLParser


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NOTE_OUTPUT_DIR = "{}/{}".format(SCRIPT_DIR, "rhel7")
XCCDF_FILE = 'U_Red_Hat_Enterprise_Linux_7_STIG_V2R1_Manual-xccdf.xml'
XCCDF_NAMESPACE = "{http://checklists.nist.gov/xccdf/1.1}"


def main():
    with open('{}/{}'.format(SCRIPT_DIR, XCCDF_FILE), 'r') as f:
        tree = parse(f)

    if not os.path.isdir(NOTE_OUTPUT_DIR):
        os.makedirs(NOTE_OUTPUT_DIR)

    for group_element in tree.findall(".//{}Group".format(XCCDF_NAMESPACE)):
        rule_element = group_element.find("{}Rule".format(XCCDF_NAMESPACE))

        # Build a dictionary with all of our rule data.
        rule = {
            'id': group_element.attrib['id'],
            'version': rule_element.find("{}version".format(XCCDF_NAMESPACE)).text,
            'title': rule_element.find("{}title".format(XCCDF_NAMESPACE)).text,
        }

        file_path = "{}/{}.rst".format(NOTE_OUTPUT_DIR, rule['id'])

        # Skip this rule if the file already exists
        if os.path.isfile(file_path):
            continue

        front_matter = "---\nid: {0}\nstig_id: {1}\nstatus: {2}\ntag: {3}\n---\n".format(rule['id'], rule['version'], "none", "misc")
        body_content = "\n{}\n".format(rule['title'])

        with open(file_path, 'wb') as f:
            f.write(front_matter.encode('utf-8'))
            f.write(body_content.encode('utf-8'))

if __name__ == '__main__':
    main()
