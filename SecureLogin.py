import sys
from PyQt5 import QtWidgets, uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginApp, self).__init__()
        uic.loadUi('tela_login.ui', self)
        
        self.pushButton.clicked.connect(self.show_registration)
        self.pushButton_2.clicked.connect(self.login)
        
    def show_registration(self):
        self.registration_window = RegistrationApp()
        self.registration_window.show()

    def login(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if self.authenticate(login, password):
            self.system_window = SystemApp()
            self.system_window.show()
        else:
            self.error_window = ErrorApp()
            self.error_window.show()
        
    def authenticate(self, login, password):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="securelogin"
        )
        
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE login = %s AND password = %s"
        cursor.execute(query, (login, password))
        result = cursor.fetchone()
        
        cursor.close()
        db.close()
        
        return result is not None

class RegistrationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(RegistrationApp, self).__init__()
        uic.loadUi('tela_cadastro.ui', self)
        
        self.pushButton.clicked.connect(self.register_user)
        
    def register_user(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="securelogin"
        )
        
        cursor = db.cursor()
        query = "INSERT INTO users (login, password) VALUES (%s, %s)"
        cursor.execute(query, (login, password))
        db.commit()
        
        cursor.close()
        db.close()
        
        QMessageBox.information(self, "Success", "User registered successfully!")
        self.close()

class SystemApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SystemApp, self).__init__()
        uic.loadUi('tela_sistema.ui', self)

class ErrorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ErrorApp, self).__init__()
        uic.loadUi('tela_senhaerrada.ui', self)
        
        self.pushButton.clicked.connect(self.back_to_login)
        
    def back_to_login(self):
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = LoginApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
