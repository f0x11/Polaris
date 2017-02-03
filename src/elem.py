#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'f0x11'


class A(object):
    pair = T
    r_pair = U
    pass


class T(object):
    pair = A
    r_pair = A
    pass


class C(object):
    pair = G
    r_pair = G
    pass


class G(object):
    pair = C
    r_pair = C
    pass


class U(object):
    pair = A
    r_pair = A
    pass
