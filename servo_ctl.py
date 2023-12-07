import RPi.GPIO as GPIO

class ServoController:
    def __init__(self):
        self.setup_servo_motor()
    
    
    def setup_servo_motor(self):
        # Setup for servo motor
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        pwm = GPIO.PWM(servoPIN, 50) # 50Hz
        pwm.start(0)