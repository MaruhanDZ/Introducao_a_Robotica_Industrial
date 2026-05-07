import numpy as np
import matplotlib.pyplot as plt

# Espaço de trabalho de robô cartesiano

# cria o ponto origem localizado em 0,0,0
O = np.array([0, 0, 0])

# define os comprimentos de cada elo
d1min, d1max = 10, 15       # x
d2min, d2max = 10, 20       # y
d3min, d3max = 10, 30       # z

# Criando figura 3D
fig = plt.figure()
# adiciona a projeção 3d na figura
ax = fig.add_subplot(111, projection='3d')
# cria um array que vai de 0 a 1 incrementando em 0.1
k = np.arange(0, 1.01, 0.1)
# cria uma meshgrid incrementando 0.1 em cada direção (x,y,z)
K1, K2, K3 = np.meshgrid(k, k, k)

X = O[0] + d1min + K1 * (d1max - d1min)    # calcula de forma vetorial todos os pontos x que o manipulador pode alcançar

Y = O[1] + d2min + K2 * (d2max - d2min)    # calcula de forma vetorial todos os pontos y que o manipulador pode alcançar

Z = O[2] + d3min + K3 * (d3max - d3min)    # calcula de forma vetorial todos os pontos em z que o manipulador pode alcançar

# plota todos os pontos calculador com polinhas vermelhas
ax.scatter(X, Y, Z, c='r', marker='o')
# define o nome de cada eixo
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# define a proporção de cada eixo sendo igual
ax.set_box_aspect([
    np.ptp(X),
    np.ptp(Y),
    np.ptp(Z)
])

# adiciona um titulo
plt.title('Espaço de Trabalho - Robô Cartesiano')
# ajusta a visualização para ficar próximo ao plotado
plt.tight_layout()
# mostra
plt.show()




