import serial
import serial.tools.list_ports

from pymycobot.mycobot280 import MyCobot280


def setup():
    print("")

    plist = list(serial.tools.list_ports.comports())
    idx = 1
    for port in plist:
        print(f"{idx} : {port}")
        idx += 1

    _in = input(f"\nPlease input 1 - {idx - 1} to choice:")
    port = str(plist[int(_in) - 1]).split(" - ")[0].strip()
    print(port)
    print("")

    baud = 115200
    _baud = input("Please input baud(default:115200):")
    try:
        baud = int(_baud)
    except Exception:
        pass
    print(baud)
    print("")

    DEBUG = False
    f = input("Wether DEBUG mode[Y/n]:")
    if f in ["y", "Y", "yes", "Yes"]:
        DEBUG = True
    # mc = MyCobot(port, debug=True)
    mc = MyCobot280(port, baud, debug=DEBUG)
    return mc
