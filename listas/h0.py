# h0.py
#
# Definindo uma resposta ao impulso e seu gráfico
#
# 14 de abril de 2022

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h0 = [ 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0 ] # resposta ao impulso
n = np.arange(-2,11)

# parâmetros gerais da fonte
plt.rcParams.update({
    'text.usetex': True,  # usa latex para gerar o texto dos gráficos
    'font.family': 'serif',
#    'font.serif': ['Times'],
    'font.size': 15
})

# traçar gráficos
fig, ax = plt.subplots()

# Traça gráficos
ax.stem(n,h0, linewidth = 1.0, color='black', label='Resposta ao impulso')

# Ajusta faixa de valores dos eixos
#ax.axis([min(dt['deltax']), max(dt['deltax']), 0, 10])

# Define títulos dos eixos
plt.ylabel('$h_0$')
plt.xlabel('$n$')

# Gera legenda
#ax.legend(loc='lower right', bbox_to_anchor=(1, 1.02),borderaxespad=0,
#        frameon=False )#, mode='expand')

# Ativa grid
ax.grid(True)

# Grava figura (pode-se escolher o formato)
plt.savefig('h0.eps')

# Exibe figura
plt.show()



