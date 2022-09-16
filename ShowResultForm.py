from PyQt5.QtWidgets import ( QWidget, QScrollArea, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QPixmap

from styles import lableStyle

class ShowResultForm(QWidget):
    def __init__(self, checked_features: list, photos_path: list):
        super().__init__()
        self.checked_features = checked_features
        self.photos_path = photos_path
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Show Result')
        self.resize(620, 720)

        layout = QVBoxLayout()

        label_title = QLabel('<font size="22"> Result </font>')
        label_title.setStyleSheet('color: #573b8a; font-weight: bold;')
        layout.addWidget(label_title)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        layout.addWidget(self.scroll)

        self.photo_box = QVBoxLayout()
        self.photo_box.setAlignment(Qt.AlignTop)
        self.photo_box.setSpacing(0)

        # for each feature show all photos
        for feature in self.checked_features:
            self.feature_box = QVBoxLayout()
            self.feature_box.setAlignment(Qt.AlignTop)
            self.feature_box.setSpacing(0)

            label_feature = QLabel(feature)
            label_feature.setStyleSheet(lableStyle)
            self.feature_box.addWidget(label_feature)

            for i in range(0, len(self.photos_path), 4):
                row = QHBoxLayout()
                for j in range(4):
                    if i+j >= len(self.photos_path):
                        break
                    photo_lable = QLabel()
                    image = QPixmap(self.photos_path[i+j])
                    image = image.scaled(150, 150, Qt.KeepAspectRatio)
                    photo_lable.setPixmap(image)
                    row.addWidget(photo_lable)
                self.feature_box.addLayout(row)
            self.photo_box.addLayout(self.feature_box)

        self.widget = QWidget()
        self.widget.setLayout(self.photo_box)
        self.scroll.setWidget(self.widget)

        self.setLayout(layout)

