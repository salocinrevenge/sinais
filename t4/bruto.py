import math
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import scipy.io as sio

Fs, y_raw = sio.wavfile.read('linkin-park-numb.wav')

print(f"formato antes de transformar: {y_raw.shape}")
y=(y_raw[:,0]+y_raw[:,1])/2
print(f"formato depois de transformar: {y.shape}")

print(f"{Fs} amostras por segundo")

def espectro(y, cor = 'tab:blue'):
    """ Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """  

    #modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    #frequencias avaliadas
    w = np.linspace(0,2*math.pi,Y.size)

    #exibe o grafico do espectro
    plt.figure() 
    plt.plot(w,Y, color=cor)
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xlim((0,2*math.pi))
    plt.show()
    
    return Y,w  

Y,w = espectro(y)
casas = 5
print(f"formato do espectro: {Y.shape}, minimo: {round(Y.min(),casas)}, maximo: {round(Y.max(),casas)}")
print(f"formato das frequencias: {w.shape}, minimo: {round(w.min(),casas)}, maximo: {round(w.max(),casas)}")

def reduzirAmostragem(y, M, Fs):
    """
    Rotina que reduz a taxa de amostragem de um sinal discreto for um fator M
    args:
        y: sinal discreto
        M: fator de reducao da taxa de amostragem
        Fs: taxa de amostragem original
    return:
        y_down: sinal discreto com taxa de amostragem reduzida
        Fs_down: taxa de amostragem reduzida
    
    o procedimento funciona da seguinte forma:
    a cada bloco de M amostras, basta reter uma amostra de y e descartar as M - 1 amostras seguintes.
    
    
    """
    y_down = y[::M]
    return y_down, Fs/M

y_down, Fs_down = reduzirAmostragem(y, 6, Fs)
Y,w = espectro(y_down, 'tab:orange')

Ms = [1, 3, 6, 12]
cores = ['tab:blue','tab:green','tab:orange', 'tab:red']
for i, M in enumerate(Ms):
    print(f"reduzindo a taxa de amostragem por um fator {M}")

    y_down, Fs_down = reduzirAmostragem(y, M, Fs)
    ipd.Audio(y_down,rate=Fs_down)
    Y,w = espectro(y_down, cores[i])
    print(f"formato do espectro: {Y.shape}, minimo: {round(Y.min(),casas)}, maximo: {round(Y.max(),casas)}")
    print(f"formato das frequencias: {w.shape}, minimo: {round(w.min(),casas)}, maximo: {round(w.max(),casas)}")