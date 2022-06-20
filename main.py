import sys
import cv2 as cv
from skimage.metrics import structural_similarity as compare_ssim
import imutils
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
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
        self.Pixmap1 = QPixmap('img/1.jpg')
        self.Pixmap1 = self.Pixmap1.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.imageField1 = QLabel("Image")
        self.imageField1.setPixmap(self.Pixmap1)
        self.imagesLayout.addWidget(self.imageField1)

        # image field 2
        self.Pixmap2 = QPixmap('img/2.jpg')
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
        self.subbtn.clicked.connect(self.showDifferences)
        self.mainLayout.addWidget(self.subbtn)

    # defining the browseImage mathod
    def browseImage(self, buttonID):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg)')
        imagePath = fname[0]
        Pixmap = QPixmap(imagePath)
        if buttonID == 1:
            Pixmap = Pixmap.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
            self.imageField1.setPixmap(QPixmap(Pixmap))
            Pixmap.save("img/1.jpg")
        elif buttonID == 2:
            Pixmap = Pixmap.scaled(IMG_SIZE, IMG_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
            self.imageField2.setPixmap(QPixmap(Pixmap))
            Pixmap.save("img/2.jpg")
        else:
            exit(0)

    def showDifferences(self):
        path = r'img/1.jpg'
        path_mod = r'img/2.jpg'

        # Using cv2.imread() method
        img = cv.imread(path)

        img_mod = cv.imread(path_mod)

        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_mod_gray = cv.cvtColor(img_mod, cv.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(img_gray, img_mod_gray, full=True)
        diff = (diff * 255).astype("uint8")

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # loop over the contours
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img_mod, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # show the output images
        cv.imshow("Here you are", img_mod)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
