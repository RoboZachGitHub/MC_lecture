import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def f(x):
	return np.sin(x)

x_vals = np.arange(0.0, np.pi, 0.01)

rands_1 = np.random.random_sample([100])
rands_2 = np.random.random_sample([100])
rand_xs = []
rand_ys = []
for x in rands_1:
	rand_xs.append(x*np.pi)

for y in rands_2:
	rand_ys.append(y*1.0)

fig, ax = plt.subplots()
ax.set_xlim((0.0, np.pi))
ax.set_xticks([0.0, 0.25*np.pi, 0.5*np.pi, 0.75*np.pi, np.pi])
ax.set_xticklabels(["$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])


plt.ylabel('sin(x)')
plt.xlabel('x')
ax.plot(x_vals, f(x_vals))
ax.plot(rand_xs, rand_ys, marker='o', linestyle='none')


plt.show()


