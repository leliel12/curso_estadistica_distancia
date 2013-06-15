#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "THE WISKEY-WARE LICENSE":
# <jbc.develop@gmai.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a WISKEY in return Juan


#===============================================================================
# DOC
#===============================================================================

"""This module contains several implementations of statistics algoritmhs

"""

import numpy as np

def Q(a):
    "Promedio de cuartiles"
    return np.average(np.percentile(a, (25, 75)))


def TRI(a):
    """Trimedian"""
    Me = np.median(a)
    values = np.percentile(a, (25, 75))
    values = np.append(values, [Me, Me])
    return np.average(values)


def MID(a):
    """Promedio inter cuartil. Calcula el promedio de los valores del 50% central
    del array"""
    l, u = np.percentile(a, (25, 75))
    return np.average(a[(a >= l) & (a <= u)])

