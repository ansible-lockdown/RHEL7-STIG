# -*- coding: utf-8 -*-

# Copyright (c) 2016, Ansible, Inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

def contains(seq, value):
    '''Opposite of the ``in`` test, allowing use as a test in filters like ``selectattr``

    .. versionadded:: 2.8
    '''
    return value in seq

class TestModule:
    ''' Ansible math jinja2 tests '''

    def tests(self):
        return {
            # set theory
            'contains':    contains,
        }
