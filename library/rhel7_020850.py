#!/usr/bin/python

# Written By - Jamie Whetsell - glitch@redhat.com

##############################################################################

import grp, pwd, spwd
import os, sys
from pwd import getpwuid

def log(msg):
    logifle = open('/tmp/aaaaaa', 'a')
    logifle.write(msg)
    logifle.write("\n")
    logifle.write("\n")
    logifle.close()

def init_permissions(check):
  # get users
  # loop over users => get home
  # get . files in home and check owner for user or root
  changed=False
  for p in pwd.getpwall():
    user = p[0]
    group = p[4]
    home = p[5]
    can_login = len(spwd.getspnam(user)[1]) > 5
    log("--------------  " + check)

    if can_login:
      # get a list of . files for the user dir
      dirs = os.listdir( home )
      for file in dirs:
        if file.startswith("."):
          if user != getpwuid(os.stat(home + "/" + file).st_gid).pw_name:
            if "root" != os.stat(home + "/" + file).st_gid:
              if check == True:
                changed=False
                #return dict(failed=True, msg="File - {} is not owned by {}".format(home + "/" + file,user))
              else:
                uid = pwd.getpwnam(user).pw_uid
                gid = grp.getgrnam(group).gr_gid
                os.chown(home + "/" + file, uid, gid)
                changed=True

  return changed

def main():
#    print init_permissions(False)

    module = AnsibleModule(
        argument_spec = dict(
            check = dict(default=False,required=False),
        ),
    )

    changed = False

    try:
      changed = init_permissions(module.params.get('check'))
    except Exception as ex:
        module.fail_json(msg=str(ex))

    res_args = dict(
        changed = changed, msg = "OK"
    )

    module.exit_json(**res_args)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
