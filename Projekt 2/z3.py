 # -*- coding: utf-8 -*-
 # ^ polskie znaki
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='Comic Sans MS') #some men just want to watch the world cooooomiiiic saaaaaanssssss
m1, m2 = 2, 3
a=1
k=3


#http://www.wolframalpha.com/input/?i=%282k%2Fm1-w%5E2%29*%282k%2Fm2-w%5E2%29-2*k%5E2%2Fm1%2Fm2*%281%2Bcos%28k*a%29%29%3D0
q=np.linspace(0,np.pi/a,1000000)
plt.xlim(0, np.pi/a)
w1 = np.sqrt((k*(m1+m2)-k*np.sqrt(m1**2+m2**2+2*m1*m2*np.cos(a*q)))/m1/m2)
w2 = np.sqrt((k*(m1+m2)+k*np.sqrt(m1**2+m2**2+2*m1*m2*np.cos(a*q)))/m1/m2)
plt.plot(q,w1, label="Gałąź akustyczna")
plt.plot(q,w2, label="Gałąź optyczna")
plt.xlabel(u'wektor falowy $q$, jednostki umowne')
plt.ylabel(u'częstość kątowa $\omega$, jednostki umowne')
plt.title("Zależność dyspersyjna w zadaniu 3 dla pierwszej strefy Brillouina")
plt.legend()
plt.grid()
plt.savefig("z3.png")
plt.show()
