import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
import matplotlib.gridspec as gs
from math import fabs

def sin_of_x(x):
	return np.sin(x)


## create the MC data set
mc_samples = 100

rands_1 = np.random.random_sample([mc_samples])
rands_2 = np.random.random_sample([mc_samples])
mc_data_x = np.zeros(mc_samples)
mc_data_y = np.zeros(mc_samples)
mc_data_colors = []
mc_data_integral = []
mc_percent_error = []
num_hits = 0
analytical_value = 2.0
for i in range(mc_samples):
	mc_data_x[i] = rands_1[i]*np.pi
	mc_data_y[i] = rands_2[i]*1.0
	if mc_data_y[i] <= sin_of_x(mc_data_x[i]):
		mc_data_colors.append('#33BEFF')
		num_hits += 1
	else:
		mc_data_colors.append('#4B7B92')

	# i + 1 = number of samples at a given iteration
	calculated_value = np.pi*(float(num_hits)/(i+1))
	mc_data_integral.append(calculated_value)
	mc_percent_error.append(100.0*(fabs((calculated_value-analytical_value)/analytical_value)))

# covert colors list to np.array, not positive if necessary
mc_data_colors = np.array(mc_data_colors)
mc_data_integral = np.array(mc_data_integral)


# create basic figure with sin function plotted and sub-figure to see accuracy
fig = plt.figure()
plots_grid = gs.GridSpec(2,3)
ax1 = fig.add_subplot(plots_grid[0:,:2])
ax1.set_xlim((0.0, np.pi))
ax1.set_ylim(0.0, 1.0)
ax1.set_xticks([0.0, 0.25*np.pi, 0.5*np.pi, 0.75*np.pi, np.pi])
ax1.set_xticklabels(["$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])


ax2 = fig.add_subplot(plots_grid[0,2])
ax2.set_xlim(0, mc_samples )
ax2.set_ylim(0.0, 1.0*np.pi)

ax3 = fig.add_subplot(plots_grid[1,2])
ax3.set_xlim(0, mc_samples )
ax3.set_ylim(0.0, 100)

x_vals = np.arange(0.0, np.pi, 0.01)
ax1.plot(x_vals, sin_of_x(x_vals), color='black', lw=2)






# Construct the scatter plot to update during animation
scat = ax1.scatter([], [])
err_plot = ax2.plot([], [], lw=2)

scat = ax1.scatter(mc_data_x,mc_data_y,color=mc_data_colors)

print len(mc_data_integral)
print len(mc_percent_error)
print len(list(range(1,mc_samples)))
print range(1,mc_samples)
integral_value_plot = ax2.plot(list(range(1,mc_samples+1)) ,mc_data_integral)
percent_error_plot = ax3.plot(list(range(1,mc_samples+1)) ,mc_percent_error)

#def init():
#	scat.set_offsets([])
#	integral_value_plot.set_data([])
#	return scat, integral_value_plot

# batcher should be an even divisor of mc_samples, plots points in batches
#batcher = 10
#def animate(i):
#	x = mc_data_x[:i*batcher]		
#	y = mc_data_y[:i*batcher]		
#	colors = mc_data_colors[:i*batcher]		
#
#	data = np.hstack(zip(x, y))
#
#	scat.set_offsets(data)
#	scat.set_edgecolors(colors)
#	scat.set_facecolors(colors)
#
#	x_err = np.arange[(i*batcher)+1]
#	y_err = mc_data_integral[:i*batcher]
#
#	err_plot.set_data(x_err[1:], y_err)
#
#	return scat, err_plot
#
#ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(1,(mc_samples/batcher)),  interval=1,  blit=False, repeat=False)

plt.show()


