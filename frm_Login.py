from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget, QMessageBox)

from frm_Main import Ui_frm_Main

import icon_TelaLogin

import os
import mysql.connector
import pandas as pd
import Controle

class Ui_frm_Login(object):
    def setupUi(self, frm_Login):
        if not frm_Login.objectName():
            frm_Login.setObjectName(u"frm_Login")
        frm_Login.setFixedSize(674, 635)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Login.setWindowIcon(QIcon(caminho_icone))
        self.frm_Login = frm_Login
        frm_Login.setStyleSheet(u"QWidget {\n"
"    background-color: #2F4F4F;\n"
"}")
        self.centralwidget = QWidget(frm_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_usuario = QLabel(self.centralwidget)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(30, 150, 111, 31))
        font = QFont()
        font.setBold(True)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Usuario = QLineEdit(self.centralwidget)
        self.txt_Usuario.setObjectName(u"txt_Usuario")
        self.txt_Usuario.setGeometry(QRect(150, 140, 511, 51))
        font1 = QFont()
        self.txt_Usuario.setFont(font1)
        self.txt_Usuario.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_senha = QLabel(self.centralwidget)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(30, 230, 111, 31))
        self.lbl_senha.setFont(font)
        self.lbl_senha.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Senha = QLineEdit(self.centralwidget)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(150, 220, 511, 51))
        self.txt_Senha.setFont(font1)
        self.txt_Senha.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Senha.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 430, 81, 121))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background: url(:/icon_login/avsIconLogo.png);\n"
"	background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 560, 251, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 600, 201, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 10, 401, 81))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    font-size: 60px;\n"
"    font-weight: bold;\n"
"    color: #FFA500;\n"
"    padding: 10px;\n"
"    border-radius: 8px;\n"
"}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 310, 481, 91))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #007BFF; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 310, 141, 91))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #6c757d; \n"
"    color: white; \n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a6268; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #495057; \n"
"}")
        frm_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_Login)

        QMetaObject.connectSlotsByName(frm_Login)
    # setupUi

    def voltar(self):
        self.frm_Login.close()


    def login(self):
         
        campos = {
             'Usuario': self.txt_Usuario.text(),
             'Senha': self.txt_Senha.text(),
        }

        for campo, valor in campos.items():
             if not valor:
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"O campo {campo} deve está preenchido!")
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
             
        self.txt_Usuario.text()
        self.txt_Senha.text()

        usuario = self.txt_Usuario.text()
        senha = self.txt_Senha.text()
        situacaoo = ''

        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database,
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT `Email`, `SENHA`, `Permissão` FROM login")

        myresult = mycursor.fetchall()
        print(myresult)

        if myresult:
            
            credenciais_corretas = False
            
            for usere, pasworde, situacao in myresult:
                if usuario == usere and senha == pasworde and situacao != situacaoo:
                     credenciais_corretas = True
                     Controle.login = situacao
                     print(Controle.login)
                     break
            
            if not credenciais_corretas:
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText("Credenciais incorretas")
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
            
            else:
                msg = QMessageBox()
                msg.setWindowTitle("SUCESSO!")
                msg.setText("Credenciais corretas, seja bem-vindo!")
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.NoIcon)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.abrirTela()
                self.voltar()

        else:
                
                print("Email não encontrado!")

    def abrirTela(self):                
        if not hasattr(self, 'frm_Main') or self.frm_Main is None or not self.frm_Main.isVisible():

                self.frm_Main = QMainWindow()
                self.ui = Ui_frm_Main()
                self.ui.setupUi(self.frm_Main)

                self.frm_Main.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Main.destroyed.connect(lambda: setattr(self, 'frm_Main', None))

                self.frm_Main.show()

        else:
                self.frm_Main.raise_()
                self.frm_Main.activateWindow()

    def retranslateUi(self, frm_Login):
        frm_Login.setWindowTitle(QCoreApplication.translate("frm_Login", u"Login", None))
        self.lbl_usuario.setText(QCoreApplication.translate("frm_Login", u"E-mail:", None))
        self.lbl_senha.setText(QCoreApplication.translate("frm_Login", u"Senha:", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("frm_Login", u"AVS-SOFTWARES", None))
        self.label_4.setText(QCoreApplication.translate("frm_Login", u"SOFTWARE E TECNOLOGIA", None))
        self.label_2.setText(QCoreApplication.translate("frm_Login", u"BEM-VINDO!", None))
        self.pushButton.setText(QCoreApplication.translate("frm_Login", u"ENTRAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("frm_Login", u"VOLTAR", None))
        
    # retranslateUi     
        self.pushButton_2.clicked.connect(self.voltar)
        self.pushButton.clicked.connect(self.login)


if __name__ == "__main__":
        app = QApplication([])
        frm_Login = QMainWindow()
        ui = Ui_frm_Login()
        ui.setupUi(frm_Login)
        frm_Login.show()
        app.exec()
