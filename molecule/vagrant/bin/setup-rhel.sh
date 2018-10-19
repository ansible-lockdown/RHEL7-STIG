#!/bin/bash -xe

# Helper script to setup a RHEL7 Vagrant Box with Packer
#
# You must download a RHEL7 iso and place it in the molecule/vagrant/ directory
# with the name 'rhel.iso'
#
# RHEL Developer Licenses are free and can be grabbed from
# https://developers.redhat.com/
#
# You must also have Vagrant, Packer, and Virtual Box (+ Extension Pack) installed
# Vagrant => https://www.vagrantup.com/downloads.html
# Packer  => https://www.packer.io/downloads.html
# VirtualBox & Extension Pack => https://www.virtualbox.org/wiki/Downloads
#

packer build rhel-packer.json
vagrant box add rhel7 RHEL7-STIG_TEST.box
