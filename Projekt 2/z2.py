import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.optimize
matplotlib.rc('font', family='Comic Sans MS') #some men just want to watch the world cooooomiiiic saaaaaanssssss

k = 1.38064852e-23
e = 1.60217662e-19
data = np.loadtxt("zad2_is_3_readable.txt")
Kelvin = 273.15
L=grubosc = 1.04e-3
S=powierzchnia = 18.9e-6
print(L/S)

T, R = temperatureC, resistanceOhm = data[:,0], data[:,1]
T+=Kelvin
G=1/R
conductivity = G*L/S

def linear_curve(x, a, b):
    return a*x+b
x = 1/T
y = np.log(conductivity*T/S)
coefficients, covs = scipy.optimize.curve_fit(linear_curve, x, y)
print(coefficients)
Eg=-coefficients[0]*k
print(Eg/e)
a, b = coefficients
sigma_zero = np.exp(b)
T_zero = Kelvin+25
conductivity_zero = sigma_zero/T_zero*np.exp(-Eg/k/T_zero)
print(conductivity_zero)
print(conductivity[0])

plt.title('Wykres Arrheniusa')
plt.plot(x,y, 'bo', label="Dane")
plt.plot(x,coefficients[1]+coefficients[0]*x, 'g--', label="Fit")
plt.xlabel(r'$T^{-1} [K^{-1}]$')
plt.ylabel(r'$\log{(\sigma T/S)}$, $[T] = 1K$, $[S] = 1m^2$, $[\sigma] = 1 S/m$')
plt.legend()
plt.grid()
plt.savefig('z2.png')
plt.show()
