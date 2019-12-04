import numpy as np
import matplotlib.pyplot as plt

archivo=np.loadtxt("monthrg.dat.txt")

año=[]
mes=[]
dat=[]
m=[]

for i in range(3476,len(archivo)):
    año.append(archivo[i,0])
    mes.append(archivo[i,1])
    dat.append(archivo[i,2])
    m.append(archivo[i,3])
    


def fourier():
    N=len(año)
    n=N
    lista_k=[]
    lista_f=[]
    for i in range(0, n):
        complejo_suma=complex(0.0, 0.0)
        for k in range(0, N):
            exponente=complex(0, ((2*np.pi*k)/N))
            complejo_suma+=m[i]*np.exp(exponente)
            lista_k.append(i)
            lista_f.append(complejo_suma)
        if m[i]==m[0]:
            omega=2*np.pi/año[i]
    print("el periodo es", " ", omega)
    
fourier()
            
plt.figure()
plt.plot(año,m)
plt.xlabel("tiempo")
plt.ylabel("manchas")
plt.savefig("solar.png")