import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

with open("zad1_dta_2_read.txt") as file:
	A=np.loadtxt(file)
time_minutes = A[:,0]
temperature_celsius = A[:,1]
HF_mW = A[:,2]
mass_g = A[:,3]

dT = np.average(np.gradient(temperature_celsius))
heat_flow_gradient = np.gradient(HF_mW, dT)

plt.ion()

plt.plot(temperature_celsius, HF_mW, "-", lw=3)
# plt.plot(temperature_celsius, heat_flow_gradient, "r-")
plt.grid(True)

for i, j, k, l, name in ((300, 430, 300, 490),(490,495, 300, 550), (500, 520, 480, 535), (580, 600, 540, 780), (743,780,608,780)):
	obszar = (i < temperature_celsius) * (temperature_celsius < j)
	t1 = temperature_celsius[obszar]
	HF = HF_mW[obszar]
	f = np.polyfit(t1, HF, 1)
	print(f)
	f1 = lambda x: f[0]*x + f[1]
	obszar2 = (k < temperature_celsius) * (temperature_celsius < l)
	t2 = temperature_celsius[obszar2]
	plt.plot(t2, f1(t2), "-", lw=2, label=name)


plt.title("DTA")
plt.ylabel("Przepływ ciepła (mW)")
plt.xlabel("Temperatura (stopnie Celsjusza)")
plt.ylim(min(HF_mW), max(HF_mW))
plt.savefig("z1.png")
plt.show()
