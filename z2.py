import numpy as np
import matplotlib.pyplot as plt

with open("zad2_bat_2_read.txt") as file:
	A=np.loadtxt(file)
time_s = A[:,0]
U_volts = A[:,1]
mass = 2e-6 #kg
I = 15.80e-6 #ampere
#czas w sekundach
#coulomb/kg
#ładunek przez masę daje miliculomby
# dT = np.average(np.gradient(time_s))
# dUdT = np.gradient(U_volts, dT)
gravimetric_capacitance_mahslashg = time_s*I/mass/3600
differentiated_capacitance = []
voltages=[]

for i in range(1,len(gravimetric_capacitance_mahslashg)-1):
	if(U_volts[i+1]-U_volts[i]!=0.0):
		differentiated_capacitance.append((gravimetric_capacitance_mahslashg[i+1]-gravimetric_capacitance_mahslashg[i-1])/(U_volts[i+1]-U_volts[i-1]))
		voltages.append(U_volts[i])

average=[]

for i in range(0,len(differentiated_capacitance)):
	przedzial = differentiated_capacitance[i-10:i+10]
	average.append(np.sum(przedzial)/len(przedzial))

doswiadczalna=max(gravimetric_capacitance_mahslashg)
teoretyczna = 0.9*442.1
fraction = doswiadczalna/teoretyczna
print(doswiadczalna, teoretyczna, fraction)

plt.ion()

plt.figure(1)
plt.title("Pojemność grawimetryczna")
plt.subplot(211)
plt.plot(gravimetric_capacitance_mahslashg, U_volts, "b-")
# plt.plot(charge, dUdT, "r-")
plt.grid()
plt.ylabel("Napiecie (V)")
plt.xlabel("Pojemnosc grawimetryczna (mAh/g)")
plt.subplot(212)
plt.plot(voltages, average, "r-")
plt.grid()
plt.xlabel("Napiecie (V)")
plt.ylabel("Zrózniczkowana pojemnosc grawimetryczna (mAh/gV)")
plt.savefig("z2.png")
plt.show()
