import numpy as np
import matplotlib.pyplot as plt

# Espaço de trabalho do manipulador

# origem
O = np.array([0, 0, 20])

# limites das juntas
theta1min, theta1max = 0, np.pi
theta2min, theta2max = 0, np.pi

k1min, k1max = 15, 15      # elo fixo k1
k2min, k2max = 10, 10      # elo fixo k2

k3min, k3max = 0, 20       # junta prismática

# figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# discretização
k = np.arange(0, 1.01, 0.1)

# malha paramétrica
THETA1, THETA2, K3 = np.meshgrid(k, k, k)

# Equação do manipulador

X = (
    O[0]
    + np.cos(theta1min + THETA1 * (theta1max - theta1min))
    * (k1min + 0 * (k1max - k1min))
    
    + np.cos(theta2min + THETA2 * (theta2max - theta2min))
    * (k2min + 0 * (k2max - k2min))
)

Y = (
    O[1]
    + np.sin(theta1min + THETA1 * (theta1max - theta1min))
    * (k1min + 0 * (k1max - k1min))
    
    + np.sin(theta2min + THETA2 * (theta2max - theta2min))
    * (k2min + 0 * (k2max - k2min))
)

Z = (
    O[2]
    - (k3min + K3 * (k3max - k3min))
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
plt.title('Espaço de Trabalho do Manipulador SCARA')

# layout
plt.tight_layout()

# exibe
plt.show()