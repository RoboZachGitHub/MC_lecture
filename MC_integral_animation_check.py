import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection

def sin_of_x(x):
	return np.sin(x)

# create basic figure with sin function plotted
fig, ax = plt.subplots()
ax = plt.axes()
ax.set_xlim((0.0, np.pi))
ax.set_ylim(0.0, 1.0)
ax.set_xticks([0.0, 0.25*np.pi, 0.5*np.pi, 0.75*np.pi, np.pi])
ax.set_xticklabels(["$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.ylabel('sin(x)')
plt.xlabel('x')
x_vals = np.arange(0.0, np.pi, 0.01)
ax.plot(x_vals, sin_of_x(x_vals), color='black', lw=2)


# create the MC data set
mc_samples = 300

rands_1 = np.random.random_sample([mc_samples])
rands_2 = np.random.random_sample([mc_samples])
mc_data_x = np.zeros(mc_samples)
mc_data_y = np.zeros(mc_samples)
mc_data_colors = []
mc_data_z = []
for i in range(mc_samples):
	mc_data_x[i] = rands_1[i]*np.pi
	mc_data_y[i] = rands_2[i]*1.0
	if mc_data_y[i] <= sin_of_x(mc_data_x[i]):
		mc_data_colors.append('r')
	else:
		mc_data_colors.append('b')

mc_data_colors = np.array(mc_data_colors)

scatter = ax.scatter(mc_data_x, mc_data_y, color=mc_data_colors)

#scatter = ax.scatter([], [], [])
#
#def animate(frames):
#	
#	
#
#	scatter(mc_data_x[:frames], mc_data_y[:frames])
#	return scatter
#
#
#ani = animation.FuncAnimation(fig, animate, frames=mc_samples,  interval=1000,  blit=False, repeat=False)

plt.show()


