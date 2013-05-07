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

if not os.path.exists("tables"):
    os.mkdir("tables")


#===============================================================================
# ACT 2.1 SEXO
#===============================================================================

SEXO_VARS = {1: u"Varón",
             2: u"Mujer"}


with open("tables/act2_1_{}.csv".format("sexo_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Sexo",
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    Ni, Hi = 0, 0
    for k, cat in sorted(SEXO_VARS.items()):
        rows = cool.filter(lambda r: int(r["SEXO"]) == k)
        ni = len(rows)
        hi = ni / float(len(cool))
        Ni += ni
        Hi += hi
        writer.writerow([cat.encode("utf8"), ni, hi, Ni, "{0:.2f}".format(Hi)])

    writer.writerow([u"Total", Ni, "{0:.2f}".format(Hi), Ni, "{0:.2f}".format(Hi)])


#===============================================================================
# ACT 2.1 CIVIL
#===============================================================================

CIVIL_VARS = {1: u"Soltero",
              2: u"Unido",
              3: u"Casado",
              4: u"Separado / divorciado",
              5: u"Viudo"}

with open("tables/act2_1_{}.csv".format("civil_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Estado Civil",
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    Ni, Hi = 0, 0
    for k, cat in sorted(CIVIL_VARS.items()):
        rows = cool.filter(lambda r: int(r["CIVIL"]) == k)
        ni = len(rows)
        hi = ni / float(len(cool))
        Ni += ni
        Hi += hi
        writer.writerow([cat.encode("utf8"), ni, hi, Ni, "{0:.2f}".format(Hi)])
    writer.writerow([u"Total", Ni, "{0:.2f}".format(Hi), Ni, "{0:.2f}".format(Hi)])


#===============================================================================
# ACT 2.1 ESTUD
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

with open("tables/act2_1_{}.csv".format("estud_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Estudios que cursa o cursó".encode("utf8"),
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    Ni, Hi = 0, 0
    for k, cat in sorted(ESTUD_VARS.items()):
        rows = cool.filter(lambda r: int(r["ESTUD"]) == k)
        ni = len(rows)
        hi = ni / float(len(cool))
        Ni += ni
        Hi += hi
        writer.writerow([cat.encode("utf8"), ni, hi, Ni, "{0:.2f}".format(Hi)])
    writer.writerow([u"Total", Ni, "{0:.2f}".format(Hi), Ni, "{0:.2f}".format(Hi)])

#===============================================================================
# ACT 2.1 VIVIEN
#===============================================================================

VIVIEN_VARS = {1: u"Casa",
               2: u"Departamento",
               3: u"Vivienda en lugar de trabajo",
               4: u"Inquilinato",
               5: u"Hotel o pensión",
               6: u"Construcción no destinada a fines habitacionales",
               7: u"Vivienda en villa",
               8: u"Otros"}

with open("tables/act2_1_{}.csv".format("vivien_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Vivienda".encode("utf8"),
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    Ni, Hi = 0, 0
    for k, cat in sorted(VIVIEN_VARS.items()):
        rows = cool.filter(lambda r: int(r["VIVIEN"]) == k)
        ni = len(rows)
        hi = ni / float(len(cool))
        Ni += ni
        Hi += hi
        writer.writerow([cat.encode("utf8"), ni, hi, Ni, "{0:.2f}".format(Hi)])
    writer.writerow([u"Total", Ni, "{0:.2f}".format(Hi), Ni, "{0:.2f}".format(Hi)])


#===============================================================================
# ACT 2.2 USTED LABORAL
#===============================================================================

USTED_VARS = {1: u"Patrón o empleado",
              2: u"Trabajador por su cuenta",
              3: u"Obrero o empleado",
              4: u"Trabajador sin salario"}

with open("tables/act3_2_{}.csv".format("usted_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Situación Laboral".encode("utf8"),
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    Ni, Hi = 0, 0
    for idx, values in enumerate(sorted(USTED_VARS.items())):
        k, cat = values
        rows = cool.filter(lambda r: int(r["USTED"]) == k)
        ni = len(rows)
        hi = ni / float(len(cool))
        Ni += ni
        Hi += hi
        writer.writerow([(unicode(idx + 1) + "- "+ cat).encode("utf8"),
                          ni, hi, Ni, "{0:.2f}".format(Hi)])
    writer.writerow([u"Total", Ni, "{0:.2f}".format(Hi), Ni, "{0:.2f}".format(Hi)])


#===============================================================================
# ACT 4.1 y 4.2 EDAD
#===============================================================================

edad_freq = {}
modes = []
high = None
for edad in cool.column("EDAD"):
    edad = int(edad)
    edad_freq[edad] = edad_freq.get(edad, 0) + 1
    if high == None or high < edad_freq[edad]:
        mode = [edad]
        high = edad_freq[edad]
    elif high == edad_freq[edad]:
        modes.append(edad)

with open("tables/act4_1_{}.csv".format("edad_freq"), "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Edad".encode("utf8"),
                     u"Frecuencia Absoluta (ni)",
                     u"Frecuencia Relativa (hi)",
                     u"Frecuencia Absoluta Acumulada (Ni)",
                     u"Frecuencia Relativa Acumulada (Hi)"])
    Ni, Hi = 0, 0
    for edad, ni in sorted(edad_freq.items()):
        hi = ni / float(len(cool))
        Ni += ni
        Hi += hi
        writer.writerow([edad, ni, hi, Ni, "{0:.2f}".format(Hi)])
    writer.writerow([u"Total", Ni, "{0:.2f}".format(Hi), Ni, "{0:.2f}".format(Hi)])
    writer.writerow([u"Media", "{0:.2f}".format(numpy.mean(edad_freq.keys()))])
    writer.writerow([u"Mediana", "{0:.2f}".format(numpy.median(edad_freq.keys()))])
    writer.writerow([u"Moda"] + mode)


#===============================================================================
# ACT 5.1
#===============================================================================

EDAD_INTER = [(10, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 69)]

edad_inter_freq = {}
for k, v in edad_freq.items():
    for idx, tops in enumerate(EDAD_INTER):
        li, ls = tops
        if k >= li and k <= ls:
            edad_inter_freq[idx] = edad_inter_freq.get(idx, 0) + v
            break


with open("tables/act5_1_{}.csv".format("edad_inter_freq"), "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Número de intervalo".encode("utf8"),
                     u"Valores que comprende",
                     u"Frecuencia",
                     u"Frecuencia relativa",
                     u"Frecuencia Relativa acumulada"])
    Hi = 0
    for idx, tops in enumerate(EDAD_INTER):
        tops = map(unicode, tops)
        ni = edad_inter_freq[idx]
        hi = ni / float(len(cool))
        Hi += hi
        writer.writerow([idx + 1, "-".join(tops), ni, hi, "{0:.2f}".format(Hi)])


#===============================================================================
# ACT 6.1
#===============================================================================

def steam_and_leaft(arr):
    arr = map(str, arr)
    sal = {}
    for e in arr:
        steam = "0" if len(e) == 1 else e[:-1]
        if steam not in sal:
            sal[steam] = []
        sal[steam].append(e if len(e) == 1 else e[-1])
        sal[steam].sort()
    return sorted(sal.items())


with open("tables/act6_1_{}.csv".format("talloyhojas"), "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([u"Frecuencia", u"Tallo", u"Hojas"])
    for t, h in steam_and_leaft(cool.column("EDAD")):
        ni = len(h)
        h = " ".join(h)
        writer.writerow([ni, t, h])


#===============================================================================
# 7.1
#===============================================================================

SUELDO_INTER = [(0, 300), (300, 600), (600, 1000), (1000, 2000), (2000, 2200)]

bi_table = {}

for var, label in SEXO_VARS.items():
    sueldos = []
    for li, ls in SUELDO_INTER:

        last = (li, ls) == SUELDO_INTER[-1]

        def sueldo_edad_filter(r):
            sueldo = int(r["SUELDO"])
            sexo = int(r["SEXO"])
            if last:
                return sexo == var and sueldo >= li and sueldo <= ls
            return sexo == var and sueldo >= li and sueldo < ls

        rows = cool.filter(sueldo_edad_filter)
        sueldos.append(len(rows))
    bi_table[label] = sueldos

with open("tables/act_7_sexo_x_edad.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow(["Sexo/Sueldo"] +
                    ["{} a {}".format(*l) for l in SUELDO_INTER] +
                    ["Total"])
    totcols = [0] * len(SUELDO_INTER)
    totot = 0
    for sex, values in bi_table.items():
        totcols = map(lambda v: sum(v), zip(totcols, values))
        totot += sum(values)
        writer.writerow([sex.encode("utf8")] + values + [sum(values)])
    writer.writerow(["Totales"] + totcols +  [totot])
