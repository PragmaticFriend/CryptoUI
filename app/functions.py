import os
import sys
import sqlite3
from sqlite3 import Error


import string
import secrets
import datetime
from pprint import pprint

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

from PySide2.QtWidgets import QTableWidgetItem, QErrorMessage, QMessageBox
from PyQt5.QtGui import QIntValidator
from settings import DB_PATH, GLOBAL_SALT, ROOT_KEY, ROOT_STANDART_PASSWORD, MESSAGES_STYLE



class AppFunctions():
    def __init__(self, arg) -> None:
        super(AppFunctions, self).__init__()
        self.arg = arg

        onlyInt = QIntValidator()
        onlyInt.setRange(4, 100)
        self.ui.passLength_2.setValidator(onlyInt)
        

    def create_connection(db_path):
        conn = None
        try:
            conn = sqlite3.connect(db_path)
        except Error as err:
            print(err)
        return conn


    def createTable():
        create_passwords_table_sql = """
        CREATE TABLE IF NOT EXISTS Passwords (
        pass_id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT,
        cipher_iv TEXT,
        cipher_data TEXT,
        creation_date DATETIME
        );"""

        conn = AppFunctions.create_connection(DB_PATH)
        try:
            curs = conn.cursor()
            curs.execute(create_passwords_table_sql)
        except Error as err:
            print(err)
            print(f"Error! Проблема с подключением к БД {DB_PATH}")

    def createRootTable():
        create_root_table = """
        CREATE TABLE IF NOT EXISTS Root (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        root_password TEXT
        );"""

        root_standart_pass = ROOT_STANDART_PASSWORD

        m = hashlib.sha256()
        m.update(root_standart_pass.encode())
        hashed_pass = m.hexdigest()

        conn = AppFunctions.create_connection(DB_PATH)
        try:
            curs = conn.cursor()
            curs.execute(create_root_table)

            insert_password_sql = f"""
                INSERT INTO Root (root_password)
                VALUES ('{hashed_pass}')
                """
            if conn.cursor().execute(insert_password_sql):
                conn.commit()

        except Error as err:
            print(err)
            print(f"Error! Проблема с подключением к БД {DB_PATH}")

    def getAllPasswords():
        get_all_passwords_sql = """
            SELECT * FROM Passwords
        """
        
        conn = AppFunctions.create_connection(DB_PATH)

        try:
            cursor = conn.cursor()
            cursor.execute(get_all_passwords_sql)
            return cursor
        
        except Error as err:
            print(err)


    def prepareDataForRender(data: list) -> list:
        result_data = []
        for row in data:
            cipher_iv_base64 = base64.b64decode(row[2])
            cipher_data_base64 = base64.b64decode(row[3])

            decrypted_password = AppFunctions.decrypt_password_aes(ROOT_KEY, cipher_iv_base64, cipher_data_base64)
            new_row = (row[0], row[1], decrypted_password.decode(), row[4])
            result_data.append(new_row)
        return result_data
            

    def renderPasswordsTable(self, data):
        data = list(data.fetchall())
        data = AppFunctions.prepareDataForRender(data)

        for row in data:
            rowPosition = self.ui.tableWidget.rowCount()

            if rowPosition > row[0]:
                continue
            item_count = 0

            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidget_item = QTableWidgetItem()

            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidget_item)

            for item in row:
                self.qtablewidget_item = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, item_count, self.qtablewidget_item)
                self.qtablewidget_item = self.ui.tableWidget.item(rowPosition, item_count)
                self.qtablewidget_item.setText(str(item))
                item_count += 1

            rowPosition += 1

    def addPassword(self):
        is_valid = True

        login = self.ui.login_2.text()
        pass_len = self.ui.passLength_2.text()
        use_numeric = self.ui.useNumeric_2.isChecked()
        use_spec_chars = self.ui.useSpecCharacters_2.isChecked()
        use_uppercase = self.ui.useUpperCase_2.isChecked()


        try:
            int(pass_len)
        except Exception:
            error_dialog = QErrorMessage()
            error_dialog.setWindowTitle("Ошибка!")
            error_dialog.setStyleSheet(MESSAGES_STYLE)
            error_dialog.showMessage('Длина пароля должна быть записана в числовом формате')
            is_valid = False
            self.ui.passLength_2.setText("")
            raise ValueError
        

        if is_valid:
            generated_pass = AppFunctions.generate_password(pass_len, use_numeric, use_spec_chars, use_uppercase)
            creation_date = datetime.datetime.now()
            conn = AppFunctions.create_connection(DB_PATH)

            cipher_iv, cipher_data = AppFunctions.encrypt_password_aes(ROOT_KEY, generated_pass)

            cipher_iv_base64 = base64.b64encode(cipher_iv)
            cipher_data_base64 = base64.b64encode(cipher_data)
            insert_password_sql = f"""
                INSERT INTO Passwords (login, cipher_iv, cipher_data, creation_date) 
                VALUES ('{login}', '{cipher_iv_base64.decode()}', '{cipher_data_base64.decode()}', '{creation_date}')
                """

            if conn.cursor().execute(insert_password_sql):
                conn.commit()
                self.ui.login_2.setText("")
                self.ui.passLength_2.setText("")
                AppFunctions.renderPasswordsTable(self, AppFunctions.getAllPasswords())

    def changeRootPasssword(self):
        is_valid = True
        
        root_new_password = self.ui.rootPassword.text()

        if len(root_new_password) < 4:
            is_valid = False
            error_dialog = QErrorMessage()
            error_dialog.setWindowTitle("Ошибка!")
            error_dialog.setStyleSheet(MESSAGES_STYLE)
            error_dialog.showMessage('Длина пароля должна быть > 3')
            self.ui.rootPassword.setText("")
            raise ValueError
            
        if is_valid:
            m = hashlib.sha256()
            m.update(root_new_password.encode())
            hashed_pass = m.hexdigest()

            conn = AppFunctions.create_connection(DB_PATH)
            try:
                update_password_sql = f"""
                    UPDATE Root
                    Set root_password = '{hashed_pass}'
                    WHERE id = 1;
                    """
                if conn.cursor().execute(update_password_sql):
                    conn.commit()

                    msg = QMessageBox() 
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Изменения сохранены")
                    msg.setText("Новый Мастер Пароль сохранен!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setStyleSheet(MESSAGES_STYLE)
                    msg.exec_()


            except Error as err:
                print(err)
                print(f"Error! Проблема при изменении Root пароля {DB_PATH}")



    def generate_password(pass_len, use_numeric, use_spec_chars, use_uppercase):
        alphabet = string.ascii_lowercase

        if use_numeric:
            alphabet += string.digits

        if use_spec_chars:
            alphabet += string.punctuation

        if use_uppercase:
            alphabet += string.ascii_uppercase

        generated_pass = ''
        for i in range(int(pass_len)):
            generated_pass += ''.join(secrets.choice(alphabet))

        return generated_pass

    @staticmethod
    def generate_salt():
        salt = get_random_bytes(32)
        return salt

    @staticmethod
    def encrypt_password_aes(key, password: str):
        # key = PBKDF2(root_password, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(password.encode(), AES.block_size))
        return cipher.iv, ciphered_data

    @staticmethod
    def decrypt_password_aes(key, cipher_iv, ciphered_data):
        cipher = AES.new(key, AES.MODE_CBC, iv=cipher_iv)
        decr_p = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        return decr_p

    @staticmethod
    def checkRootPasswordHash(input_pass):
        m_input = hashlib.sha256()
        m_input.update(input_pass.encode())
        hashed_pass_input = m_input.hexdigest()
        hashed_root_pass = AppFunctions.getRootPassword()

        if hashed_pass_input == hashed_root_pass:
            return True
        else:
            return False

    @staticmethod
    def getRootPassword():
        get_all_passwords_sql = """
            SELECT * FROM Root
        """
        
        conn = AppFunctions.create_connection(DB_PATH)

        try:
            cursor = conn.cursor()
            cursor.execute(get_all_passwords_sql)
        except Error as err:
            print("Ошибка в чтении Root пароля")
            print(err)
        else:
            id_, hashed_pass = list(cursor.fetchall())[0]
            return hashed_pass

   

if __name__ == "__main__":
    ...
    print(os.getcwd())
