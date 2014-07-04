
import numpy as np

a = 20.458643709
b = -0.2412979503
def reg(xi):
    return a + b * xi


x = map(float,[
27, 61, 37, 23, 46, 58, 29, 36, 64, 40,
])
y = map(float, [
15,
6,
10,
18,
9,
7,
14,
11,
5,
8,
])
yr = map(reg, y)

acum = 0
for yi, yir in zip(y, yr):
    acum += (yi - yir) ** 2


print acum / 8


#~ SCR = []
#~ SCE = []
#~ SCT = []
#~ for idx, yi in enumerate(y):
    #~ yie = ye[idx]
    #~ SCR.append((yie - np.average(y)) ** 2)
    #~ SCE.append((yi - yie) ** 2)
    #~ SCT.append((yi - np.average(y)) ** 2)
#~
#~ SCT = sum(SCT)
#~ SCR = sum(SCR)
#~ SCE = sum(SCE)
#~
#~ b = 1.1643859049
#~ Sb = []
#~ for xi in x:
    #~ Sb.append((xi - np.average(x)) ** 2)
#~ Sb = sum(Sb)
#~
#~ print "Sb =", Sb
#~ print "t =", b / Sb
#~ print len(x)
#~
#~
#~
#~
#~
#~
#~
