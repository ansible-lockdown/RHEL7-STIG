# release Stig October 2020

[Version 3, Rel 1 released on Oct 23, 2020](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R1_STIG.zip)

## Whats new

- New auditing tool all controlled via defaults main. run on host using [goss](https://github.com/aelsabbahy/goss)
- Seperate role required (use ansible galaxy with requirements.yml)
- reorder of rules inline with DISA changes
- Amalgamation of OEL rules into RHEL
- Ability to turn FIPS on and off in defaults/main.yml - runs in prelim with set_fact

refer to STIG documentation for specific changes

## High level changes within tasks

- Python3 now default for control node (should be backward compatible in setup)
- Grub password no longer created using passlib needs to be supplied as variable

  - assert has been created if rule still enabled and password not changed

- use of the packages facts module
- ability to set own Ciphers and MACs (defaults to FIPS) - note this can affect logins with grub settings
