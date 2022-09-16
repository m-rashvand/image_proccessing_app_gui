import sys
from PyQt5.QtWidgets import (QApplication,)
from LoginForm import LoginForm

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()

    sys.exit(app.exec_())
