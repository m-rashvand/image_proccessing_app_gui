from PyQt5.QtWidgets import ( QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt, pyqtSlot

from GetPhotoForm import GetPhotoForm
from styles import buttonStyle, LineEditStyle, lableStyle

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 480)

        layout = QVBoxLayout()

        label_login = QLabel('<font size="22"> Login </font>')
        label_login.setStyleSheet('color: #573b8a; font-weight: bold;')
        login = QHBoxLayout()
        login.addWidget(label_login)
        login.setAlignment(Qt.AlignCenter)
        layout.addLayout(login)

        label_name = QLabel('<font size="4"> Username </font>')
        label_name.setStyleSheet(lableStyle)
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Username')
        self.lineEdit_username.setStyleSheet(LineEditStyle)

        name = QHBoxLayout()
        name.addWidget(label_name)
        name.addWidget(self.lineEdit_username)
        layout.addLayout(name)

        label_password = QLabel('<font size="4"> Password </font>')
        label_password.setStyleSheet(lableStyle)
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setStyleSheet(LineEditStyle)
        password = QHBoxLayout()
        password.addWidget(label_password)
        password.addWidget(self.lineEdit_password)
        layout.addLayout(password)


        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        button_login.setStyleSheet(buttonStyle)
        layout.addWidget(button_login)

        label_empty = QLabel('')
        layout.addWidget(label_empty)

        self.setLayout(layout)

    @pyqtSlot()
    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'user' and self.lineEdit_password.text() == '1234':
            msg.setText('Welcome')
            msg.exec_()
            self.cams = GetPhotoForm()
            self.cams.show()
            self.close()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()
