import numpy as np
import matplotlib.pyplot as plt

# Cria um vetor de valores x de 0 a 2*pi (uma volta completa)
x = np.linspace(0, 2 * np.pi, 100)

# Calcula os valores da função seno para cada valor de x
y = np.sin(x)

# Cria o gráfico
plt.figure(figsize=(8, 4))  # Define o tamanho da figura
plt.plot(x, y, label='Senoide')  # Plota a senoide
plt.xlabel('Ângulo (radianos)')  # Rótulo do eixo x
plt.ylabel('Seno(x)')  # Rótulo do eixo y
plt.title('Gráfico de uma Senoide')  # Título do gráfico
plt.grid(True)  # Ativa a grade no gráfico
plt.legend()  # Mostra a legenda

# Exibe o gráfico
plt.show()
