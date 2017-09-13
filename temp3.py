import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

plt.subplot (111)

n=np.linspace(-np.pi,np.pi,100,endpoint=True)
#Esto lo que reflejara es que entre a la facultad en 2014 y que hasta el momento sigo estudiando por eso lo he centrado en 2014 y tiene la amplitud de los 3 anios               
m = 3*np.cos(n)

x = [   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22]
y = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

line, = plt.plot(n, m,,x,y) 



ax = plt.subplot(211)

t=np.linspace(-np.pi,np.pi,100,endpoint=True)
#Esto lo que reflejara es que entre a la facultad en 2014 y que hasta el momento sigo estudiando por eso lo he centrado en 2014 y tiene la amplitud de los 3 anios
s = 3*np.cos(t)+2014

line, = plt.plot(t, s,lw=2)
plt.xlim(-4,4)
plt.ylim(2010,2020)
plt.ylabel('Anio')
plt.xlabel('Anios transcurridos')
plt.savefig('temp3.png')
plt.show()

