#!/usr/bin/python

# Written By - Jamie Whetsell - glitch@redhat.com

##############################################################################

DOCUMENTATION = '''
---
module: init_files
short_description: Checks or fixes where it can stigs related to init files
description:
    - Checks or fixes where it can stigs related to init files
author:
    - "James Whetsell (@zer0glitch)"
options:
  check:
    description:
      - when set to true will not make file changes
    required: false
  users:
    description:
      - fix user on files
    required: false
  groups:
    description:
      - fix group on files
    required: false
  permissions:
    description:
      - fix permissions on files
    required: false
  paths:
    description:
      - Validate paths of files
    required: false
'''

EXAMPLES = '''

- name: "MEDIUM | RHEL-07-020840 | PATCH | All local initialization files for interactive users must be owned by the home directory user or root."
  init_files: check=True user=True

- name: "MEDIUM | RHEL-07-020850 | PATCH | Local initialization files for local interactive users must be group-owned by the users primary group or root."
  init_files: check=True group=True

- name: "MEDIUM | RHEL-07-020860 | PATCH | All local initialization files must have mode 0740 or less permissive."
  init_files: check=True permissions=True

- name: "MEDIUM | RHEL-07-020870 | PATCH | All local interactive user initialization files executable search paths must contain only absolute paths."
  init_files: check=True paths=True
'''

RETURNS = '''
output:
  description: List of files that are changed, or need to be changed
'''

import grp, pwd, spwd
import os, sys
from pwd import getpwuid
from stat import *



class init_files:

  def fix_user(self, check, user, group, file_owner, file_group,  file):

    if (user == file_owner) or ("root" == file_owner):
      self.changed=False
    else:
      if check == True:
        self.mod_fail=True
        self.changes.append("{} has the wrong user {} should be {}.".format(file, file_owner, user))
        self.changed = False
      else:
        self.changes.append("{} has the wrong user {} should be {}.".format(file, file_owner, user))
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(file_group).gr_gid
        os.chown(file, uid, gid)
        self.changed=True

  def fix_group(self, check, user, group, file_owner, file_group,  file):

    if (user == file_group) or ("root" == file_group):
      self.changed=False
    else:
      if check == True:
        self.changes.append("{} has the wrong group {} should be {}.".format(file, file_group, group))
        self.mod_fail=True
      else:
        self.changes.append("{} has the wrong group {} should be {}.".format(file, file_group, group))
        uid = pwd.getpwnam(file_owner).pw_uid
        gid = grp.getgrnam(group).gr_gid
        os.chown(file, uid, gid)
        self.changed=True

  def fix_permissions(self, check, user, group, file_owner, file_group,  file):

    oct_mode = oct(os.stat(file).st_mode)

    user_mode=int(oct_mode[4])
    group_mode=int(oct_mode[5])
    world_mode=int(oct_mode[6])

    if (group_mode > 4) or (world_mode > 0):
      if check == True:
        self.changes.append("{} has the wrong permissions.".format(file))
        self.mod_fail=True
      else:
        self.changes.append("Fixing permission on {}.".format(file))
        if group_mode > 4:
          group_mode = 4

        mode = "0{}{}{}".format(user_mode,group_mode,0)

        os.chmod(file, eval(mode))
        self.changed=True
    else:
      self.changed=False

  def check_paths(self, check_file, home):

    file_d = open(check_file, "r")

    content = file_d.readlines()

    for line in content:
      if "PATH" in line and "=" in line:
        newline = line.replace("$HOME", home + "/")
        paths = newline.split(":")
        for path in paths :
          if path.startswith("/"):
            if not os.path.abspath(path).startswith(home):
              self.mod_fail=True
              self.changes.append("{} contains an executable path outside the home directory".format(check_file))

    file_d.close()

  def __init__(self, check, users, groups, permissions, files):

    self.check = check
    self.users = users
    self.groups = groups
    self.permissions = permissions
    self.files = files
    self.mod_fail=False
    self.changes=[]
    self.changed=False


  def execute(self, check, users, groups, permissions, files):

    for p in pwd.getpwall():
      user = p[0]
      group = p[4]
      home = p[5]
      can_login = len(spwd.getspnam(user)[1]) > 5
      returnVal = dict(msg="OK")

      if can_login:
        # get a list of . files for the user dir
        dirs = os.listdir( home )
        for file_name in dirs:
          if file_name.startswith("."):
            init_file =  home + "/" + file_name
            file_owner = getpwuid(os.stat(init_file).st_uid).pw_name
            file_group = getpwuid(os.stat(init_file).st_gid).pw_name

            is_file = os.path.isfile(init_file)

            if (users == True) and (is_file):
              self.fix_user(check, user, group, file_owner, file_group, init_file)

            if (groups == True) and (is_file):
              self.fix_group(check, user, group, file_owner, file_group, init_file)

            if (permissions == True) and (is_file):
              self.fix_permissions(check, user, group, file_owner, file_group, init_file)

            if (files and is_file):
              self.check_paths(init_file, home)

    return self.changes

def main():
#    play = init_files(False, False, False, False, True)

    module = AnsibleModule(
        argument_spec = dict(
            check = dict(default=False,required=False),
            user = dict(default=False,required=False),
            group = dict(default=False,required=False),
            permissions = dict(default=False,required=False),
            paths = dict(default=False,required=False),
        ),
    )

    play = init_files(module.params.get('check'), module.params.get("user"), module.params.get("group"), module.params.get("permissions"), module.params.get("paths"))
    try:

      play.execute(module.params.get('check'), module.params.get("user"), module.params.get("group"), module.params.get("permissions"), module.params.get("paths"))

    except Exception as ex:
        module.fail_json(msg=str(ex))

    #res_args = dict(
       #changed = play.changed, msg = play.changes, failed=play.mod_fail
    #)

    if play.mod_fail:
      res_args = dict(success=False, changed=play.changed, changes=play.changes, msg=play.changes)
      module.fail_json(**res_args)
      return
    else:
      res_args = dict(success=True, changed=play.changed, changes=play.changes, msg=play.changes)
      module.exit_json(**res_args)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
