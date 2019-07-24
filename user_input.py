
# Common Imports

# Project Specific Imports
from sense_hat import SenseHat

# Custom File Imports
import modes

class InputController:
    def __init__(self):
        mode = modes.MAIN
        
    def getUpdates(self, controller, sensor):
        mode = modes.MAIN
        events = sensor.stick.get_events()

        for event in events:
            if event.action == 'released':
                if event.direction == 'down':
                    controller.mode = modes.SETTINGS
                elif event.direction == 'middle':
                    if controller.mode == modes.SETTINGS:
                        controller.dim = not controller.dim
                elif event.direction == 'up':
                    controller.mode = controller.prevMode
