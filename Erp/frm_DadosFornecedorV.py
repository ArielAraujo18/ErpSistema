from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QMessageBox)
from validate_docbr import CPF

import icon_add
import icon_voltar

import Controle
import mysql.connector
import pandas as pd
import requests
import os

class Ui_frm_DadosFornecedor(object):
    def setupUi(self, frm_DadosFornecedor):
        if not frm_DadosFornecedor.objectName():
            frm_DadosFornecedor.setObjectName(u"frm_DadosFornecedor")
        frm_DadosFornecedor.setFixedSize(513, 539)
        self.frm_DadosFornecedor = frm_DadosFornecedor
        frm_DadosFornecedor.setStyleSheet(u"QWidget {\n"
"    background-color: #2c2c2c;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosFornecedor)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(10, 40, 101, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosFornecedor)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(120, 30, 201, 41))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_celular = QLabel(frm_DadosFornecedor)
        self.lbl_celular.setObjectName(u"lbl_celular")
        self.lbl_celular.setGeometry(QRect(10, 120, 61, 16))
        self.lbl_celular.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.lbl_cpf = QLabel(frm_DadosFornecedor)
        self.lbl_cpf.setObjectName(u"lbl_cpf")
        self.lbl_cpf.setGeometry(QRect(340, 40, 41, 20))
        self.lbl_cpf.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_celular = QLineEdit(frm_DadosFornecedor)
        self.txt_celular.setObjectName(u"txt_celular")
        self.txt_celular.setGeometry(QRect(80, 110, 131, 41))
        self.txt_celular.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_cpf = QLineEdit(frm_DadosFornecedor)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(390, 30, 121, 41))
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
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
        self.lbl_Rua.setGeometry(QRect(250, 200, 31, 16))
        self.lbl_Rua.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_Rua = QLineEdit(frm_DadosFornecedor)
        self.txt_Rua.setObjectName(u"txt_Rua")
        self.txt_Rua.setGeometry(QRect(290, 190, 181, 41))
        self.txt_Rua.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
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
        self.lbl_cidade.setGeometry(QRect(10, 200, 61, 20))
        self.lbl_cidade.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_cidade = QLineEdit(frm_DadosFornecedor)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(70, 190, 161, 41))
        self.txt_cidade.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
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
        self.lbl_bairro.setGeometry(QRect(10, 280, 51, 21))
        self.lbl_bairro.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_bairro = QLineEdit(frm_DadosFornecedor)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(70, 270, 151, 41))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
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
        self.lbl_cep.setGeometry(QRect(230, 120, 41, 21))
        self.lbl_cep.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_cep = QLineEdit(frm_DadosFornecedor)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(270, 110, 91, 41))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Numero = QLineEdit(frm_DadosFornecedor)
        self.txt_Numero.setObjectName(u"txt_Numero")
        self.txt_Numero.setGeometry(QRect(450, 110, 61, 41))
        self.txt_Numero.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Numero = QLabel(frm_DadosFornecedor)
        self.lbl_Numero.setObjectName(u"lbl_Numero")
        self.lbl_Numero.setGeometry(QRect(380, 120, 61, 21))
        self.lbl_Numero.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_email = QLineEdit(frm_DadosFornecedor)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(70, 350, 371, 41))
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
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
        self.lbl_email.setGeometry(QRect(10, 360, 51, 21))
        self.lbl_email.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosFornecedor)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(280, 430, 101, 91))
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
        self.btn_cancelar = QPushButton(frm_DadosFornecedor)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(150, 430, 101, 91))
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
        self.lbl_cpfT = QLabel(frm_DadosFornecedor)
        self.lbl_cpfT.setObjectName(u"lbl_cpfT")
        self.lbl_cpfT.setGeometry(QRect(310, 80, 201, 20))
        self.lbl_cpfT.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.lbl_cpf_2 = QLabel(frm_DadosFornecedor)
        self.lbl_cpf_2.setObjectName(u"lbl_cpf_2")
        self.lbl_cpf_2.setGeometry(QRect(240, 280, 31, 20))
        self.lbl_cpf_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.comboSituacao = QComboBox(frm_DadosFornecedor)
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.setObjectName(u"comboSituacao")
        self.comboSituacao.setGeometry(QRect(270, 270, 201, 41))
        self.comboSituacao.setStyleSheet(u"QComboBox {\n"
"    background-color: #2c3e50;\n"
"    color: #ecf0f1;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #34495e;\n"
"    background-color: #34495e;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border-left: 6px solid transparent;\n"
"    border-right: 6px solid transparent;\n"
"    border-top: 8px solid #ecf0f1;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #34495e;\n"
"    color: #ecf0f1;\n"
"    selection-background-color: #1abc9c;\n"
"    selection-color: #ffffff;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    outline: none;\n"
"    min-width: 100px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #1abc9c;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #16a085;\n"
"}\n"
"\n"
"/* Barra de rolagem vertical personalizada */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2c3e50;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #1abc9c;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"/* Barra de rolagem horizontal personalizada */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"   "
                        " background: #2c3e50;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #1abc9c;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"")
        self.lbl_EmailT = QLabel(frm_DadosFornecedor)
        self.lbl_EmailT.setObjectName(u"lbl_EmailT")
        self.lbl_EmailT.setGeometry(QRect(230, 160, 221, 20))
        self.lbl_EmailT.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")

        self.retranslateUi(frm_DadosFornecedor)

        QMetaObject.connectSlotsByName(frm_DadosFornecedor)
    # setupUi
    def adicionarFornecedor(self):
        razaoSocial = self.txt_razao.text()
        cnpj = self.txt_cnpj.text()
        contato = self.txt_contato.text()
        cep = self.txt_cep.text()
        numero = self.txt_Numero.text()
        cidade = self.txt_cidade.text()
        rua = self.txt_Rua.text()
        bairro = self.txt_bairro.text()
        uf = self.comboSituacao.currentText()
        email = self.txt_email.text()

        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO fornecedor (`Razão Social`, `Cnpj`, `Contato`, `Cep`, `Número`, `Cidade`, `Rua`, `Bairro`, `UF`, `E-mail`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (razaoSocial, cnpj, contato, cep, numero, cidade, rua, bairro, uf, email)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'registro(s) inserido(s)')
        mycursor.close()

        self.txt_razao.setText("")
        self.txt_contato.setText("")
        self.txt_cnpj.setText("")
        self.txt_cidade.setText("")
        self.txt_Rua.setText("")
        self.txt_bairro.setText("")
        self.txt_cep.setText("")
        self.txt_email.setText("")

        msg = QMessageBox()
        msg.setWindowTitle('Sucesso!')
        msg.setText('Fornecedor adicionado com sucesso!')
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        msg.setWindowIcon(QIcon(caminho_icone))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosFornecedor.close()

    def sairTela(self, frm_DadosFornecedor):
        frm_DadosFornecedor.close()

    def alterarFornecedor(self):
        razaoSocial = self.txt_razao.text()
        cnpj = self.txt_cnpj.text()
        contato = self.txt_contato.text()
        cep = self.txt_cep.text()
        numero = self.txt_Numero.text()
        cidade = self.txt_cidade.text()
        rua = self.txt_Rua.text()
        bairro = self.txt_bairro.text()
        uf = self.comboSituacao.currentText()
        email = self.txt_email.text()

        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
        mycursor = mydb.cursor()

        sql = """
        UPDATE fornecedor
        SET `Razão Social` = %s, Cnpj = %s, Contato = %s, Cep = %s, Número = %s, Cidade = %s, Rua = %s, Bairro = %s, UF = %s, E-mail = %s,
        WHERE IdFornecedor = %s
        """
        val = (razaoSocial, cnpj, contato, cep, numero, cidade, rua, bairro, uf, email, Controle.idConsulta)

        mycursor.execute(sql, val)
        mydb.commit()

        msg = QMessageBox()
        msg.setWindowTitle('Sucesso!')
        msg.setText('Fornecedor alterado com sucesso!')
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        msg.setWindowIcon(QIcon(caminho_icone))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosFornecedor.close()

    def retranslateUi(self, frm_DadosFornecedor):
        frm_DadosFornecedor.setWindowTitle(QCoreApplication.translate("frm_DadosFornecedor", u"Form", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Raz\u00e3o Social:", None))
        self.lbl_celular.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Contato:", None))
        self.lbl_cpf.setText(QCoreApplication.translate("frm_DadosFornecedor", u"CNPJ:", None))
        self.txt_celular.setInputMask(QCoreApplication.translate("frm_DadosFornecedor", u"(00) 0 0000-0000", None))
        self.txt_cpf.setInputMask(QCoreApplication.translate("frm_DadosFornecedor", u"000.000.000-00", None))
        self.lbl_Rua.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Rua:", None))
        self.lbl_cidade.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Cidade:", None))
        self.lbl_bairro.setText(QCoreApplication.translate("frm_DadosFornecedor", u"Bairro:", None))
        self.lbl_cep.setText(QCoreApplication.translate("frm_DadosFornecedor", u"CEP:", None))
        self.txt_cep.setInputMask(QCoreApplication.translate("frm_DadosFornecedor", u"00000-000", None))
        self.lbl_Numero.setText(QCoreApplication.translate("frm_DadosFornecedor", u"N\u00famero:", None))
        self.txt_email.setText("")
        self.lbl_email.setText(QCoreApplication.translate("frm_DadosFornecedor", u"E-mail:", None))
        self.btn_cadastrar.setText("")
        self.btn_cancelar.setText("")
        self.lbl_cpfT.setText(QCoreApplication.translate("frm_DadosFornecedor", u"INFORME O CNPJ DO FORNECEDOR", None))
        self.lbl_cpf_2.setText(QCoreApplication.translate("frm_DadosFornecedor", u"UF:", None))
        self.comboSituacao.setItemText(0, QCoreApplication.translate("frm_DadosFornecedor", u"Prefiro n\u00e3o informar", None))
        self.comboSituacao.setItemText(1, QCoreApplication.translate("frm_DadosFornecedor", u"Acre (AC)", None))
        self.comboSituacao.setItemText(2, QCoreApplication.translate("frm_DadosFornecedor", u"Alagoas (AL)", None))
        self.comboSituacao.setItemText(3, QCoreApplication.translate("frm_DadosFornecedor", u"Amap\u00e1 (AP)", None))
        self.comboSituacao.setItemText(4, QCoreApplication.translate("frm_DadosFornecedor", u"Amazonas (AM)", None))
        self.comboSituacao.setItemText(5, QCoreApplication.translate("frm_DadosFornecedor", u"Bahia (BA)", None))
        self.comboSituacao.setItemText(6, QCoreApplication.translate("frm_DadosFornecedor", u"Cear\u00e1 (CE)", None))
        self.comboSituacao.setItemText(7, QCoreApplication.translate("frm_DadosFornecedor", u"Esp\u00edrito Santo (ES)", None))
        self.comboSituacao.setItemText(8, QCoreApplication.translate("frm_DadosFornecedor", u"Goi\u00e1s (GO)", None))
        self.comboSituacao.setItemText(9, QCoreApplication.translate("frm_DadosFornecedor", u"Maranh\u00e3o (MA)", None))
        self.comboSituacao.setItemText(10, QCoreApplication.translate("frm_DadosFornecedor", u"Mato Grosso (MT)", None))
        self.comboSituacao.setItemText(11, QCoreApplication.translate("frm_DadosFornecedor", u"Mato Grosso do Sul (MS)", None))
        self.comboSituacao.setItemText(12, QCoreApplication.translate("frm_DadosFornecedor", u"Minas Gerais (MG)", None))
        self.comboSituacao.setItemText(13, QCoreApplication.translate("frm_DadosFornecedor", u"Par\u00e1 (PA)", None))
        self.comboSituacao.setItemText(14, QCoreApplication.translate("frm_DadosFornecedor", u"Para\u00edba (PB)", None))
        self.comboSituacao.setItemText(15, QCoreApplication.translate("frm_DadosFornecedor", u"Paran\u00e1 (PR)", None))
        self.comboSituacao.setItemText(16, QCoreApplication.translate("frm_DadosFornecedor", u"Pernambuco (PE)", None))
        self.comboSituacao.setItemText(17, QCoreApplication.translate("frm_DadosFornecedor", u"Piau\u00ed (PI)", None))
        self.comboSituacao.setItemText(18, QCoreApplication.translate("frm_DadosFornecedor", u"Rio de Janeiro (RJ)", None))
        self.comboSituacao.setItemText(19, QCoreApplication.translate("frm_DadosFornecedor", u"Rio Grande do Norte (RN)", None))
        self.comboSituacao.setItemText(20, QCoreApplication.translate("frm_DadosFornecedor", u"Rio Grande do Sul (RS)", None))
        self.comboSituacao.setItemText(21, QCoreApplication.translate("frm_DadosFornecedor", u"Rond\u00f4nia (RO)", None))
        self.comboSituacao.setItemText(22, QCoreApplication.translate("frm_DadosFornecedor", u"Roraima (RR)", None))
        self.comboSituacao.setItemText(23, QCoreApplication.translate("frm_DadosFornecedor", u"Santa Catarina (SC)", None))
        self.comboSituacao.setItemText(24, QCoreApplication.translate("frm_DadosFornecedor", u"S\u00e3o Paulo (SP)", None))
        self.comboSituacao.setItemText(25, QCoreApplication.translate("frm_DadosFornecedor", u"Sergipe (SE)", None))
        self.comboSituacao.setItemText(26, QCoreApplication.translate("frm_DadosFornecedor", u"Tocantins (TO)", None))

        self.lbl_EmailT.setText(QCoreApplication.translate("frm_DadosFornecedor", u"INFORME O CEP DO SEU FORNECEDOR", None))
    # retranslateUi

        if Controle.tiposTelaDadosCliente == 'incluir':
            print('incluindo')
            self.btn_cadastrar.clicked.connect(self.adicionarFornecedor)
        if Controle.tiposTelaDadosCliente == 'alterar':
            print('Alterando')
            self.btn_cadastrar.clicked.connect(self.alterarFornecedor)

        self.btn_cancelar.clicked.connect(lambda: self.sairTela(frm_DadosFornecedor))

        ##Condições da tela    
        if Controle.tiposTelaDadosCliente == 'incluir':
                print('Frm_DadosFornecedor: ', Controle.tiposTelaDadosCliente)
                self.txt_razao.setEnabled(True)
                self.txt_cnpj.setEnabled(True)
                self.txt_contato.setEnabled(True) 
                self.txt_cep.setEnabled(True)     
                self.txt_Numero.setEnabled(True)      
                self.txt_cidade.setEnabled(True)
                self.txt_Rua.setEnabled(True)
                self.txt_bairro.setEnabled(True)
                self.comboSituacao.setEnabled(True)
                self.txt_email.setEnabled(True)

        elif Controle.tiposTelaDadosCliente == 'consultar':            
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_razao.setEnabled(False)
                self.txt_cnpj.setEnabled(False)
                self.txt_contato.setEnabled(False) 
                self.txt_cep.setEnabled(False)     
                self.txt_Numero.setEnabled(False)      
                self.txt_cidade.setEnabled(False)
                self.txt_Rua.setEnabled(False)
                self.txt_bairro.setEnabled(False)
                self.comboSituacao.setEnabled(False)
                self.txt_email.setEnabled(False)
                self.btn_cadastrar.setEnabled(False)
                self.btn_cancelar.setEnabled(True)
        
                print('Conectando...')
                mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM Fornecedor WHERE idFornecedor = '" + Controle.idConsulta + "'"
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                print (myresult)
                mycursor.close()

                df = pd.DataFrame(myresult, columns=["idFornecedor", "Razão Social", "Cnpj", "Contato", "Cep", "Número", "Cidade", "Rua", "Bairro", "UF", "E-mail"])
                razaoSocial = df['Razão Social'][0]
                cnpjF = df['Cnpj'][0]
                contatoF = df['Contato'][0]
                CepF = df['Cep'][0]
                numero = df['Número'][0]
                cidadeF = df['Cidade'][0]
                ruaF = df['Rua'][0]
                bairroF = df['Bairro'][0]
                uf = df['UF'][0]
                emailF = df['E-mail'][0]

                self.txt_razao.setText(razaoSocial)
                self.txt_cnpj.setText(cnpjF)
                self.txt_contato.setText(contatoF)
                self.txt_cep.setText(CepF)     
                self.txt_Numero.setText(numero)      
                self.txt_cidade.setText(cidadeF)
                self.txt_Rua.setText(ruaF)
                self.txt_bairro.setText(bairroF)
                self.comboSituacao.setText(uf)
                self.txt_email.setText(emailF)

        elif Controle.tiposTelaDadosCliente == 'alterar':
                print('DadosFornecedor: ', Controle.tiposTelaDadosCliente)
                self.txt_razao.setEnabled(True)
                self.txt_cnpj.setEnabled(True)
                self.txt_contato.setEnabled(True) 
                self.txt_cep.setEnabled(True)     
                self.txt_Numero.setEnabled(True)      
                self.txt_cidade.setEnabled(True)
                self.txt_Rua.setEnabled(True)
                self.txt_bairro.setEnabled(True)
                self.comboSituacao.setEnabled(True)
                self.txt_email.setEnabled(True)
                self.btn_cadastrar.setEnabled(True)
                self.btn_cancelar.setEnabled(True)

                print('Conectando...')
                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM fornecedor WHERE idFornecedor = '" + Controle.idConsulta + "'"
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                mycursor.close()

                df = pd.DataFrame(myresult, columns=["idFornecedor", "Razão Social", "Contato", "Cnpj", "Cidade", "Rua", "Bairro", "Cep", "E-mail"])
                razaoSocial = df['Razão Social'][0]
                cnpjF = df['Cnpj'][0]
                contatoF = df['Contato'][0]
                CepF = df['Cep'][0]
                numero = df['Número'][0]
                cidadeF = df['Cidade'][0]
                ruaF = df['Rua'][0]
                bairroF = df['Bairro'][0]
                uf = df['UF'][0]
                emailF = df['E-mail'][0]
                
                self.txt_razao.setText(razaoSocial)
                self.txt_cnpj.setText(cnpjF)
                self.txt_contato.setText(contatoF)
                self.txt_cep.setText(CepF)     
                self.txt_Numero.setText(numero)      
                self.txt_cidade.setText(cidadeF)
                self.txt_Rua.setText(ruaF)
                self.txt_bairro.setText(bairroF)
                self.comboSituacao.setText(uf)
                self.txt_email.setText(emailF)

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosFornecedor= QWidget()
    ui = Ui_frm_DadosFornecedor()
    ui.setupUi(frm_DadosFornecedor)
    frm_DadosFornecedor.show()
    app.exec()