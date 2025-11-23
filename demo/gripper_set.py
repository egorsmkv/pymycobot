from pymycobot import MyCobot280
import time

# Update the serial port to your actual port, open the gripper fully, then run this script
port = "com8"

mc = MyCobot280(port)

print(
    "Current gripper position before zero-point calibration: ",
    mc.get_gripper_value(),
)
time.sleep(0.1)
mc.set_gripper_calibration()
time.sleep(0.1)
print(
    "Current gripper position after zero-point calibration (the gripper will lock if calibration succeeds and the position will be close to 100): ",
    mc.get_gripper_value(),
)
time.sleep(0.1)
print("Start updating gripper parameters...")
datas = [10, 0, 1, 150]
address = [21, 22, 23, 16]
current_datas = []
new_datas = []
for addr in address:
    current_datas.append(mc.get_servo_data(7, addr))
    time.sleep(0.1)
print("Current gripper parameters: ", current_datas)
for addr in range(len(address)):
    mc.set_servo_data(7, address[addr], datas[addr])
    time.sleep(0.1)
for addr in address:
    new_datas.append(mc.get_servo_data(7, addr))
    time.sleep(0.1)
print("Updated gripper parameters: ", new_datas)
