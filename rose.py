import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


n = 800
A = 1.995653
B = 1.27689
C = 8


r = np.linspace(0, 1, n)
theta = np.linspace(-2, 20 * np.pi, n)
R, THETA = np.meshgrid(r, theta)


PEtalnum = 3.6
x = 1 - (1/2) * ((5/4) * (1 - (PEtalnum * THETA) % (2 * np.pi) / np.pi) ** 2 - 1/4) ** 2
phi = (np.pi / 2) * np.exp(-THETA / (C * np.pi))
y = A * (R ** 2) * (B * R - 1) ** 2 * np.sin(phi)
R2 = x * (R * np.sin(phi) + y * np.cos(phi))


X = R2 * np.sin(THETA)
Y = R2 * np.cos(THETA)
Z = x * (R * np.cos(phi) - y * np.sin(phi))


colors = np.zeros((10, 3))
colors[:, 0] = np.linspace(1, 0.25, 10) 
colormap = plt.get_cmap("Reds")


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, facecolors=colormap((Z - Z.min()) / (Z.max() - Z.min())), linewidth=0)


ax.view_init(elev=42, azim=-40.5)

plt.show()
