import time
import platform
import serial
import serial.tools.list_ports
from pymycobot.ultraArmP340 import ultraArmP340

plist = [
    str(x).split(" - ")[0].strip() for x in serial.tools.list_ports.comports()
]

# Automatically select the system and connect to the robot arm
if platform.system() == "Windows":
    ua = ultraArmP340(plist[0], 115200)
    ua.go_zero()
elif platform.system() == "Linux":
    ua = ultraArmP340("/dev/ttyUSB0", 115200)
    ua.go_zero()

# Positions for arm movement
angles = [
    [-81.71, 0.0, 0.0],
    [-90.53, 21.77, 47.56],
    [-90.53, 0.0, 0.0],
    [-59.01, 21.77, 45.84],
    [-59.01, 0.0, 0.0],
]

ua.set_angles(angles[0], 50)
time.sleep(3)

i = 5
# Loop 5 times
while i > 0:
    # Open the gripper
    ua.set_gripper_state(0)
    time.sleep(2)
    # Close the gripper
    ua.set_gripper_state(1)
    time.sleep(2)
    i -= 1
