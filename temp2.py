import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t=np.linspace(-np.pi,np.pi,100,endpoint=True)
#Esto lo que reflejara es que entre a la facultad en 2014 y que hasta el momento sigo estudiando por eso lo he centrado en 2014 y tiene la amplitud de los 3 anios
s = 3*np.cos(t)+2014

line, = plt.plot(t, s,lw=2)
plt.xlim(-4,4)
plt.ylim(2010,2020)
plt.ylabel('Anio')
plt.xlabel('Anios transcurridos')
plt.show()

