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

with open("tables/act3_cant_hs_tab.csv", "w") as fp:
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

with open("tables/act3_antig.csv", "w") as fp:
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

with open("tables/act3_sueldo.csv", "w") as fp:
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

#===============================================================================
# EJE 4
#===============================================================================

with open("tables/act4_sexoXsueldo.csv", "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([
        "Sueldo", "V(ni)", "V(Ni)", "M(ni)", "M(Ni)", "Tot(ni)", "Tot(Ni)"
    ])

    Ni_v = 0
    Ni_m = 0
    Ni_tot = 0
    for sueldo in sorted(set(cool.column("SUELDO"))):

        ni_v = len(cool.filter(lambda r: r["SUELDO"] == sueldo and r["SEXO"] == 1))
        ni_m = len(cool.filter(lambda r: r["SUELDO"] == sueldo and r["SEXO"] == 2))

        Ni_v += ni_v
        Ni_m += ni_m
        Ni_tot += ni_v + ni_m

        writer.writerow([sueldo, ni_v, Ni_v, ni_m, Ni_m, ni_v + ni_m, Ni_tot])


    writer.writerow(["Total", "", Ni_v, "", Ni_m, "", Ni_tot])


#===============================================================================
# ACT 5
#===============================================================================

ESTUD_VARS = {0: u"No sabe leer ni escribir",
              1: u"Primario",
              2: u"Nacional",
              3: u"Comercial",
              4: u"Normal",
              5: u"Técnica",
              6: u"Otra enseñanza media",
              7: u"Superior",
              8: u"Universitaria"}

SEXO_VARS = {1: u"Varón",
             2: u"Mujer"}

with open("tables/act5_stud_sexo.csv", "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([
        "Estudios", "V(ni)", "V(Ni)", "M(ni)", "M(Ni)", "Tot(ni)", "Tot(Ni)"
    ])

    Ni_v = 0
    Ni_m = 0
    Ni_tot = 0
    for estud in sorted(set(cool.column("ESTUD"))):

        ni_v = len(cool.filter(lambda r: r["ESTUD"] == estud and r["SEXO"] == 1))
        ni_m = len(cool.filter(lambda r: r["ESTUD"] == estud and r["SEXO"] == 2))

        Ni_v += ni_v
        Ni_m += ni_m
        Ni_tot += ni_v + ni_m

        writer.writerow([ESTUD_VARS[estud].encode("utf8"),
                         ni_v, Ni_v, ni_m, Ni_m, ni_v + ni_m, Ni_tot])


    writer.writerow(["Total", "", Ni_v, "", Ni_m, "", Ni_tot])


