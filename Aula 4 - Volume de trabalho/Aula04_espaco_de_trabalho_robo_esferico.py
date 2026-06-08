import numpy as np
import matplotlib.pyplot as plt

# Espaço de trabalho do manipulador esférico

# origem
O = np.array([0, 0, 0])

# limites das juntas
k1min, k1max = 15, 15                    # elo fixo k1
theta1min, theta1max = 0, np.pi         # rotação theta1
theta2min, theta2max = -np.pi/4, np.pi/4 # rotação theta2
k2min, k2max = 10, 20                   # elo k2

# figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# discretização
k = np.arange(0, 1.01, 0.1)

# malha paramétrica
K1, THETA1, THETA2, K2 = np.meshgrid(k, k, k, k)

# Equação do manipulador

X = (
    O[0]
    + np.cos(theta1min + THETA1 * (theta1max - theta1min))
    * (k2min + K2 * (k2max - k2min))
)

Y = (
    O[1]
    + np.sin(theta1min + THETA1 * (theta1max - theta1min))
    * np.cos(theta2min + THETA2 * (theta2max - theta2min))
    * (k2min + K2 * (k2max - k2min))
)

Z = (
    O[2]
    + (k1min + K1 * (k1max - k1min))
    + np.sin(theta2min + THETA2 * (theta2max - theta2min))
    * (k2min + K2 * (k2max - k2min))
)

# plotagem
ax.scatter(X, Y, Z, c='r', marker='o', s=5)

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
plt.title('Espaço de Trabalho do Manipulador Esférico')

# layout
plt.tight_layout()

# exibe
plt.show()