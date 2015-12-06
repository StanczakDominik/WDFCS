import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d,PiecewisePolynomial
from sympy import *


PATH_TO_FILE="zad1_dta_2_read.txt"


time=[]
temp=[]
Hf=[]
Mass=[]

with open("zad1_dta_2_read.txt") as file:
	data=np.loadtxt(file)
time = data[:, 0] #reads first column
temp = data[:, 1]
Hf = data[:, 2]
Mass = data[:, 3]


szkliste = (temp > temp[0]) & (temp < 473.0)

f=interp1d(temp,Hf,kind="linear")

y_interpolated=f(temp)
y_prime=np.diff(temp[szkliste])
plt.plot(temp,Hf,color="green",linewidth=3)
plt.plot(temp[szkliste],y_prime, color="red")
plt.title(u'Krzywa DSC materiału szklistego',fontsize=18)
plt.xlabel(u'Temp [°C]')
plt.ylabel('Heat flow [mW]')
plt.legend()
plt.show()
