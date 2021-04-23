import numpy as np
import matplotlib.pyplot as plt
#$$A = \left\{\begin{array}\\2x + 8y \\ 4x + 11y\end{array}\right. $$
A = np.array([[2, 8], [4, 11]])

def plotgraph(lines):
    plt.xlim(0, 15)
    plt.ylim(0, 15)
    plt.quiver([0, 0], [0, 0], lines[:, 0], lines[:, 1], angles='xy', scale_units='xy', scale=1, color=['red', 'blue'])
    plt.show()

plotgraph(A)