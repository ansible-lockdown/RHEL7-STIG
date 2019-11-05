# -*- coding: utf-8 -*-

# Copyright (c) 2017, the Jinja Team
# BSD 3-Clause "New" or "Revised" License (see https://opensource.org/licenses/BSD-3-Clause)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import operator

def test_in(value, seq):
    """Check if value is in seq.
    Copied from Jinja 2.10 https://github.com/pallets/jinja/pull/665

    .. versionadded:: 2.10
    """
    return value in seq


class TestModule:
    ''' Tests from jinja 2.10 for compat with older jinja2 on RHEL 7. '''

    def tests(self):
        return {
            'in':          test_in,
            '==':          operator.eq,
            'eq':          operator.eq,
            'equalto':     operator.eq,
            '!=':          operator.ne,
            'ne':          operator.ne,
            '>':           operator.gt,
            'gt':          operator.gt,
            'greaterthan': operator.gt,
            'ge':          operator.ge,
            '>=':          operator.ge,
            '<':           operator.lt,
            'lt':          operator.lt,
            'lessthan':    operator.lt,
            '<=':          operator.le,
            'le':          operator.le,
        }
