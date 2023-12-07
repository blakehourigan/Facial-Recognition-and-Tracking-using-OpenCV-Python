import cv2
import RPi.GPIO as GPIO

from config import CONFIG
from servo_ctl import ServoController
from gui import GUI

class Controller: 
    def __init__(self) -> None:  
        self.config = CONFIG() # instantiate gui and config classes
        self.gui = GUI()
        
        self.face_model = self.config.get_face_model()   # get face model and camera from config
        
        self.cam = self.config.get_camera()
        
        self.servo_controller = ServoController()
        
        self.detectFaces()

    def detectFaces(self) -> None:
        while True:
            ret, frame = self.cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
            faces = self.face_model.detectMultiScale(gray, 1.1, 4) 

            for (x, y, w, h) in faces:
                # Calculate position of face and move servo
                number = self.servo_controller.setServoAngle()
                
                # draw a rectangle around the face
                self.gui.place_rectangle(frame, x, y, w, h)
               
            frame = self.gui.create_border(frame)    
            
            self.gui.place_text(frame, faces)
            
            self.gui.display_frame(frame)
            
    def exit(self) -> None:
        # On press of q, release the camera and destroy all windows
        self.cam.release()
        cv2.destroyAllWindows()
        self.servo_ctl.cleanup()
        GPIO.cleanup()

