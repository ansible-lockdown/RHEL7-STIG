Getting started
===============

This role is part of the `Ansible Lockdown`_ project and can be used as a 
standalone role or it can be used along with other Ansible roles and playbooks.

.. _Ansible Lockdown: https://github.com/ansible/ansible-lockdown

.. contents::
   :local:
   :backlinks: none

Requirements
------------
This documentation assumes that the reader has completed the steps within the
`Ansible installation guide <http://docs.ansible.com/ansible/intro_installation.html>`_.

The following additional libraries are required on the Ansible control node:

``passlib`` >= 1.5 (1.6.5 is available in RHEL and CentOS as ``python-passlib``)

``jmespath`` (available in RHEL and CentOS as ``python-jmespath``)

Installation
-------------------------------------

The recommended installation methods for this role are
``ansible-galaxy`` (recommended) or ``git``.

Using ``ansible-galaxy``
~~~~~~~~~~~~~~~~~~~~~~~~

The easiest installation method is to use the ``ansible-galaxy`` command that
is provided with your Ansible installation:

.. code-block:: console

   ansible-galaxy install git+https://github.com/mindpointgroup/rhel7-stig

The ``ansible-galaxy`` command will install the role into
``/etc/ansible/roles/rhel7-stig`` and this makes it easy to use with
Ansible playbooks.

Using ``git``
~~~~~~~~~~~~~

Start by cloning the role into a directory of your choice:

.. code-block:: console

   mkdir -p ~/.ansible/roles/
   git clone https://github.com/mindpointgroup/rhel7-stig ~/.ansible/roles/rhel7-stig

Ansible looks for roles in ``~/.ansible/roles`` by default.

If the role is cloned into a different directory, that directory must be
provided with the ``roles_path`` option in ``ansible.cfg``. The following is
an example of a ``ansible.cfg`` file that uses a custom path for roles:

.. code-block:: ini

   [DEFAULTS]
   roles_path = /etc/ansible/roles:/home/myuser/custom/roles

With this configuration, Ansible looks for roles in ``/etc/ansible/roles`` and
``~/custom/roles``.

Usage
-----

This role works well with existing playbooks. The following is an
example of a basic playbook that uses this role:

.. code-block:: yaml

    ---

    - hosts: servers
      become: yes
      roles:
        - role: rhel7-stig
          when:
            - ansible_os_family == 'RedHat'
            - ansible_distribution_major_version | version_compare('7', '=')

The role is fully customizable by setting the variables provided in the ``defaults/main.yml``.
These variables are designed so that categories/severities or individual rules can be enabled,
disabled, or can alter configuration for various STIG items in the role. For more details
on the available variables, refer to the :ref:`stig_controls_label`
section.

.. note::

    The role requires elevated privileges and must be run as a user with ``sudo``
    access. The example above uses the ``become`` option, which causes Ansible to use
    sudo before running tasks.

.. warning::

    It is strongly recommended to run the role in check mode (often called a
    `dry run`) first before making any modifications. This gives the deployer
    the opportunity to review all of the proposed changes before applying the
    role to the system. Use the ``--check`` parameter with ``ansible-playbook``
    to use check mode.
