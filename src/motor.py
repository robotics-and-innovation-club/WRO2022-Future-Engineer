import gpiozero as gpio
from gpiozero.pins.pigpio import PiGPIOFactory
import time


class Servo:
    def __init__(self, pin: int, servo_angle: float = 180, min_angle: float = None, max_angle: float = None):
        """create servo class

        Args:
            pin (int): Servo signal pin
        """
        factory = None
        # factory = PiGPIOFactory()
        self._pin = pin
        self._servo_angle = servo_angle
        self._min_angle = min_angle
        self._max_angle = max_angle
        if self._min_angle is None:
            self._min_angle = 0
        if self._max_angle is None:
            self._max_angle = servo_angle
        self._servo = gpio.AngularServo(pin=self._pin, initial_angle=None, min_angle=0, max_angle=self._servo_angle, min_pulse_width=0.5 /
                                        1000, max_pulse_width=2.5 / 1000, frame_width=20 / 1000, pin_factory=factory)

    def __q_lerp(self, value: float, ease: float):
        """convert a linear value to an ease value according to the smoothness (0->1)"""
        return pow(value, ease)/(pow(value, ease)+pow(1-value, ease))

    def __variable_limit(self, val: float, min_n: float, max_n: float):
        """limit value to min_n and max_n

        Args:
            val (float): value to limit
            min_n (float): min value
            max_n (float): max value

        Returns: val, state
            val, float: value after the limit
            state, bool: if value is out of limit return False else return True
        """
        if val < min_n:
            return min_n, False
        elif val > max_n:
            return max_n, False
        else:
            return val, True

    def __return_servo_position_on_state(self, from_position: float, to_position: float, percent: float, ease: float):
        """convert a linear value to an ease value according to the smoothness (0->1)"""
        size = to_position - from_position
        percent, state = self.__variable_limit(
            val=percent, min_n=0, max_n=50)
        percent /= 100
        first_state = from_position+self.__q_lerp(percent, ease)*size
        last_state = from_position+self.__q_lerp(1-percent, ease)*size
        final_state = to_position
        return first_state, last_state, final_state

    def set_angle(self, angle: float):
        """set servo angle (-1 mean disable servo)

        Args:
            angle (float): to servo angle

        Returns: state, now angle
            state, bool: if servo angle that limit in init (min_angle and max_angle) is exceeded return False else return True
            now angle, float: now servo angle in degrees
        """
        # disable servo if angle is -1
        if angle == -1:
            return True, self.disble()

        now = self.get_angle()
        if now == -1:
            now = 0
        to = self.__return_servo_position_on_state(
            from_position=now, to_position=angle, percent=20, ease=2)
        for i in to:
            self._servo.angle, state = self.__variable_limit(
                val=i, min_n=self._min_angle, max_n=self._max_angle)
        return state, self.get_angle()

    def get_angle(self):
        """get now servo angle (-1 mean servo is disable)

        Returns:
            float: servo angle in degrees
        """
        angle = self._servo.angle
        if angle is None:
            angle = -1
        return angle

    def disble(self):
        """disable servo
        """
        self._servo.value = None