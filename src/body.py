#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from individual.leader import Leader
from individual.operator import Operator

__author__ = 'f0x11'


class Body(object):
    def __int__(self, role):
        self.role = role
        self.leader = Leader()
        self.operator = Operator()

    def reproduce(self):
        # 自己有资源时，会选择繁殖
        pass

    def live(self):
        pass
