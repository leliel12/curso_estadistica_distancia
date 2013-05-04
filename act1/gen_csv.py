#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

import csvcool

with open("EPH.csv") as fp:
    cool = csvcool.read(fp, encoding="utf8")

#===============================================================================
# ACT 2.1 SEXO
#===============================================================================

SEXO_VARS = {1: u"Varón",
             2: u"Mujer"}


with open("tables/act2_1_{}.csv".format("sexo_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Sexo", u"Frecuencia"])
    cnt = 0
    for k, cat in sorted(SEXO_VARS.items()):
        rows = cool.filter(lambda r: int(r["SEXO"]) == k)
        writer.writerow([cat.encode("utf8"), len(rows)])
        cnt += len(rows)
    writer.writerow([u"Total", cnt])


#===============================================================================
# ACT 2.1 CIVIL
#===============================================================================

CIVIL_VARS = {1: u"Soltero",
              2: u"Unido",
              3: u"Casado",
              4: u"Separado/divorciado",
              5: u"Viudo"}

with open("tables/act2_1_{}.csv".format("civil_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Estado Civil", u"Frecuencia"])
    cnt = 0
    for k, cat in sorted(CIVIL_VARS.items()):
        rows = cool.filter(lambda r: int(r["CIVIL"]) == k)
        writer.writerow([cat.encode("utf8"), len(rows)])
        cnt += len(rows)
    writer.writerow([u"Total", cnt])


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
                     u"Frecuencia"])
    cnt = 0
    for k, cat in sorted(ESTUD_VARS.items()):
        rows = cool.filter(lambda r: int(r["ESTUD"]) == k)
        writer.writerow([cat.encode("utf8"), len(rows)])
        cnt += len(rows)
    writer.writerow([u"Total", cnt])

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

    writer.writerow([u"Vivienda".encode("utf8"), u"Frecuencia"])
    cnt = 0
    for k, cat in sorted(VIVIEN_VARS.items()):
        rows = cool.filter(lambda r: int(r["VIVIEN"]) == k)
        writer.writerow([cat.encode("utf8"), len(rows)])
        cnt += len(rows)
    writer.writerow([u"Total", cnt])


#===============================================================================
# ACT 2.1 USTED LABORAL
#===============================================================================

USTED_VARS = {1: u"Patrón o empleado",
              2: u"Trabajador por su cuenta",
              3: u"Obrero o empleado",
              4: u"Trabajador sin salario"}

with open("tables/act3_2_{}.csv".format("usted_freq"), "w") as fp:
    writer = csv.writer(fp)

    writer.writerow([u"Situación Laboral".encode("utf8"), u"Frecuencia"])
    cnt = 0
    for idx, values in enumerate(sorted(USTED_VARS.items())):
        k, cat = values
        rows = cool.filter(lambda r: int(r["USTED"]) == k)
        writer.writerow([(unicode(idx) + "- "+ cat).encode("utf8"), len(rows)])
        cnt += len(rows)
    writer.writerow([u"Total", cnt])

