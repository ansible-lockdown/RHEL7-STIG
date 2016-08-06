RHEL 7 DISA STIG
================

**This role is still under active development.**

Configure a RHEL 7 system be be DISA STIG compliant. CAT I findings will be correceted and audited by default. CAT II and III findigs can be enabled by setting the appropriate variables to `yes`.

The RHEL 7 STIG is currently in draft form. This role is based on [Version 1, Revision 0.2 released on July 15, 2016](http://iase.disa.mil/stigs/os/unix-linux/Pages/index.aspx).


Requirements
------------

RHEL 7. Other versions are not supported.

Role Variables
--------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `rhel7stig_cat1_audit` | `yes` | Audit for CAT I findings      |
| `rhel7stig_cat2_audit` | `no`  | Audit for CAT II findings     |
| `rhel7stig_cat3_audit` | `no`  | Audit for CAT III findings    |
| `rhel7stig_cat1_patch` | `yes` | Correct CAT I findings        |
| `rhel7stig_cat2_patch` | `no`  | Correct CAT II findings       |
| `rhel7stig_cat3_patch` | `no`  | Correct CAT III findings      |
| `rhel7stig_gui` | `no` | Whether or not to run tasks related to auditing/patching the desktop environment |
| `rhel7stig_av_package` | `no` | Anti-virus package(s) to install and service to start and enable. |
| `rhel7stig_lftpd_required` | `no` | If set to `no`, remove `lftpd`. |
| `rhel7stig_tftp_required` | `no` | If set to `no`, remove `tftp` client and server packages. |
| `rhel7stig_snmp_community` | `Endgam3Ladyb0g` | SNMP community string that will replace `public` and `private` in `snmpd.conf`. |
| `rhel7stig_bootloader_password` | `Boot1tUp!` | GRUB2 bootloader password. This should be stored in an Anisble Vault. |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: rhel7-stig, when: "ansible_os_family == 'RedHat' and ansible_os_major_verision == 7"}

License
-------

MIT
