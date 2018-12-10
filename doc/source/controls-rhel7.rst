.. _stig_controls_label:

STIG Controls
===================================================

This role follows the |stig_name| `Security Technical Implementation Guide (STIG)`_.
The guide has over 200 controls that apply to various parts of a Linux system, and it
is updated regularly by the Defense Information Systems Agency (DISA). DISA is part of the
United States Department of Defense. The current version of this role follows |stig_version|
of the |stig_name_short| STIG.

Controls are divided into groups based on the following properties:

* **Severity:**

  * *High severity* or **CAT I** controls have a large impact on the security of a
    system. They also have the largest operational impact to a system and
    deployers should test them thoroughly in non-production environments.

  * *Medium severity* or **CAT II** controls are the bulk of the items in the STIG and 
    they have a moderate level of impact on the security of a system.
    Many controls in this category will have an operational impact on 
    a system and should be tested thoroughly before implementation.

  * *Low severity* or **CAT III** controls have a smaller impact on overall security, but they
    are generally easier to implement with a much lower operational impact.

* **Implementation Status:**

  * *Implemented* controls are automatically implemented with automated tasks.
    Deployers can often opt out of these controls by adjusting Ansible
    variables. These variables are documented with each control below.

  * *Exception* denote controls that cannot be completed via automated tasks.
    Some of these controls must be applied during the initial provisioning
    process for new servers while others require manual inspection of the
    system.

  * *Opt-In* controls have automated tasks written, but these tasks are
    disabled by default. These controls are often disabled because they could
    cause disruptions on a production system, or they do not provide a
    significant security benefit. Each control can be enabled with Ansible
    variables and these variables are documented with each control below.

  * *Verification Only* controls have tasks that verify that a control is met.
    These tasks do not take any action on the system, but they often display
    debug output with additional instructions for deployers.

.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/os/unix-linux/Pages/red-hat.aspx

Although the STIG is specific to Red Hat Enterprise Linux 7, it can also be applied
to CentOS 7 systems.

.. toctree::
   :maxdepth: 2

   rhel7/auto_controls-by-severity.rst
   rhel7/auto_controls-by-status.rst
   rhel7/auto_controls-all.rst
