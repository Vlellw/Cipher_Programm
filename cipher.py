import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QTextEdit, QComboBox, QFrame
from PyQt6.QtGui import QIcon
import random

key13 = '!@#$%^&*()_-=+.,?\|}]{[<>/'
key12 = 'abcdefghijklmnopqrstuvwxyz'

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифровальщик")
        self.setGeometry(0, 0, 618, 432)
        self.setStyleSheet("background-color: rgb(51, 51, 51); font-family: Segoe UI;")

        self.label_4 = QLabel(self)
        self.label_4.setGeometry(50, 180, 71, 16)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setText("Ввод текста")

        self.label_5 = QLabel(self)
        self.label_5.setGeometry(310, 180, 231, 16)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setText("Шифрованный/дешифрованный текст")

        self.frame = QFrame(self)
        self.frame.setGeometry(50, 30, 511, 101)
        self.frame.setStyleSheet(
            "background-color: rgba(16, 16, 16, 30); border: 3px solid rgba(88, 88, 88, 80); border-radius: 5px;")

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setGeometry(260, 50, 251, 51)
        self.comboBox.setStyleSheet(
            "color: white; font-weight: bold; font-size: 8pt; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(38, 38, 38, 255), stop:1 rgba(62, 62, 62, 255));")
        self.comboBox.addItems(["Шифр Цезаря", "Шифр Полибия", "Шифр Виженера", "Шифр Аникина", "Шифр Васильева", "Шифр Левинского"])

        self.label_7 = QLabel(self.frame)
        self.label_7.setGeometry(260, 0, 251, 51)
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setText("                      Метод Шифрования")

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setGeometry(0, 0, 261, 51)
        self.pushButton_4.setStyleSheet(
            "color: white; font-weight: bold; font-size: 8pt; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(38, 38, 38, 255), stop:1 rgba(62, 62, 62, 255)); border: 1px solid rgb(134, 134, 134); border-radius: 2px; icon-size: 22px;")
        self.pushButton_4.setText("Зашифровать")

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setGeometry(0, 50, 261, 51)
        self.pushButton_5.setStyleSheet(
            "color: white; font-weight: bold; font-size: 8pt; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(38, 38, 38, 255), stop:1 rgba(62, 62, 62, 255)); border: 1px solid rgb(134, 134, 134); border-radius: 2px; icon-size: 22px;")
        self.pushButton_5.setText("Дешифровать")

        self.textEdit_3 = QTextEdit(self)
        self.textEdit_3.setGeometry(50, 300, 256, 91)
        self.textEdit_3.setStyleSheet(
            "color: white; background-color: rgb(25, 25, 25); border-radius: 5px; border: 1px solid rgb(117, 117, 117); font-size: 16pt")

        self.label_6 = QLabel(self)
        self.label_6.setGeometry(50, 280, 71, 20)
        self.label_6.setStyleSheet("color: white; background-color: none")
        self.label_6.setText("Ввод ключа")

        self.label_3 = QTextEdit(self)
        self.label_3.setGeometry(310, 200, 251, 191)
        self.label_3.setStyleSheet(
            "color: white; background-color: rgb(25, 25, 25); border-radius: 5px; border: 1px solid rgb(117, 117, 117); font-size: 16pt")
        self.label_3.setText("")

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(50, 200, 256, 81)
        self.textEdit.setStyleSheet(
            "color: white; background-color: rgb(25, 25, 25); border-radius: 5px; border: 1px solid rgb(117, 117, 117); font-size: 16pt")

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(312, 140, 250, 31)
        self.pushButton_2.setStyleSheet(
            "color: white; font-weight: bold; font-size: 8pt; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(38, 38, 38, 255), stop:1 rgba(62, 62, 62, 255)); border: 1px solid rgb(134, 134, 134); border-radius: 2px; icon-size: 22px;")
        self.pushButton_2.setText("Предыдущее действие")

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(50, 140, 260, 31)
        self.pushButton.setStyleSheet(
            "color: white; font-weight: bold; font-size: 8pt; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(38, 38, 38, 255), stop:1 rgba(62, 62, 62, 255)); border: 1px solid rgb(134, 134, 134); border-radius: 2px; icon-size: 22px;")
        self.pushButton.setText("Удалить текст")
        self.pushButton.setEnabled(True)

        self.pushButton.clicked.connect(self.clear_text_fields)

        self.pushButton_4.clicked.connect(self.encrypt_decrypt)
        self.pushButton_5.clicked.connect(self.encrypt_decrypt)

        self.pushButton_2.clicked.connect(self.prev_action)

        self.prev_action = []

    def clear_text_fields(self):
        self.textEdit.clear()
        self.textEdit_3.clear()
        self.label_3.clear()

    def encrypt_decrypt(self):
        cipher = self.comboBox.currentText()
        text = self.textEdit.toPlainText()
        key = self.textEdit_3.toPlainText()
        self.prev_action.append((cipher, text, key))

        if cipher == "Шифр Цезаря":
            if self.sender() == self.pushButton_4:
                encrypted_text = self.encode_cesar(text, int(key))
            else:
                encrypted_text = self.decode_cesar(text, int(key))
        elif cipher == "Шифр Виженера":
            if self.sender() == self.pushButton_4:
                encrypted_text = self.visiner_encrypt(text, str(key))
            else:
                encrypted_text = self.visiner_decrypt(text, str(key))
        elif cipher == "Шифр Полибия":
            if self.sender() == self.pushButton_4:
                encrypted_text = self.encode_poliby(text, key)
            else:
                encrypted_text = self.decode_polibiya(text, key)
        elif cipher == "Шифр Аникина":
            if self.sender() == self.pushButton_4:
                encrypted_text = self.encode_anikin(text, key)
            else:
                encrypted_text = self.decode_anikin(text, key)
        elif cipher == "Шифр Васильева":
            if self.sender() == self.pushButton_4:
                encrypted_text = self.encrypt_vasilyev(str(text), int(key))
            else:
                encrypted_text = self.decrypt_vasilyev(str(text), int(key))
        elif cipher == "Шифр Левинского":
            if self.sender() == self.pushButton_4:
                encrypted_text = self.encode_vlad(text, int(key))
            else:
                encrypted_text = self.decode_vlad(text, int(key))

        self.label_3.setText(str(encrypted_text))
        self.next_action = []

    def encode_cesar(self, msg, sdv):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        msg = msg.lower()
        itog = ""
        for i in msg:
            if i not in alphabet:
                itog += i
            else:
                itog += alphabet[(alphabet.find(i) + sdv) % len(alphabet)]
        return itog

    def decode_cesar(self, line, shif):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shift = int(shif)
        line2 = ''
        if shift > 26:
            while shift > 26:
                shift -= 26
        elif shift < -26:
            while shift < -26:
                shift += 26
        elif shift == 0:
            return line
        alphabet2 = alphabet[shift:len(alphabet)] + alphabet[:shift]
        for x in line:
            if x in alphabet2:
                for i in range(len(alphabet2)):
                    if x == alphabet2[i]:
                        line2 = line2 + alphabet[i]
            else:
                line2 = line2 + x
        return line2

    def visiner_encrypt(self, line, key):
        a = []
        b = key
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z']
        if len(line) == len(key):
            return key
        else:
            while len(key) < len(line):
                key += b
        text = ""
        for i in range(len(line)):
            text += alphabet[((alphabet.index(line[i]) + alphabet.index(key[i])) % 26)]
        return text

    def visiner_decrypt(self, line, key):
        a = []
        b = key
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z']
        if len(line) == len(key):
            return key
        else:
            while len(key) < len(line):
                key += b
        text = ""
        for i in range(len(line)):
            text += alphabet[((alphabet.index(line[i]) - alphabet.index(key[i])) % 26)]
        return text

    def encode_poliby(self, msg, key):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        matrix = [[alphabet[i * 6 + j] for j in range(6)] for i in range(6)]
        msg = msg.lower()
        itog = ""
        for i in msg:
            for j in range(len(matrix)):
                if i in matrix[j]:
                    itog += str(j) + str(matrix[j].index(i)) + " "
                    break
        itog = itog[:-1]
        return itog

    def decode_polibiya(self, line2, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        matrix = []
        line = []
        cnt = 0
        for x in alphabet:
            cnt += 1
            line.append(x)
            if cnt == 6:
                matrix.append(line)
                line = []
                cnt = 0
        matrix2 = []
        for i in range(len(matrix)):
            line4 = []
            cnt2 = 0
            for k in range(len(matrix[i])):
                cnt2 += 1
                line4.append(str(i) + str(k))
                if cnt2 == 6:
                    matrix2.append(line4)
                    cnt2 = 0
        numbers = line2.split(' ')
        line3 = ''
        for x in numbers:
            y = x
            flag = 0
            for i in range(len(matrix2)):
                for k in range(len(matrix2[i])):
                    if y == matrix2[i][k]:
                        line3 = line3 + matrix[i][k]
                        flag = 1
            if flag == 0:
                line3 = line3 + y
        return line3

    def encode_anikin(self, line, shift=random.randint(0, 26)):
        global key13
        global key12
        shift = int(shift)
        while shift >= 26:
            shift = shift - 26
        flag = 0
        line3 = ''
        line2 = ''
        key = key13[shift:] + key13[:shift]
        for i in range(len(line)):
            flag = 0
            for k in range(len(key12)):
                if line[i] == key12[k]:
                    line2 = line2 + key[k]
                    flag = 1
                    break
            if flag == 0:
                line3 = line3 + line[i]
        return line2

    def decode_anikin(self, line, shift):
        global key13
        global key12
        shift = int(shift)
        while shift >= 26:
            shift = shift - 26
        line2 = ''
        line3 = ''
        flag = 0
        key = key13[shift:] + key13[:shift]
        for i in range(len(line)):
            flag = 0
            for k in range(len(key)):
                if line[i] == key[k]:
                    line2 = line2 + key12[k]
                    flag = 1
                    break
            if flag == 0:
                line3 = line3 + line[i]
        return line2

    def encrypt_vasilyev(self, text, key):
        encrypted_text = ''
        for char in text:
            if char.isascii():
                ascii_value = ord(char)
                encrypted_char = ascii_value * key
                encrypted_text += str(encrypted_char) + ' '
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt_vasilyev(self, encrypted_text, key):
        letters = encrypted_text.split()
        decrypted_text = ''
        for letter in range(len(letters)):
            letters[letter] = chr(round(int(letters[letter]) / key))
        for k in letters:
            decrypted_text += k
        return decrypted_text

    def encode_vlad(self, s1, key):
        r = 0
        g = 0
        b = 0
        w1 = []
        q1 = self.alphabet()
        kol = 0
        for i in s1:
            while kol < q1[i]:
                if g <= (250 - key):
                    g += key
                elif r <= (250 - key):
                    r += key
                elif b <= (250 - key):
                    b += key
                kol += 1
            w1.append(str(r) + '/' + str(g) + '/' + str(b))
            r = 0
            g = 0
            b = 0
            kol = 0
        return "and".join(map(str, w1))

    def alphabet(self):
        q1 = {}
        kol = 0
        w1 = [' ', ',', '.', 'a', 'b', 'c', 'd',
              'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p',
              'q', 'r', 's', 't',
              'u', 'v', 'w', 'x',
              'y', 'z']
        for i in w1:
            q1[i] = kol
            kol += 1
        return q1

    def decode_vlad(self, s1, key):
        m1 = ''
        q1 = self.alphabet()
        for i in s1.split('and'):
            i = i.split('/')
            r = int(i[0])
            g = int(i[1])
            b = int(i[2])
            kol = (b / key) + (r / key) + (g / key)
            for z in q1:
                if q1[z] == kol:
                    m1 = m1 + z
                    break
        return m1

    def prev_action(self):
        self.next_action.append(self.prev_action.pop())
        cipher, text, key = self.prev_action[-1]
        self.comboBox.setCurrentText(cipher)
        self.textEdit.setText(text)
        self.textEdit_3.setText(key)
        self.encrypt_decrypt()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
