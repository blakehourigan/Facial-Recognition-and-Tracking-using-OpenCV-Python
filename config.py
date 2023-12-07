import cv2

class CONFIG:
    def __init__(self) -> None:
        # Choose model to use for OpenCV face detection
        self.face_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # get the first available camera 
        self.cam = cv2.VideoCapture(0)        
        
        self.servo_PIN = 17

    def get_camera(self) -> cv2.VideoCapture:
        return self.cam
    
    def get_face_model(self) -> cv2.CascadeClassifier:
        return self.face_model
    
    def get_servo_pin(self) -> int:
        return self.servo_PIN





