from pymycobot.ultraArmP340 import ultraArmP340
import time
import serial
import serial.tools.list_ports
# The imports above bring in the packages needed for the project

# ultraArmP340 initialization requires two arguments:
#   The first is the serial port string, for example:
#       linux: "/dev/ttyUSB0"
#       windows: "COM3"
#   The second is the baud rate: 115200
#
#   For example:
#         linux:
#              ua = ultraArmP340("/dev/USB0", 115200)
#           windows:
#              ua = ultraArmP340("COM3", 115200)
#

plist = [
    str(x).split(" - ")[0].strip() for x in serial.tools.list_ports.comports()
]

# Initialize an ultraArmP340 object
# The code below is for creating the object on Windows
ua = ultraArmP340(plist[0], 115200)

# ultraArmP340 must home before coordinate or angle motion to get correct values
ua.go_zero()
time.sleep(0.5)

# Turn on the pump
ua.set_gpio_state(0)

# Wait 2 seconds
time.sleep(3)


# Turn off the pump
ua.set_gpio_state(1)

time.sleep(2)
