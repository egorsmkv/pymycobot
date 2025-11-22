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
#
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

# Get the current head coordinates and pose
coords = ua.get_coords_info()
time.sleep(2)
print(coords)

# Move the arm to coordinates [57.0, -10, 30] at 80 mm/s
ua.set_coords([57.0, -10, 30], 80)

# Wait 2 seconds
time.sleep(2)

# Move the arm to coordinates [-13.7, 40, 20] at 80 mm/s
ua.set_coords([-13.7, 40, 20], 80)

# Wait 2 seconds
time.sleep(2)

# Change only the head x coordinate to -40 at 70 mm/s
ua.set_coord(1, -40, 70)
