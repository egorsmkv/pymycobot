from .protocol_packet_handler import *

# 1 byte
FIRMWARE_MAJOR = 0x00
FIRMWARE_MINOR = 0x01
SERVO_MAJOR = 0x03
SERVO_MINOR = 0x04
BAUD = 6
RETURN_DELAY = 7
PHASE = 18
MAX_TEMPERATURE = 13
MAX_VOLTAGE = 14
SERVO_P = 21
SERVO_D = 22
SERVO_I = 23
CLOCKWISE_INSENSITIVE_ZONE = 26
COUNTERCLOCKWISE_INSENSITIVE_ZONE = 27
D_CONTROL_TIME = 81
# 2 bytes
MIN_START_FORCE = 24


class sms_sts(protocol_packet_handler):
    def __init__(self, portHandler):
        protocol_packet_handler.__init__(self, portHandler, 0)

    def get_servo_baud(self, id):
        """Get the servo baud rate

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, BAUD)
        return res[0] if res[1] != -2 else None

    def set_servo_baud(self, id, value):
        """Set the servo baud rate"""
        return self.write1ByteTxRx(id, BAUD, value)

    def get_servo_response_speed(self, id):
        """Get the servo response speed

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, RETURN_DELAY)
        return res[0] if res[1] != -2 else None

    def set_servo_response_speed(self, id, value):
        """Set the servo response speed"""
        return self.write1ByteTxRx(id, RETURN_DELAY, value)

    def get_servo_phase(self, id):
        """Get the servo phase

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, PHASE)
        return res[0] if res[1] != -2 else None

    def set_servo_phase(self, id, value):
        """Set the servo phase"""
        return self.write1ByteTxRx(id, PHASE, value)

    def get_servo_max_temperature(self, id):
        """Get the maximum temperature for the servo

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, MAX_TEMPERATURE)
        return res[0] if res[1] != -2 else None

    def set_servo_max_temperature(self, id, value):
        """Set the maximum temperature for the servo"""
        return self.write1ByteTxRx(id, MAX_TEMPERATURE, value)

    def get_servo_max_voltage(self, id):
        """Get the maximum voltage for the servo

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, MAX_VOLTAGE)
        return res[0] if res[1] != -2 else None

    def set_servo_max_voltage(self, id, value):
        """Set the maximum voltage for the servo"""
        return self.write1ByteTxRx(id, MAX_VOLTAGE, value)

    def get_servo_pid(self, id):
        """Get the servo PID values

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res_p = self.read1ByteTxRx(id, SERVO_P)
        res_i = self.read1ByteTxRx(id, SERVO_I)
        res_d = self.read1ByteTxRx(id, SERVO_D)
        return [
            res_p[0] if res_p[1] != -2 else None,
            res_i[0] if res_i[1] != -2 else None,
            res_d[0] if res_d[1] != -2 else None,
        ]

    def set_servo_pid(self, id, pid):
        """Set the servo PID values"""
        self.write1ByteTxRx(id, SERVO_P, pid[0])
        self.write1ByteTxRx(id, SERVO_I, pid[1])
        self.write1ByteTxRx(id, SERVO_D, pid[2])

    def get_servo_clockwise(self, id):
        """Get the servo clockwise dead zone

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, CLOCKWISE_INSENSITIVE_ZONE)
        return res[0] if res[1] != -2 else None

    def set_servo_clockwise(self, id, value):
        """Set the servo clockwise dead zone"""
        return self.write1ByteTxRx(id, CLOCKWISE_INSENSITIVE_ZONE, value)

    def get_servo_counter_clockwise(self, id):
        """Get the servo counterclockwise dead zone

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, COUNTERCLOCKWISE_INSENSITIVE_ZONE)
        return res[0] if res[1] != -2 else None

    def set_servo_counter_clockwise(self, id, value):
        """Set the servo counterclockwise dead zone"""
        return self.write1ByteTxRx(
            id, COUNTERCLOCKWISE_INSENSITIVE_ZONE, value
        )

    def get_servo_d_time(self, id):
        """Get the servo D control time

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, D_CONTROL_TIME)
        return res[0] if res[1] != -2 else None

    def set_servo_d_time(self, id, value):
        """Set the servo D control time"""
        return self.write1ByteTxRx(id, D_CONTROL_TIME, value)

    def get_servo_min_start(self, id):
        """Get the minimum starting force for the servo

        Args:
            id: Motor ID.

        Return:
            None: Failed to fetch.
        """
        scs_present_speed, scs_comm_result, scs_error = self.read2ByteTxRx(
            id, MIN_START_FORCE
        )
        return (
            self.scs_tohost(scs_present_speed, 15)
            if scs_comm_result != -2
            else None
        )

    def set_servo_min_start(self, id, value):
        """Set the minimum starting force for the servo"""
        return self.write2ByteTxRx(id, MIN_START_FORCE, value)

    def search_servo(self, id):
        """Check whether the servo exists

        Args:
            id: Servo ID.

        Return:
            0: Exists.
            -6: Does not exist.
            None: Failed to fetch.
        """
        res = self.ping(id)
        if res == -2:
            return None
        return res

    def get_servo_error(self, id):
        """Get servo error information

        Return:
            error_info: The returned decimal data converted to binary.\n
                Bit0  Bit1  Bit2 Bit3 Bit4 Bit5. If the bit is 1, the corresponding error occurred.\n
                Voltage  Sensor Temperature Current Angle Overload. A 0 bit means no related error.\n
                None: Failed to fetch.
        """
        res = self.read1ByteTxRx(id, 0x41)
        if res[1] == -2:
            return None
        return res[0]

    def get_servo_firmware_version(self, id):
        """Get motor firmware version information

        Return:
            list: [Firmware major version, firmware minor version, servo major version, servo minor version], -1 means failure
        """
        res = []
        command = [FIRMWARE_MAJOR, FIRMWARE_MINOR, SERVO_MAJOR, SERVO_MINOR]
        for add in command:
            r = self.read1ByteTxRx(id, add)
            if r[1] == -2:
                res.append(-1)
            else:
                res.append(r[0])
        return res
