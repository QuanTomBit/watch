
# Common Imports
from datetime import datetime

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import modes
import colors as clr
import num_dicts

import controller # For accessing global values


def printMat(matrix):
    for i in range(len(matrix)):
        if i != 0 and (i+1) % 8 == 0:
            print(str(matrix[i]) + '\n')
        else:
            print(str(matrix[i]) +', ', end='')

    return None

    
def displayThousandsMain(controller, matrix):
    steps = str(controller.totalSteps)

    thousands = steps[1] # Get thousands of steps
    tensThousands = steps[0] # Get tens of thousands
    
    # Convert string representing number to 3x5 matrix of number display
    tensThousandsMat = num_dicts.getMainScreenNum(tensThousands, clr.T)
    thousandsMat = num_dicts.getMainScreenNum(thousands, clr.B)

    # Set tens of thousands value in matrix
    for i in range(len(tensThousandsMat)):
        matrix[i + 5 * int(i / 3)] = tensThousandsMat[i]

    # Set thousands value in matrix
    for i in range(len(thousandsMat)):
        matrix[3 + i + 5 * int(i / 3)] = thousandsMat[i]

    return None


def displayHundredsMain(controller, matrix):
    steps = str(controller.totalSteps)

    hundreds = int(steps[2:]) # Get hundreds of steps
    tens = int(steps[3])

    # Holds the indices of where on the matrix each hundred value is displayed
    pixelIndices = [6, 7, 14, 15, 22, 23, 30, 31, 38, 39]

    # Display hundreds of steps taken by showing green as a full 100 steps
    # Orange is less than 50, and yellow id over 50
    hunLen = int(hundreds/100)
    for i in range(len(pixelIndices)):
        if i < hunLen:
            matrix[pixelIndices[i]] = clr.G
        elif i == hunLen:
            if tens == 0:
                matrix[pixelIndices[i]] = clr.OFF
            elif tens < 5:
                matrix[pixelIndices[i]] = clr.O
            else:
                matrix[pixelIndices[i]] = clr.Y
        else:
            matrix[pixelIndices[i]] = clr.OFF

    return None


def displayClockMain(matrix):
    currTime = datetime.now()
    hour = num_dicts.getMainScreenHour(currTime.hour)
    minute = currTime.minute

    for i in range(len(hour)):
        matrix[hour[i]] = clr.R
    
    return None


def displayMain(controller, sensor):
    matrix = [clr.OFF for i in range(64)]

    displayThousandsMain(controller, matrix)
    displayHundredsMain(controller, matrix)
    displayClockMain(matrix)
    sensor.set_pixels(matrix)
    return None


def displayError():
    return None


def update(controller, sensor, mode):
    if (mode == modes.MAIN):
        displayMain(controller, sensor)
    else:
        displayError()
