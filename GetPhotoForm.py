from PyQt5.QtWidgets import ( QWidget,)


class GetPhotoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Choose Photos')
        self.resize(500, 480)
