import numpy as np
import matplotlib.pyplot as plt
import random

#primer punto.
x=[2.031331588946557076e+00, 5.886777538940683563e+00, 2.195744759275823021e+00, 6.821886748452244298e+00, 8.793952398085184141e-01, 2.951577398416659559e+00,4.454332895499525158e+00, -1.804396045394615955e+00, -5.841925974092386120e+00, -1.113495627653518838e+00]


def f(x, sigma):
    return (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*(x**2/(sigma**2)))

L=1
listaL=[]
sigma=np.linspace(1, 10,10)
#for j in range(10):
for i in range (10):
    L=L*f(x[i], sigma[i])
    listaL.append(L)

#segundo
def cd(h, sigma):
    return (f((sigma+h)/2, sigma)-f((sigma-h)/2, sigma))/h

der=[]
for i in range(10):
    s=cd(0.01, sigma[i])
    der.append(s)
listai=der

#tercer punto
def rapson( imax ):
    eps=0.2
    dx=0.3
    x=[2.031331588946557076e+00, 5.886777538940683563e+00, 2.195744759275823021e+00, 6.821886748452244298e+00, 8.793952398085184141e-01, 2.951577398416659559e+00,4.454332895499525158e+00, -1.804396045394615955e+00, -5.841925974092386120e+00, -1.113495627653518838e+00]
    for i in range(0, imax+1):
        F=f(x[i], 8)
        if np.abs(F)<=eps:
            break
        df= (f(x[i] + (dx/2))-f(x[i]-(dx/2)))/dx
        dx=-F/df
        x+=dx
    return(dx)

print(rapson(10))



plt.figure()
plt.hist( listaL)
plt.xlabel("sigma")
plt.ylabel("Derivada(sigam)")
plt.savefig("sigma.png")