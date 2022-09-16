from PyQt5.QtWidgets import ( QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt, pyqtSlot

from GetPhotoForm import GetPhotoForm

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 480)

        layout = QVBoxLayout()

        label_login = QLabel('<font size="22"> Login </font>')
        login = QHBoxLayout()
        login.addWidget(label_login)
        login.setAlignment(Qt.AlignCenter)
        layout.addLayout(login)

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Username')

        name = QHBoxLayout()
        name.addWidget(label_name)
        name.addWidget(self.lineEdit_username)
        layout.addLayout(name)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        password = QHBoxLayout()
        password.addWidget(label_password)
        password.addWidget(self.lineEdit_password)
        layout.addLayout(password)


        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
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
