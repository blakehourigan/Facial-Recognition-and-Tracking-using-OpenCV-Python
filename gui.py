import cv2
import numpy as np

class GUI:
    def __init__(self) -> None:
        self.border_size = 50
        self.setup()
    
    def display_frame(self, frame) -> None:
        # Display the resulting frame, press q to quit the application
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            exit()
    
    def create_border(self, frame) -> np.ndarray:
        frame = cv2.copyMakeBorder(frame, self.border_size, self.border_size, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        return frame
    
    def place_text(self, frame, faces) -> None:
        cv2.putText(frame, 'Number of faces detected: ' + str(len(faces)) , (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1,\
            (255, 50, 0), 2)
        
        cv2.putText(frame,'Press \'q\' to quit', (0, frame.shape[0] - 15), cv2.FONT_HERSHEY_SIMPLEX, 1,\
        (255, 50, 0), 2)
    
    def place_rectangle(self, frame, x, y, w, h) -> None:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    def cleanup(self):
        # Perform any cleanup tasks here
        pass
