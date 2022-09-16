from PyQt5.QtWidgets import ( QWidget, )


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 480)

    