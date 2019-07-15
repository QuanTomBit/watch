
# Common Imports

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import modes

MEASURE_PER_TWO = 40
FORWARD = 1
PEAK = 0
BACKWARD = -1


def checkStepSpan(stepSpan):
    rateOfChange = []
    prevMeasure = stepSpan[0]
    for i in range(1, MEASURE_PER_TWO):
        currMeasure = stepSpan[i]
        rate = currMeasure - prevMeasure
        
        if rate > PEAK:
            rateOfChange.append(FORWARD)
        elif rate < PEAK:
            rateOfChange.append(BACKWARD)
        


def detectSteps(controller):
    numSteps = checkStepSpan(controller.stepSpan)


