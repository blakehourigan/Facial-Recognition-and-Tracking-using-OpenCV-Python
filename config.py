import cv2

class CONFIG:
    def __init__(self):
        # Choose model to use for OpenCV face detection
        self.face_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # get the first available camera 
        self.cam = cv2.VideoCapture(0)        

    def get_camera(self):
        return self.cam
    
    def get_face_model(self):
        return self.face_model





