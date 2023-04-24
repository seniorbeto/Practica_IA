from os import path
OBJECTIVE = 22
INIT_TEMPERATURE = 16.0
INIT_THERMOSTAT_STATE = True # True = ON, False = OFF
COST_ON = 1.5
COST_OFF = 0.2
SOURCE_PATH = str(path.dirname(path.abspath(__file__)))
print(SOURCE_PATH)