import numpy as np
import matplotlib.pyplot as plt

# Espaço de trabalho de robô cilindrico

# cria o ponto origem localizado em 0,0,0
O = np.array([0, 0, 0])

# define os comprimentos de cada elo
d1min, d1max = 0, 15       # junta k1
thetamin, thetamax = 0, np.pi       # junta theta
d2min, d2max = 10, 30       # junta k2

# Criando figura 3D
fig = plt.figure()

# adiciona a projeção 3d na figura
ax = fig.add_subplot(111, projection='3d')

# cria um array que vai de 0 a 1 incrementando em 0.1
k = np.arange(0, 1.01, 0.1)

# cria uma meshgrid incrementando 0.1 em cada direção (x,y,z)
K1, theta, K2 = np.meshgrid(k, k, k)

X = O[0] + np.cos(thetamin + theta * (thetamax - thetamin)) * (d2min + K2 * (d2max - d2min))

Y = O[1] + np.sin(thetamin + theta * (thetamax - thetamin)) * (d2min + K2 * (d2max - d2min))

Z = O[2] + d1min + K1 * (d1max - d1min)

# plota os pontos
ax.scatter(X, Y, Z, c='r', marker='o')

# nomes dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# mesma escala nos eixos
ax.set_box_aspect([
    np.ptp(X),
    np.ptp(Y),
    np.ptp(Z)
])

# título
plt.title('Espaço de Trabalho - Robô Cilindrico')

# ajusta layout
plt.tight_layout()

# mostra gráfico
plt.show()