#This is the Autonomous Code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

drone.set_drone_LED(0,0,255,100)
drone.move_distance(0, 0, 0.9,1)
drone.hover(5)
drone.set_yaw(0)
drone.move_forward(distance=1.7, units="m", speed=1)
drone.set_yaw(0)

color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data)
#note, after research putting * "unpacks it"
#so then it won't dump it in like ((r, g, b)) but instead like (r,g,b)
#must be tested
drone.hover()


drone.land()

drone.close()