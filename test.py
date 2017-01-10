import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


rands_1 = np.random.random_sample(3,)
rands_2 = np.random.random_sample(3,)
rands_3 = np.random.random_sample(3,)

print rands_1
print rands_2
print rands_3

fig, ax = plt.subplots()


ax.scatter(rands_1, rands_2, c=rands_3)


plt.show()


