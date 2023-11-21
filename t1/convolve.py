import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def getNext(quantidade, wn = [1,0.5]):
    for _ in range(quantidade):
        wn.append((wn[-1]*0.5)-(wn[-2]*0.07))
    return wn
    

def main():
    # p1
    s = [1,-0.5,0.07]
    w1 = [1,0.5,0.5**2, 0.5**3, 0.5**4]
    w2 = [1, -0.75, 1.5, -0.2, 0.3]

    print(np.convolve(s, w1))
    print(np.convolve(s, w2))

    """
    respostas:
    [ 1.  0.     0.07   0.035    0.0175  -0.0225  0.004375]
    [ 1.  -1.25  1.945  -1.0025  0.505   -0.164   0.021 ]

    conclusao: a convolucao w1 parece gerar um resultado mais proximo
    do sistema identidade (impulso), se aproximando do resultado esperado
    para remover o ruído inserido no sinal s. Já a convolucao w2 parece
    realizar o oposto, se distanciando do sinal impulso.
    """

    # w2
    alphabet = np.array([1+1j,1-1j,-1+1j,-1-1j])
    s = np.random.choice(alphabet,(500,))
    simbolosDiferentes = set()
    x = np.convolve(s, [1,-0.5,0.07])
    for simbolo in x:
        if simbolo not in simbolosDiferentes:
            simbolosDiferentes.add(simbolo)
    
    print(f"Há {len(simbolosDiferentes)} simbolos diferentes no sinal x") #: 68

    y1 = np.convolve(x, w1)
    y2 = np.convolve(x, w2)
    y3 = np.convolve(x, getNext(100))
    if True:
        # sinal original
        plt.scatter(x=np.real(s),y=np.imag(s), color='blue', alpha=0.3)
        plt.show()
        # imprime o grafico de linha do modulo dos valores
        plt.plot(np.abs(s), color='blue')
        plt.show()

        # sinal transmitido
        plt.scatter(x=np.real(x),y=np.imag(x), color='red', alpha=0.3)
        plt.show()
        # imprime o grafico de linha do modulo dos valores
        plt.plot(np.abs(x), color='red')
        plt.show()

        # sinal corrigido com filtro 1
        plt.scatter(x=np.real(y1),y=np.imag(y1), color='orange', alpha=0.3)
        plt.show()
        # imprime o grafico de linha do modulo dos valores
        plt.plot(np.abs(y1), color='orange')
        plt.show()

        # sinal corrigido com filtro 2
        plt.scatter(x=np.real(y2),y=np.imag(y2), color='gray', alpha=0.3)
        plt.show()
        # imprime o grafico de linha do modulo dos valores
        plt.plot(np.abs(y2), color='gray')
        plt.show()

        # sinal corrigido com filtro calculado com 100 termos
        plt.scatter(x=np.real(y3),y=np.imag(y3), color='green', alpha=0.3)
        plt.show()
        # imprime o grafico de linha do modulo dos valores
        plt.plot(np.abs(y3), color='green')
        plt.show()

    sigma = 0.2
    eta=sigma*np.random.randn(x.size,)+sigma*1j*np.random.randn(x.size,)    #sigma é o desvio padrão
    r=x+eta

    # plota r e x no mesmo grafico de plt
    plt.scatter(x=np.real(x),y=np.imag(x), color='blue', label='sinal depois de transmitido', alpha=0.3)
    plt.scatter(x=np.real(r),y=np.imag(r), color='red', label='sinal transmitido com ruído', alpha=0.3)
    plt.legend(loc='lower right', fontsize=8)
    plt.show()

    y1 = np.convolve(r, w1)
    y2 = np.convolve(r, w2)
    y3 = np.convolve(r, getNext(100))

    plt.scatter(x=np.real(s),y=np.imag(s), color='blue', label='sinal entrada', alpha=0.3)
    plt.scatter(x=np.real(y1),y=np.imag(y1), color='red', label='sinal de saida', alpha=0.3)
    plt.legend(loc='lower right', fontsize=8)
    plt.title('filtro 1')
    plt.show()

    plt.scatter(x=np.real(s),y=np.imag(s), color='blue', label='sinal entrada', alpha=0.3)
    plt.scatter(x=np.real(y2),y=np.imag(y2), color='red', label='sinal de saida', alpha=0.3)
    plt.legend(loc='lower right', fontsize=8)
    plt.title('filtro 2')
    plt.show()

    plt.scatter(x=np.real(s),y=np.imag(s), color='blue', label='sinal entrada', alpha=0.3)
    plt.scatter(x=np.real(y3),y=np.imag(y3), color='green', label='sinal de saida', alpha=0.3)
    plt.legend(loc='lower right', fontsize=8)
    plt.title('filtro calculado com 100 termos')
    plt.show()



main()
