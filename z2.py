import numpy as np
import matplotlib.pyplot as plt

with open("zad2_bat_2_read.txt") as file:
	A=np.loadtxt(file)
time_s = A[:,0]
U_volts = A[:,1]
mass = 2e-3
I = 15.80e-6
# dT = np.average(np.gradient(time_s))
# dUdT = np.gradient(U_volts, dT)
gravimetric_capacitance_mahslashg = time_s*I/1000/mass
differentiated_capacitance = np.zeros(len(gravimetric_capacitance_mahslashg)-1)

for i in range(len(gravimetric_capacitance_mahslashg)-1):
	differentiated_capacitance[i]=(gravimetric_capacitance_mahslashg[i+1]-gravimetric_capacitance_mahslashg[i])/(time_s[i+1]-time_s[i])

plt.ion()

plt.figure(1)
plt.subplot(211)
plt.plot(gravimetric_capacitance_mahslashg, U_volts, "b-")
# plt.plot(charge, dUdT, "r-")
plt.grid()
plt.ylabel("Napiecie (V)")
plt.xlabel("Pojemnosc grawimetryczna (mAh/g)")
plt.subplot(212)
plt.plot(U_volts[:-1], differentiated_capacitance, "r-")
plt.grid()
plt.xlabel("Napiecie (V)")
plt.ylabel("Zróżniczkowana pojemnosc grawimetryczna (mAh/gs)")
plt.savefig("z2.png")
plt.show()
