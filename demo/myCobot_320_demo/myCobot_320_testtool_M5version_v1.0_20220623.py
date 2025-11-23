#!/usr/bin/env python3
import os
import sys

sys.path.append(os.getcwd())
import tkinter
from tkinter import ttk
import time
import threading
import serial
import serial.tools.list_ports

from pymycobot.mycobot320 import MyCobot320

LOG_NUM = 0

multiple_angle = [
    [90, -90, 90, 90, 90, 90],
    [-90, 90, -90, -90, -90, -90],
    [-171.38, 70.57, 41.66, -24.87, -82.88, 6.76],
    [0.43, -92.72, 92.9, 87.71, 89.56, -0.17],
]

multiple_angle_grip = [
    [79.1, -30.41, -96.85, 40, 88.85, 0],
    [79.1, -60.41, -96.85, 80, 88.85, 0],
    [79.1, -30.41, -96.85, 40, 88.85, 0],
    [-27.59, -8.78, -127.26, 45.35, 88.85, 0],
    [-27.59, -60, -90, 60.35, 88.85, 0],
    [-27.59, -8.78, -127.26, 45.35, 88.85, 0],
]


class MycobotTest:
    def __init__(self):
        self.mycobot = None

        self.win = tkinter.Tk()
        self.win.title("Raspberry Pi Mycobot Test Tool")
        self.win.geometry(
            "918x480+10+10"
        )  # 290x160 as window size; +10 +10 sets the default popup location

        self.port_label = tkinter.Label(self.win, text="Select serial port:")
        self.port_label.grid(row=0)
        self.port_list = ttk.Combobox(
            self.win, width=15, postcommand=self.get_serial_port_list
        )  # Create a dropdown menu
        self.get_serial_port_list()  # Populate dropdown values
        self.port_list.current(0)
        self.port_list.grid(row=0, column=1)

        self.baud_label = tkinter.Label(self.win, text="Select baud rate:")
        self.baud_label.grid(row=1)
        self.baud_list = ttk.Combobox(self.win, width=15)
        self.baud_list["value"] = ("1000000", "115200")
        self.baud_list.current(1)
        self.baud_list.grid(row=1, column=1)

        # Connect
        self.connect_label = tkinter.Label(self.win, text="Connect mycobot:")
        self.connect_label.grid(row=2)
        self.connect = tkinter.Button(
            self.win, text="Connect", command=self.connect_mycobot
        )
        self.disconnect = tkinter.Button(
            self.win, text="Disconnect", command=self.disconnect_mycobot
        )
        self.connect.grid(row=3)
        self.disconnect.grid(row=3, column=1)

        # Check servo.
        self.check_label = tkinter.Label(self.win, text="Check connection:")
        self.check_label.grid(row=4)
        self.check_btn = tkinter.Button(
            self.win, text="Start checking", command=self.check_mycobot_servos
        )
        self.check_btn.grid(row=4, column=1)

        # Calibration.
        self.calibration_num = None
        self.calibration_label = tkinter.Label(self.win, text="Calibrate servo:")
        self.calibration_label.grid(row=5)
        self.calibration_btn = tkinter.Button(
            self.win, text="Start calibration", command=self.calibration_mycobot
        )
        self.calibration_btn.grid(row=5, column=1)

        # LED.
        self.set_color_label = tkinter.Label(self.win, text="Test Atom light board:")
        self.set_color_label.grid(row=6, columnspan=2)
        self.color_red = tkinter.Button(
            self.win, text="Set red", command=lambda: self.send_color("red")
        )
        self.color_green = tkinter.Button(
            self.win, text="Set green", command=lambda: self.send_color("green")
        )
        self.color_red.grid(row=7)
        self.color_green.grid(row=7, column=1)

        # Aging test.
        self.aging_stop = False
        self.movement_label = tkinter.Label(self.win, text="Aging loop action:")
        self.movement_label.grid(row=8)
        self.start_btn = tkinter.Button(
            self.win, text="Start", command=self.start_aging_test
        )
        self.start_btn.grid(row=9)
        self.stop_btn = tkinter.Button(
            self.win, text="Stop", command=self.stop_aging_test
        )
        self.stop_btn.grid(row=9, column=1)

        # Release
        self.release_btn = tkinter.Button(
            self.win, text="Relax all motors", command=self.release_mycobot
        )
        self.release_btn.grid(row=10)

        # Focus
        self.focus_btn = tkinter.Button(
            self.win, text="Power on all motors", command=self.focus_mycobot
        )
        self.focus_btn.grid(row=10, column=1)

        # rectify
        # self.rectify_btn = tkinter.Button(
        #     self.win, text="Calibrate PID", command=self.rectify_mycobot
        # )
        # self.rectify_btn.grid(row=10, column=1)

        # I/O
        self.test_IO_label = tkinter.Label(self.win, text="Test I/O:")
        self.test_IO_label.grid(row=11)
        self.test_basic_btn = tkinter.Button(
            self.win, text="Test base I/O", command=self.test_basic
        )
        self.test_atom_btn = tkinter.Button(
            self.win, text="Test end-effector I/O", command=self.test_atom
        )
        self.test_basic_btn.grid(row=12)
        self.test_atom_btn.grid(row=12, column=1)

        # Log output.
        self.log_label = tkinter.Label(self.win, text="Log:")
        self.log_label.grid(row=0, column=12)
        _f = tkinter.Frame(self.win)
        _bar = tkinter.Scrollbar(_f, orient=tkinter.VERTICAL)
        self.log_data_Text = tkinter.Text(
            _f, width=100, height=35, yscrollcommand=_bar.set
        )
        _bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        _bar.config(command=self.log_data_Text.yview)
        self.log_data_Text.pack()
        # self.log_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        _f.grid(row=1, column=12, rowspan=15, columnspan=10)

    def run(self):
        self.win.mainloop()  # run
        self.aging_stop = False
        if self.aging_stop:
            self.aging.join()

    # ============================================================
    # Connect method
    # ============================================================
    def connect_mycobot(self):
        self.prot = port = self.port_list.get()
        if not port:
            self.write_log_to_Text("Please select the serial port")
            return
        self.baud = baud = self.baud_list.get()
        if not baud:
            self.write_log_to_Text("Please select the baud rate")
            return
        baud = int(baud)

        try:
            # self.mycobot = MyCobot(PI_PORT, PI_BAUD)
            self.mycobot = MyCobot320(port, baud)
            time.sleep(0.5)
            self.mycobot._write([255, 255, 3, 22, 1, 250])
            time.sleep(0.5)
            # self.mycobot = MyCobot("/dev/cu.usbserial-0213245D", 115200)
            self.write_log_to_Text("Connection successful!")
        except Exception as e:
            err_log = f"""\
                \rConnection failed!!!
                \r=================================================
                {e}
                \r=================================================
            """
            self.write_log_to_Text(err_log)

    def disconnect_mycobot(self):
        if not self.has_mycobot():
            return

        try:
            del self.mycobot
            self.mycobot = None
            self.write_log_to_Text("Disconnected successfully!")
        except AttributeError:
            self.write_log_to_Text("mycobot is not connected!!!")

    # ============================================================
    #  Function method
    # ============================================================
    def release_mycobot(self):
        if not self.has_mycobot():
            return
        self.mycobot.release_all_servos()
        self.write_log_to_Text("Release over.")

    def focus_mycobot(self):
        if not self.has_mycobot():
            return
        self.mycobot.power_on()
        self.write_log_to_Text("Power on over.")

    def check_mycobot_servos(self):
        # self.connect_mycobot()
        if not self.has_mycobot():
            return

        # ping_commands = [
        #     [255, 255, 1, 2, 1, 251],
        #     [255, 255, 2, 2, 1, 250],
        #     [255, 255, 3, 2, 1, 249],
        #     [255, 255, 4, 2, 1, 248],
        #     [255, 255, 5, 2, 1, 247],
        #     [255, 255, 6, 2, 1, 246],
        #     [255, 255, 7, 2, 1, 246],
        # ]
        # res = []
        # for idx, command in enumerate(ping_commands, start=1):
        #     self.mycobot._write(command)
        #     time.sleep(0.1)
        #     if not self.mycobot._read():
        #         res.append(idx)
        #     time.sleep(0.1)
        res = []
        for i in range(1, 8):
            _data = self.mycobot.get_servo_data(i, 5)
            time.sleep(0.02)
            # self.write_log_to_Text("connect servo error".format(_data))
            if _data != i:
                res.append(i)
        if res:
            self.write_log_to_Text(f"Joint {res} cannot communicate!!!")
        else:
            self.write_log_to_Text("All joints are connected normally.")

    def calibration_mycobot(self):
        """Calibration button click event.

        Click to calibrate one motor at a time and calibrate in turn. After all
        calibration, resume initialization.
        """
        if not self.has_mycobot():
            return

        if not self.calibration_num:
            self.calibration_num = 0

        self.calibration_num += 1

        self.mycobot.set_servo_calibration(self.calibration_num)
        time.sleep(0.1)
        self.mycobot.focus_servo(self.calibration_num)
        time.sleep(0.5)
        pos = self.mycobot.get_angles()
        self.write_log_to_Text(
            f"Calibrating motor {self.calibration_num} finished."
        )

        if self.calibration_num == 6:
            self.write_log_to_Text("All calibrations completed.")
            self.calibration_num = None
            # self.rectify_mycobot()
            self._calibration_test()

    def send_color(self, color: str):
        if not self.has_mycobot():
            return

        color_dict = {
            "red": [255, 0, 0],
            "green": [0, 255, 0],
            "blue": [0, 0, 255],
        }
        self.mycobot.set_color(*color_dict[color])
        self.write_log_to_Text(f"Send color: {color}.")

    def start_aging_test(self):
        if not self.has_mycobot():
            return
        self.aging_stop = False
        self.aging = threading.Thread(target=self.aging_test, daemon=True)
        self.aging.start()
        self.write_log_to_Text("Start loop aging test ...")

    def stop_aging_test(self):
        try:
            self.aging_stop = True
            self.write_log_to_Text("End loop aging test.")
            self.aging.join()
        except:
            self.write_log_to_Text("Failed to end aging test!!!")

    # def rectify_mycobot(self):
    #     if not self.has_mycobot():
    #         return
    #
    #     data_id = [21, 22, 23, 24, 26, 27]
    #     data    = [10, 0, 1, 0, 3, 3]
    #     for i in range(1,7):
    #         for j in range(len(data_id)):
    #             self.mycobot.set_servo_data(i, data_id[j], data[j])
    #             time.sleep(0.2)
    #             _data = self.mycobot.get_servo_data(i, data_id[j])
    #             time.sleep(0.2)
    #             if _data == data[j]:
    #                 self.write_log_to_Text("Servo motor :" + str(i) + "  data_id : " + str(data_id[j]) + "   data: " + str(_data) + "  modify successfully ")
    #             else:
    #                 self.write_log_to_Text("Servo motor :"  + str(i) + "  data_id : " + str(data_id[j]) + "   data: " + str(_data) + "  modify error ")

    def test_basic(self):
        pin_no = [1, 2, 3, 4, 5, 6]
        for p in pin_no:
            self.write_log_to_Text("Set pin %s to 0 " % p)
            self.mycobot.set_basic_output(p, 0)
            time.sleep(0.5)
        time.sleep(1)
        for p in pin_no:
            self.write_log_to_Text(
                "Read pin %s as : %s" % (p, self.mycobot.get_basic_input(p))
            )
            time.sleep(0.5)
        time.sleep(1)
        for p in pin_no:
            self.write_log_to_Text("Set pin %s to 1 " % p)
            self.mycobot.set_basic_output(p, 1)
            time.sleep(0.5)
        time.sleep(1)
        for p in pin_no:
            self.write_log_to_Text(
                "Read pin %s as : %s" % (p, self.mycobot.get_basic_input(p))
            )
            time.sleep(0.5)

    def test_atom(self):
        pin_in = [19, 22]
        pin_out = [23, 33]
        for p in pin_out:
            self.write_log_to_Text("Set pin %s to 0 " % p)
            self.mycobot.set_digital_output(p, 0)
            time.sleep(0.5)
        time.sleep(1)
        for p in pin_in:
            self.write_log_to_Text(
                "Read pin %s as : %s" % (p, self.mycobot.get_digital_input(p))
            )
            time.sleep(0.5)
        time.sleep(1)
        for p in pin_out:
            self.write_log_to_Text("Set pin %s to 1 " % p)
            self.mycobot.set_digital_output(p, 1)
            time.sleep(0.5)
        time.sleep(1)
        for p in pin_in:
            self.write_log_to_Text(
                "Read pin %s as : %s" % (p, self.mycobot.get_digital_input(p))
            )
            time.sleep(0.5)
        time.sleep(1)

    # ============================================================
    # Utils method
    # ============================================================
    def has_mycobot(self):
        """Check whether it is connected on mycobot"""
        if not self.mycobot:
            self.write_log_to_Text("mycobot is not connected!!!")
            return False
        return True

    def aging_test(self):
        while True:
            speed = [50, 100]
            joint = [1, 2, 3, 4, 5, 6]
            angle = [0, 168, 90, 130, 145, 165, 180]
            coord = ["y", "z", "x"]

            self.mycobot.set_color(0, 0, 255)

            self.mycobot.wait(1).send_angles([0, 0, 0, 0, 0, 0], speed[1])

            # Single-joint motion
            for a in range(1):
                for j in joint:
                    for sp in speed:
                        if sp == 10:
                            t = 10
                        elif sp == 50:
                            t = 5
                        elif sp == 100:
                            t = 3

                        if self.aging_stop:
                            return

                        self.mycobot.wait(t).send_angle(j, angle[j], sp)
                        print(self.aging_stop)
                        self.mycobot.wait(t).send_angle(j, angle[j] * (-1), sp)
                        print(self.aging_stop)
                        self.mycobot.wait(t).send_angle(j, angle[0], sp)
                        print(self.aging_stop)

            # Multi-joint motion
            for b in range(2):
                for sp in speed:
                    if sp == 10:
                        t = 10
                    elif sp == 50:
                        t = 5
                    elif sp == 100:
                        t = 3
                    for mul in multiple_angle:
                        if self.aging_stop:
                            return
                        self.mycobot.wait(t).send_angles(mul, sp)

            self.mycobot.wait(5).send_angles([0, 0, 0, 0, 0, 0], speed[1])

            # Cartesian motion
            self.mycobot.wait(5).send_angles(
                [0, -25, -115, 45, -80, 0], speed[1]
            )
            time.sleep(2)

            for c in range(2):
                for sp in speed:
                    data_list = [235.4, -117.3, 244.5, 9.14, -25.44, 85.62]
                    self.mycobot.wait(5).send_coords(data_list, speed[1], 1)
                    if sp == 10:
                        t = 10
                    elif sp == 50:
                        t = 3
                    elif sp == 100:
                        t = 1

                    for cd in coord:
                        if cd == "x":
                            i = 0
                        elif cd == "y":
                            i = 1
                        elif cd == "z":
                            i = 2
                        print(cd)
                        if self.aging_stop:
                            return

                        data_list[i] = data_list[i] + 90
                        self.mycobot.wait(t).send_coords(data_list, sp, 1)
                        print(t, data_list, sp)

                        data_list[i] = data_list[i] - 140
                        self.mycobot.wait(t).send_coords(data_list, sp, 1)
                        print(t, data_list, sp)

            self.mycobot.wait(5).send_angles([0, 0, 0, 0, 0, 0], speed[1])

            # Typical action (grasping)
            for d in range(2):
                for sp in speed:
                    if sp == 10:
                        t = 10
                    elif sp == 50:
                        t = 3
                    elif sp == 100:
                        t = 2
                    for mulg in multiple_angle_grip:
                        if self.aging_stop:
                            return
                        self.mycobot.wait(t).send_angles(mulg, sp)

            self.mycobot.wait(5).send_angles([0, 0, 0, 0, 0, 0], speed[1])

    def _calibration_test(self):
        self.write_log_to_Text("Start calibration test.")
        self.mycobot.set_fresh_mode(1)
        time.sleep(0.5)
        angles = [0, 0, 0, 0, 0, 0]
        test_angle = [-20, 20, 0]
        for i in range(6):
            for j in range(3):
                angles[i] = test_angle[j]
                self.mycobot.send_angles(angles, 0)
                time.sleep(2)
        self.write_log_to_Text("Calibration test finished.")

    def get_serial_port_list(self):
        plist = [
            str(x).split(" - ")[0].strip()
            for x in serial.tools.list_ports.comports()
        ]
        print(plist)
        self.port_list["value"] = plist
        return plist

    def get_current_time(self):
        """Get current time with format."""
        current_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())
        )
        return current_time

    def write_log_to_Text(self, logmsg: str):
        global LOG_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # New line

        if LOG_NUM <= 18:
            self.log_data_Text.insert(tkinter.END, logmsg_in)
            LOG_NUM += len(logmsg_in.split("\n"))
            # print(LOG_NUM)
        else:
            self.log_data_Text.insert(tkinter.END, logmsg_in)
            self.log_data_Text.yview("end")


if __name__ == "__main__":
    MycobotTest().run()
