from pymycobot.ultraArmP340 import ultraArmP340
import time
import serial
import serial.tools.list_ports

# Put the imports above at the top of the file to bring in the project package

# ultraArmP340 initialization requires two arguments: serial port and baud rate
#   The first is the serial port string, for example:
#       linux: "/dev/ttyUSB0"
#       windows: "COM3"
#   The second is the baud rate: 115200
#   Examples:
#           linux:
#              ua = ultraArmP340("/dev/USB0", 115200)
#           windows:
#              ua = ultraArmP340("COM3", 115200)

# Get the list of serial ports
plist = [
    str(x).split(" - ")[0].strip() for x in serial.tools.list_ports.comports()
]

# Initialize an ultraArmP340 object
# The code below is for creating the object on Windows

ua = ultraArmP340(plist[0], 115200)
# ultraArmP340 must home before coordinate or angle motion to get correct values
ua.go_zero()
time.sleep(0.5)

# Move each joint to [0, 0, 0] by passing in the angle parameters
ua.set_angles([0, 0, 0], 50)

# Wait to ensure the arm reaches the target position
time.sleep(2.5)

# Move joint 1 to 90 degrees
ua.set_angle(1, 90, 50)
# Wait to ensure the arm reaches the target position
time.sleep(2)

# The code below will swing the arm left and right
# Set the number of loops
num = 7

while num > 0:
    # Move joint 2 to 45 degrees
    ua.send_angle(2, 45, 50)

    # Wait to ensure the arm reaches the target position
    time.sleep(3)

    # Move joint 2 to -15 degrees
    ua.set_angle(2, -15, 50)

    # Wait to ensure the arm reaches the target position
    time.sleep(3)

    num -= 1

# Fold the arm. You can manually move the arm, call get_angles() to read the angles,
# and then use those angles to move the arm to the position you want.
ua.set_angles([88.68, 60, 30], 50)

# Wait to ensure the arm reaches the target position
time.sleep(2.5)
