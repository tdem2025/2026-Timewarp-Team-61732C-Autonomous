#This is the Autonomous Code
#Import CoDrone EDU Libraries
from codrone_edu.drone import *

#Connect to drone and takeoff to ~36in
drone = Drone()
drone.pair()

drone.takeoff()

#Begin by taking off, turning off LED, ascending, and going through first key-hole
drone.set_drone_LED(100,100,100,100)
drone.send_absolute_position(0, 0, 1.45, 2, 0, 0)
#drone.hover(5)
drone.set_yaw(0)
drone.set_yaw(0)


#Go through wind tunnel twice and come back, try to land on the blue cube
#we may need to remeasure some things.... or it was just the ac messing with us
drone.send_absolute_position(2, 0, 1.45, 2, 0, 0)
drone.send_absolute_position(4.55, 0, 1.60, 0.5, 0, 0)
drone.set_yaw(0)
drone.send_absolute_position(4.57, 0, 1.45, 0.5, 0, 0)
drone.set_yaw(0)
drone.send_absolute_position(4.55, 0, 1.55, 0.5, 0, 0)
drone.set_yaw(0)
drone.send_absolute_position(0.45, 0, 1.45, 0.5, 0, 0)
drone.set_yaw(0)
drone.send_absolute_position(0.45, 0, 0.9, 0.5, 0, 0)
drone.set_yaw(0)


#End code with a land and close
drone.land()

drone.close()