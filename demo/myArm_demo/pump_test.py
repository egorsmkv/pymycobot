from pymycobot.myarm import MyArm
import time
from RPi import GPIO

# Initialize a MyCobot object
mc = MyArm("/dev/ttyAMA0")

# Initialization
GPIO.setmode(GPIO.BCM)
# Pins 20/21 control the solenoid valve and exhaust valve respectively
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


# Turn on the pump
def pump_on():
    # Open the solenoid valve
    GPIO.output(20, 0)


# Stop the pump
def pump_off():
    # Close the solenoid valve
    GPIO.output(20, 1)
    time.sleep(0.05)
    # Open the exhaust valve
    GPIO.output(21, 0)
    time.sleep(1)
    GPIO.output(21, 1)
    time.sleep(0.05)


pump_on()
time.sleep(6)
pump_off()
time.sleep(3)
