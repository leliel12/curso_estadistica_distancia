#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, os

import numpy

import csvcool


#===============================================================================
# READ FILE
#===============================================================================

with open("EPH.csv") as fp:
    cool = csvcool.read(fp, encoding="utf8")
    cool = cool.type_corrector(cool.discover_types())


if not os.path.exists("tables"):
    os.mkdir("tables")

#===============================================================================
# EJE 1
#===============================================================================

EDAD_INTER = [(10, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 69)]

edad_inter_freq = {}
for edad in cool.column("EDAD"):
    for li, ls in EDAD_INTER:
        if li <= edad <= ls:
            edad_inter_freq[(li, ls)] = edad_inter_freq.get((li, ls), 0) + 1
            break

with open("tables/act1_edad.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Número de intervalo".encode("utf8"),
                     u"Valores que comprende",
                     u"Frecuencia",
                     u"Frecuencia relativa",
                     u"Frecuencia Relativa acumulada"])
    Hi = 0
    for idx, tops in enumerate(EDAD_INTER):
        ni = float(edad_inter_freq[tuple(tops)])
        hi = ni / len(cool)
        Hi += hi
        tops = map(unicode, tops)
        writer.writerow([idx + 1, "-".join(tops), ni, hi, "{0:.2f}".format(Hi)])

