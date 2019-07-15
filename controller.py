
# Common Imports
import time

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import user_input
from action import ActionController
import display

MEASURE_PER_TWO = 40 # Also found in action.py
MAX_STEPS = 99980

class Controller:
    def __init__(self):
        self.sensor = SenseHat()
        self.stepSpan = [0 for i in range(MEASURE_PER_TWO)]
        self.totalSteps = 0


    def runWatch(self, actCon):
        self.sensor.set_rotation(180)
        # MAIN CONTROL LOOP
        while (True):
            mode = user_input.getUpdates(self.sensor)
            if (self.totalSteps < MAX_STEPS):
                actCon.detectSteps(self)

            display.update(self, self.sensor, mode)
            


if __name__ == '__main__':
    
    con = Controller()
    actCon = ActionController()

    con.runWatch(actCon)
