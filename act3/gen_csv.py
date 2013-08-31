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

with open("tables/act2_cant_hs_tab.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"hs",
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    acum = 0
    for h in sorted(set(cool.column("HS.TRA"))):
        ni = len(cool.filter(lambda r: r["HS.TRA"] == h))
        hi = float(ni) / len(cool)
        Ni = ni + acum
        Hi = float(Ni) / len(cool)
        writer.writerow([h, ni, hi, Ni, Hi])
        acum = Ni

with open("tables/act2_antig.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Antigüedad".encode("utf8"),
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    acum = 0
    for h in sorted(set(cool.column("ANTIGUE"))):
        ni = len(cool.filter(lambda r: r["ANTIGUE"] == h))
        hi = float(ni) / len(cool)
        Ni = ni + acum
        Hi = float(Ni) / len(cool)
        writer.writerow([h, ni, hi, Ni, Hi])
        acum = Ni

with open("tables/act2_sueldo.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Sueldo".encode("utf8"),
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    acum = 0
    for h in sorted(set(cool.column("SUELDO"))):
        ni = len(cool.filter(lambda r: r["SUELDO"] == h))
        hi = float(ni) / len(cool)
        Ni = ni + acum
        Hi = float(Ni) / len(cool)
        writer.writerow([h, ni, hi, Ni, Hi])
        acum = Ni

