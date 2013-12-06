#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

import csv, os

import numpy as np

from scipy import stats

import matplotlib.pyplot as plt

import csvcool



#===============================================================================
# READ FILE
#===============================================================================

with open("EPH.csv") as fp:
    cool = csvcool.read(fp, encoding="utf8")
    cool = cool.type_corrector(cool.discover_types())


if not os.path.exists("tables"):
    os.mkdir("tables")

if not os.path.exists("figs"):
    os.mkdir("figs")


#===============================================================================
# EJE 3
#===============================================================================
