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
        self.imagesLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # initializing the buttons layout
        self.buttonsLayout = QHBoxLayout()

        # image field 1
        self.Pixmap1 = QPixmap('img/Mona_Lisa.jpg')
        self.Pixmap1 = self.Pixmap1.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.imageField1 = QLabel("Image")
        self.imageField1.setPixmap(self.Pixmap1)
        self.imagesLayout.addWidget(self.imageField1)

        # image field 2
        self.Pixmap2 = QPixmap('img/Mona_Lisa.jpg')
        self.Pixmap2 = self.Pixmap2.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.imageField2 = QLabel("Image")
        self.imageField2.setPixmap(self.Pixmap2)
        self.imagesLayout.addWidget(self.imageField2)

        # upload image buttons
        self.btn1 = QPushButton("Browse image 1")
        self.buttonsLayout.addWidget(self.btn1)
        self.btn1.clicked.connect(lambda: self.browseImage(1))

        self.btn2 = QPushButton("Browse image 2")
        self.buttonsLayout.addWidget(self.btn2)
        self.btn2.clicked.connect(lambda: self.browseImage(2))

        # setting mainLayout as a default layout
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.imagesLayout)
        self.mainLayout.addLayout(self.buttonsLayout)

        # adding the submit button
        self.subbtn = QPushButton("Show Differences")
        self.mainLayout.addWidget(self.subbtn)

    # defining the browseImage mathod
    def browseImage(self, buttonID):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png)')
        imagePath = fname[0]
        Pixmap = QPixmap(imagePath)
        if buttonID == 1:
            Pixmap = Pixmap.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
            self.imageField1.setPixmap(QPixmap(Pixmap))
        elif buttonID == 2:
            Pixmap = Pixmap.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
            self.imageField2.setPixmap(QPixmap(Pixmap))
        else:
            exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())