import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt

cs = np.array(['r', 'b', 'b', 'b', 'b'])

plt.scatter(np.random.random(5), np.random.random(5), color=cs)

plt.show()
