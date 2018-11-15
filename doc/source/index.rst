=========================================================
Automated security hardening for Linux hosts with Ansible
=========================================================

What does the role do?
----------------------

The ansible-hardening Ansible role uses industry-standard security
hardening guides to secure Linux hosts. Although the role is designed to work
well in OpenStack environments that are deployed with OpenStack-Ansible, it can
be used with almost any Linux system.

It all starts with the `Security Technical Implementation Guide (STIG)`_ from
the `Defense Information Systems Agency (DISA)`_, part of the United States
Department of Defense. The guide is released with a public domain license and
it is commonly used to secure systems at public and private organizations
around the world.

Each configuration from the STIG is analyzed to determine what impact it could
have on a live production environment and how to implement it in Ansible. Tasks
are added to the role that configure a host to meet the configuration
requirement. Each task is documented to explain what was changed, why it was
changed, and what deployers need to understand about the change.

Deployers have the option to pick and choose which configurations are applied
using Ansible variables and tags. Some tasks allow deployers to provide custom
configurations to tighten down or relax certain requirements.

.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/Pages/index.aspx
.. _Defense Information Systems Agency (DISA): http://www.disa.mil/

Documentation
-------------

The following documentation applies to the Queens release (currently under
active development). Documentation for the latest stable and previous stable
releases is found within the *Releases* section below.

.. toctree::
   :maxdepth: 2

   getting-started.rst
   faq.rst
   deviations.rst
   controls-rhel7.rst
   controls-contrib.rst
   developer-guide.rst

Releases
--------

Deployers should use the latest stable release for all production deployments.

devel
~~~~~~

* **Status:** Active development

* **STIG Version:**
  RHEL 7 STIG Version 2, Release 1 *(Published on 2018-09-26)*

* **Supported Operating Systems:**

  * Red Hat Enterprise Linux 7
  * CentOS 7

* **Targeted Operating Systems:**

These are not yet supported but are on the target list.
  * Debian 8 Jessie
  * Fedora 26
  * openSUSE Leap 42.2 and 42.3
  * SUSE Linux Enterprise 12 

* **Documentation:**

  * `ansible-hardening Queens Release Notes`_

.. _ansible-hardening Queens Release Notes: http://docs.openstack.org/releasenotes/ansible-hardening/unreleased.html
