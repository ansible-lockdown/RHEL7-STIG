RHEL 7 DISA STIG
================




Requirements
------------

RHEL 7. Other versions are not supported.

Role Variables
--------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `rhel7stig_cat1_patch` | True | Correct CAT I findings |
| `rhel7stig_cat2_patch` | False | Correct CAT II findings |
| `rhel7stig_cat3_patch` | False | Correct CAT III findings |

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
