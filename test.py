#Python code
#Python Test Code To Learn The Basics Of Coding CoDrone EDU
#This just has the drone do basic movements (takeoff, turn left and right,go up and down, and forward and back).
from codrone_edu.drone import *

drone = Drone()
drone.pair() # pair automatically, may not always work
# if drone.pair doesn't work then try drone.pair(port_name = 'COM3')    # pair with a specific port (Must be set)


drone.takeoff()
drone.hover(2)
drone.turn_left(90)
drone.hover(2)
drone.turn_right(90)
drone.hover(2)
drone.move_distance(0, 0, 0.25, 1)
drone.hover(2)
drone.move_distance(0, 0, -0.25, 1)
drone.hover(2)
drone.move_forward(distance=12, units="in", speed=1)
drone.hover(2)
drone.move_backward(distance=12, units="in", speed=1)
drone.hover(2)
drone.move_left(distance=12, units="in", speed=1)
drone.hover(2)
drone.move_right(distance=12, units="in", speed=1)
drone.hover(2)
drone.land()

#disconnects the drone
drone.close()