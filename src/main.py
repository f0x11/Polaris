#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from body import Body

__author__ = 'f0x11'

MAX_PER_MEMORY = 1024 * 1024
MAX_PER_CPUS = 0.5

is_leader = True    # or False


def main():
    me = Body()
    me.live()
