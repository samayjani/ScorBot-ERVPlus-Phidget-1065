import keyboard
from homing import homing
from manual import manual

print("=== ScorBot-ER V + ===")
print("_______Welcome_______")

print("Key H :Home Position")
print("Key M :Manual Mode")



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