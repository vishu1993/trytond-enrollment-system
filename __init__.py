# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from enrollment_system import Party


def register():
    Pool.register(
        Party,
        module='enrollment_system', type_='model'
    )
