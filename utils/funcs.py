import numpy as np
import matplotlib.pyplot as plt

def plotar_seno_e_cosseno():
    plt.figure(figsize=(8, 6))
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, label='seno')
    plt.plot(x, z, label='cosseno')
    plt.grid()
    plt.legend()
   


# plotar uma exponencial decrescente
def plotar_exponencial_decrescente():
    plt.figure(figsize=(8, 6))
    x = np.linspace(-2, 2, 100)
    y = np.exp(-x)
    plt.plot(x, y)
    plt.grid()
    

# plontando uma janela retangular
def plotar_janela_retangular():
    plt.figure(figsize=(8, 6))
    x = np.linspace(-2, 2, 100)
    y = np.zeros(len(x))
    y[abs(x) <= 1] = 1
    plt.plot(x, y)
    plt.grid()