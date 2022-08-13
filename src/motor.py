import gpiozero as gpio

motor_pin = {"IN1": 2, "IN2": 3, "EN": 7}

motor = gpio.Motor(forward=motor_pin["IN1"], backward=motor_pin["IN2"], enable=motor_pin["EN"], pwm=True)