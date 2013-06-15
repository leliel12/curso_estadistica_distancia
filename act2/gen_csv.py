#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

import csv, os

import numpy as np

import matplotlib.pyplot as plt

import csvcool

import advest


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


#===============================================================================
# EJE 4
#===============================================================================

fig_eje4_hstra = plt.figure()
ax_plot_varones_hstra = fig_eje4_hstra.add_subplot(121)
ax_plot_varones_hstra.boxplot(cool.filter(lambda r: r["SEXO"] == 1).column("HS.TRA"))
quart = np.percentile(cool.filter(lambda r: r["SEXO"] == 1).column("HS.TRA"),
                      [0, 25, 50, 75, 100])
ax_plot_varones_hstra.set_xlabel("Hombres {}".format(quart))

ax_plot_mujeres_hstra = fig_eje4_hstra.add_subplot(122)
ax_plot_mujeres_hstra.boxplot(cool.filter(lambda r: r["SEXO"] == 2).column("HS.TRA"))
quart = np.percentile(cool.filter(lambda r: r["SEXO"] == 2).column("HS.TRA"),
                      [0, 25, 50, 75, 100])
ax_plot_mujeres_hstra.set_xlabel("Mujeres {}".format(quart))

plt.savefig("figs/act4_boxplot_hstra.png")


fig_eje4_antigue = plt.figure()
ax_plot_varones_antigue = fig_eje4_antigue.add_subplot(121)
ax_plot_varones_antigue.boxplot(cool.filter(lambda r: r["SEXO"] == 1).column("ANTIGUE"))
quart = np.percentile(cool.filter(lambda r: r["SEXO"] == 1).column("ANTIGUE"),
                      [0, 25, 50, 75, 100])
ax_plot_varones_antigue.set_xlabel("Hombres {}".format(quart))

ax_plot_mujeres_antigue = fig_eje4_antigue.add_subplot(122)
ax_plot_mujeres_antigue.boxplot(cool.filter(lambda r: r["SEXO"] == 2).column("ANTIGUE"))
quart = np.percentile(cool.filter(lambda r: r["SEXO"] == 2).column("ANTIGUE"),
                      [0, 25, 50, 75, 100])
ax_plot_mujeres_antigue.set_xlabel("Mujeres {}".format(quart))

plt.savefig("figs/act4_boxplot_antigue.png")


#===============================================================================
# EJE 4
#===============================================================================


with open("tables/act5_1.csv", "w") as fp:

    def ests(coll):
        return ["{0:.2f}".format(np.average(coll)),
                Counter(coll).most_common(1)[0][0],
                np.percentile(coll, 25),
                np.percentile(coll, 50),
                np.percentile(coll, 75),
                np.max(coll) - np.min(coll)]

    writer = csv.writer(fp)

    writer.writerow(["Variables", "Media", "Modo",
                     "Q1", "Mediana", "Q3", "Rango"])

    writer.writerow(["Hs. Trabajo"] + ests(cool.column("HS.TRA")))
    writer.writerow([u"Antigüedad".encode("utf8")] + ests(cool.column("ANTIGUE")))
    writer.writerow(["Sueldo"] + ests(cool.column("SUELDO")))


with open("tables/act5_2.csv", "w") as fp:

    def ests(coll):
        return [np.min(coll), np.max(coll),
                "{0:.2f}".format(np.var(coll)),
                "{0:.2f}".format(np.std(coll)),
                advest.Q(coll),
                advest.TRI(coll)]

    writer = csv.writer(fp)

    writer.writerow(["Variables", u"Mínimo".encode("utf8"),
                     u"Máximo".encode("utf8"), "Varianza",
                     u"Desv. Estándar".encode("utf8"), "Q Promedio", "TRI"])

    writer.writerow(["Hs. Trabajo"] + ests(cool.column("HS.TRA")))
    writer.writerow([u"Antigüedad".encode("utf8")] + ests(cool.column("ANTIGUE")))
    writer.writerow(["Sueldo"] + ests(cool.column("SUELDO")))


with open("tables/act5_3.csv", "w") as fp:

    def ests(coll):
        return ["{0:.2f}".format(advest.MID(coll)),
                "{0:.2f}".format(advest.varQ(coll)),
                "{0:.2f}".format(advest.H1_yule(coll)),
                "{0:.2f}".format(advest.H3_kelly(coll)),
                "{0:.2f}".format(advest.K1_kurtosis(coll)),
                0]

    writer = csv.writer(fp)

    writer.writerow(["Variables", "MID", u"CVc Cuartílico".encode("utf8"),
                     "H1 Yule", "H3 Kelly", "K1 Curtosis", "SK Pearson"])

    writer.writerow(["Hs. Trabajo"] + ests(cool.column("HS.TRA")))
    writer.writerow([u"Antigüedad".encode("utf8")] + ests(cool.column("ANTIGUE")))
    writer.writerow(["Sueldo"] + ests(cool.column("SUELDO")))









