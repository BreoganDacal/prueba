import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define los vértices de la pirámide
vertices = np.array([
    [0, 0, 1],  # vértice superior
    [-1, -1, 0],  # base
    [1, -1, 0],  
    [1, 1, 0],  
    [-1, 1, 0]
])

# Define los vértices de la pirámide invertida (Merkaba)
vertices_invertidos = vertices.copy()
vertices_invertidos[:, 2] = -vertices_invertidos[:, 2]

# Define las caras de la pirámide
caras = [
    [vertices[0], vertices[1], vertices[2]],  
    [vertices[0], vertices[2], vertices[3]],  
    [vertices[0], vertices[3], vertices[4]],  
    [vertices[0], vertices[4], vertices[1]],  
    [vertices[1], vertices[2], vertices[3], vertices[4]]  
]

# Define las caras de la pirámide invertida
caras_invertidas = [
    [vertices_invertidos[0], vertices_invertidos[1], vertices_invertidos[2]],  
    [vertices_invertidos[0], vertices_invertidos[2], vertices_invertidos[3]],  
    [vertices_invertidos[0], vertices_invertidos[3], vertices_invertidos[4]],  
    [vertices_invertidos[0], vertices_invertidos[4], vertices_invertidos[1]],  
    [vertices_invertidos[1], vertices_invertidos[2], vertices_invertidos[3], vertices_invertidos[4]]  
]

# Función de actualización para la animación
def actualizar(num):
    ax.clear()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    
    # Rotación alrededor del eje Z para la pirámide normal
    angulo = np.radians(num)
    rot_matriz = np.array([
        [np.cos(angulo), -np.sin(angulo), 0],
        [np.sin(angulo), np.cos(angulo), 0],
        [0, 0, 1]
    ])
    
    vertices_rotados = np.dot(vertices, rot_matriz.T)
    
    caras_rotadas = [
        [vertices_rotados[0], vertices_rotados[1], vertices_rotados[2]],  
        [vertices_rotados[0], vertices_rotados[2], vertices_rotados[3]],  
        [vertices_rotados[0], vertices_rotados[3], vertices_rotados[4]],  
        [vertices_rotados[0], vertices_rotados[4], vertices_rotados[1]],  
        [vertices_rotados[1], vertices_rotados[2], vertices_rotados[3], vertices_rotados[4]]  
    ]
    
    # Rotación alrededor del eje Z para la pirámide invertida (sentido contrario)
    angulo_inv = np.radians(-num)
    rot_matriz_inv = np.array([
        [np.cos(angulo_inv), -np.sin(angulo_inv), 0],
        [np.sin(angulo_inv), np.cos(angulo_inv), 0],
        [0, 0, 1]
    ])
    
    vertices_rotados_inv = np.dot(vertices_invertidos, rot_matriz_inv.T)
    
    caras_rotadas_inv = [
        [vertices_rotados_inv[0], vertices_rotados_inv[1], vertices_rotados_inv[2]],  
        [vertices_rotados_inv[0], vertices_rotados_inv[2], vertices_rotados_inv[3]],  
        [vertices_rotados_inv[0], vertices_rotados_inv[3], vertices_rotados_inv[4]],  
        [vertices_rotados_inv[0], vertices_rotados_inv[4], vertices_rotados_inv[1]],  
        [vertices_rotados_inv[1], vertices_rotados_inv[2], vertices_rotados_inv[3], vertices_rotados_inv[4]]  
    ]
    
    ax.add_collection3d(Poly3DCollection(caras_rotadas, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.6))
    ax.add_collection3d(Poly3DCollection(caras_rotadas_inv, facecolors='magenta', linewidths=1, edgecolors='b', alpha=0.6))

# Configurar la animación
ani = animation.FuncAnimation(fig, actualizar, frames=360, interval=50)

plt.show()
