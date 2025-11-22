# Read myArm C joint angles and send them
import socket
from pymycobot import MyArmC, MyArmM
import serial.tools.list_ports
import time


def get_port():  # Get all serial port numbers
    port_list = serial.tools.list_ports.comports()
    i = 1
    res = {}
    for port in port_list:
        print(f"{i} - {port.device}")
        res[str(i)] = port.device
        i += 1
    return res


def main():
    port_dict = get_port()
    print(
        "Note: After the program is started, the M750 will follow the C650 to do the same action. Please place the two machines in the same position to avoid sudden swinging of the machines."
    )
    port_c = input("input myArm C port: ")
    c_port = port_dict[port_c]
    c = MyArmC(c_port, debug=False)
    HOST = "127.0.0.1"
    PORT = 8001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Request connection
    client.connect((HOST, PORT))
    while True:
        angle = c.get_joints_angle()
        if angle is not None:
            data = "\n" + str(angle)
            client.send(data.encode("utf-8"))


if __name__ == "__main__":
    main()
