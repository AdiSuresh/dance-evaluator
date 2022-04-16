# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from importlib.resources import path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
import os
import numpy as np
import pandas as pd
import mediapipe as mp
import Copy_File
import Compare_Dance
import Capture_Pose
# import runpy

# class VideoThread(QThread):
#     change_pixmap_signal = pyqtSignal(np.ndarray)

#     def __init__(self):
#         super().__init__()
#         self._run_flag = True

#     def run(self):
        
#         # Capture Pose captures the pose of the user records it and stores it in the output/Your_Dance folder

#         path=0 
#         save_output=True
        
#         op_path = './output/Your_Dance'

#         mp_drawing = mp.solutions.drawing_utils
#         mp_pose = mp.solutions.pose


#         # capture from web cam
#         cap = cv2.VideoCapture(0)

#         pose_at_frame = []
#         calc_timestamps = []
#         offset = 0.0
#         landmark_dict = {
#             0: 'Head_end',
#             11: 'UpperArmL',
#             12: 'UpperArmR',
#             13: 'LoweArmL',
#             14: 'LoweArmR',
#             15: 'HandL',
#             16: 'HandR',
#             23: 'Hip.L',
#             24: 'Hip.R',
#             25: 'ShinL',
#             26: 'ShinR',
#             27: 'FootL',
#             28: 'FootR',
#             31: 'FootL_end',
#             32: 'FootR_end'
#         }
#         with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#             while self._run_flag:
#                 ret, cv_img = cap.read()
#                 if ret:
#                     if len(calc_timestamps) == 0:
#                         offset = cap.get(cv2.CAP_PROP_POS_MSEC)
#                         calc_timestamps.append(0.0)
#                     else:
#                         calc_timestamps.append(calc_timestamps[-1] + cap.get(cv2.CAP_PROP_POS_MSEC) - offset)

#                     results = pose.process(cv_img)

#                     landmarks = dict()
#                     keys = landmark_dict.keys()
#                     if results.pose_landmarks is not None:
#                         for index, landmark in enumerate(results.pose_landmarks.landmark):
#                             if index in keys:
#                                 landmarks[landmark_dict[index]] = [landmark.x,
#                                                                 landmark.y,
#                                                                 landmark.z]

#                         pose_at_frame.append({
#                             'timestamp': calc_timestamps[-1],
#                             'landmarks': landmarks,
#                         })
                    
#                     # render detections
#                     mp_drawing.draw_landmarks(
#                         cv_img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                         mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
#                         mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
#                     )
                    
#                     # to flip the camera
#                     cv_img = cv2.flip(cv_img, flipCode = 1)


#                     self.change_pixmap_signal.emit(cv_img)
            
#             if save_output:
#                 df = pd.DataFrame(pose_at_frame)
#                 path = os.path.join(op_path, 'output.csv')
#                 df.to_csv(path)


#             # shut down capture system
#             cap.release()

#     def stop(self):
#         """Sets run flag to False and waits for thread to finish"""
#         self._run_flag = False
#         self.wait()


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Record your Dance Moves")
#         self.disply_width = 640
#         self.display_height = 480
#         # create the label that holds the image
#         self.image_label = QLabel(self)
#         self.image_label.resize(self.disply_width, self.display_height)
#         # create a text label
#         self.textLabel = QLabel('Get Ready to Dance')

#         # create a vertical box layout and add the two labels
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.image_label)
#         vbox.addWidget(self.textLabel)
#         # set the vbox layout as the widgets layout
#         self.setLayout(vbox)

#         # create the video capture thread
#         self.thread = VideoThread()
#         # connect its signal to the update_image slot
#         self.thread.change_pixmap_signal.connect(self.update_image)
#         # start the thread
#         self.thread.start()

#     def closeEvent(self, event):
#         self.thread.stop()
#         event.accept()



#     @pyqtSlot(np.ndarray)
#     def update_image(self, cv_img):
#         """Updates the image_label with a new opencv image"""
#         qt_img = self.convert_cv_qt(cv_img)
#         self.image_label.setPixmap(qt_img)
    
#     def convert_cv_qt(self, cv_img):
#         """Convert from an opencv image to QPixmap"""
#         rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
#         return QPixmap.fromImage(p)

class Home_Screen(QWidget):
    def upload_video(self):
        # exec(open("Copy_File.py").read())
        # os.system('python Copy_File.py')
        # runpy.run_path(path_name='Copy_File.py')

        # let's just run the function instead
        Copy_File.App()

    
    def record_dance(self):
        # Call capture_pose
		
        os.system('python capture_pose.py')
        # os.system('python pose_est\pose_est\capture_pose.py')
        # runpy.run_path(path_name='pose_est\pose_est\main.py')

        # capture_pose.App()
		

    def compare_dance(self):
        Compare_Dance.App()
        # os.system('python Compare_Dance.py')

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dance Evaluator')

        windowLayout = QHBoxLayout()
        
        Upload_video = QPushButton('Upload Video File to Estimate')
        # Upload Video File to Estimate
        Upload_video.clicked.connect(self.upload_video)
        windowLayout.addWidget(Upload_video)
        
        Record_Dance = QPushButton('Record your Dance Moves to Score')
        # Record your Dance Moves to Score
        Record_Dance.clicked.connect(self.record_dance)
        windowLayout.addWidget(Record_Dance)
        

        Compare_Dance = QPushButton('Comparing Dance Moves')
        # Comparing Dance Moves
        Compare_Dance.clicked.connect(self.compare_dance)
        windowLayout.addWidget(Compare_Dance)

        self.setLayout(windowLayout)

        self.show()



if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = Home_Screen()
    sys.exit(app.exec_())
    

# class Ui_Home_Screen(object):
#     def upload_video(self):
#         # exec(open("Copy_File.py").read())
#         # os.system('python Copy_File.py')
#         # runpy.run_path(path_name='Copy_File.py')

#         # let's just run the function instead
#         Copy_File.App()

    
#     def record_dance(self):
#         # Call capture_pose
		
#         os.system('python capture_pose.py')
#         # os.system('python pose_est\pose_est\capture_pose.py')
#         # runpy.run_path(path_name='pose_est\pose_est\main.py')

#         # capture_pose.App()
		

#     def compare_dance(self):
#         Compare_Dance.App()
#         # os.system('python Compare_Dance.py')

#     def setupUi(self, Home_Screen):
#         Home_Screen.setObjectName("Home_Screen")
#         Home_Screen.resize(800, 600)
#         Home_Screen.setStyleSheet("font-size: 20px;")
#         self.centralwidget = QWidget(Home_Screen)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout = QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName("gridLayout")
        
#         self.Upload_video = QPushButton(self.centralwidget)
#         self.Upload_video.setObjectName("Upload_video")
        
#         self.Upload_video.clicked.connect(self.upload_video)
        
#         self.gridLayout.addWidget(self.Upload_video, 0, 0, 1, 1)
#         self.Record_Dance = QPushButton(self.centralwidget)
#         self.Record_Dance.setObjectName("Record_Dance")
#         self.gridLayout.addWidget(self.Record_Dance, 0, 1, 1, 1)

#         self.Upload_video.clicked.connect(self.record_dance)


#         self.Compare_Dance = QPushButton(self.centralwidget)
#         self.Compare_Dance.setObjectName("Compare_Dance")
#         self.gridLayout.addWidget(self.Compare_Dance, 1, 0, 1, 2)

#         self.Compare_Dance.clicked.connect(self.compare_dance)

#         Home_Screen.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(Home_Screen)
#         self.menubar.setGeometry(QRect(0, 0, 800, 34))
#         self.menubar.setObjectName("menubar")
#         Home_Screen.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(Home_Screen)
#         self.statusbar.setObjectName("statusbar")
#         Home_Screen.setStatusBar(self.statusbar)

#         self.retranslateUi(Home_Screen)
#         QMetaObject.connectSlotsByName(Home_Screen)

    



#     def retranslateUi(self, Home_Screen):
#         _translate = QCoreApplication.translate
#         Home_Screen.setWindowTitle(_translate("Home_Screen", "MainWindow"))
#         self.Upload_video.setText(_translate("Home_Screen", "Upload Video File to Estimate"))
#         self.Record_Dance.setText(_translate("Home_Screen", "Record Your Dance Moves to Score"))
#         self.Compare_Dance.setText(_translate("Home_Screen", "Comparing Dance Moves"))


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     Home_Screen = QMainWindow()
#     ui = Ui_Home_Screen()
#     ui.setupUi(Home_Screen)
#     Home_Screen.show()
#     sys.exit(app.exec_())