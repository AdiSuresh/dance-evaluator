import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import pandas as pd
import numpy as np
import ast
import statistics as stat



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


        vbox = QVBoxLayout()

        accuracy, score = self.score()
        # print(accuracy)


        # Image_Label = QLabel()
        # pixmap = QPixmap('assets/nice_job.jpg')
        # Image_Label.setPixmap(pixmap)

        # vbox.addWidget(Image_Label)
        Image_Label = QLabel()
        pixmap = QPixmap('assets/celebrate2.jpg')
        Image_Label.setPixmap(pixmap)
        Image_Label.resize(640, 466)


        l1 = QLabel()
        l1.setText("<h1>Your accuracy is:</h1>")
        l2 = QLabel()
        l2.setText("<h1>"+str(accuracy)+"%</h1>")



        l3 = QLabel()
        l3.setText("<h1>Your Score is :</h1>")
        l4 = QLabel()
        l4.setText("<h1>"+str(score)+"</h1>")

        vbox.addWidget(Image_Label)
        vbox.addWidget(l1)
        vbox.addWidget(l2)
        vbox.addWidget(l3)
        vbox.addWidget(l4)        

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
        # reading the generated csv files
        upload = pd.read_csv('output/Upload/output.csv')
        your_dance = pd.read_csv('output/Your_Dance/output.csv')

        # Upload file CSV to numpy array
        upload_complete = []
        for i in range(0, upload.shape[0]):
            upload_dict = ast.literal_eval(upload.loc[i, 'landmarks'])
            upload_data = list(upload_dict.values())
            upload_complete.append(upload_data)
        
        uc_nparray = np.array(upload_complete)

        # Your Dance File CSV to numpy array
        your_dance_complete = []
        for i in range(0, your_dance.shape[0]):
            your_dance_dict = ast.literal_eval(your_dance.loc[i, 'landmarks'])
            your_dance_data = list(your_dance_dict.values())
            your_dance_complete.append(your_dance_data)
    
        ydc_nparray = np.array(your_dance_complete)

        # Converting 3D Numpy Array to 1D
        ydc = ydc_nparray.ravel()
        uc = uc_nparray.ravel()

        distance, path = fastdtw(ydc, uc, dist=euclidean)

        # To Calculate the Median of Path one and two
        path_one = []
        path_two = []
        for i in path:
            path_one.append(i[0])
            path_two.append(i[1])
        median_path_one = stat.median(path_one)
        median_path_two = stat.median(path_two)

        median_total = median_path_one + median_path_two

        # accuracy formula: round((1 - (distance/median_total)) * 100, 2)
        accuracy = round(((1 - (distance/median_total)) * 100), 2)
        score = int(accuracy * 6.66)

        return accuracy, score




        
    
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
