RHEL 7 DISA STIG Testing
================
Local testing of this role can be accomplished easily by using Vagrant. The included Vagrantfile has box definitions for a CentOS 7 and RHEL 7 based test machine. Additionally there are various playbooks in this directory for applying the STIG role to the boxes and there is a provision step in the Vagrantfile that will apply the role when the machine boots.

Testing the idempotence of the role can be acomplished by running the role_idempotent_check.yml playbook 

Requirements
------------
vagrant>=2.0

ansible>=2.4.0.0

Galaxy Roles

samdoran.redhat-subscription

```shell
ansible-galaxy install -r requirements.yml
```

If testing the RHEL7 images and you are using the Galaxy role above `samdoran.redhat-subscription` you need to set the following vars. Default setting is shown below.
```
rhn_username: "{{ lookup('env', 'RHN_USERNAME') }}"
rhn_password: "{{ lookup('env', 'RHN_PASSWORD') }}"
```

`vagrant-inventory` file with proper values in it.
```ini
[baseline_hosts]
centos7 ansible_port=2200  ansible_ssh_private_key_file=.vagrant/machines/centos7-stig/virtualbox/private_key
rhel7 ansible_port=2201 ansible_ssh_private_key_file=.vagrant/machines/rhel7-stig/virtualbox/private_key

[baseline_hosts:vars]
ansible_host=127.0.0.1
ansible_user=vagrant
```

Example Testing
-----------------

Spin up a new CentOS and RHEL box in Vagrant to run the tests on and apply the STIG.

```shell
vagrant up
```

Or if you don't want to run the initial provision steps at this time.

```shell
vagrant up --no-provision
```

Not running the provision steps in vagrant is sometimes preferred because vagrant will not run the play in parallel on both hosts, it will run on each host in serial. 

If you did not provision in the above step then run Ansible to provision the host.

```shell
ansible-playbook -i vagrant-inventory apply_role.yml -e @extra_vars_vagrant.yml
```

If there are no failures then we want apply the role again and test for idempotence.

```shell
ansible-playbook -i vagrant-inventory role_idempotent_check.yml
```
The idempotence check playbook runs the STIG role in silent mode (redirecting play/task output to JSON). You will not see each individual task run and it will take ~5min to complete.

After you are done you may see output like below if the idempotence check fails. The `assert` tasks give pass or fail for CentOS 7 and RHEL 7 respectively and give a list of the non-idempotent tasks from the run.

```
TASK [assert] ******************************************************************
fatal: [centos7]: FAILED! => {
    "assertion": "play_output.stats.centos7.changed == 0", 
    "changed": false, 
    "evaluated_to": false, 
    "failed": true, 
    "msg": "Role FAILED idempotent test on CentOS7: [u'MEDIUM | V-51363 | PATCH | The system must use a Linux Security Module configured to enforce limits on system services.', u'LOW | V-51369 | PATCH | The system must use a Linux Security Module configured to limit the privileges of system services.'] tasks reported change on second run."
}
fatal: [rhel7]: FAILED! => {
    "assertion": "play_output.stats.rhel7.changed == 0", 
    "changed": false, 
    "evaluated_to": false, 
    "failed": true, 
    "msg": "Role FAILED idempotent test on RHEL7: [u'MEDIUM | V-51363 | PATCH | The system must use a Linux Security Module configured to enforce limits on system services.', u'LOW | V-38567 | PATCH | The audit system must be configured to audit all use of setuid and setgid programs.', u'LOW | V-51369 | PATCH | The system must use a Linux Security Module configured to limit the privileges of system services.'] tasks reported change on second run."
}

PLAY RECAP ******************************************************************
centos7                    : ok=5    changed=1    unreachable=0    failed=1   
rhel7                      : ok=5    changed=1    unreachable=0    failed=1   
```

After you are done you should clean up.

```shell
ansible-playbook -i vagrant-inventory deregister.yml
vagrant destroy -f
```
