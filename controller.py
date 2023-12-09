import cv2

from config import CONFIG
from servo_ctl import ServoController
from gui import GUI

class Controller: 
    def __init__(self) -> None:  
        self.config = CONFIG() # instantiate gui and config classes
        self.gui = GUI(self)
        
        self.face_model = self.config.get_face_model()   # get face model and camera from config
        
        self.cam = self.config.get_camera()
        
        self.servo_controller = ServoController()
        
        self.detect_faces()

    def detect_faces(self) -> None:
        angle = 90
        self.servo_controller.set_servo_angle(angle)

        while True:
            ret, frame = self.cam.read()
                    
            frame_center_x, frame_center_y = self.get_frame_center(frame)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale for ease of analysis
            faces = self.face_model.detectMultiScale(gray, 1.1, 4) 

            for (x, y, w, h) in faces:
                                
                # draw a rectangle around faces detected 
                self.gui.place_rectangle(frame, x, y, w, h)

                center_x = x + w // 2
                center_y = y + h // 2
                
                self.gui.place_center_dot(frame, center_x, center_y, (0, 255, 0))
                self.gui.place_center_dot(frame, frame_center_x, frame_center_y, (0, 0, 255))

                
                angle = self.check_face_left_right(center_x, frame_center_x, angle)     # Calculate position of face and move servo
                
               
            frame = self.gui.create_border(frame)    
            
            self.gui.place_text(frame, faces)
            
            self.gui.display_frame(frame)
            
    def get_frame_center(self, frame) -> int:
        height, width = frame.shape[:2] 
        
        frame_center_x = width // 2
        frame_center_y = height // 2
        
        return frame_center_x, frame_center_y
            
    def check_face_left_right(self, center_x, frame_center_x, angle) -> None:
        """ Checking if face is to the left or right of the frame center, and moving the servo accordingly
        """
        
        difference = abs(center_x - frame_center_x)
        movement = max(.5, difference // 100)
        
        print("Face center: ", center_x,"Frame center: ", frame_center_x)
        print("Difference b/w them: ", difference)
        print("Movement: ", movement)
        
        if center_x < frame_center_x:
            angle += movement
        elif center_x > frame_center_x:
            angle -= movement
        else:
            print("Dead Center")
        self.servo_controller.set_servo_angle(angle)
        return angle
    
    def exit(self) -> None:
        """ On press of q, release the camera, cleanup the servo class, and destroy all windows
        """
        
        self.cam.release()
        cv2.destroyAllWindows()
        self.servo_controller.cleanup()

