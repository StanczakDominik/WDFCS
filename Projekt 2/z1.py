import numpy as np

z = numer_zestawu = 3
i = numer_indeksu = 261604

Lambda = ((z+2)*100 + i%100)*1e-9
print(Lambda/1e-9) #nm
# dla 504 nm http://www.wolframalpha.com/input/?i=color+of+504+nm+light
#zielony?

# szerokość studni
d=10e-9

c=299792458
h=6.62607004e-34
m=9.10938356e-31
e=1.60217662e-19
from numpy import pi
hbar=h/2/pi

a=4.82

E1 = hbar**2/2/m*(1*pi/d)**2
print(E1/e) #eV
Eg=h*c/Lambda-2*E1
print(Eg/e) #eV

Eg_trial=Eg_CdS = 2.42*e #cadmium sulfide
Eg_MgSe=4*e #magnesium selenide? czy coś

E1_new = (h*c/Lambda-Eg_trial)/2
new_d = pi/(2*E1_new*m/hbar**2)**0.5
print(new_d/1e-9) #nm

d=hbar*pi*np.sqrt(1/m/(h*c/Lambda-Eg_trial))
print(d/1e-9)
