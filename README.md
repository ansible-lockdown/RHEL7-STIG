RHEL 7 DISA STIG
================

[![pipeline status](https://gitlab.com/mindpointgroup/lockdown-enterprise/rhel-7-stig/badges/master/pipeline.svg)](https://gitlab.com/mindpointgroup/lockdown-enterprise/rhel-7-stig/commits/master)

Configure a RHEL 7 system to be DISA STIG compliant. All findings will be audited by default. Non-disruptive CAT I, CAT II, and CAT III findings will be corrected by default. Disruptive finding remediation can be enabled by setting `rhel7stig_disruption_high` to `yes`.

This role is based on RHEL 7 DISA STIG: [Version 3, Rel 1 released on Oct 23, 2020](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R1_STIG.zip).

Updating
--------

Coming from a previous release.

As with all releases and updates, It is suggested to test and align controls.
This contains rewrites and ID reference changes as per STIG documentation.

- The password hash
  - If adopting grub password has to be supplied and variables updated.
  - It no longer tries to create the hash.

More information can be found in the [ChangeLog](./ChangeLog.md)

Auditing (new)
--------------

This can be turned on or off within the defaults/main.yml file. False by default refer to wiki for more details.

This is much quicker, very lightweight, checking (where possible) config compliance and live/running settings.

A new form of auditing has been develeoped, by using a small (12MB) go binary called [goss](https://github.com/aelsabbahy/goss) along with the relevant configurations to check. Without the need for infrastructure or other tooling.
This audit will not only check the config has the correct setting but aims to capture if it is running with that configuration also trying to remove [false positives](https://www.mindpointgroup.com/blog/is-compliance-scanning-still-relevant/) in the process.

Refer to [RHEL7-STIG-Audit](http://https://github.com/ansible-lockdown/RHEL7-STIG-Audit).

Requirements
------------

RHEL 7 or CentOS 7 - Other versions are not supported.
Access to download or add the goss binary and content to the system if using auditing. options are available on how to get the content to the system.

Dependencies
------------

- Python3
- Ansible 2.9+

Ansible is set to run in a python3 environment.

Dependencies required for the playbook are installed on the endpoint if required.

Role Variables
--------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `rhel7stig_cat1_patch` | `yes` | Correct CAT I findings        |
| `rhel7stig_cat2_patch` | `yes`  | Correct CAT II findings       |
| `rhel7stig_cat3_patch` | `yes`  | Correct CAT III findings      |
| `rhel_07_######` | [see defaults/main.yml](./defaults/main.yml)  | Individual variables to enable/disable each STIG ID. |
| `rhel7stig_gui` | `no` | Whether or not to run tasks related to auditing/patching the desktop environment |
| `rhel7stig_system_is_router` | `no` | Run tasks that disable router functions. |
| `rhel7stig_antivirus_required` | `no` | Run tasks related to Anit-Virus package installation. |
| `rhel7stig_av_package` | [see defaults/main.yml](./defaults/main.yml) | Anti-virus package(s) to install and service to start and enable. |
| `rhel7stig_time_service` | `chronyd` | Set to `ntpd` or `chronyd`. |
| `rhel7stig_time_service_configs` | [see defaults/main.yml](./defaults/main.yml) | Time service packages and service configs. |
| `rhel7stig_firewall_service` | `firewalld` | Set to `firewalld` or `iptables`. |
| `rhel7stig_vsftpd_required` | `no` | If set to `no`, remove `vsftpd`. |
| `rhel7stig_tftp_required` | `no` | If set to `no`, remove `tftp` client and server packages. |
| `rhel7stig_autofs_required` | `no` | If set to `no`, disable `autofs` service. |
| `rhel7stig_kdump_required` | `no` | If set to `no`, disable `kdump` service. |
| `rhel7stig_snmp_community` | `Endgam3Ladyb0g` | SNMP community string that will replace `public` and `private` in `snmpd.conf`. |
| `rhel7stig_bootloader_password_hash` | `grub.pbkdf2.sha512.changethispassword` | GRUB2 bootloader password hash. This should be the hash and stored in an Ansible Vault |
| `rhel7stig_boot_superuser` | `root` | Used to set the boot superuser in the GRUB2 config. |
| `rhel7stig_aide_cron` | [see defaults/main.yml](./defaults/main.yml) | AIDE Cron settings |
| `rhel7stig_maxlogins` | `10` | Set maximum number of simultaneous system logins (RHEL-07-040000) |
| `rhel7stig_logon_banner` | [see defaults/main.yml](./defaults/main.yml) | Logon banner displayed when logging in to the system. Defaults to nicely formatted standard logon banner. |
| `rhel7stig_password_complexity` | see below for specific settings | Dictionary of password complexity settings |
| `rhel7stig_password_complexity.ucredit` | `-1` | Minimum number of upper-case characters to be set in a new password - expressed as a negative number.  |
| `rhel7stig_password_complexity.lcredit` | `-1` | Minimum number of lower-case characters to be set in a new password - expressed as a negative number.  |
| `rhel7stig_password_complexity.dcredit` | `-1` | Minimum number of numeric characters to be set in a new password - expressed as a negative number.  |
| `rhel7stig_password_complexity.ocredit` | `-1` | Minimum number of special characters to be set in a new password - expressed as a negative number.  |
| `rhel7stig_password_complexity.difok` | `8` | Minimum number of characters in new password that must not be present in the old password.  |
| `rhel7stig_password_complexity.minclass` | `4` | Minimum number of required classes of characters for the new password. (digits, upper, lower, other)  |
| `rhel7stig_password_complexity.maxrepeat` | `3` | Maximum number of allowed same consecutive characters in a new password. |
| `rhel7stig_password_complexity.maxclassrepeat` | `4` | Maximum number of allowed same consecutive characters in the same **class** in the new password. |
| `rhel7stig_password_complexity.minlen` | `15` | Minimum number of characters in a new password. |
| `rhel7stig_shell_session_timeout` | `file: /etc/profile` `timeout: 600` | Dictionary of session timeout setting and file (TMOUT setting can be set in multiple files) |

Example Playbook
----------------

- hosts: servers
  roles:
  - role: rhel-7-stig
  when:
  - ansible_os_family == 'RedHat'
  - ansible_distribution_major_version | version_compare('7', '=')

Example Audit Summary
---------------------

This is based on a vagrant image with selections enabled. e.g. No Gui or firewall.
Note: More tests are run during audit as we check config and running state.

```sh
ok: [rhel7test] => {
    "msg": [
        "The pre remediation results are: Count: 308, Failed: 156, Duration: 44.108s.",
        "The post remediation results are: Count: 308, Failed: 14, Duration: 37.647s.",
        "Full breakdown can be found in /var/tmp",
        ""
    ]
}
  ]
}
PLAY RECAP ****************************************************************************************************************
rhel7test         : ok=369  changed=192  unreachable=0  failed=0  skipped=125  rescued=0  ignored=0  
```
