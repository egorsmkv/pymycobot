from pymycobot.ultraArmP340 import ultraArmP340
import serial
import serial.tools.list_ports

# Coordinates of the blocks to be moved
green_pos = [
    [74.6, 167.55, 120],
    [74.6, 167.55, 92.45],
    [74.6, 167.55, 52.45],
    [74.6, 167.55, 12.45],
]
red_pos = [
    [112.67, 173.5, 120],
    [112.67, 173.5, 92.45],
    [112.67, 173.5, 52.45],
    [112.67, 173.5, 12.45],
]
yellow_pos = [
    [150.92, 167.61, 120],
    [150.92, 167.61, 92.45],
    [150.92, 167.61, 52.45],
    [150.92, 167.61, 12.45],
]

# Coordinates where the blocks should be placed
cube_pos_g = [[200, -75, 120], [200, -75, 15], [200, -75, 55], [200, -75, 95]]
cube_pos_r = [[150.63, -75, 15], [150.63, -75, 55], [150.63, -75, 95]]
cube_pos_y = [[109.63, -75, 15], [109.63, -75, 55], [109.63, -75, 95]]

# Approach orientation for the blocks being picked up
block_high = [60, 5, 0]

# Orientation at the drop-off location
cube_high = [-30, 10, 10]

# Get the list of serial ports
plist = [
    str(x).split(" - ")[0].strip() for x in serial.tools.list_ports.comports()
]

# Connect to the serial port
ua = ultraArmP340(plist[0], 115200)

# ultraArmP340 must home before coordinate or angle motion to get correct values
ua.go_zero()
ua.sleep(0.5)


# Yellow
# Move the first block
# Move toward the block
ua.set_angles(block_high, 50)
ua.sleep(0.5)

ua.set_coords(yellow_pos[0], 50)
ua.sleep(1)

# Reach the block position
ua.set_coords(yellow_pos[1], 50)
ua.sleep(1)
# Turn on the pump
ua.set_gpio_state(0)
ua.sleep(0.5)

# Move above the target location
ua.set_angles(cube_high, 50)
ua.sleep(0.5)

# Lower to the target position
ua.set_coords(cube_pos_y[0], 50)
ua.sleep(0.5)
# Turn off the pump
ua.set_gpio_state(1)
ua.sleep(0.5)

# Move back above the block position; later moves follow the same pattern
ua.set_angles(cube_high, 50)
ua.sleep(0.5)

# 2
ua.set_angles(block_high, 50)
ua.sleep(0.5)

ua.set_coords(yellow_pos[0], 50)
ua.sleep(1)

ua.set_coords(yellow_pos[2], 50)
ua.sleep(1)
ua.set_gpio_state(0)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_y[1], 50)
ua.sleep(0.5)
ua.set_gpio_state(1)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

# Red
# 1
ua.set_angles(block_high, 50)
ua.sleep(0.5)

ua.set_coords(red_pos[0], 50)
ua.sleep(1)

ua.set_coords(red_pos[1], 50)
ua.sleep(1)
ua.set_gpio_state(0)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_r[0], 50)
ua.sleep(0.5)
ua.set_gpio_state(1)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

# 2
ua.set_angles(block_high, 50)
ua.sleep(0.5)

ua.set_coords(red_pos[0], 50)
ua.sleep(1)

ua.set_coords(red_pos[2], 50)
ua.sleep(1)
ua.set_gpio_state(0)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_r[1], 50)
ua.sleep(0.5)
ua.set_gpio_state(1)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)


# Green
# 1
ua.set_angles(block_high, 50)
ua.sleep(0.5)

ua.set_coords(green_pos[0], 50)
ua.sleep(1)

ua.set_coords(green_pos[1], 50)
ua.sleep(1)
ua.set_gpio_state(0)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_g[0], 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_g[1], 50)
ua.sleep(0.5)
ua.set_gpio_state(1)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

# 2
ua.set_angles(block_high, 50)
ua.sleep(0.5)

ua.set_coords(green_pos[0], 50)
ua.sleep(1)

ua.set_coords(green_pos[2], 50)
ua.sleep(1)
ua.set_gpio_state(0)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_g[0], 50)
ua.sleep(0.5)

ua.set_coords(cube_pos_g[2], 50)
ua.sleep(0.5)
ua.set_gpio_state(1)
ua.sleep(0.5)

ua.set_angles(cube_high, 50)
ua.sleep(0.5)
