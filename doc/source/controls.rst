.. _stig_controls_label:

STIG Controls
=============

This role follows the |stig_name| `Security Technical Implementation Guide (STIG)`_.
The guide has over 200 controls that apply to various parts of a Linux system, and it
is updated regularly by the Defense Information Systems Agency (DISA). DISA is part of the
United States Department of Defense. The current version of this role follows |stig_version|
of the |stig_name_short| STIG.

Controls are divided into groups based on the following properties:

Control Severities
~~~~~~~~~~~~~~~~~~

:ref:`High (CAT I) <severity-high>`
  These controls have a large impact on the security of a
  system. They also have the largest operational impact to a system and
  deployers should test them thoroughly in non-production environments.

:ref:`Medium (CAT II) <severity-medium>`
  These controls are the bulk of the items in the STIG and 
  they have a moderate level of impact on the security of a system.
  Many controls in this category will have an operational impact on 
  a system and should be tested thoroughly before implementation.

:ref:`Low (CAT III) <severity-low>`
  These controls have a smaller impact on overall security, but they
  are generally easier to implement with a much lower operational impact.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~
It is important to understand the implementation status of each control and
the potential impact each task can have on a system. Some controls are not
implemented for various technical reasons. Some are implemented but disabled
by default. And others are just peform a check and report back if manual
changes need to be made to meet the STIG control.

:ref:`Implemented <status-Implemented>`
  These controls are fully implemented and they may have configurations which
  can be adjusted. The notes for each control will identify which configuration
  options are available.

:ref:`Complexity High <status-Complexity-High>`
  These controls are deemed too complex to safely rememdiate via automated
  controls. The tasks for these controls perform automated checks and will
  report the result of the check in Ansible task output. The purpose of this
  output is to alert deployers to items that would fail an audit against the
  STIG and should be rememdiated manually. Execution and reporting from these
  tasks can be enabled or disabled via the appropriate variables.

  .. code-block:: yaml

      rhel7stig_complexity_high: no
      rhel7stig_audit_complex: yes

:ref:`Disruption High <status-Disruption-High>`
  These controls are classified as having a high likelihood of distruption on a
  system and disabled by default. Automatic rememdiation can be enabled by
  setting the appropriate variables, however the deployer should be aware
  that they are often disabled because they could cause harm to a subset of
  systems. Each control has notes that explains the caveats of the control
  and how to enable it if needed.

  .. code-block:: yaml
  
      rhel7stig_disruption_high: no
      rhel7stig_audit_disruptive: yes

:ref:`Not Implemented <status-Not-Implemented>`
  These are controls that have not yet been implemented. The goal of this project
  is to have no controls in this status. This does not mean 100% of the controls
  will be fully implemented. Just that 100% of the controls will be in one of the
  above status categories. We welcome any help in getting these controls implemented.

Deployers should review the full list of controls 
:ref:`sorted by implementation status <controls-by-status>`.


Control Deviation
~~~~~~~~~~~~~~~~~

The role deviates from some of the STIG's requirements when a security control
could cause significant issues with production systems. Additionally specific
control settings, which are controlled by role variables, can deviate from
the mandated STIG settings. Deployers should review and update the default
configurations to meet the needs of their environment.

.. note::

   All of the default configurations are found within ``defaults/main.yml``.


.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/os/unix-linux/Pages/red-hat.aspx

Controls
~~~~~~~~

.. toctree::
   :maxdepth: 1

   auto_controls-all.rst

.. toctree::
   :maxdepth: 2

   auto_controls-by-severity.rst
   auto_controls-by-status.rst
