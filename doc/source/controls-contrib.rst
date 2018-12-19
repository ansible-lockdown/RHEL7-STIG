Additional Controls
===================

Although the Security Technical Implementation Guide (STIG) contains a very
comprehensive set of security configurations, some contributors want to add
extra security configurations to the role. The *contrib* portion of the 
role is designed to implement those configurations as an optional set of tasks.

In general, *contrib* controls are limited to items to meet backwards compatibility
with the `Openstack Ansible Hardening`_ project. It is recommended that new *contrib*
items (things that don't address specific STIG items) should be addressed in a separate
Ansible role.

.. _Openstack Ansible Hardening: https://github.com/openstack/ansible-hardening

**BELOW IS NOT YET IMPLEMENTED IN THIS ROLE**

*The below configurations and variables are not yet implemented. This page and
message are being kept until it is implemented.*

The *contrib* hardening configurations are disabled by default, but they can
be enabled by setting the following Ansible variable:

.. code-block:: yaml

    rhel7stig_security_contrib_enabled: yes

The individual tasks are controlled by Ansible variables in
``defaults/main.yml`` that are defined under the
``rhel7stig_security_contrib:`` variable.

Kernel
------

C-00001 - Disable IPv6
~~~~~~~~~~~~~~~~~~~~~~

Some systems do not require IPv6 connectivity and the presence of link local
IPv6 addresses can present an additional attack surface for lateral movement.
Deployers can set the following variable to disable IPv6 on all network
interfaces:

.. code-block:: yaml

    rhel7_stig_security_contrib:
        disable_ipv6: yes

.. warning::

    Deployers should test this change in a test environment before applying it
    in a production deployment. Applying this change to a production system
    that relies on IPv6 connectivity will cause unexpected downtime.
