Developer Guide
===============

Building a development environment
----------------------------------

**NEED CONTENT**

*Insert dev environment setup and test running instructions.*


Writing documentation
---------------------
Documentation for individual controls is automatically generated where possible.
There is also the ability to add deployer notes for individual tasks that discuss
the specific implementation or risks with running the task/etc. Variables that
control the execution of each task are automatically pulled from the Ansible task
files themselves. 

Deployer notes
~~~~~~~~~~~~~~
Deployer notes are optional and can be added for each control that needs
additional data to be provided to role users. The notes are simply rST 
(reStructuredText) fragments and can contain simple blocks of text or
more complex rST formatted text. The system matches deployer notes to STIG
controls based on the note filename, which should follow the format
``RHEL-07-010010.rst``.

All of the notes are found within ``doc/metadata/notes``. Here is an example:

.. literalinclude:: ../metadata/notes/example-note.rst
   :language: yaml

The note should be brief, but it must answer a few critical questions:

* What does the change do to a system?
* What is the value of making this change?
* How can a deployer opt out or opt in for a particular change?
* Is there additional documentation available online that may help a deployer
  decide whether or not this change is valuable to them?

Run ``make html`` from the ``doc/`` directory to rebuild the documentation
and review your changes.
