from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget, QMessageBox)
import icon_voltar
import icon_add

import os
import mysql.connector
import Controle
import pandas as pd

class Ui_frm_DadosProdutos(object):
    def setupUi(self, frm_DadosProdutos):
        if not frm_DadosProdutos.objectName():
            frm_DadosProdutos.setObjectName(u"frm_DadosProdutos")
        frm_DadosProdutos.setFixedSize(518, 554)
        self.frm_DadosProdutos = frm_DadosProdutos
        frm_DadosProdutos.setStyleSheet(u"QWidget {\n"
"    background-color: #2c2c2c;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosProdutos)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(10, 50, 141, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosProdutos)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(160, 40, 261, 41))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_qtd = QLabel(frm_DadosProdutos)
        self.lbl_qtd.setObjectName(u"lbl_qtd")
        self.lbl_qtd.setGeometry(QRect(10, 170, 101, 20))
        self.lbl_qtd.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_Valor = QLabel(frm_DadosProdutos)
        self.lbl_Valor.setObjectName(u"lbl_Valor")
        self.lbl_Valor.setGeometry(QRect(280, 170, 51, 21))
        self.lbl_Valor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosProdutos)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(140, 460, 101, 91))
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
        self.txt_qtd = QLineEdit(frm_DadosProdutos)
        self.txt_qtd.setObjectName(u"txt_qtd")
        self.txt_qtd.setGeometry(QRect(120, 160, 141, 41))
        self.txt_qtd.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_valor = QLineEdit(frm_DadosProdutos)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setGeometry(QRect(340, 160, 151, 41))
        self.txt_valor.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_Fornecedor = QLabel(frm_DadosProdutos)
        self.lbl_Fornecedor.setObjectName(u"lbl_Fornecedor")
        self.lbl_Fornecedor.setGeometry(QRect(10, 240, 101, 20))
        self.lbl_Fornecedor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_obs = QLabel(frm_DadosProdutos)
        self.lbl_obs.setObjectName(u"lbl_obs")
        self.lbl_obs.setGeometry(QRect(10, 340, 101, 20))
        self.lbl_obs.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosProdutos)
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
        self.comboBox = QComboBox(frm_DadosProdutos)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 220, 361, 51))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
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
        self.textEdit = QTextEdit(frm_DadosProdutos)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(120, 290, 371, 121))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 16px; /* Fonte maior */\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"    text-align: left; /* Alinha o texto \u00e0 esquerda */\n"
"    vertical-align: top; /* Escreve do topo */\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}")
        self.lbl_maxCarac = QLabel(frm_DadosProdutos)
        self.lbl_maxCarac.setObjectName(u"lbl_maxCarac")
        self.lbl_maxCarac.setGeometry(QRect(120, 420, 101, 16))
        self.lbl_maxCarac.setStyleSheet(u"QLabel {\n"
"    font-size: 10px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_emissao = QLineEdit(frm_DadosProdutos)
        self.txt_emissao.setObjectName(u"txt_emissao")
        self.txt_emissao.setGeometry(QRect(90, 100, 101, 41))
        self.txt_emissao.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_nome_2 = QLabel(frm_DadosProdutos)
        self.lbl_nome_2.setObjectName(u"lbl_nome_2")
        self.lbl_nome_2.setGeometry(QRect(10, 110, 71, 21))
        self.lbl_nome_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_nome_3 = QLabel(frm_DadosProdutos)
        self.lbl_nome_3.setObjectName(u"lbl_nome_3")
        self.lbl_nome_3.setGeometry(QRect(210, 110, 131, 21))
        self.lbl_nome_3.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Validade = QLineEdit(frm_DadosProdutos)
        self.txt_Validade.setObjectName(u"txt_Validade")
        self.txt_Validade.setGeometry(QRect(350, 100, 101, 41))
        self.txt_Validade.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_maxCarac_2 = QLabel(frm_DadosProdutos)
        self.lbl_maxCarac_2.setObjectName(u"lbl_maxCarac_2")
        self.lbl_maxCarac_2.setGeometry(QRect(470, 420, 21, 21))
        self.lbl_maxCarac_2.setStyleSheet(u"QLabel {\n"
"    font-size: 10px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.retranslateUi(frm_DadosProdutos)

        QMetaObject.connectSlotsByName(frm_DadosProdutos)
    # setupUi

    def adiconarProdutos(self):
        nome = self.txt_nome.text()
        emissao = self.txt_emissao.text()
        validade = self.txt_Validade.text()
        quantidade = self.txt_qtd.text()
        valor = self.txt_valor.text()
        fornecedor = self.comboBox.currentText() 
        obs = self.textEdit.toPlainText()

        if emissao == '//':
              emissao = None
        if validade == '//':
              validade = None
        if quantidade == '':
              quantidade = 0

        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO produtos(`Nome`, `Emissão`, `Validade`, `Quantidade`, `Valor`, `Fornecedor`, `Observação`) values (%s, %s, %s, %s, %s, %s, %s)"
        val = (nome, emissao, validade, quantidade, valor, fornecedor, obs)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, 'Registro(s) inserido(s)')

        mycursor.close()
        mydb.close()

        self.carregarFornecedores()        

        self.txt_nome.setText("")
        self.txt_emissao.setText("")
        self.txt_Validade.setText("")
        self.txt_qtd.setText("")
        self.txt_valor.setText("R$")
        self.textEdit.setPlainText("")
        self.comboBox.setCurrentIndex(0)

        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Produto adicionado com sucesso!")
        icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
        msg.setWindowIcon(QIcon(icon_path))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def carregarFornecedores(self):
        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT `Razão Social` FROM fornecedor")
        resultados = mycursor.fetchall()
                
        self.comboBox.clear()

        for fornecedor in resultados:
                print(f"Adicionando fornecedor: {fornecedor[0]}")  # Imprime para depuração
                self.comboBox.addItem(fornecedor[0])

        mycursor.close()

        mydb.close()

    def retranslateUi(self, frm_DadosProdutos):
        frm_DadosProdutos.setWindowTitle(QCoreApplication.translate("frm_DadosProdutos", u"Dados Produtos", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosProdutos", u"Nome do Produto:", None))
        self.lbl_qtd.setText(QCoreApplication.translate("frm_DadosProdutos", u"Quantidade:", None))
        self.lbl_Valor.setText(QCoreApplication.translate("frm_DadosProdutos", u"Valor:", None))
        self.btn_cancelar.setText("")
        self.txt_qtd.setText("")
        self.txt_valor.setText("R$")
        self.lbl_Fornecedor.setText(QCoreApplication.translate("frm_DadosProdutos", u"Fornecedor:", None))
        self.lbl_obs.setText(QCoreApplication.translate("frm_DadosProdutos", u"Observa\u00e7\u00e3o:", None))
        self.btn_cadastrar.setText("")
        self.lbl_maxCarac.setText(QCoreApplication.translate("frm_DadosProdutos", u"max: 500 caracteres", None))
        self.txt_emissao.setInputMask(QCoreApplication.translate("frm_DadosProdutos", u"00/00/0000", None))
        self.txt_emissao.setText(QCoreApplication.translate("frm_DadosProdutos", u"//", None))
        self.lbl_nome_2.setText(QCoreApplication.translate("frm_DadosProdutos", u"Emiss\u00e3o:", None))
        self.lbl_nome_3.setText(QCoreApplication.translate("frm_DadosProdutos", u"Data de validade:", None))
        self.txt_Validade.setInputMask(QCoreApplication.translate("frm_DadosProdutos", u"00/00/0000", None))
        self.txt_Validade.setText(QCoreApplication.translate("frm_DadosProdutos", u"//", None))
        self.lbl_maxCarac_2.setText(QCoreApplication.translate("frm_DadosProdutos", u"0", None))
    # retranslateUi
        self.carregarFornecedores()

        if Controle.tiposTelaDadosCliente == 'incluir':
              print('incluir')
              self.btn_cadastrar.clicked.connect(self.adiconarProdutos)
        if Controle.tiposTelaDadosCliente == 'alterar':
               print('alterar')
               self.btn_cadastrar.clicked.connect(self.alterarProdutos)

        self.btn_cancelar.clicked.connect(lambda: self.sairTela(frm_DadosProdutos))

        ##Condições da tela
        if Controle.tiposTelaDadosCliente == 'consultar':
                print('DadosProdutos: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(False)
                self.txt_qtd.setEnabled(False)
                self.txt_valor.setEnabled(False)
                self.comboBox.setEnabled(False)
                self.textEdit.setEnabled(False)
                self.btn_cadastrar.setEnabled(False)
                print('Conectando')

                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSQL = """
                SELECT Nome, Quantidade, Valor, Fornecedor, Observação
                FROM produtos
                WHERE idProdutos = %s
                """
                mycursor.execute(consultaSQL, (Controle.idConsulta,))
                myresult = mycursor.fetchall()
                
                df = pd.DataFrame(myresult, columns=["Nome", "Quantidade", "Valor", "Fornecedor", "Observação"])
                
                self.txt_nome.setText(str(df['Nome'][0]))
                self.txt_qtd.setText(str(df['Quantidade'][0]))
                self.txt_valor.setText(str(df['Valor'][0]))
                #adicionando fornecedor na combobox
                fornecedor = str(df['Fornecedor'][0])
                print("Fornecedor:", fornecedor)
                #verificando se o fornecedor existe
                if fornecedor not in [self.comboBox.itemText(i) for i in range(self.comboBox.count())]:
                        self.comboBox.addItem(fornecedor)
                self.comboBox.setCurrentText(fornecedor)
                self.textEdit.setText(str(df['Observação'][0]))
        elif Controle.tiposTelaDadosCliente == 'incluir':
                self.carregarFornecedores()
                print('incluindo')
                self.txt_nome.setEnabled(True)
                self.txt_emissao.setEnabled(True)
                self.txt_Validade.setEnabled(True)
                self.txt_qtd.setEnabled(True)
                self.txt_valor.setEnabled(True)
                self.comboBox.setEnabled(True)
                self.textEdit.setEnabled(True)
                self.btn_cadastrar.setEnabled(True)                                               
        elif Controle.tiposTelaDadosCliente == 'alterar':
                print('DadosProdutos: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(True)
                self.txt_qtd.setEnabled(True)
                self.txt_valor.setEnabled(True)
                self.comboBox.setEnabled(True)
                self.textEdit.setEnabled(True)
                
                print('Conectando...')
                
                
                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                
                consultarSQL = "SELECT * FROM produtos WHERE idProdutos = '" + Controle.idConsulta + "'"
                mycursor.execute(consultarSQL)
                myresult = mycursor.fetchone()
                
                nome = myresult[1]
                quantidade = myresult[2]
                valor = myresult[3]
                fornecedor_atual = myresult[4]
                obs = myresult[5]

               
                self.txt_nome.setText(nome)
                self.txt_qtd.setText(str(quantidade))
                self.txt_valor.setText(str(valor))
                self.textEdit.setText(obs)
                
                self.comboBox.clear()

                mycursor.execute("SELECT `Razão Social` FROM fornecedor")
                fornecedores = mycursor.fetchall()
                
                for fornecedor_item in fornecedores:
                        self.comboBox.addItem(fornecedor_item[0])
                
                self.comboBox.setCurrentText(fornecedor_atual)
                
                mycursor.close()
                mydb.close()

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosProdutos = QWidget()
    ui = Ui_frm_DadosProdutos()
    ui.setupUi(frm_DadosProdutos)
    frm_DadosProdutos.show()
    app.exec()