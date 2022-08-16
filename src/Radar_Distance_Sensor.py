import board
import busio
import adafruit_vl53l0x


class VL53L0X():
    def __init__(self):
        """create VL53L0X class on I2C bus
        """
        self._i2c = busio.I2C(board.SCL, board.SDA)
        self._sensor = adafruit_vl53l0x.VL53L0X(self._i2c)

    def get_distance(self):
        """get distance from sensor in cm

        Returns:
            float: distance in cm
        """
        return self._sensor.range/10
