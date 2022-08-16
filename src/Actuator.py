import gpiozero as gpio
from gpiozero.pins.pigpio import PiGPIOFactory
import time

from Radar_Distance_Sensor import *

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


class Motor:
    def __init__(self, IN1: int, IN2: int, EN: int, dir1: bool):
        """motor control

        Args:
            IN1 (int): IN1 pin
            IN2 (int): IN2 pin
            EN (int): EN pin (enable pin)
            dir (bool): if True mean no needed to flip the direction (forward is forward), if False mean need to flip the direction (forward is backward)
        """
        factory = None
        # factory = PiGPIOFactory()
        self._motor_pin = {"IN1": IN1, "IN2": IN2, "EN": EN}
        self._motor = gpio.Motor(
            forward=self._motor_pin["IN1"], backward=self._motor_pin["IN2"], enable=self._motor_pin["EN"], pwm=True, pin_factory=factory)
        self.dir = dir1

    def forward(self, speed: int):
        """move the motor forward with dir 

        Args:
            speed (int): 0-100 slow to fast
        """
        speed = speed/100
        if self.dir:
            self._motor.forward(speed)
        else:
            self._motor.backward(speed)

    def backward(self, speed: int):
        """move the motor backward with dir 

        Args:
            speed (int): 0-100 slow to fast
        """
        speed = speed/100
        if self.dir:
            self._motor.backward(speed)
        else:
            self._motor.forward(speed)

    def stop(self):
        """stop the motor
        """
        self._motor.stop()


class Car:
    def __init__(self):
        """create car class
        """
        self._mid_servo_angle = 98
        self._servo = Servo(pin=12, servo_angle=180,
                            min_angle=self._mid_servo_angle-50, max_angle=self._mid_servo_angle+50)
        self._motor = Motor(IN1=5, IN2=6, EN=13, dir1=False)

    def forward(self, speed: float = 50):
        """move the car forward with speed (0-100)

        Args:
            speed (float): 0-100 slow to fast
        """
        self._motor.forward(speed)

    def backward(self, speed: float = 50):
        """move the car backward with speed (0-100)

        Args:
            speed (float): 0-100 slow to fast
        """
        self._motor.backward(speed)

    def right(self, angle: float = 5, speed: float = None):
        """ streer the car right with angle 

        Args:
            angle (float): angle to rotate from mid angle. Defaults to 5.
            speed (float): speed of car (0-100) Defaults to None. None mean no need to change speed.
        """
        angle += self._mid_servo_angle
        self._servo.set_angle(angle)
        if speed != None:
            self.forward(speed)

    def left(self, angle: float = 5, speed: float = None):
        """ streer the car left with angle 

        Args:
            angle (float): angle to rotate from mid angle. Defaults to 5.
            speed (float): speed of car (0-100) Defaults to None. None mean no need to change speed.
        """
        angle = self._mid_servo_angle - angle
        self._servo.set_angle(angle)
        if speed != None:
            self.forward(speed)

    def stop(self):
        """stop the car
        """
        self._servo.set_angle(self._mid_servo_angle)
        self._motor.stop()

    def straight_forward(self, speed: float = 50):
        """move the car straight forward with speed (0-100)
        """
        self._servo.set_angle(self._mid_servo_angle)
        self.forward(speed)

    def straight_backward(self, speed: float = 50):
        """move the car straight backward with speed (0-100)
        """
        self._servo.set_angle(self._mid_servo_angle)
        self.backward(speed)
