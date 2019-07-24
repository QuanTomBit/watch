
# Common Imports
import time

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
from user_input import InputController
from action import ActionController
import display
import modes

MEASURE_PER_TWO = 40 # Also found in action.py
MAX_STEPS = 99980

class Controller:
    def __init__(self):
        self.sensor = SenseHat()
        self.stepSpan = [0 for i in range(MEASURE_PER_TWO)]
        self.totalSteps = 0
        self.dim = False
        self.mode = modes.MAIN
        self.prevMode = modes.MAIN # For returning from settings screen


    def runWatch(self, actCon, inCon):
        self.sensor.set_rotation(180)
        
        # MAIN CONTROL LOOP
        while (True):
            if (self.totalSteps < MAX_STEPS):
                actCon.detectSteps(self)

            inCon.getUpdates(self, self.sensor)
            display.update(self, self.sensor, self.mode)

            


if __name__ == '__main__':
    
    con = Controller()
    actCon = ActionController()
    inCon = InputController()

    con.runWatch(actCon, inCon)
