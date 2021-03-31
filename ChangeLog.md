# release Stig Jan 2021

[Version 3, Rel 2 released on Jan 22, 2021](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R2_STIG.zip)

## Whats new

- New auditing tool all controlled via defaults main. run on host using [goss](https://github.com/aelsabbahy/goss)
- default variables also set the audit steps if run from ansible.
- Seperate role required (use ansible galaxy with requirements.yml)
- reorder of rules inline with DISA changes
- Amalgamation of OEL rules into RHEL
- Ability to turn FIPS on and off in defaults/main.yml - runs in prelim with set_fact
- If Python3 installed adds the epel repo to install python-rpm and then disables the repo after installing
- Adding of the goss module to the library path
- deprecation warnings should be cleared

refer to STIG documentation for specific changes

## Whats new in Release 1.0.1
- renamed goss.yml to goss.py and aligned ansible.cfg
  - thanks to Thulium-Drake

## High level changes within tasks

- Python 2 & 3 (preferred) working an setup for control node and host
- Grub password no longer created using passlib needs to be supplied as variable

  - assert has been created if rule still enabled and password not changed

- use of the packages facts module
- ability to set own Ciphers and MACs (defaults to FIPS) - note this can affect logins with grub settings
- Oracle Enterprise Linux - whilst other versions have specific OEL controls. With the latest release there more controlled contained in RHEL. These contain all OEL requirements too.

