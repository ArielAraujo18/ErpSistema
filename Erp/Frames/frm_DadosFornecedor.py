# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_DadosFornecedor.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import icon_voltar_rc
import icon_add_rc

class Ui_frm_DadosFornecedor(object):
    def setupUi(self, frm_DadosFornecedor):
        if not frm_DadosFornecedor.objectName():
            frm_DadosFornecedor.setObjectName(u"frm_DadosFornecedor")
        frm_DadosFornecedor.resize(526, 566)
        frm_DadosFornecedor.setStyleSheet(u"QWidget {\n"
"    background-color: #2c2c2c;\n"
"}")
        self.lbl_razao = QLabel(frm_DadosFornecedor)
        self.lbl_razao.setObjectName(u"lbl_razao")
        self.lbl_razao.setGeometry(QRect(20, 50, 111, 21))
        self.lbl_razao.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_razao = QLineEdit(frm_DadosFornecedor)
        self.txt_razao.setObjectName(u"txt_razao")
        self.txt_razao.setGeometry(QRect(140, 40, 351, 41))
        self.txt_razao.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.lbl_contato = QLabel(frm_DadosFornecedor)
        self.lbl_contato.setObjectName(u"lbl_contato")
        self.lbl_contato.setGeometry(QRect(30, 100, 71, 20))
        self.lbl_contato.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_Cnpj = QLabel(frm_DadosFornecedor)
        self.lbl_Cnpj.setObjectName(u"lbl_Cnpj")
        self.lbl_Cnpj.setGeometry(QRect(60, 150, 51, 20))
        self.lbl_Cnpj.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosFornecedor)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(160, 460, 101, 91))
        self.btn_cancelar.setAutoFillBackground(False)
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_voltar/voltar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    padding-left: 40px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffcdd2;\n"
"    border-color: #e57373;\n"
"    color: #d32f2f; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e57373;\n"
"    border-color: #b71c1c;\n"
"    padding-left: 44px;\n"
"    padding-top: 2px;\n"
"}")
        self.txt_contato = QLineEdit(frm_DadosFornecedor)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setGeometry(QRect(110, 90, 381, 41))
        self.txt_contato.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.txt_cnpj = QLineEdit(frm_DadosFornecedor)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setGeometry(QRect(110, 140, 381, 41))
        self.txt_cnpj.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.lbl_Rua = QLabel(frm_DadosFornecedor)
        self.lbl_Rua.setObjectName(u"lbl_Rua")
        self.lbl_Rua.setGeometry(QRect(60, 250, 41, 20))
        self.lbl_Rua.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Rua = QLineEdit(frm_DadosFornecedor)
        self.txt_Rua.setObjectName(u"txt_Rua")
        self.txt_Rua.setGeometry(QRect(110, 240, 381, 41))
        self.txt_Rua.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.lbl_cidade = QLabel(frm_DadosFornecedor)
        self.lbl_cidade.setObjectName(u"lbl_cidade")
        self.lbl_cidade.setGeometry(QRect(40, 200, 61, 20))
        self.lbl_cidade.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosFornecedor)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(280, 460, 101, 91))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_add/add.png); \n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0;\n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf; \n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px; \n"
"    padding-top: 4px;\n"
"}")
        self.txt_cidade = QLineEdit(frm_DadosFornecedor)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(110, 190, 381, 41))
        self.txt_cidade.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.lbl_bairro = QLabel(frm_DadosFornecedor)
        self.lbl_bairro.setObjectName(u"lbl_bairro")
        self.lbl_bairro.setGeometry(QRect(40, 300, 61, 21))
        self.lbl_bairro.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_bairro = QLineEdit(frm_DadosFornecedor)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(110, 290, 381, 41))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.lbl_email = QLabel(frm_DadosFornecedor)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(40, 400, 61, 21))
        self.lbl_email.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_email = QLineEdit(frm_DadosFornecedor)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(110, 390, 381, 41))
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.txt_cep = QLineEdit(frm_DadosFornecedor)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(110, 340, 381, 41))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
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
        self.lbl_cep = QLabel(frm_DadosFornecedor)
        self.lbl_cep.setObjectName(u"lbl_cep")
        self.lbl_cep.setGeometry(QRect(60, 350, 41, 21))
        self.lbl_cep.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.retranslateUi(frm_DadosFornecedor)

        QMetaObject.connectSlotsByName(frm_DadosFornecedor)
    # setupUi

    def retranslateUi(self, frm_DadosFornecedor):
        frm_DadosFornecedor.setWindowTitle(QCoreApplication.translate("frm_DadosFornecedor", u"Form", None))
        self.lbl_razao.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Raz\u00e3o Social:", None))
        self.lbl_contato.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Contato:", None))
        self.lbl_Cnpj.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Cnpj:", None))
        self.btn_cancelar.setText("")
        self.txt_contato.setInputMask(QCoreApplication.translate("frm_DadosFornecedor", u"(00) 0 0000-0000", None))
        self.txt_cnpj.setInputMask(QCoreApplication.translate("frm_DadosFornecedor", u"00.000.000/0000-00", None))
        self.lbl_Rua.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Rua:", None))
        self.lbl_cidade.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Cidade:", None))
        self.btn_cadastrar.setText("")
        self.lbl_bairro.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Bairro:", None))
        self.lbl_email.setText(QCoreApplication.translate("frm_DadosFornecedor", u"E-mail:", None))
        self.txt_email.setInputMask("")
        self.txt_cep.setInputMask(QCoreApplication.translate("frm_DadosFornecedor", u"00000-000", None))
        self.lbl_cep.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Cep:", None))
    # retranslateUi

