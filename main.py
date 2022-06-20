import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QLineEdit,
    QDialog,
    QFileDialog
)

IMG_SIZE = 500
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.initUI()
    def initWindow(self):
        self.setWindowTitle("Image Difference Recognition")
        self.setGeometry(100, 100, 500, 700)
    def initUI(self):
        # initializing the main layout
        self.mainLayout = QVBoxLayout()

        # initializing the images layout
        self.imagesLayout = QHBoxLayout()

        # initializing the buttons layout
        self.buttonsLayout = QHBoxLayout()

        # image field
        Pixmap = QPixmap('img/Mona_Lisa.jpg')
        Pixmap = Pixmap.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.imageField = QLabel("Image")
        self.imageField.setPixmap(Pixmap)
        self.mainLayout.addWidget(self.imageField)

        # upload image buttons
        self.btn1 = QPushButton("Browse image 1")
        self.buttonsLayout.addWidget(self.btn1)
        self.btn1.clicked.connect(self.browseImage)

        self.btn2 = QPushButton("Browse image 2")
        self.buttonsLayout.addWidget(self.btn2)
        self.btn2.clicked.connect(self.browseImage)

        # setting mainLayout as a default layout
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.buttonsLayout)

    # defining the browseImage mathod
    def browseImage(self, buttonID):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png)')
        imagePath = fname[0]
        Pixmap = QPixmap(imagePath)
        Pixmap = Pixmap.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.imageField.setPixmap(QPixmap(Pixmap))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())