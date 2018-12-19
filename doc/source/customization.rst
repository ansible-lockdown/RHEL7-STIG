Role Customization
==================

This role can be fully customized to fit your specific environment. In fact
for most users it is recommended that they customize/tweak the role variables
before applying across their envirnoment.

.. contents::
   :local:
   :backlinks: none

Tailoring
---------

It is recommended that you tailor this roles tasks for your environment by using
the comprehensive set of variables defined in ``defaults/main.yml``. There are
several ways to override default role variables in Ansible. We cover the recommended
techniques below.

Using ``group_vars``
~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to tailor this role to your environment is by using ``group_vars``:

    **NEED CONTENT**
    
    *insert example for group_vars tailoring*

Variables
---------
The role has a large number of variables that allow the deployer to control the execution
of specific tasks (on/off) as well as the configuration or settings for the tasks and the
controls they implement. For example the deployer can choose to enable or disable tasks
by severity/category *cat1 | high, cat2 | medium, cat3 | low*. The deployer can also set
things like whether any *GUI* related tasks should run or tailor specific STIG settings
like the logon banner text or password complexity settings. We don't cover all the variables
in this section but we do cover some of the major ones. Generally the variables that control
specific tasks or control configurations are detailed in the
:ref:`controls documentation <stig_controls_label>`.

Enable tasks by category/severity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These variables allow enabling/disabling cat1, cat2, or cat3 rules in bulk. Disabling these
will take precedence over individual task variables but enabling them will not. i.e. If the
``rhel7stig_cat3_patch`` variable is set to ``no`` then all *cat3* tasks will be skipped
regardless of their :ref:`individual settings <individual_rule_vars>`. However if the *cat3*
variable is enabled individual tasks could still be skipped if their variable is disabled.

.. code-block:: yaml

    rhel7stig_cat1_patch: yes
    rhel7stig_cat2_patch: yes
    rhel7stig_cat3_patch: yes

Complex tasks
~~~~~~~~~~~~~
There are several variables that control the execution or behavior of tasks that the
implementers of this role have deemed to be too complex or risky to automatically
remediate. These rules have tasks that audit the system and will optionally report
``changed`` and will report back (via debug statements) if the system would fail
the check. The deployer can use this information to manually remediate the finding.
The execution and reporting behavior of these tasks is controlled by two variables:

.. code-block:: yaml

    # Controls execution of these tasks
    rhel7stig_complexity_high: no

    # Controls whether the tasks reports changed or not
    rhel7stig_audit_complex: yes

Disruptive tasks
~~~~~~~~~~~~~~~~
These varaibles are similar to the *complex task* variables. They control the
execution or behavior of tasks that perform automated remediation but are shown
to be potentially disruptive to systems when used in production environments.
The risk of automated remediation of with these tasks is high.
These rules have tasks that audit the system and will optionally report
``changed`` and will report back (via debug statements) if the system would fail
the check. The deployer can use this information to manually remediate the finding.
The execution and reporting behavior of these tasks is controlled by two variables:

.. code-block:: yaml

    # Controls execution of these tasks
    rhel7stig_disruption_high: no

    # Controls whether the tasks reports changed or not
    rhel7stig_audit_disruptive: yes

Required system services
~~~~~~~~~~~~~~~~~~~~~~~~
These variables allow the deployer to specify that services are required by the system
to perform its mission. Except for ``ssh``, it is important to note that having these
services installed and enabled are deviations from the STIG benchmark and should have
corresponding documentation approved by the system owner or other signing authority.

.. code-block:: yaml

    rhel7stig_ssh_required: yes
    rhel7stig_vsftpd_required: no
    rhel7stig_tftp_required: no
    rhel7stig_autofs_required: no
    rhel7stig_kdump_required: no
    rhel7stig_ipsec_required: no

Graphical User Interface items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This variable enables or disables all tasks related to *GUI* packages. i.e. These
generally would only apply to a system with the ``GNOME`` package installed. This
is not to say that ``KDE``, ``XFCE``, or one of the many other desktop systems 
would not need to have similar controls in place, but the STIG currently only
covers ``GNOME`` settings.

.. code-block:: yaml

    rhel7stig_gui: no

.. _individual_rule_vars:

Individual STIG rules
~~~~~~~~~~~~~~~~~~~~~
These variables enable or disable individual rules or more specifically tasks or
blocks of tasks that enforce individual STIG rules. Each STIG item with an ID
following the format *RHEL-07-###### (ex. RHEL-07-010010)* will have a corresponding
variable in the below format. For more information on each rule and its default state
please see the :ref:`controls documentation <stig_controls_label>`.

.. code-block:: yaml

    rhel_07_######: true
