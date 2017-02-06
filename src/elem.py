#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'f0x11'


class A(object):
    pair = T
    r_pair = U


class T(object):
    pair = A
    r_pair = A


class C(object):
    pair = G
    r_pair = G


class G(object):
    pair = C
    r_pair = C


class U(object):
    pair = A
    r_pair = A
