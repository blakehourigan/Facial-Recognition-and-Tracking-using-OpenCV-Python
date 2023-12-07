import cv2
import RPi.GPIO as GPIO

from config import CONFIG
from servo_ctl import ServoController

class Controller: 
    def __init__(self):  
        self.config = CONFIG()
        
        self.face_model = self.config.get_face_model()   # get face model and camera from config
        
        self.cam = self.config.get_camera()
        
        self.servo_controller = ServoController()
        
        self.detectFaces()

        
    def setServoAngle(self):
        calculated_angle = 0; 
        return calculated_angle

    def detectFaces(self):
        while True:
            ret, frame = self.cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_model.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                # Calculate position of face and move servo
                number = self.setServoAngle()
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break

    def exit(self):
        # When everything done, release the capture
        cam.release()
        cv2.destroyAllWindows()
        pwm.stop()
        GPIO.cleanup()

