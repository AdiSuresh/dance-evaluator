import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Dance Pose Checker'
        self.left = 0
        self.top = 10
        self.width = 1280
        self.height = 500
        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Upload Video File to Estimate
        self.b1 = QPushButton(self)
        self.b1.setText("Upload Video File to Estimate")
        self.b1.move(256,50)
        self.b1.setStyleSheet("padding: 50px; font-size: 16px;")
        self.b1.clicked.connect(self.upload_video)

\
        # Record Dance Moves to Score
        self.b2 = QPushButton(self)
        self.b2.setText("Record Your Dance Moves in Score")
        self.b2.move(768, 50)
        self.b2.setStyleSheet("padding: 50px; font-size: 16px;")

        # Compare pre-recorded dance moves
        self.b3 = QPushButton(self)
        self.b3.setText("Comparing Dance Moves")
        self.b3.move(256, 300)
        self.b3.setStyleSheet("padding: 50px; font-size: 16px;")

        self.show()

        def upload_video(self):
            fileitem = form['filename']

            # check if the file has been uploaded


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
