# serie-fourier-pulso-retangular.py
#
# autor: Ronaldo de Freitas Zampolo
# data: 8 de outubro de 2019
#
# - gráfico dos coeficientes da série de Fourier de um pulso retangular periódico
# - gráfico de reconstrução parcial, com seleção do número de coeficientes a usar
# - cálculo e gráfico do erro de reconstrução.

import numpy as np
import matplotlib.pyplot as plt

# coeficientes da serie de Fourier
a = np.zeros((101,1))

a[ 0 ] = 1/2
for k in range(1,len(a)):
    a[ k ] = 0.5 * np.sin( k * np.pi / 2 ) / ( k * np.pi / 2 )

# Parametros
M = [ 0, 1, 3, 5, 10, 50, 100 ] # indice máximo do coeficiente a ser utilizado na reconstrução
N = 1000 # número de pontos do sinal a serem calculados
T = 1    # meio período do pulso retangular
t = np.linspace(-T,T,N) # vetor de amostras de tempo

#i = 0

xr = np.zeros(len(t)) # sinal de referência
for i in range(len(t)):
    if np.abs(t[i]) < (T/2):
        xr[i] = 1

xm = [] # inicialização do sinal reconstruído (lista vazia)
erro = []

for m in M:

    soma = a[0] * np.ones(len(t))    
    if m != 0:
        for i in range(1,m+1):
            soma += a[i] * 2 * np.cos( (i * np.pi / T ) * t )
    xm.append(soma)
    erro.append(xr-soma)
    

plt.figure()
plt.stem(a)
plt.grid(True)
plt.xlabel('$k$')
plt.ylabel('$a_k$')
plt.title('Coeficientes da série de Fourier')

plt.figure()
plt.plot(t,xm[0],'r',t,xm[1],'g',t,xm[2],'b', t, xm[3], 'c', t, xm[4], 'm', t, xm[5], 'y', t, xm[6],'k' )
plt.grid(True)
plt.xlabel('$t$')
plt.ylabel('$xm$')
plt.title('Sinal reconstruído')

plt.figure()
plt.plot(t,erro[0],'r',t,erro[1],'g',t,erro[2],'b', t, erro[3], 'c', t, erro[4], 'm', t, erro[5], 'y', t, erro[6],'k' )
plt.grid(True)
plt.xlabel('$t$')
plt.ylabel('$erro$')
plt.title('Erro de reconstrução')

plt.show()
