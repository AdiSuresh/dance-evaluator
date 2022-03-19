import sys
from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Dance Pose Checker'
        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 720
        self.initUI()

    def button_clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        self.label.setText("my first label!            ")
        self.label.move(50, 50)

        self.b1 = QPushButton(self)
        self.b1.setText("Upload Video File to Estimate")
        self.b1.move(200,200)
        self.b1.clicked.connect(self.button_clicked)

        self.b2 = QPushButton(self)
        self.b2.setText("Record Your Dance Moves in Score")
        self.b2.move(800, 200)

        self.b3 = QPushButton(self)
        self.b3.setText("Comparing Dance Moves")
        self.b3.move(500, 500)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
