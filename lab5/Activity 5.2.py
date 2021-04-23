import numpy as np
import matplotlib.pyplot as plt
#$$A = \left\{\begin{array}\\2x + 8y \\ 4x + 11y\\ y + 5z\end{array}\right. $$
A = np.array([[2, 8, 0], [4, 11, 0], [0, 1, 5]])


def plotgraph(lines):
    fig = plt.figure()
    D1 = fig.gca(projection='3d')
    D1.set_xlim([0, 10])
    D1.set_ylim([0, 10])
    D1.set_zlim([0, 10])
    origin = (0, 0, 0)
    D1.quiver(origin, origin, origin,
               lines[:, 0], lines[:, 1], lines[:, 2],
               arrow_length_ratio=0.05, colors=['red', 'blue', 'green'])
    plt.show()

plotgraph(A)