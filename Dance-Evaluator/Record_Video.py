# import the opencv library
import cv2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):

    target = r'D:/All Projects/dancing-ai-robot/fyp-gui/pose_est/videos/Uploaded'

    def __init__(self):
        super().__init__()
        
        self.record()

    def record(self):
        # define a video capture object
        vid = cv2.VideoCapture(0)

        while(True):

            # Capture the video frame
            # by frame
            ret, frame = vid.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # After the loop release the cap object
        vid.release()