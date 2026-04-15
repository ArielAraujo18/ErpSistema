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

class Ui_frm_DadosCliente(object):
    def setupUi(self, frm_DadosCliente):
        if not frm_DadosCliente.objectName():
            frm_DadosCliente.setObjectName(u"frm_DadosCliente")
        frm_DadosCliente.setFixedSize(498, 603)
        self.frm_DadosCliente = frm_DadosCliente
        frm_DadosCliente.setStyleSheet(u"QWidget {\n"
"    background-color: #2c2c2c;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosCliente)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(10, 40, 51, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosCliente)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(60, 30, 201, 41))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_celular = QLabel(frm_DadosCliente)
        self.lbl_celular.setObjectName(u"lbl_celular")
        self.lbl_celular.setGeometry(QRect(280, 40, 61, 16))
        self.lbl_celular.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.lbl_cpf = QLabel(frm_DadosCliente)
        self.lbl_cpf.setObjectName(u"lbl_cpf")
        self.lbl_cpf.setGeometry(QRect(10, 120, 41, 20))
        self.lbl_cpf.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_celular = QLineEdit(frm_DadosCliente)
        self.txt_celular.setObjectName(u"txt_celular")
        self.txt_celular.setGeometry(QRect(340, 30, 131, 41))
        self.txt_celular.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_cpf = QLineEdit(frm_DadosCliente)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.textChanged.connect(self.validarCpf)
        self.txt_cpf.setGeometry(QRect(50, 110, 121, 41))
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Rua = QLabel(frm_DadosCliente)
        self.lbl_Rua.setObjectName(u"lbl_Rua")
        self.lbl_Rua.setGeometry(QRect(250, 200, 31, 16))
        self.lbl_Rua.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_Rua = QLineEdit(frm_DadosCliente)
        self.txt_Rua.setObjectName(u"txt_Rua")
        self.txt_Rua.setGeometry(QRect(290, 190, 181, 41))
        self.txt_Rua.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_cidade = QLabel(frm_DadosCliente)
        self.lbl_cidade.setObjectName(u"lbl_cidade")
        self.lbl_cidade.setGeometry(QRect(10, 200, 61, 20))
        self.lbl_cidade.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_cidade = QLineEdit(frm_DadosCliente)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(70, 190, 161, 41))
        self.txt_cidade.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_bairro = QLabel(frm_DadosCliente)
        self.lbl_bairro.setObjectName(u"lbl_bairro")
        self.lbl_bairro.setGeometry(QRect(10, 280, 51, 21))
        self.lbl_bairro.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_bairro = QLineEdit(frm_DadosCliente)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(70, 270, 151, 41))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_cep = QLabel(frm_DadosCliente)
        self.lbl_cep.setObjectName(u"lbl_cep")
        self.lbl_cep.setGeometry(QRect(190, 120, 41, 21))
        self.lbl_cep.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_cep = QLineEdit(frm_DadosCliente)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.textChanged.connect(self.buscaCep)
        self.txt_cep.setGeometry(QRect(230, 110, 91, 41))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Numero = QLineEdit(frm_DadosCliente)
        self.txt_Numero.setObjectName(u"txt_Numero")
        self.txt_Numero.setGeometry(QRect(310, 270, 61, 41))
        self.txt_Numero.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Numero = QLabel(frm_DadosCliente)
        self.lbl_Numero.setObjectName(u"lbl_Numero")
        self.lbl_Numero.setGeometry(QRect(240, 280, 61, 21))
        self.lbl_Numero.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_email = QLineEdit(frm_DadosCliente)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(70, 430, 371, 41))
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_email = QLabel(frm_DadosCliente)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(10, 440, 51, 21))
        self.lbl_email.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.txt_pontuacao = QLineEdit(frm_DadosCliente)
        self.txt_pontuacao.setObjectName(u"txt_pontuacao")
        self.txt_pontuacao.setEnabled(True)
        self.txt_pontuacao.setGeometry(QRect(430, 110, 51, 41))
        self.txt_pontuacao.setEnabled(False)
        self.txt_pontuacao.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #FFFFFF ;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_email_2 = QLabel(frm_DadosCliente)
        self.lbl_email_2.setObjectName(u"lbl_email_2")
        self.lbl_email_2.setGeometry(QRect(340, 120, 81, 21))
        self.lbl_email_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosCliente)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(270, 500, 101, 91))
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
        self.btn_cancelar = QPushButton(frm_DadosCliente)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(140, 500, 101, 91))
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
        self.lbl_cpfT = QLabel(frm_DadosCliente)
        self.lbl_cpfT.setObjectName(u"lbl_cpfT")
        self.lbl_cpfT.setGeometry(QRect(10, 160, 161, 20))
        self.lbl_cpfT.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.lbl_cpf_2 = QLabel(frm_DadosCliente)
        self.lbl_cpf_2.setObjectName(u"lbl_cpf_2")
        self.lbl_cpf_2.setGeometry(QRect(10, 360, 31, 20))
        self.lbl_cpf_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.comboSituacao = QComboBox(frm_DadosCliente)
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
        self.comboSituacao.setGeometry(QRect(40, 350, 201, 41))
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
        self.lbl_EmailT = QLabel(frm_DadosCliente)
        self.lbl_EmailT.setObjectName(u"lbl_EmailT")
        self.lbl_EmailT.setGeometry(QRect(180, 160, 201, 20))
        self.lbl_EmailT.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")

        self.retranslateUi(frm_DadosCliente)

        QMetaObject.connectSlotsByName(frm_DadosCliente)
    # setupUi

    def buscaCep(self):
        cep = self.txt_cep.text().replace(".", "").replace("-", "")
        if len(cep) == 8:
                url = f"https://viacep.com.br/ws/{cep}/json/"
                resposta = requests.get(url, timeout=5)
                dados = resposta.json()
                uf = dados.get("uf", "")

                if "erro" in dados:
                        self.lbl_EmailT.setText('❌ CEP INVÁLIDO')
                        return 

                self.txt_Rua.setText(dados.get("logradouro", ""))
                self.txt_bairro.setText(dados.get("bairro", ""))
                self.txt_cidade.setText(dados.get("localidade", ""))
                self.comboSituacao.setCurrentText(dados.get("uf", ""))
                for i in range(self.comboSituacao.count()):
                      texto = self.comboSituacao.itemText(i)
                      if f'({uf})' in texto:
                                self.comboSituacao.setCurrentIndex(i)
                                break

    def validarCpf(self):
        cpf = CPF()
        clienteCpf = self.txt_cpf.text()

        cpf_numero = clienteCpf.replace(".", "").replace("-","")

        if cpf.validate(cpf_numero):
                self.lbl_cpfT.setText("✅ CPF VÁLIDO")
                return
        else:
                self.lbl_cpfT.setText("❌ CPF INVÁLIDO")
                return

    def adicionarCliente(self):
        Controle.pontos = 0
        #Pegando os dados digitados
        nomeCliente = self.txt_nome.text()
        celularCliente = self.txt_celular.text()
        cpfCliente = self.txt_cpf.text()
        uf = self.comboSituacao.currentText()
        cidadeCliente = self.txt_cidade.text()
        ruaCliente = self.txt_Rua.text()
        bairroCliente = self.txt_bairro.text()
        numeroCliente = self.txt_Numero.text()
        cepCliente = self.txt_cep.text()
        emailCliente = self.txt_email.text()

        #VERIFICAÇÕES
        if numeroCliente == '':
                numeroCliente = 0

        #if cpfCliente != '':
                self.validarCpf(cpfCliente)



        #CONECTANDO BANCO DE DADOS
        mydb = mysql.connector.connect( 
                host= Controle.host,
                user= Controle.user,
                password= Controle.password,
                database= Controle.database
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO cliente(`Nome`, `Celular`, `Cpf`, `UF`, `Cidade`, `Rua`, `Bairro`, `Número`, `Cep`, `E-mail`, `Pontos`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nomeCliente, celularCliente, cpfCliente, uf, cidadeCliente, ruaCliente, bairroCliente, numeroCliente, cepCliente, emailCliente, Controle.pontos)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, 'Record(s) inserted')
        mycursor.close()

        #limpando os campos
        self.txt_nome.setText("")
        self.txt_celular.setText("")
        self.txt_cidade.setText("")
        self.txt_cpf.setText("")
        self.comboSituacao.setCurrentIndex(0)
        self.txt_Rua.setText("")
        self.txt_bairro.setText("")
        self.txt_Numero.setText("")
        self.txt_cep.setText("")
        self.txt_email.setText("")
        
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Adicionado com Sucesso!")
        msg.setWindowIcon(QIcon((r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png")))
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosCliente.close()
                        
    def sairTela(self, frm_DadosCliente):
        frm_DadosCliente.close()


    def alterarCliente(self): 

        nomeCliente = self.txt_nome.text()
        celularCliente = self.txt_celular.text()
        cpfCliente = self.txt_cpf.text()
        uf = self.comboSituacao.currentText()
        cidadeCliente = self.txt_cidade.text()
        ruaCliente = self.txt_Rua.text()
        bairroCliente = self.txt_bairro.text()
        numeroCliente = self.txt_Numero.text()
        cepCliente = self.txt_cep.text()
        emailCliente = self.txt_email.text() 
        pontuacao = self.txt_pontuacao.text() 

        #conectando ao bd
        mydb = mysql.connector.connect(
        host=Controle.host,
        user=Controle.user,
        password=Controle.password,
        database=Controle.database
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT Pontos FROM cliente WHERE IdCliente = %s", (Controle.idConsulta,))
        pontos_atual = mycursor.fetchone()

        pontos = pontos_atual[0]  

        sql = """
        UPDATE cliente
        SET Nome = %s, Celular = %s, Cpf = %s, UF = %s, Cidade = %s, Rua = %s,
        Bairro = %s, Número = %s, Cep = %s, `E-mail` = %s, Pontos = %s
        WHERE IdCliente = %s
        """

        val = (
                nomeCliente, celularCliente, cpfCliente, uf, cidadeCliente,
                ruaCliente, bairroCliente, numeroCliente, cepCliente,
                emailCliente, pontuacao, Controle.idConsulta
        )

        mycursor.execute(sql, val)
        mydb.commit()

        print(f"{mycursor.rowcount} registro(s) alterado(s).")

        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Alterado com Sucesso!")
        msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        self.frm_DadosCliente.close()

    def retranslateUi(self, frm_DadosCliente):
        frm_DadosCliente.setWindowTitle(QCoreApplication.translate("frm_DadosCliente", u"Dados do Cliente", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosCliente", u"Nome:", None))
        self.lbl_celular.setText(QCoreApplication.translate("frm_DadosCliente", u"Celular: ", None))
        self.lbl_cpf.setText(QCoreApplication.translate("frm_DadosCliente", u"CPF:", None))
        self.txt_celular.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"(00) 0 0000-0000", None))
        self.txt_cpf.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"000.000.000-00", None))
        self.lbl_Rua.setText(QCoreApplication.translate("frm_DadosCliente", u"Rua:", None))
        self.lbl_cidade.setText(QCoreApplication.translate("frm_DadosCliente", u"Cidade:", None))
        self.lbl_bairro.setText(QCoreApplication.translate("frm_DadosCliente", u"Bairro:", None))
        self.lbl_cep.setText(QCoreApplication.translate("frm_DadosCliente", u"CEP:", None))
        self.txt_cep.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"00000-000", None))
        self.lbl_Numero.setText(QCoreApplication.translate("frm_DadosCliente", u"N\u00famero:", None))
        self.txt_email.setText("")
        self.lbl_email.setText(QCoreApplication.translate("frm_DadosCliente", u"E-mail:", None))
        self.txt_pontuacao.setText("0")
        self.txt_Numero.setText("0")
        self.lbl_email_2.setText(QCoreApplication.translate("frm_DadosCliente", u"Pontua\u00e7\u00e3o:", None))
        self.btn_cadastrar.setText("")
        self.btn_cancelar.setText("")
        self.lbl_cpfT.setText(QCoreApplication.translate("frm_DadosCliente", u"INFORME O CPF DO CLIENTE", None))
        self.lbl_cpf_2.setText(QCoreApplication.translate("frm_DadosCliente", u"UF:", None))
        self.comboSituacao.setItemText(0, QCoreApplication.translate("frm_DadosCliente", u"Prefiro n\u00e3o informar", None))
        self.comboSituacao.setItemText(1, QCoreApplication.translate("frm_DadosCliente", u"Acre (AC)", None))
        self.comboSituacao.setItemText(2, QCoreApplication.translate("frm_DadosCliente", u"Alagoas (AL)", None))
        self.comboSituacao.setItemText(3, QCoreApplication.translate("frm_DadosCliente", u"Amap\u00e1 (AP)", None))
        self.comboSituacao.setItemText(4, QCoreApplication.translate("frm_DadosCliente", u"Amazonas (AM)", None))
        self.comboSituacao.setItemText(5, QCoreApplication.translate("frm_DadosCliente", u"Bahia (BA)", None))
        self.comboSituacao.setItemText(6, QCoreApplication.translate("frm_DadosCliente", u"Cear\u00e1 (CE)", None))
        self.comboSituacao.setItemText(7, QCoreApplication.translate("frm_DadosCliente", u"Esp\u00edrito Santo (ES)", None))
        self.comboSituacao.setItemText(8, QCoreApplication.translate("frm_DadosCliente", u"Goi\u00e1s (GO)", None))
        self.comboSituacao.setItemText(9, QCoreApplication.translate("frm_DadosCliente", u"Maranh\u00e3o (MA)", None))
        self.comboSituacao.setItemText(10, QCoreApplication.translate("frm_DadosCliente", u"Mato Grosso (MT)", None))
        self.comboSituacao.setItemText(11, QCoreApplication.translate("frm_DadosCliente", u"Mato Grosso do Sul (MS)", None))
        self.comboSituacao.setItemText(12, QCoreApplication.translate("frm_DadosCliente", u"Minas Gerais (MG)", None))
        self.comboSituacao.setItemText(13, QCoreApplication.translate("frm_DadosCliente", u"Par\u00e1 (PA)", None))
        self.comboSituacao.setItemText(14, QCoreApplication.translate("frm_DadosCliente", u"Para\u00edba (PB)", None))
        self.comboSituacao.setItemText(15, QCoreApplication.translate("frm_DadosCliente", u"Paran\u00e1 (PR)", None))
        self.comboSituacao.setItemText(16, QCoreApplication.translate("frm_DadosCliente", u"Pernambuco (PE)", None))
        self.comboSituacao.setItemText(17, QCoreApplication.translate("frm_DadosCliente", u"Piau\u00ed (PI)", None))
        self.comboSituacao.setItemText(18, QCoreApplication.translate("frm_DadosCliente", u"Rio de Janeiro (RJ)", None))
        self.comboSituacao.setItemText(19, QCoreApplication.translate("frm_DadosCliente", u"Rio Grande do Norte (RN)", None))
        self.comboSituacao.setItemText(20, QCoreApplication.translate("frm_DadosCliente", u"Rio Grande do Sul (RS)", None))
        self.comboSituacao.setItemText(21, QCoreApplication.translate("frm_DadosCliente", u"Rond\u00f4nia (RO)", None))
        self.comboSituacao.setItemText(22, QCoreApplication.translate("frm_DadosCliente", u"Roraima (RR)", None))
        self.comboSituacao.setItemText(23, QCoreApplication.translate("frm_DadosCliente", u"Santa Catarina (SC)", None))
        self.comboSituacao.setItemText(24, QCoreApplication.translate("frm_DadosCliente", u"S\u00e3o Paulo (SP)", None))
        self.comboSituacao.setItemText(25, QCoreApplication.translate("frm_DadosCliente", u"Sergipe (SE)", None))
        self.comboSituacao.setItemText(26, QCoreApplication.translate("frm_DadosCliente", u"Tocantins (TO)", None))

        self.lbl_EmailT.setText(QCoreApplication.translate("frm_DadosCliente", u"INFORME O CEP DO SEU CLIENTE", None))
    # retranslateUi

        if Controle.tiposTelaDadosCliente == 'incluir':
                self.btn_cadastrar.clicked.connect(self.adicionarCliente)
        if Controle.tiposTelaDadosCliente == 'alterar':
                self.btn_cadastrar.clicked.connect(self.alterarCliente)
                print('Dados Cliente: ', Controle.tiposTelaDadosCliente)
        self.btn_cancelar.clicked.connect(lambda: self.sairTela(frm_DadosCliente))
        ##Condições da tela
        if Controle.tiposTelaDadosCliente == 'incluir':
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(True)
                self.txt_celular.setEnabled(True)
                self.txt_cpf.setEnabled(True)
                self.comboSituacao.setEnabled(True)
                self.txt_cidade.setEnabled(True)
                self.txt_Rua.setEnabled(True)
                self.txt_bairro.setEnabled(True)
                self.txt_Numero.setEnabled(True)
                self.txt_cep.setEnabled(True)
                self.txt_email.setEnabled(True)
                self.txt_pontuacao.setEnabled(False)
                self.btn_cadastrar.setEnabled(True)
        elif Controle.tiposTelaDadosCliente == 'consultar':            
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(False)
                self.txt_celular.setEnabled(False)
                self.txt_cpf.setEnabled(False)
                self.txt_cidade.setEnabled(False)
                self.txt_Rua.setEnabled(False)
                self.txt_bairro.setEnabled(False)
                self.txt_Numero.setEnabled(False)
                self.txt_cep.setEnabled(False)
                self.txt_email.setEnabled(False)
                self.txt_pontuacao.setEnabled(False)
                self.comboSituacao.setEnabled(False)
                self.btn_cadastrar.setEnabled(False)
                #Conexão com bd
                print('Conectando...')
                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM cliente WHERE idCliente = '" + Controle.idConsulta + "'"
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                mycursor.close()
                df = pd.DataFrame(myresult, columns=["idCliente", "Nome", "Celular", "Cpf", "UF", "Cidade", "Rua", "Bairro", "Número", "Cep", "E-mail", "Pontos"])
                nomeCliente = df['Nome'][0]
                celularCliente = df['Celular'][0]
                cpfCliente = df['Cpf'][0]
                cidadeCliente = df['Cidade'][0]
                ruaCliente = df['Rua'][0]
                bairroCliente = df['Bairro'][0]
                NumeroCliente = df['Número'][0]
                cepCliente = df['Cep'][0]
                emailCliente = df['E-mail'][0]
                uf = df['UF'][0]
                pontos = df['Pontos'][0]
                #setar na tela do sitema
                self.txt_nome.setText(nomeCliente)
                self.txt_celular.setText(celularCliente)
                self.txt_cpf.setText(cpfCliente)
                self.txt_Rua.setText(ruaCliente)
                self.txt_cidade.setText(cidadeCliente)
                self.txt_bairro.setText(bairroCliente)
                self.txt_Numero.setText(str(NumeroCliente))
                self.txt_cep.setText(cepCliente)
                self.txt_email.setText(emailCliente)
                self.txt_pontuacao.setText(str(pontos))
                self.comboSituacao.setCurrentText(uf)
        elif Controle.tiposTelaDadosCliente == 'alterar':
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(True)
                self.txt_celular.setEnabled(True)
                self.txt_cpf.setEnabled(True)
                self.txt_cidade.setEnabled(True)
                self.txt_Rua.setEnabled(True)
                self.txt_bairro.setEnabled(True)
                self.txt_Numero.setEnabled(True)
                self.txt_cep.setEnabled(True)
                self.txt_email.setEnabled(True)
                self.txt_pontuacao.setEnabled(False)
                self.btn_cadastrar.setEnabled(True)
                #Conexão com bd
                self.host = Controle.host
                self.user = Controle.user
                self.password = Controle.password
                self.database = Controle.database 
                print('Conectando...')
                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM cliente WHERE idCliente = '" + Controle.idConsulta + "'"
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                mycursor.close()
                df = pd.DataFrame(myresult, columns=["idCliente", "Nome", "Celular", "Cpf", "UF", "Cidade", "Rua", "Bairro", "Número", "Cep", "E-mail", "Pontos"])
                nomeCliente = df['Nome'][0]
                celularCliente = df['Celular'][0]
                cpfCliente = df['Cpf'][0]
                uf = df['UF'][0]
                cidadeCliente = df['Cidade'][0]
                ruaCliente = df['Rua'][0]
                bairroCliente = df['Bairro'][0]
                NumeroCliente = df['Número'][0]
                cepCliente = df['Cep'][0]
                emailCliente = df['E-mail'][0]
                pontos = df['Pontos'][0]
                #Setar na tela do sitema
                self.txt_nome.setText(nomeCliente)
                self.txt_celular.setText(celularCliente)
                self.txt_cpf.setText(cpfCliente)
                self.txt_Rua.setText(ruaCliente)
                self.txt_cidade.setText(cidadeCliente)
                self.txt_bairro.setText(bairroCliente)
                self.txt_Numero.setText(str(NumeroCliente))
                self.txt_cep.setText(cepCliente)
                self.txt_email.setText(emailCliente)
                self.txt_pontuacao.setText(str(pontos))
                self.comboSituacao.setCurrentText(uf)

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosCliente = QWidget()
    ui = Ui_frm_DadosCliente()
    ui.setupUi(frm_DadosCliente)
    frm_DadosCliente.show()
    app.exec()