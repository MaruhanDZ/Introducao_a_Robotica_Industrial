import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================================================
# Matrizes de rotação
# ============================================================

def rot_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])

def rot_y(theta):
    return np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rot_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

# ============================================================
# Objetos
# ============================================================

cube_origin = np.array([
    [ 3,  3,  3],
    [-3,  3,  3],
    [-3, -3,  3],
    [ 3, -3,  3],
    [ 3,  3, -3],
    [-3,  3, -3],
    [-3, -3, -3],
    [ 3, -3, -3]
])

cube_offset = cube_origin + np.array([10,10,10])

point = np.array([[3,3,3]])

# ============================================================
# Faces do cubo
# ============================================================

faces_idx = [
    [0,1,2,3],  # topo
    [4,5,6,7],  # base
    [0,1,5,4],  # frente
    [2,3,7,6],  # trás
    [0,3,7,4],  # direita
    [1,2,6,5]   # esquerda
]

# Cores das faces

face_colors = [
    'red',
    'blue',
    'green',
    'yellow',
    'orange',
    'purple'
]

# ============================================================
# Figura
# ============================================================

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

plt.subplots_adjust(left=0.25, bottom=0.3)

# ============================================================
# Sliders
# ============================================================

ax_x = plt.axes([0.25, 0.20, 0.65, 0.03])
ax_y = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_z = plt.axes([0.25, 0.10, 0.65, 0.03])

# Agora de 0° até 360°

slider_x = Slider(ax_x, 'Theta X', 0, 360, valinit=0)
slider_y = Slider(ax_y, 'Theta Y', 0, 360, valinit=0)
slider_z = Slider(ax_z, 'Theta Z', 0, 360, valinit=0)

# ============================================================
# Seleção do objeto
# ============================================================

radio_ax = plt.axes([0.02, 0.5, 0.15, 0.2])

radio = RadioButtons(
    radio_ax,
    ('Ponto', 'Cubo', 'Cubo Offset')
)

# ============================================================
# Configuração fixa da câmera
# ============================================================

CAM_ELEV = 25
CAM_AZIM = 35

# ============================================================
# Atualização
# ============================================================

def update(val):

    # Salva câmera atual
    elev = ax.elev
    azim = ax.azim

    ax.clear()

    theta_x = np.deg2rad(slider_x.val)
    theta_y = np.deg2rad(slider_y.val)
    theta_z = np.deg2rad(slider_z.val)

    R = rot_z(theta_z) @ rot_y(theta_y) @ rot_x(theta_x)

    selected = radio.value_selected

    if selected == 'Ponto':
        pts = point

    elif selected == 'Cubo':
        pts = cube_origin

    else:
        pts = cube_offset

    rotated = np.array([R @ p for p in pts])

    # --------------------------------------------------------
    # Ponto
    # --------------------------------------------------------

    if selected == 'Ponto':

        ax.scatter(
            rotated[:,0],
            rotated[:,1],
            rotated[:,2],
            s=100,
            color='red'
        )

    # --------------------------------------------------------
    # Cubos
    # --------------------------------------------------------

    else:

        faces = []

        for face in faces_idx:
            faces.append(rotated[face])

        cube = Poly3DCollection(
            faces,
            facecolors=face_colors,
            edgecolor='black',
            linewidths=1.5,
            alpha=0.6
        )

        ax.add_collection3d(cube)

    # --------------------------------------------------------
    # Eixos
    # --------------------------------------------------------

    lim = 15

    ax.set_box_aspect([1,1,1])

    # Eixo X
    ax.plot(
        [-lim, lim],
        [0,0],
        [0,0],
        linewidth=2
    )

    # Eixo Y
    ax.plot(
        [0,0],
        [-lim, lim],
        [0,0],
        linewidth=2
    )

    # Eixo Z
    ax.plot(
        [0,0],
        [0,0],
        [-lim, lim],
        linewidth=2
    )

    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_zlim([-lim, lim])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.grid(True)

    # Mantém a câmera fixa
    if elev == 30 and azim == -60:
        ax.view_init(elev=CAM_ELEV, azim=CAM_AZIM)
    else:
        ax.view_init(elev=elev, azim=azim)

    plt.draw()

# ============================================================
# Eventos
# ============================================================

slider_x.on_changed(update)
slider_y.on_changed(update)
slider_z.on_changed(update)

radio.on_clicked(update)

# Inicializa câmera
ax.view_init(elev=CAM_ELEV, azim=CAM_AZIM)

update(None)

plt.show()