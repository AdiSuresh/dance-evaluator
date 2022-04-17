import sys
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import pandas as pd


class App(QWidget):

    # target = r'D:/All Projects/dancing-ai-robot/fyp-gui/pose_est/videos'
    rows, diff_lines = None, 0


    def __init__(self):
        super().__init__()
        self.title = 'Comparing Dance Moves'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)

        # To set up the logo
        logo = QIcon()
        logo.addPixmap(QPixmap('assets/logo.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(logo)

        self.uploaded = 'output/Upload/output.csv'

        self.recorded = 'output/Your_Dance/output.csv'


        vbox = QHBoxLayout()

        accuracy = self.score()
        # print(accuracy)


        # Image_Label = QLabel()
        # pixmap = QPixmap('assets/nice_job.jpg')
        # Image_Label.setPixmap(pixmap)

        # vbox.addWidget(Image_Label)


        l2 = QLabel()
        l2.setText("<h1>Your accuracy is :</h1>")
        l1 = QLabel()
        l1.setText("<h1>"+str(accuracy)+"</h1>")


        vbox.addWidget(l2)
        vbox.addWidget(l1)

         # To fix the width and height
        self.setMaximumSize(self.width(), self.height())

        self.setLayout(vbox)

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
        with open(self.uploaded, 'r') as csv1, open(self.recorded, 'r') as csv2:
            import1 = csv1.readlines()
            import2 = csv2.readlines()
            self.rows = len(import1)
            self.diff_lines = self.rows
            with open('output/data_diff.csv', 'w') as outFile:         
                for self.row in import2:
                    # looping through import2 and checking on import1
                    if self.row not in import1:
                        self.diff_lines -= 1
                        outFile.write(self.row)
 
        if self.rows and self.diff_lines:
            return self.compute()
        return 0
    
    def compute(self):
        a = self.rows
        b = self.diff_lines
        return round(float(100 - 100*(2*(a-b)/(a+b))),3)
    
    # def openUpload(self):
    #     # Uploaded Video file selection

    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     uploaded, _ = QFileDialog.getOpenFileName(self,"Uploaded Video Files", "./output/Upload","CSV Files (.csv)", options=options)
        
    #     # Need to include authentication to verify file format
    #     if uploaded:
    #         # original = uploaded
    #         # shutil.copy(original, self.target)
    #         return uploaded
        

    # def openYourDance(self):
    #     # Recorded Video file selection
        
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     recorded, _ = QFileDialog.getOpenFileName(self,"Recorded Video Files", "./output/Your_Dance","CSV Files(.csv)", options=options)
        
    #     # Need to include authentication to verify file format
    #     if recorded:
    #         # original = recorded
    #         # shutil.copy(original, self.target)
    #         return recorded
            
    
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
