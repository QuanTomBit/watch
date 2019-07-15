
# Common Imports
import time

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import action
import display

class Controller:
    def __init__(self):
        self.sensor = SenseHat()
        self.totalSteps = 13000


    def runWatch(self):
        # MAIN CONTROL LOOP
        #while (True):
        mode = action.getUpdates(self.sensor)

        display.update(self, self.sensor, mode)
        time.sleep(1)


if __name__ == '__main__':
    con = Controller()

    con.runWatch()
