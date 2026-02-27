#This is the Emergany Stop lol
from codrone_edu.drone import *

#Connect to drone and takeoff to ~36in
drone = Drone()
drone.pair()

drone.takeoff()

drone.land()
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data, brightness = 255)
drone.set_controller_LED(*color_data, brightness = 255)


drone.close()