from PyQt5.QtWidgets import ( QWidget, QPushButton, QCheckBox,
                             QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSlot

from ShowResultForm import ShowResultForm
from styles import checkBoxStyle, buttonStyle

class FeatureSelectionForm(QWidget):
    def __init__(self, photos_path: list, checked_features: list = []):
        super().__init__()
        self.photos_path = photos_path
        self.checked_features = checked_features
        self.setWindowTitle('feature Selection')
        self.resize(500, 480)

        layout = QVBoxLayout()

        label_title = QLabel('<font size="22"> Choose Features </font>')
        label_title.setStyleSheet('color: #573b8a; font-weight: bold;')
        layout.addWidget(label_title)

        # 20 check boxes for features 0 to 20
        self.check_boxes = []
        for i in range(5):
            row = QHBoxLayout()
            for j in range(4):
                check_box = QCheckBox('feature ' + str(i*4+j))
                check_box.setStyleSheet(checkBoxStyle)
                row.addWidget(check_box)
                self.check_boxes.append(check_box)
            layout.addLayout(row)

        button_box = QHBoxLayout()

        button_next = QPushButton('next')
        button_next.clicked.connect(self.next_page)
        button_next.setStyleSheet(buttonStyle)
        button_box.addWidget(button_next)


        layout.addLayout(button_box)

        self.setLayout(layout)

    @pyqtSlot()
    def next_page(self):
        self.checked_features = []
        for check_box in self.check_boxes:
            if check_box.isChecked():
                self.checked_features.append(check_box.text())
        self.cams = ShowResultForm(self.checked_features, self.photos_path)
        self.cams.show()
        self.close()
