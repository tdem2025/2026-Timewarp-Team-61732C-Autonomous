#This is the Emergany Stop lol
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.emergency_stop()
#we can try doing drone.land()