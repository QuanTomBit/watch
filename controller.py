
# Common Imports
import time

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import user_input
import action
import display

MEASURE_PER_TWO = 40 # Also found in action.py
MAX_STEPS = 99990

class Controller:
    def __init__(self):
        self.sensor = SenseHat()
        self.stepSpan = [0 for i in range(MEASURE_PER_TWO)]
        self.totalSteps = 3450


    def runWatch(self):
        # MAIN CONTROL LOOP
        while (True):
            mode = user_input.getUpdates(self.sensor)
            if (self.totalSteps < MAX_STEPS):
                action.detectSteps(self)

            display.update(self, self.sensor, mode)
            time.sleep(1)


if __name__ == '__main__':
    con = Controller()

    con.runWatch()
