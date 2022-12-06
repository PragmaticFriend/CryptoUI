import os
import sys
from ui_interface import Ui_MainWindow
from ui_interface_login import Ui_MainWindow as Ui_MainWindow_Login
from Custom_Widgets.Widgets import *

from settings import MESSAGES_STYLE


settings = QSettings()

from functions import AppFunctions


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Войти', self)
        self.buttonLogin.clicked.connect(self.handleLogin)

        font = QFont()
        font.setFamily(u"Inter")
        font.setPointSize(8)
        self.setStyleSheet(MESSAGES_STYLE)

        self.textPass.setFont(font)
        self.buttonLogin.setFont(font)
        self.setWindowTitle("Введите Мастер Пароль")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(30)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

        AppFunctions.createRootTable()

    def handleLogin(self):
        if AppFunctions.checkRootPasswordHash(self.textPass.text()):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка!', 'Неправильный Мастер-пароль')



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        json_style_path = "data\style.json"
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui)

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            json_style_path
            })
        self.show()

        QAppSettings.updateAppSettings(self)

        AppFunctions.createTable()
        AppFunctions.renderPasswordsTable(self, AppFunctions.getAllPasswords())
        
        self.ui.addPassBtn.clicked.connect(lambda: AppFunctions.addPassword(self))
        self.ui.saveRootPasswordBtn.clicked.connect(lambda: AppFunctions.changeRootPasssword(self))


        settings = QSettings()
        settings.setValue("THEME", "Темно-Синяя")

        QAppSettings.updateAppSettings(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
