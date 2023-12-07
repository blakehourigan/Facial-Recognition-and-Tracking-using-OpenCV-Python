import RPi.GPIO as GPIO
from config import CONFIG

class ServoController:
    def __init__(self) -> None:
        self.servo_PIN = CONFIG().get_servo_pin()
        
        self.angle = 90 # default angle for servo motor
        
        self.setup_servo_motor()
    
    def setup_servo_motor(self) -> None:
        # Setup for servo motor

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_PIN, GPIO.OUT)
        pwm = GPIO.PWM(self.servo_PIN, 50) # 50Hz standard frequency for servo motors
        pwm.start(0)
        
    def setServoAngle(self, angle) -> int:
        desired_angle = angle   # need to find out what pwm value corresponds to what angle
        
        cycle = desired_angle / 18 + 2 # standard formula for calculating duty cycle

        pwm.ChangeDutyCycle(cycle)
    
    def cleanup(self) -> None:
        # Perform any cleanup tasks here
        pass