import fastf1 as ff1
import matplotlib.font_manager as fm
import numpy as np
import matplotlib as mpl

from matplotlib import pyplot as plt
from labellines import labelLine, labelLines
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

ff1.Cache.enable_cache('cache')  # optional but recommended

year = 2021
wknd = 16
ses = 'R'
driver = 'BOT'
colorvalue = 'Speed'
colormap = mpl.cm.plasma

weekend = ff1.get_session(year, wknd)
session = ff1.get_session(year, wknd, ses)
laps = session.load_laps(with_telemetry=True)
lap = laps.pick_driver(driver).pick_fastest()

# Track with segments

x = lap.telemetry['X']              # values for x-axis
y = lap.telemetry['Y']              # values for y-axis
dydx = lap.telemetry[colorvalue]     # value to base color gradient on

# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Create a plot
fig, axs = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))

# Create title for plotting
prop = fm.FontProperties(fname='f1.otf')
fig.suptitle(f'{weekend.name} {year} - {driver} - {colorvalue}', fontproperties=prop, size=24, y=0.97)

# Create background track line
axs.plot(lap.telemetry['X'], lap.telemetry['Y'], color='black', linestyle='-', linewidth=16 ,zorder=0)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle='-', linewidth=3)

# Set the values used for colormapping
lc.set_array(dydx)

# Merge all line segments together
line = axs.add_collection(lc)

# Create legend
cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])
normlegend = mpl.colors.Normalize(vmin=dydx.min(), vmax=dydx.max())
legend = mpl.colorbar.ColorbarBase(cbaxes, norm=normlegend, cmap=colormap, orientation="horizontal")

# Adjust margins and turn of axis
plt.subplots_adjust(left=0.1 ,right=0.9, top=0.9, bottom=0.12)
axs.axis('off')

# Show the plot
plt.show()
