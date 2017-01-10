import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection


xy = (np.random.random((5,2)))
xy = xy.reshape(-1, 1, 2)
segments = np.hstack([xy[:-1], xy[1:]])

#cs = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1)])

cs = np.array(['#e41a1c', '#377eb8', '#4daf4a'])

fig, ax = plt.subplots()


line_segments = LineCollection(segments, colors=cs)
#line_segments = LineCollection(segments, colors=cs)
#line_segments = LineCollection(segments, cmap=plt.cm.gist_ncar)
line_segments.set_array(np.random.random(xy.shape[0]))

ax.add_collection(line_segments)
ax.autoscale_view()
plt.show()


