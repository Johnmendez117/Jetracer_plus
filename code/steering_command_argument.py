# steering_command
#4-21-23 version
# Auther: John Mendez 
# Importing required libraries  
from jetracer.nvidia_racecar import NvidiaRacecar

import argparse
# creating the objects, for the control over the robot 
car = NvidiaRacecar()
# adding a way to input into a program "--value" flag 
parser = argparse.ArgumentParser()
# we are parcing the imput of the user
parser.add_argument('--value', type=float, required=True)
# we are commanding the car to change steering 
args = parser.parse_args()
car.steering = args.value

print= ("The command servo is: ", args.value)
