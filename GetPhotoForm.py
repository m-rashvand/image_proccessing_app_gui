from PyQt5.QtWidgets import ( QWidget, QPushButton, QScrollArea, QLabel, QFileDialog, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt, pyqtSlot

from FeatureSelectionForm import FeatureSelectionForm
from styles import buttonStyle2, lableStyle2

class GetPhotoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Choose Photos')
        self.resize(600, 720)
        self.photos_path = []

        layout = QVBoxLayout()

        photos_lable = QLabel('<font size="22"> Photos </font>')
        photos_lable.setStyleSheet('color: #573b8a; font-weight: bold;')
        photos_lable.setAlignment(Qt.AlignCenter)
        layout.addWidget(photos_lable)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        layout.addWidget(self.scroll)

        self.photo_box = QVBoxLayout()
        self.photo_box.setAlignment(Qt.AlignTop)
        self.photo_box.setSpacing(0)

        box_bottons = QHBoxLayout()
        layout.addLayout(box_bottons)

        button_login = QPushButton('select photos')
        button_login.clicked.connect(self.get_file_name)
        button_login.setStyleSheet(buttonStyle2)
        box_bottons.addWidget(button_login)

        button_remove = QPushButton('remove all')
        button_remove.clicked.connect(self.remove_photos)
        button_remove.setStyleSheet(buttonStyle2)
        box_bottons.addWidget(button_remove)

        button_next = QPushButton('next')
        button_next.clicked.connect(self.next_page)
        button_next.setStyleSheet(buttonStyle2)
        box_bottons.addWidget(button_next)

        self.widget = QWidget()
        self.widget.setLayout(self.photo_box)
        self.scroll.setWidget(self.widget)
        self.setLayout(layout)

    @pyqtSlot()
    def next_page(self):
        self.cams = FeatureSelectionForm(self.photos_path)
        self.cams.show()
        self.close()

    @pyqtSlot()
    def get_file_name(self):
        file_names, f = QFileDialog.getOpenFileNames(
            self, 'Open File', 'E:', "Image files (*.jpg *.gif)")

        for file_name in file_names:
            if file_name:
                if file_name in self.photos_path:
                    continue
                self.photos_path.append(file_name)
                photo_lable = QLabel(file_name)
                photo_lable.setStyleSheet(lableStyle2)
                self.photo_box.addWidget(photo_lable)


    @pyqtSlot()
    def remove_photos(self):
        # remove all items from the photo_box and photos_path
        for i in range(len(self.photos_path)):
            self.photo_box.itemAt(0).widget().setParent(None)

        self.photos_path = []
