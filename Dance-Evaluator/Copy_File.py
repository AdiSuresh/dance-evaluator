import sys
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


class App(QWidget):

    target = r'D:/All Projects/Dance Evaluator/Dance-Evaluator/videos/Uploaded'

    def __init__(self):
        super().__init__()
        self.title = 'Select Video File to Upload'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # To set up the logo
        logo = QIcon()
        logo.addPixmap(QPixmap('assets/logo.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(logo)

        self.video_path = self.openFileNameDialog()
        
        self.catchpose()

        # self.openFileNamesDialog()
        # self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Video File to Upload", "","All Files (*);;MP4 (.mp4);; MOV (.mov);; WMV (.wmv);; FLV (.flv);; AVI (.avi)", options=options)
        
        # Need to include authentication to verify file format
        if fileName:
            original = fileName
            shutil.copy(original, self.target)
            # print(fileName)
            return fileName

    def catchpose(self):
        cap = cv2.VideoCapture(self.video_path)
        with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    # print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    break

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)

                # Draw the pose annotation on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        cap.release()

    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py);;CSV Files (*.csv)", options=options)
    #     if files:
    #         print(files)
    
    # def saveFileDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         original = fileName
    #         shutil.copyfile(original, self.target)
    #         print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
