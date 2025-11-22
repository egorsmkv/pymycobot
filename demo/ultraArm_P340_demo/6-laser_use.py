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

plist = [
    str(x).split(" - ")[0].strip() for x in serial.tools.list_ports.comports()
]

# Initialize an ultraArmP340 object
# The code below is for creating the object on Windows
ua = ultraArmP340(plist[0], 115200)
ua.go_zero()

time.sleep(2)

ua.set_pwm(128)
