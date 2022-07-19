# Changelog

## Release 1.6.0
- Update to STIG v3r7 Apr 27th 2022
- Removed unnecessary local.yml

## Release 1.3.3

- update to STIG v3r6 Jan 27th 2022
- update to rules for all listed
- migrated auditd conf to template - handlers added
- udpated audit components

### Cat 1

- 010291 - new control

### Cat 2

- RHEL-07-010190
- RHEL-07-010310 - change in value
- RHEL-08-010339 - new control
- RHEL-07-010342
- RHEL-07-010343
- RHEL-07-010344 - new control
- RHEL-07-020023
- RHEL-07-020029 - new control

## AUDITD rules

- RHEL-07-030360
- RHEL-07-030370 - merged 030380 030390 030400
- RHEL-07-030410 - merged 030420 030430
- RHEL-07-030440 - merged 030450 030460 030470 030480 030490
- RHEL-07-030510 - merged 030500 030520 030530 030540 030550
- RHEL-07-030560
- RHEL-07-030570
- RHEL-07-030580
- RHEL-07-030590
- RHEL-07-030610
- RHEL-07-030620
- RHEL-07-030630
- RHEL-07-030640
- RHEL-07-030650
- RHEL-07-030660
- RHEL-07-030670
- RHEL-07-030680
- RHEL-07-030690
- RHEL-07-030700
- RHEL-07-030710
- RHEL-07-030720
- RHEL-07-030740
- RHEL-07-030750
- RHEL-07-030760
- RHEL-07-030770
- RHEL-07-030780
- RHEL-07-030800
- RHEL-07-030810
- RHEL-07-030819
- RHEL-07-030820 merged 030821
- RHEL-07-030830
- RHEL-07-030840
- RHEL-07-030870
- RHEL-07-030871
- RHEL-07-030872
- RHEL-07-030873
- RHEL-07-030874
- RHEL-07-030910 merged 030880 030890 030900 030920

### Cat 3

## Release 1.3.2

issues fixed:

- #385 - efi path fix - Thanks to danbarr
- #386 - meta/main.yml typo correction - Thanks to Yeroc

## Release 1.3.1

### Whats new in 1.3.1

- issue templates and PR templates

## Release 1.3.0

### Release STIG Version

[Version 3, Rel 4 released on Jul 23, 2021](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R4_STIG.zip)

### What's new 1.3

- Updated to match Version 3 release 4 benchmarks from Jul 2021
- Refined controls to use package_facts to shorten blocks

## Release 1.2.0

### Release STIG Version 3.3

[Version 3, Rel 3 released on Jan 22, 2021](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R3_STIG.zip)

### What's new in 1.2

- Updated tags on each control with more control data (Vul ID, CCI, Group Title, and Rule ID)
- Updated to match Version 3 Release 3 benchmarks from Apr 2021
- Audit controls standardised
- optional reboot added - default no reboot

## Release 1.1.1

### release Stig Jan 2021

[Version 3, Rel 2 released on Jan 22, 2021](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R2_STIG.zip)

## Whats new

- New auditing tool all controlled via defaults main. run on host using [goss](https://github.com/aelsabbahy/goss)
- default variables also set the audit steps if run from ansible.
  - Seperate role required (use ansible galaxy with requirements.yml)
- Python 2 & 3 (preferred) working an setup for control node and host
- Grub password no longer created using passlib needs to be supplied as variable
- reorder of rules inline with DISA changes
- Amalgamation of OEL rules into RHEL
- Ability to turn FIPS on and off in defaults/main.yml - runs in prelim with set_fact
- If Python3 installed adds the epel repo to install python-rpm and then disables the repo after installing
- Adding of the goss module to the library path
- deprecation warnings should be cleared
  - assert has been created if rule still enabled and password not changed
- use of the packages facts module
- ability to set own Ciphers and MACs (defaults to FIPS) - note this can affect logins with grub settings
- Oracle Enterprise Linux - whilst other versions have specific OEL controls. With the latest release there more controlled contained in RHEL. These contain all OEL requirements too.

refer to STIG documentation for specific changes

## Release 1.0.2

- #351 create_home from true to yes
- #353 Tidy up and rework of RHEL-07-21350 - rhel7stig_use_fips default vars set to true. Will change fips=0 in /etc/default/grub if true and extra vars passed
- General lint and control tidy up.

## Release 1.0.1

- renamed goss.yml to goss.py and aligned ansible.cfg
  - thanks to Thulium-Drake
