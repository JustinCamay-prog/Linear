import numpy as np
import matplotlib.pyplot as plt

vectorA = np.array([2,0])
vectorB = np.array([2,-2])

scalar = np.arange(-3,3,1)

scalar1, scalar2 = np.meshgrid(scalar,scalar)
scalar1, scalar2 = np.meshgrid(scalar,scalar)
scalar1, scalar2 = np.meshgrid(scalar,scalar)
vectR = vectorA + vectorB


spanRx1 = scalar1 * vectorA[0] + scalar2 * vectorB[0]
spanRy1 = scalar1 * vectorA[1] + scalar2 * vectorB[1]

spanRx2 = scalar1 * vectorA[0] + scalar2 * vectorB[0]
spanRy2 = scalar1 * vectorA[1] + scalar2 * vectorB[1]

spanRx3 = scalar1 * vectorA[0] + scalar2 * vectorB[0]
spanRy3 = scalar1 * vectorA[1] + scalar2 * vectorB[1]

plt.scatter(spanRx1,spanRy1, s=10, alpha=0.75)
plt.scatter(spanRx2,spanRy2, s=10, alpha=0.75)
plt.scatter(spanRx3,spanRy3, s=10, alpha=0.75)

plt.xlim(-20,20)
plt.ylim(-20,20)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()