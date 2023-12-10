from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import time
import keyboard
import sys


#Declare any event handlers here. These will be called every time the associated event occurs.

def control(serial, velocity, duration):
	#Create your Phidget channels
	dcMotor0 = DCMotor()

	#Set addressing parameters to specify which channel to open (if any)
	dcMotor0.setDeviceSerialNumber(serial)

	#Open your Phidgets and wait for attachment
	dcMotor0.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.
	dcMotor0.setTargetVelocity(velocity)
	time.sleep(duration)

	#Close your Phidgets once the program is done.
	dcMotor0.close()

# while True:
# 	if keyboard.read_key() == "l":
# 		print("go Left")
# 		control(146552, -1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "r":
# 		print("go Right")
# 		control(146552, 1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "f":
# 		print("go Forward")
# 		control(146520, 1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "b":
# 		print("go Backward")
# 		control(146520, -1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "u":
# 		print("go Up")
# 		control(146627, 1, 4)
# 		# sys.exit()
# 	if keyboard.read_key() == "d":
# 		print("go Down")
# 		control(146627, -1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "o":
# 		print("Open Gripper")
# 		control(146491, -1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "c":
# 		print("Close Gripper")
# 		control(146491, 1, 2)
# 		# sys.exit()
# 	if keyboard.read_key() == "0":
# 		print("Finish Program")
# 		sys.exit()

# gripper
control(146491, 1, 2)
# wristroll
control(146640, -1, 8)
# elbow
control(146520, 1, 10)


# shoulder
control(146627, -1, 8)
# base
control(146552, -1, 15) 
# control(146640, -1, 4)
# control(146520, 1, 5)
