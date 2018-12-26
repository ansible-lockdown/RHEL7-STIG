=========================================================
Automated security hardening for Linux hosts with Ansible
=========================================================

.. image:: https://secure.travis-ci.org/MindPointGroup/RHEL7-STIG.svg?branch=devel
   :alt: Build Status Badge
   :target: https://travis-ci.org/MindPointGroup/RHEL7-STIG

.. raw:: html

    <p><iframe src="https://ghbtns.com/github-btn.html?user=MindPointGroup&repo=RHEL7-STIG&type=watch&count=true&size=large&v=2"
    allowtransparency="true" frameborder="0" scrolling="0" width="200px" height="35px"></iframe></p>

What does the role do?
----------------------
This role uses the |stig_name| `Security Technical Implementation Guide (STIG)`_ guidance 
from the `Defense Information Systems Agency (DISA)`_. The STIG is released with a 
public domain license and it is commonly used to secure systems at public and private
organizations around the world.

We analyze each configuration hardening item from the applicable STIG benchmark
to determine what impact it has on a live production environment and how to
best implement it using Ansible. Tasks are added to the role that configure a host
to meet the configuration requirements. Each task is documented to explain what was
changed, why it was changed, and what deployers need to understand about the change.

Deployers have the option to enable/disable STIG items that do not suit their environments
needs. Each STIG item has an associated variable that can be used to switch it on or off.
Additionally, the items that have configurable values, i.e. number of password attempts, will
generally have a corresponding variable that allows for customization of the applied value.
It is imperative for each deployer to understand the regulations and compliance requirements
that their organization and specific environments are responsible for meeting in order to
effeectively implement the controls in the |stig_name_short| STIG.

.. _Security Technical Implementation Guide (STIG): http://iase.disa.mil/stigs/os/unix-linux/Pages/red-hat.aspx
.. _Defense Information Systems Agency (DISA): http://www.disa.mil/

Documentation
-------------

The following documentation applies to the devel branch and is currently under
active development. Documentation for the latest stable and previous stable
releases will be generated and available once the first stable release is cut.

.. toctree::
   :maxdepth: 2

   getting-started.rst
   customization.rst
   controls.rst
   controls-contrib.rst
   developer-guide.rst
   faq.rst

Releases
--------

devel
~~~~~~

* **Status:** Active development

* **STIG Version:**
  |stig_name_short| |stig_version| *(Published on* |stig_release_date| *)*

* **Supported Operating Systems:**

  * Red Hat Enterprise Linux 7
  * CentOS 7

* **Targeted Operating Systems:**

These are not yet supported but are on the target list.
  * Debian 8 Jessie
  * Fedora 26
  * openSUSE Leap 42.2 and 42.3
  * SUSE Linux Enterprise 12 
