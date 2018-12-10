Control Deviations
==================================================================

The role deviates from some of the STIG's requirements when a security control
could cause significant issues with production systems or when an item can't be
realistically implemented via automation. The role classifies each control
into an implementation status and provides notes on why a certain control is
skipped, altered, or only reports a status.

The following provides a brief overview of each implementation status:

Implemented
  These controls are fully implemented and they may have configurations which
  can be adjusted. The notes for each control will identify which configuration
  options are available.

Exception
  If a control requires manual intervention outside the host, or if it could
  cause significant harm to a host, it will be skipped and listed as an
  exception. All controls in this category are not implemented in Ansible.

Opt-In
  The controls in the opt-in list are implemented in Ansible, but are disabled
  by default. They are often disabled because they could cause harm to a subset
  of systems. Each control has notes that explains the caveats of the control
  and how to enable it if needed.

Verification Only
  These controls have tasks that verify that a control is met.
  These tasks do not take any action on the system, but they often display
  debug output with additional instructions for deployers.

Deployers should review the full list of controls
`sorted by implementation status <rhel7/auto_controls-by-status.html>`_.

.. note::

   All of the default configurations are found within ``defaults/main.yml``.
