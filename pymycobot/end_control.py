from pymycobot.common import ProtocolCode, ProGripper, FingerGripper


class ForceGripper:
    def calibration_parameters(self, *args, **kwargs):
        pass

    def _mesg(self, *args, **kwargs):
        pass

    # Set torque gripper
    def set_pro_gripper(
        self, gripper_id, gripper_address, value=0, has_return=False
    ):
        # Call calibration parameter helper
        self.calibration_parameters(
            class_name=self.__class__.__name__,
            gripper_id=gripper_id,
            gripper_address=gripper_address,
        )
        # Send command to set torque gripper
        return self._mesg(
            ProtocolCode.MERCURY_SET_TOQUE_GRIPPER,
            gripper_id,
            [gripper_address],
            [value],
            has_return=has_return,
        )

    # Get torque gripper
    def get_pro_gripper(self, gripper_id, gripper_address):
        # Call calibration parameter helper
        self.calibration_parameters(
            class_name=self.__class__.__name__,
            gripper_id=gripper_id,
            gripper_address=gripper_address,
        )
        # Send command to get torque gripper
        return self._mesg(
            ProtocolCode.MERCURY_GET_TOQUE_GRIPPER,
            gripper_id,
            [gripper_address],
        )

    # Set torque gripper angle
    def set_pro_gripper_angle(self, gripper_id, gripper_angle):
        # Call calibration parameter helper
        self.calibration_parameters(
            class_name=self.__class__.__name__,
            gripper_id=gripper_id,
            gripper_angle=gripper_angle,
        )
        # Send command to set torque gripper angle
        return self.set_pro_gripper(
            gripper_id, ProGripper.SET_GRIPPER_ANGLE, gripper_angle
        )

    # Set torque gripper open
    def set_pro_gripper_open(self, gripper_id):
        # Call calibration parameter helper
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        return self.set_pro_gripper(
            gripper_id, ProGripper.SET_GRIPPER_ANGLE, 100
        )

    def set_pro_gripper_close(self, gripper_id):
        # Set torque gripper closed
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        # Call calibration parameter helper
        return self.set_pro_gripper(
            gripper_id, ProGripper.SET_GRIPPER_ANGLE, 0
        )
        # Send command to set torque gripper closed

    def get_pro_gripper_angle(self, gripper_id):
        # Get torque gripper angle
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        # Call calibration parameter helper
        return self.get_pro_gripper(gripper_id, ProGripper.GET_GRIPPER_ANGLE)
        # Send command to get torque gripper angle

    def set_pro_gripper_calibration(self, gripper_id):
        # Set torque gripper calibration
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        # Call calibration parameter helper
        return self.set_pro_gripper(
            gripper_id, ProGripper.SET_GRIPPER_CALIBRATION
        )
        # Send command to set torque gripper calibration

    def get_pro_gripper_status(self, gripper_id):
        # Get torque gripper status
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        # Call calibration parameter helper
        return self.get_pro_gripper(gripper_id, ProGripper.GET_GRIPPER_STATUS)
        # Send command to get torque gripper status

    def set_pro_gripper_torque(self, gripper_id, torque):
        # Set torque gripper torque
        self.calibration_parameters(
            class_name=self.__class__.__name__,
            gripper_id=gripper_id,
            torque=torque,
        )
        # Call calibration parameter helper
        return self.set_pro_gripper(
            gripper_id, ProGripper.SET_GRIPPER_TORQUE, torque
        )
        # Send command to set torque gripper torque

    def get_pro_gripper_torque(self, gripper_id):
        # Get torque gripper torque
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        # Call calibration parameter helper
        return self.get_pro_gripper(gripper_id, ProGripper.GET_GRIPPER_TORQUE)
        # Send command to get torque gripper torque

    def set_pro_gripper_speed(self, gripper_id, speed):
        # Set torque gripper speed
        self.calibration_parameters(
            class_name=self.__class__.__name__,
            gripper_id=gripper_id,
            speed=speed,
        )
        # Call calibration parameter helper
        return self.set_pro_gripper(
            gripper_id, ProGripper.SET_GRIPPER_SPEED, speed
        )
        # Send command to set torque gripper speed

    def get_pro_gripper_speed(self, gripper_id):
        # Get torque gripper speed
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        # Call calibration parameter helper
        return self.get_pro_gripper(gripper_id, ProGripper.GET_GRIPPER_SPEED)
        # Send command to get torque gripper speed

    def set_pro_gripper_abs_angle(self, gripper_id, angle):
        # Set torque gripper absolute angle
        return self.set_pro_gripper(
            gripper_id,
            ProGripper.SET_GRIPPER_ABS_ANGLE,
            angle,
            has_return=True,
        )
        # Send command to set torque gripper absolute angle

    def set_pro_gripper_pause(self, gripper_id):
        return self.set_pro_gripper(gripper_id, ProGripper.SET_GRIPPER_PAUSE)

    def set_pro_gripper_stop(self, gripper_id):
        return self.set_pro_gripper(gripper_id, ProGripper.SET_GRIPPER_STOP)

    def set_pro_gripper_resume(self, gripper_id):
        return self.set_pro_gripper(gripper_id, ProGripper.SET_GRIPPER_RESUME)


class ThreeHand:
    def calibration_parameters(self, *args, **kwargs):
        pass

    def _mesg(self, *args, **kwargs):
        pass

    def __set_tool_fittings_value(self, addr, *args, gripper_id=14, **kwargs):
        kwargs["has_replay"] = True
        self.calibration_parameters(
            class_name=self.__class__.__name__, gripper_id=gripper_id
        )
        return self._mesg(
            ProtocolCode.MERCURY_SET_TOQUE_GRIPPER,
            gripper_id,
            [addr],
            *args or ([0x00],),
            **kwargs,
        )

    def __get_tool_fittings_value(self, addr, *args, gripper_id=14, **kwargs):
        kwargs["has_replay"] = True
        return self._mesg(
            ProtocolCode.MERCURY_GET_TOQUE_GRIPPER,
            gripper_id,
            [addr],
            *args or ([0x00],),
            **kwargs,
        )

    def get_hand_firmware_major_version(self, gripper_id=14):
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_MAJOR_FIRMWARE_VERSION,
            gripper_id=gripper_id,
        )

    def get_hand_firmware_minor_version(self, gripper_id=14):
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_MINOR_FIRMWARE_VERSION,
            gripper_id=gripper_id,
        )

    def set_hand_gripper_id(self, new_hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, new_hand_id=new_hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_ID,
            [new_hand_id],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_id(self, gripper_id=14):
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_ID, gripper_id=gripper_id
        )

    def set_hand_gripper_angle(self, hand_id, gripper_angle, gripper_id=14):
        """Set the angle of the single joint of the gripper

        Args:
            hand_id (int): 1 ~ 6
            gripper_angle (int): 0 ~ 100
            gripper_id (int) : 1 ~ 254
        """
        self.calibration_parameters(
            class_name=self.__class__.__name__,
            hand_id=hand_id,
            gripper_angle=gripper_angle,
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_ANGLE,
            [hand_id],
            [gripper_angle],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_angle(self, hand_id, gripper_id=14):
        """Get the angle of the single joint of the gripper

        Args:
            hand_id (int): 1 ~ 6
            gripper_id (int) : 1 ~ 254

        Return:
            gripper_angle (int): 0 ~ 100
        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_ANGLE,
            [hand_id],
            gripper_id=gripper_id,
        )

    def set_hand_gripper_angles(self, angles, speed, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, speed=speed
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_ANGLES,
            [angles],
            [speed],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_angles(self, gripper_id=14):
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_ALL_ANGLES, gripper_id
        )

    def set_hand_gripper_torque(self, hand_id, torque, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id, torque=torque
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_TORQUE,
            [hand_id],
            [torque],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_torque(self, hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_TORQUE,
            [hand_id],
            gripper_id=gripper_id,
        )

    def set_hand_gripper_calibrate(self, hand_id, gripper_id=14):
        """Setting the gripper jaw zero position

        Args:
            hand_id (int): 1 ~ 6
            gripper_id (int): 1 ~ 254
        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_CALIBRATION,
            [hand_id],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_status(self, gripper_id=14):
        """Get the clamping status of the gripper

        Args:
            gripper_id (int): 1 ~ 254

        Return:
            0 - Moving
            1 - Stopped moving, no clamping detected
            2 - Stopped moving, clamping detected
            3 - After clamping detected, the object fell
        """
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_STATUS, gripper_id=gripper_id
        )

    def set_hand_gripper_enabled(self, flag, gripper_id=14):
        """Set the enable state of the gripper

        Args:
            gripper_id (int): 1 ~ 254
            flag (int): 0 or 1

        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, flag=flag
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_ENABLED,
            [flag],
            gripper_id=gripper_id,
        )

    def set_hand_gripper_speed(self, hand_id, speed, gripper_id=14):
        """Set the speed of the gripper

        Args:
            hand_id (int): 1 ~ 6
            speed (int): 1 ~ 100
            gripper_id (int): 1 ~ 254

        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id, speed=speed
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_SPEED,
            [hand_id],
            [speed],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_default_speed(self, hand_id, gripper_id=14):
        """Get the default speed of the gripper

        Args:
            hand_id (int): 1 ~ 6
            gripper_id (int): 1 ~ 254

        Return:
            default speed (int): 1 ~ 100

        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_DEFAULT_SPEED,
            [hand_id],
            gripper_id=gripper_id,
        )

    def set_hand_gripper_pinch_action(self, pinch_mode, gripper_id=14):
        """Set the pinching action of the gripper

        Args:
            gripper_id (int): 1 ~ 254
            pinch_mode (int):
                0 - Index finger and thumb pinch
                1 - Middle finger and thumb pinch
                2 - Three-finger grip
                3 - Two-finger grip
        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, pinch_mode=pinch_mode
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_PINCH_ACTION,
            pinch_mode,
            gripper_id=gripper_id,
        )

    def set_hand_gripper_p(self, hand_id, value, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_P,
            [hand_id],
            [value],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_p(self, hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_P, [hand_id], gripper_id=gripper_id
        )

    def set_hand_gripper_d(self, hand_id, value, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_D,
            [hand_id],
            [value],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_d(self, hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_D, [hand_id], gripper_id=gripper_id
        )

    def set_hand_gripper_i(self, hand_id, value, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_I,
            [hand_id],
            [value],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_i(self, hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_I, [hand_id], gripper_id=gripper_id
        )

    def set_hand_gripper_min_pressure(self, hand_id, value, gripper_id=14):
        """Set the minimum starting force of the single joint of the gripper

        Args:
            hand_id (int): 1 ~ 6
            value (int): 0 ~ 254
            gripper_id (int): 1 ~ 254

        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_MIN_PRESSURE,
            [hand_id],
            [value],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_min_pressure(self, hand_id, gripper_id=14):
        """Set the minimum starting force of the single joint of the gripper

        Args:
            gripper_id (int): 1 ~ 254
            hand_id (int): 1 ~ 6

        Return:
            min pressure value (int): 0 ~ 254

        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_MIN_PRESSURE,
            [hand_id],
            gripper_id=gripper_id,
        )

    def set_hand_gripper_clockwise(self, hand_id, value, gripper_id=14):
        """state: 0 or 1, 0 - disable, 1 - enable"""
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_CLOCKWISE,
            [hand_id],
            [value],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_clockwise(self, hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_CLOCKWISE,
            hand_id,
            gripper_id=gripper_id,
        )

    def set_hand_gripper_counterclockwise(self, hand_id, value, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__set_tool_fittings_value(
            FingerGripper.SET_HAND_GRIPPER_COUNTERCLOCKWISE,
            [hand_id],
            [value],
            gripper_id=gripper_id,
        )

    def get_hand_gripper_counterclockwise(self, hand_id, gripper_id=14):
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_GRIPPER_COUNTERCLOCKWISE,
            [hand_id],
            gripper_id=gripper_id,
        )

    def get_hand_single_pressure_sensor(self, hand_id, gripper_id=14):
        """Get the counterclockwise runnable error of the single joint of the gripper

        Args:
            gripper_id (int): 1 ~ 254
            hand_id (int): 1 ~ 6

        Return:
            int: 0 ~ 4096

        """
        self.calibration_parameters(
            class_name=self.__class__.__name__, hand_id=hand_id
        )
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_SINGLE_PRESSURE_SENSOR,
            [hand_id],
            gripper_id=gripper_id,
        )

    def get_hand_all_pressure_sensor(self, gripper_id=14):
        """Get the counterclockwise runnable error of the single joint of the gripper

        Args:
           gripper_id (int): 1 ~ 254

        Return:
            int: 0 ~ 4096

        """
        return self.__get_tool_fittings_value(
            FingerGripper.GET_HAND_ALL_PRESSURE_SENSOR, gripper_id=gripper_id
        )

    def set_hand_gripper_pinch_action_speed_consort(
        self, pinch_pose, rank_mode, gripper_id=14, idle_flag=None
    ):
        """Setting the gripper pinching action-speed coordination

        Args:
            pinch_pose (int): 0 ~ 4
                0: All joints return to zero
                1: Index finger and thumb pinch together
                2: Middle finger and thumb pinch together
                3: Index finger and middle finger pinch together
                4: Three fingers together
            rank_mode (int): 0 ~ 5
                The degree of closure,the higher the level, the more closed
            gripper_id (int): 1 ~ 254
            idle_flag (int): default None or 1
                Idle flag. By default, there is no such byte. When this byte is 1, the idle finger can be freely manipulated.

        """
        if idle_flag is None:
            self.calibration_parameters(
                class_name=self.__class__.__name__,
                pinch_pose=pinch_pose,
                rank_mode=rank_mode,
            )
            return self.__set_tool_fittings_value(
                FingerGripper.SET_HAND_GRIPPER_PINCH_ACTION_SPEED_CONSORT,
                pinch_pose,
                rank_mode,
                gripper_id=gripper_id,
            )
        else:
            self.calibration_parameters(
                class_name=self.__class__.__name__,
                pinch_pose=pinch_pose,
                rank_mode=rank_mode,
                idle_flag=idle_flag,
            )
            return self.__set_tool_fittings_value(
                FingerGripper.SET_HAND_GRIPPER_PINCH_ACTION_SPEED_CONSORT,
                pinch_pose,
                rank_mode,
                idle_flag,
                gripper_id=gripper_id,
            )
