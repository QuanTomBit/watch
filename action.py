
# Common Imports
from datetime import datetime

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import modes

MEASURE_PER_TWO = 40
FORWARD = 1
PEAK = 0
BACKWARD = -1

class ActionController:
    def __init__(self):
        self.lastMeasureTaken = datetime.now()
        
    def takeMeasurement(self, controller):
        elapsedTime = datetime.now() - self.lastMeasureTaken
        
        if elapsedTime.microseconds >= 3000:
            self.lastMeasureTaken = datetime.now()
            sensor = controller.sensor
            y = round(sensor.get_accelerometer_raw()['y'], 3)
            controller.stepSpan.pop(0)
            controller.stepSpan.append(y)

    def checkStepSpan(self, controller):
        stepSpan = controller.stepSpan
        rateOfChange = []
        numPeaks = 0 # Theoretically a peak equates to a step
        prevMeasure = stepSpan[0]
        
        for i in range(1, MEASURE_PER_TWO):
            currMeasure = stepSpan[i]
            rate = currMeasure - prevMeasure
            
            if rate > PEAK+0.25:
                rateOfChange.append(FORWARD)
            elif rate < PEAK-0.25:
                rateOfChange.append(BACKWARD)

        if len(rateOfChange) > 0:
            prevRate = rateOfChange[0]
            for i in range(1, len(rateOfChange)):
                if rateOfChange[i] != prevRate:
                    numPeaks += 1
                prevRate = rateOfChange[i]

        if numPeaks >= 3 and numPeaks < 7:
            controller.stepSpan = [0 for i in range(MEASURE_PER_TWO)]
            return numPeaks
        else:
            return 0


    def detectSteps(self, controller):
        self.takeMeasurement(controller)
        numSteps = self.checkStepSpan(controller)
        controller.totalSteps += numSteps


