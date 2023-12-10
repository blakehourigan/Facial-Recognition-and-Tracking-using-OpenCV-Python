import pigpio
from config import CONFIG
import time

class ServoController:
    def __init__(self) -> None:
        self.servo_PIN = CONFIG().get_servo_pin()

        self.initialize_and_sweep_servo()

    def initialize_and_sweep_servo(self) -> None:    
        self.pi = pigpio.pi() # instantiate pigpio.pi() class for hardware PWM
        
        sweeping = True

        while sweeping:                    # sweep servo from 0 to 180 degrees and back
            for i in range(0, 185, 5):
                self.set_servo_angle(i)
                
                time.sleep(0.025)
            for i in range(180, -5, -5):
                if i == 0:
                    sweeping = False
                self.set_servo_angle(i)
                time.sleep(.025)    
    
    def set_servo_angle(self, angle) -> None:
        """ 
        Map the angle that we want to the pulse width range of the servo.

        Pulse width for maximum angle (180) is 2500us, while min (0) is 500us, so we set forumla such that 
        max angle gives 1 and yields 2500us, and min angle gives 0 and yields 500us
        """
        
        pulse_width = 500 + (angle / 180.0) * 2000
        self.pi.set_servo_pulsewidth(self.servo_PIN, pulse_width)
        
    def cleanup(self) -> None:
        """
        reset angle to 0 degrees and release the hardware PWM pin
        """
        
        self.set_servo_angle(0)
        
        self.pi.stop()