from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
import mediapipe as mp
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import pandas as pd
import os


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        
        # Capture Pose captures the pose of the user records it and stores it in the output/Your_Dance folder

        path=0 
        save_output=True
        
        op_path = './output/Your_Dance'

        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose


        # capture from web cam
        cap = cv2.VideoCapture(0)

        pose_at_frame = []
        calc_timestamps = []
        offset = 0.0
        landmark_dict = {
            0: 'Head_end',
            11: 'UpperArmL',
            12: 'UpperArmR',
            13: 'LoweArmL',
            14: 'LoweArmR',
            15: 'HandL',
            16: 'HandR',
            23: 'Hip.L',
            24: 'Hip.R',
            25: 'ShinL',
            26: 'ShinR',
            27: 'FootL',
            28: 'FootR',
            31: 'FootL_end',
            32: 'FootR_end'
        }
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self._run_flag:
                ret, cv_img = cap.read()
                if ret:
                    if len(calc_timestamps) == 0:
                        offset = cap.get(cv2.CAP_PROP_POS_MSEC)
                        calc_timestamps.append(0.0)
                    else:
                        calc_timestamps.append(calc_timestamps[-1] + cap.get(cv2.CAP_PROP_POS_MSEC) - offset)

                    results = pose.process(cv_img)

                    landmarks = dict()
                    keys = landmark_dict.keys()
                    if results.pose_landmarks is not None:
                        for index, landmark in enumerate(results.pose_landmarks.landmark):
                            if index in keys:
                                landmarks[landmark_dict[index]] = [landmark.x,
                                                                landmark.y,
                                                                landmark.z]

                        pose_at_frame.append({
                            'timestamp': calc_timestamps[-1],
                            'landmarks': landmarks,
                        })
                    
                    # render detections
                    mp_drawing.draw_landmarks(
                        cv_img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
                    )
                    
                    # to flip the camera
                    cv_img = cv2.flip(cv_img, flipCode = 1)


                    self.change_pixmap_signal.emit(cv_img)
            
            if save_output:
                df = pd.DataFrame(pose_at_frame)
                path = os.path.join(op_path, 'output.csv')
                df.to_csv(path)


            # shut down capture system
            cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Record your Dance Moves")
        
        # To set up the logo
        logo = QIcon()
        logo.addPixmap(QPixmap('assets/logo.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(logo)
        
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Get Ready to Dance')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()



    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())