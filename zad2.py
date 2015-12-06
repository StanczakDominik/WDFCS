# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d,PiecewisePolynomial
from sympy import *


PATH_TO_FILE="zad2_bat_2_read.txt"
prad=float(15.8/1000000)
mass=float(2./1000000)
# time=[]
# voltage=[]


# inFile = open(PATH_TO_FILE)
# for line in inFile:
# 	#line = inFile.readline()
# 	fields=line.split()
# 	#print fields
# 	time.append(int(fields[0])
# 	voltage.append(fields[1].replace(",","."))





time=[]
voltage=[]


data = np.loadtxt(PATH_TO_FILE)
time = data[:, 0] #reads first column
voltage = data[:, 1]
capacity=prad*time/mass/3600
plt.title(u'Bateria litowa',fontsize=18)
#plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel(u'Pojemność grawimetryczna Q [mAh/g]')
plt.ylabel('Napięcie U [V]')
plt.legend()
plt.plot(capacity,voltage)
plt.show()
