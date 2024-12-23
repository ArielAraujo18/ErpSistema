from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import icon_cadastrar
import icon_cancelar

import mysql.connector
import Controle
import pandas as pd

class Ui_frm_DadosProdutos(object):
    def setupUi(self, frm_DadosProdutos):
        if not frm_DadosProdutos.objectName():
            frm_DadosProdutos.setObjectName(u"frm_DadosProdutos")
        frm_DadosProdutos.setFixedSize(526, 540)
        frm_DadosProdutos.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        frm_DadosProdutos.setStyleSheet(u"QWidget {\n"
"    background-color: #FFCCCB;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosProdutos)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(70, 50, 61, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosProdutos)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(130, 40, 361, 41))
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
        self.lbl_qtd.setGeometry(QRect(20, 110, 101, 20))
        self.lbl_qtd.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_Valor = QLabel(frm_DadosProdutos)
        self.lbl_Valor.setObjectName(u"lbl_Valor")
        self.lbl_Valor.setGeometry(QRect(70, 170, 51, 20))
        self.lbl_Valor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosProdutos)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(150, 440, 101, 91))
        self.btn_cancelar.setAutoFillBackground(False)
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_cancelar/cancelar.png);\n"
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
        self.txt_qtd.setGeometry(QRect(130, 100, 361, 41))
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
        self.txt_valor.setGeometry(QRect(130, 160, 361, 41))
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
        self.lbl_Fornecedor.setGeometry(QRect(20, 220, 101, 20))
        self.lbl_Fornecedor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_obs = QLabel(frm_DadosProdutos)
        self.lbl_obs.setObjectName(u"lbl_obs")
        self.lbl_obs.setGeometry(QRect(20, 340, 101, 20))
        self.lbl_obs.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosProdutos)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(290, 440, 101, 91))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_cadastrar/cadastrar.png); \n"
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
        self.comboBox.setGeometry(QRect(130, 220, 361, 31))
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
        self.textEdit.setGeometry(QRect(123, 290, 371, 121))
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
        self.lbl_maxCarac.setGeometry(QRect(410, 410, 111, 16))
        self.lbl_maxCarac.setStyleSheet(u"QLabel {\n"
"    font-size: 10px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_contador = QLabel(frm_DadosProdutos)
        self.lbl_contador.setObjectName(u"lbl_contador")
        self.lbl_contador.setGeometry(QRect(470, 270, 21, 20))

        self.retranslateUi(frm_DadosProdutos)

        QMetaObject.connectSlotsByName(frm_DadosProdutos)
    # setupUi

    def retranslateUi(self, frm_DadosProdutos):
        frm_DadosProdutos.setWindowTitle(QCoreApplication.translate("frm_DadosProdutos", u"Dados Produtos", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosProdutos", u"Nome:", None))
        self.lbl_qtd.setText(QCoreApplication.translate("frm_DadosProdutos", u"Quantidade:", None))
        self.lbl_Valor.setText(QCoreApplication.translate("frm_DadosProdutos", u"Valor:", None))
        self.btn_cancelar.setText("")
        self.txt_qtd.setInputMask(QCoreApplication.translate("frm_DadosProdutos", u"00000000000000000000000000000000000000000000000000", None))
        self.txt_qtd.setText("")
        self.txt_valor.setInputMask(QCoreApplication.translate("frm_DadosProdutos", u"R$", None))
        self.lbl_Fornecedor.setText(QCoreApplication.translate("frm_DadosProdutos", u"Fornecedor:", None))
        self.lbl_obs.setText(QCoreApplication.translate("frm_DadosProdutos", u"Observa\u00e7\u00e3o:", None))
        self.btn_cadastrar.setText("")
        self.lbl_maxCarac.setText(QCoreApplication.translate("frm_DadosProdutos", u"max: 500 caracteres", None))
        self.lbl_contador.setText(QCoreApplication.translate("frm_DadosProdutos", u"000", None))
    # retranslateUi
    ##Condições do botão



        ##Condições da tela
        if Controle.tiposTelaDadosCliente == 'consultar':
                print('DadosProdutos: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(True)
                self.txt_qtd.setEnabled(True)
                self.txt_valor.setEnabled(True)
                self.comboBox.setEnabled(True)
                self.textEdit.setEnabled(True)
                self.btn_cadastrar.setEnabled(True)
                print('Conectando')
                mydb = mysql.connector.connect(
                     host = 'localhost',
                     user = 'Ariel',
                     password = 'IRani18@#',
                     database = 'sistema'
                )
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM produtos WHERE idProdutos = '"  + Controle.idConsulta + "'" 
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                
                #Convertendo de bd para df
                df = pd.DataFrame(myresult, columns=["Nome", "Quantidade", "Valor", "Fornecedor", "Observação"])
                nome = df['Nome'][0]
                quantidade = df['Quantidade'][0]
                valor = df['Valor'][0]
                forncedor = df['Fornecedor'][0]
                observacao = df['Observação'][0]
                #Setando na tabela do sys
                self.txt_nome.setText(nome)
                self.txt_qtd.setText(quantidade)
                self.txt_valor.setText(valor)
                self.comboBox.setEditText(forncedor)
                self.textEdit.setText(observacao)
                

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosProdutos = QWidget()
    ui = Ui_frm_DadosProdutos()
    ui.setupUi(frm_DadosProdutos)
    frm_DadosProdutos.show()
    app.exec()