import sys
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Scoring
import os


class App(QWidget):

    # target = r'D:/All Projects/dancing-ai-robot/fyp-gui/pose_est/videos'


    def __init__(self):
        super().__init__()
        self.title = 'Comparing Dance Moves'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        uploaded = self.openUpload()
        print(uploaded)
        recorded = self.openYourDance()
        print(recorded)

        self.score()

        # scoring = QPushButton('Score', self)
        # scoring.clicked.connect(self.score)

        # v_box = QVBoxLayout()
        # v_box.addWidget(scoring)
        # self.setLayout(v_box)

        # self.openFileNamesDialog()
        # self.saveFileDialog()
        
        self.show()
    
    # scoring function 
    def score(self):
        print('Scoring Function')
        os.system('python Scoring.py')
        # Scoring.Ui_Scoring()

    
    def openUpload(self):
        # Uploaded Video file selection

        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        uploaded, _ = QFileDialog.getOpenFileName(self,"Uploaded Video Files", "./pose_est/output/Upload","All Files (*);; CSV (.csv)", options=options)
        
        # Need to include authentication to verify file format
        if uploaded:
            # original = uploaded
            # shutil.copy(original, self.target)
            return uploaded
        

    def openYourDance(self):
        # Recorded Video file selection
        
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        recorded, _ = QFileDialog.getOpenFileName(self,"Recorded Video Files", "./pose_est/output/Your_Dance","All Files (*);; CSV (.csv)", options=options)
        
        # Need to include authentication to verify file format
        if recorded:
            # original = recorded
            # shutil.copy(original, self.target)
            return recorded
            
    
    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     # options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;CSV Files (*.csv)", options=options)
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
