import fastf1 as ff1
import fastf1
from timple.timedelta import strftimedelta

#Made using Fast F1 by Siddharth Tewari
fastf1.Cache.enable_cache('cache')

laps = ff1.get_session(2021, 'Turkey', 'R').load_laps()

td = laps.pick_driver('HAM').pick_fastest()['LapTime']
print("Hamilton")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('BOT').pick_fastest()['LapTime']
print("Bottas")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('VER').pick_fastest()['LapTime']
print("Verstappen")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('PER').pick_fastest()['LapTime']
print("Perez")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('NOR').pick_fastest()['LapTime']
print("NOR")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('RIC').pick_fastest()['LapTime']
print("Riccardo")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('SAI').pick_fastest()['LapTime']
print("Sainz")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('LEC').pick_fastest()['LapTime']
print("Leclerc")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('VET').pick_fastest()['LapTime']
print("Vettel")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('STR').pick_fastest()['LapTime']
print("Stroll")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('GAS').pick_fastest()['LapTime']
print("Gasly")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('TSU').pick_fastest()['LapTime']
print("Tsunoda")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('ALO').pick_fastest()['LapTime']
print("ALonso")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('OCO').pick_fastest()['LapTime']
print("Ocon")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('RAI').pick_fastest()['LapTime']
print("Kimi")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('GIO').pick_fastest()['LapTime']
print("Giovinazzi")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('RUS').pick_fastest()['LapTime']
print("Russell")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('LAT').pick_fastest()['LapTime']
print("Latifi")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('MSC').pick_fastest()['LapTime']
print("Mick")
print(strftimedelta(td, '%m:%s.%ms'))

td = laps.pick_driver('MAZ').pick_fastest()['LapTime']
print("Mazepin")
print(strftimedelta(td, '%m:%s.%ms'))
