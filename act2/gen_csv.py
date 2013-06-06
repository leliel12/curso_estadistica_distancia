#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, os

import numpy as np

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

with open("tables/act1_edad_meds.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Medida", "Valor"])
    writer.writerow([u"Media",
                     "{0:.2f}".format(np.average(cool.column("EDAD")))])
    writer.writerow([u"Mediana",
                     "{0:.2f}".format(np.median(cool.column("EDAD")))])
    writer.writerow([u"Desviación Standar".encode("utf-8"),
                     "{0:.2f}".format(np.std(cool.column("EDAD")))])


#===============================================================================
# EJE 2
#===============================================================================

fig_eje2 = plt.figure()
ax_plot2 = fig_eje2.add_subplot(111)
ax_plot2.boxplot(cool.column("EDAD"))
plt.savefig("figs/act2_boxplot_edad.png")
np.percentile(cool.column("EDAD"), [0, 25, 75, 100])
plt.close()


#===============================================================================
# EJE 3
#===============================================================================

fig_eje3 = plt.figure()

ax_plot3_varones = fig_eje3.add_subplot(121)
ax_plot3_varones.boxplot(cool.filter(lambda r: r["SEXO"] == 1).column("EDAD"))
ax_plot3_varones.set_xlabel("Hombres")

ax_plot3_mujeres = fig_eje3.add_subplot(122)
ax_plot3_mujeres.boxplot(cool.filter(lambda r: r["SEXO"] == 2).column("EDAD"))
ax_plot3_mujeres.set_xlabel("Mujeres")

plt.savefig("figs/act3_boxplot_edad.png")
plt.close()


