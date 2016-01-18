import numpy as np
import matplotlib.pyplot as plt

# plt.ion()
# plt.figure(1)
# plt.grid()
# plt.xlabel("2 Theta")
# plt.ylabel("Natezenie, w znormalizowanych arbitralnych jednostkach")
#
# for name in ("zad3_xrd_1.txt", "zad3_xrd_2.txt", "zad3_xrd_3.txt", "zad3_xrd_4.txt", "zad3_xrd_5.txt", "zad3_xrd_6.txt", "zad3_xrd_7.txt"):
# 	with open(name) as file:
# 		A=np.loadtxt(file)
# 	x = A[:,0]
# 	y = A[:,1]
# 	y = y/max(y)
# 	plt.plot(x, y, "-", label=name)

lambda_w=1.4767e-10
hkl = (0, 1, 2)
a = 3.15e-10
f0=1
f1=1
print("h\tk\tl\tn\td\t2T\tF")
ds = set()
doubleangles_maxes = []
Is_maxes = []
doubleangles_mins = []
Is_mins = []
for h in hkl:
	for k in hkl:
		for l in hkl:
			if(h==k==l==0):
				continue
			for n in range(1,2):
				d = a/np.sqrt(h**2+k**2+l**2)
				if d in ds:
					continue
				ds.add(d)
				sin=n*lambda_w/2./d
				if(sin>1 or sin<-1):
					# print("sin {0:.2f}".format(sin))
					continue
				doubletheta = 2*np.arcsin(sin)
				doubletheta_degrees = doubletheta*180/np.pi
				if(doubletheta_degrees>90 or doubletheta_degrees<20):
					# print("doubletheta_degrees {0:.2f}".format(doubletheta_degrees))
					continue
				I = (f0+f1*np.exp(1j*np.pi*(h+k+l)))**2
				if(I>1):
					doubleangles_maxes.append(doubletheta_degrees)
					Is_maxes.append(I)
				else:
					doubleangles_mins.append(doubletheta_degrees)
					Is_mins.append(I)
				print("{0:1d}\t{1}\t{2}\t{3}\t{4:1.4e}\t{5:1.4f}\t{6:1.4f}".format(h, k, l, n, d, doubletheta, I.real))

maxes = [I/max(Is_maxes)/10 for I in Is_maxes]
mins = [I/10 for I in Is_mins]

plt.plot(doubleangles_maxes, maxes, "ro", label="Wzmocnienia")
plt.plot(doubleangles_mins, mins, "bo", label="Wygaszenia")
plt.title("Dyfraktogram")
plt.legend()
plt.savefig("z3.png")
plt.show()
