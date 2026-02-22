from codrone_edu.drone import *

#Connect to drone and takeoff to ~36in
drone = Drone()
drone.pair()

drone.takeoff()

drone.send_absolute_position(0, 0, 0.5, 3, 0, 0)
drone.send_absolute_position(0.3, 0, 0.5, 1, 0, 0)
drone.send_absolute_position(0.3, 0, 0.5, 1, 0, 0)


drone.land()