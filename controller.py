
# Common Imports
import time

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import action
import display


sensor = SenseHat()
totalSteps = 12600
timeClock = time.localtime()

if __name__ == '__main__':

    # MAIN CONTROL LOOP
    #while (True):
    for i in range(11):
        mode = action.getUpdates(sensor)
        global totalSteps
        totalSteps = 100

        display.update(sensor, mode)
        time.sleep(1)
