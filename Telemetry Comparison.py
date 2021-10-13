import fastf1 as ff1
import matplotlib.font_manager as fm
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()

ff1.Cache.enable_cache('cache')  # optional but recommended

year = 2021
wknd = 16
ses = 'Q'
drv1 = 'VER'
drv2 = 'HAM'

weekend = ff1.get_session(year, wknd)
session = ff1.get_session(year, wknd, ses)
laps = session.load_laps(with_telemetry=True)

first_driver = laps.pick_driver(drv1)
first_driver_info = session.get_driver(drv1)
first_color = plotting.team_color(first_driver_info.team)
second_driver = laps.pick_driver(drv2)
second_driver_info = session.get_driver(drv2)
second_color = plotting.team_color(second_driver_info.team)

first_driver = laps.pick_driver(drv1).pick_fastest()
first_car = first_driver.get_car_data()
second_driver = laps.pick_driver(drv2).pick_fastest()
second_car = second_driver.get_car_data()

fig, ax = plt.subplots(6)

prop = fm.FontProperties(fname='F1.otf')
fig.suptitle(f'{first_driver_info.familyname} vs {second_driver_info.familyname} - Fastest lap - {weekend.name} {year} {ses}', fontproperties=prop, size=18)

l2, = ax[0].plot(second_car['Time'], second_car['Speed'], color=second_color)
l1, = ax[0].plot(first_car['Time'], first_car['Speed'], color=first_color)
ax[1].plot(second_car['Time'], second_car['RPM'], color=second_color)
ax[1].plot(first_car['Time'], first_car['RPM'], color=first_color)
ax[2].plot(second_car['Time'], second_car['nGear'], color=second_color)
ax[2].plot(first_car['Time'], first_car['nGear'], color=first_color)
ax[3].plot(second_car['Time'], second_car['Throttle'], color=second_color)
ax[3].plot(first_car['Time'], first_car['Throttle'], color=first_color)
ax[4].plot(second_car['Time'], second_car['Brake'], color=second_color)
ax[4].plot(first_car['Time'], first_car['Brake'], color=first_color)
ax[5].plot(second_car['Time'], second_car['DRS'], color=second_color)
ax[5].plot(first_car['Time'], first_car['DRS'], color=first_color)

ax[0].set_ylabel("Speed [km/h]")
ax[1].set_ylabel("RPM [#]")
ax[2].set_ylabel("Gear [#]")
ax[3].set_ylabel("Throttle [%]")
ax[4].set_ylabel("Brake [%]")
ax[5].set_ylabel("DRS")

ax[0].get_xaxis().set_ticklabels([])
ax[1].get_xaxis().set_ticklabels([])
ax[2].get_xaxis().set_ticklabels([])
ax[3].get_xaxis().set_ticklabels([])
ax[4].get_xaxis().set_ticklabels([])

fig.align_ylabels()
fig.legend((l1, l2), (f'{first_driver_info.familyname}', f'{second_driver_info.familyname}'), 'upper right')

plt.subplots_adjust(left=0.06 ,right=0.99, top=0.9, bottom=0.05)
plt.show()

