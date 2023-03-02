# RHEL 7 DISA STIG

![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL7-STIG/CommunityToDevel?label=Devel%20Build%20Status&style=plastic)
![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL7-STIG/DevelToMain?label=Main%20Build%20Status&style=plastic)
![Release](https://img.shields.io/github/v/release/ansible-lockdown/RHEL7-STIG?style=plastic)

Configure a RHEL 7 system to be DISA STIG compliant. All findings will be audited by default. Non-disruptive CAT I, CAT II, and CAT III findings will be corrected by default. Disruptive finding remediation can be enabled by setting `rhel7stig_disruption_high` to `yes`.

This role is based on RHEL 7 DISA STIG: [Version 3, Rel 10 released on Jan 26, 2023](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_7_V3R10_STIG.zip).

## Join us

On our [Discord Server](https://discord.io/ansible-lockdown) to ask questions, discuss features, or just chat with other Ansible-Lockdown users

## Updating

Coming from a previous release.

As with all releases and updates, It is suggested to test and align controls.
This contains rewrites and ID reference changes as per STIG documentation.

- The password hash
  - If adopting grub password has to be supplied and variables updated.
  - It no longer tries to create the hash.

More information can be found in the [ChangeLog](./ChangeLog.md)

## Auditing (new)

This can be turned on or off within the defaults/main.yml file with the variable rhel7stig_run_audit. The value is false by default, please refer to the wiki for more details.

This is a much quicker, very lightweight, checking (where possible) config compliance and live/running settings.

A new form of auditing has been develeoped, by using a small (12MB) go binary called [goss](https://github.com/aelsabbahy/goss) along with the relevant configurations to check. Without the need for infrastructure or other tooling.
This audit will not only check the config has the correct setting but aims to capture if it is running with that configuration also trying to remove [false positives](https://www.mindpointgroup.com/blog/is-compliance-scanning-still-relevant/) in the process.

Refer to

- [RHEL7-STIG-Audit](https://github.com/ansible-lockdown/RHEL7-STIG-Audit).

## Requirements

RHEL 7 or CentOS 7 - Other versions are not supported.
Access to download or add the goss binary and content to the system if using auditing. options are available on how to get the content to the system.

**General:**

- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible

  - [Main Ansible documentation page](https://docs.ansible.com)
  - [Ansible Getting Started](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
  - [Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
  - [Ansible Community Info](https://docs.ansible.com/ansible/latest/community/index.html)
- Functioning Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, needed packages installed, and infrastructure setup.
- Please read through the tasks in this role to gain an understanding of what each control is doing. Some of the tasks are disruptive and can have unintended consiquences in a live production system. Also familiarize yourself with the variables in the defaults/main.yml file or the [Main Variables Wiki Page](https://github.com/ansible-lockdown/RHEL7-STIG/wiki/Main-Variables).
- While check_mode may work, This is not supported.

### Please be aware

- This does set the single user password for grub this does need to be defined - You can create the hash on a RHEL 7.9 system using the command 'grub2-mkpasswd-pbkdf2'
- Some controls make changes to sudo, please ensure a sudo password is set for the user and it is added to the way to run your playbook.

## Documentation

- [Repo GitHub Page](https://ansible-lockdown.github.io/RHEL7-STIG/)
- [Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown)
- [Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise)
- [Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration)
- [Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise)
- [Wiki](https://github.com/ansible-lockdown/RHEL7-STIG/wiki)

## Dependencies

- Python3 (preferred)
- Ansible 2.9+
- jmespath

Ansible is set to run in a python3 environment.

Dependencies required for the playbook are installed on the endpoint if required.

## Role Variables

This role is designed that the end user should not have to edit the tasks themselves. All customizing should be done via the defaults/main.yml file or with extra vars within the project, job, workflow, etc. These variables can be found [here](https://github.com/ansible-lockdown/RHEL7-STIG/wiki/Main-Variables) in the Main Variables Wiki page. All variables are listed there along with descriptions.

## Tags

There are many tags available for added control precision. Each control has it's own set of tags noting the control number as well as what parts of the system that control addresses.

Below is an example of the tag section from a control within this role. Using this example if you set your run to skip all controls with the tag ssh, this task will be skipped. The
opposite can also happen where you run only controls tagged with ssh.

```sh
tags:
    - RHEL-07-010050
    - ssh
    - dod_logon_banner
```

## Example Audit Summary

This is based on a vagrant image with selections enabled. e.g. No Gui iptables firewall

Note: More tests are run during audit as we check config and running state.

```sh
ok: [cent7_bios] => {
    "msg": [
        "The pre remediation results are: Count: 505, Failed: 214, Duration: 14.808s.",
        "The post remediation results are: Count: 505, Failed: 34, Duration: 43.593s.",
        "Full breakdown can be found in /opt",
        ""
    ]
}
  ]
}
PLAY RECAP ****************************************************************************************************************
rhel7test         : ok=369  changed=192  unreachable=0  failed=0  skipped=125  rescued=0  ignored=0  
```

## Branches

- **devel** - This is the default branch and the working development branch. Community pull requests will pull into this branch
- **main** - This is the release branch
- **reports** - This is a protected branch for our scoring reports, no code should ever go here
- **gh_pages** - github pages
- **all other branches** - Individual community member branches

## Community Contribution

We encourage you (the community) to contribute to this role. Please read the rules below.

- Your work is done in your own individual branch. Make sure to Signed-off and GPG sign all commits you intend to merge.
- All community Pull Requests are pulled into the devel branch
- Pull Requests into devel will confirm your commits have a GPG signature, Signed-off, and a functional test before being approved
- Once your changes are merged and a more detailed review is complete, an authorized member will merge your changes into the main branch for a new release.

## Pipeline Testing

uses:

- Ansible-core 2.12
- Ansible collections - pulls in the latest version based on requirements file
- Runs the audit using the devel branch
- This is an automated test that occurs on pull requests into devel

## Support

This is a community project at its core and will be managed as such.

If you would are interested in dedicated support to assist or provide bespoke setups

- [Ansible Counselor](https://www.mindpointgroup.com/products/ansible-counselor-on-demand-ansible-services-and-consulting/)
- [Try us out](https://engage.mindpointgroup.com/try-ansible-counselor)

## Credits

This repo originated from work done by [Sam Doran](https://github.com/samdoran/ansible-role-stig)
