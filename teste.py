## FUNCAO PLOTAR SENO E COSSENO
import numpy as np
import matplotlib.pyplot as plt

def plotar_seno_e_cosseno():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, label='seno')
    plt.plot(x, z, label='cosseno')
    plt.grid()
    plt.legend()
    plt.show()

plotar_seno_e_cosseno()
# plotar uma exponencial decrescente
def plotar_exponencial_decrescente():
    x = np.linspace(-2, 2, 100)
    y = np.exp(-x)
    plt.plot(x, y)
    plt.grid()
    plt.show()
    
plotar_exponencial_decrescente()



