import keyboard
from homing import homing
from manual import manual
from by_angles import by_angles
from functions import gripper_close, gripper_open
import sys

print("=== ScorBot-ER V + ===")
print("_______Welcome_______")

print("Key H :Home Position")
print("Key M :Manual Mode")
print("Key P :Pick and Place by Angles")


# ScorBot Start Code: Final Program
while True:

	if keyboard.read_key() == "H":
			print("Home")
			homing()
			print("Press M for Manual Mode")
			# sys.exit()
	
	if keyboard.read_key() == "M":
			print("Manual Mode")
			manual()
			# sys.exit()
	
	if keyboard.read_key() == "P":
			print("Pick and Place by Angles\n")
			print("Pick Position Define:")
			gripper_open()
			by_angles()
			gripper_close()
			print("Place Position Define:\n")
			by_angles()
			gripper_open()
			homing()
			sys.exit()