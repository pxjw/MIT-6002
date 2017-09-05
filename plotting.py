#! /usr/bin/python
# -*- coding: utf-8 -*-

import pylab
# from matplotlib.font_manager import FontProperties
# import matplotlib.pyplot as plt
# import numpy as np
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


# from matplotlib.font_manager import ttfFontProperty
# import matplotlib.pyplot as plt
# import os
# import os.path
# import numpy as np
# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,7,3,5])
# # pylab.show()
#
# # pylab.savefig("graph1")
# pylab.plot([1,2,3,4],[2,3,4,5])
# # pylab.savefig("newgra")

# fontManager.ttflist

# font = ttfFontProperty(fname=r"c:\windows\fonts\simsun.ttc", size=14)

pylab.figure(2)
pylab.title("XiaoYing financing, 6 month blue/ 12 moth red,30 year values;re cost 10000")
pylab.xlabel("year")
pylab.ylabel("values")

firstmoney=50000
accuessrate=0.072

year=30
values=[]

exprate=0.03
for i in range(year+1):
    values.append(firstmoney)
    firstmoney+=firstmoney*accuessrate
    firstmoney-=firstmoney*exprate
    firstmoney+=10000

pylab.plot(range(year+1),values,'b')


secondmoney=50000
Xrate=0.08

year=30
xvalue=[]
for ix in range(year+1):
    xvalue.append(secondmoney)
    secondmoney+=secondmoney*Xrate
    secondmoney-=secondmoney*exprate
    secondmoney+=10000

pylab.plot(range(year+1),xvalue,'r')

# pylab.savefig("xiaoying rev")


# pylab.show()
# pylab.savefig("xiaoying rev recost")