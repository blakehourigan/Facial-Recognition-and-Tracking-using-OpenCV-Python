import RPi.GPIO as GPIO

class ServoController:
    def __init__(self) -> None:
        self.setup_servo_motor()
    
    
    def setup_servo_motor(self) -> None:
        # Setup for servo motor
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        pwm = GPIO.PWM(servoPIN, 50) # 50Hz
        pwm.start(0)
        
    def setServoAngle(self) -> int:
        calculated_angle = 0; 
        return calculated_angle
    
    def cleanup(self) -> None:
        # Perform any cleanup tasks here
        pass