from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget, QMessageBox)
from PySide6 import QtCore


import pandas as pd
import Controle
import mysql.connector

import icon_cadastrar
import icon_cancelar

class Ui_frm_DadosValores(object):
    def setupUi(self, frm_DadosValores):
        if not frm_DadosValores.objectName():
            frm_DadosValores.setObjectName(u"frm_DadosValores")
        frm_DadosValores.setFixedSize(638, 654)
        frm_DadosValores.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        self.frm_DadosValores = frm_DadosValores
        frm_DadosValores.setStyleSheet(u"QWidget {\n"
"    background-color: #40E0D0;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosValores)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(70, 50, 61, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosValores)
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
        self.lbl_emissao = QLabel(frm_DadosValores)
        self.lbl_emissao.setObjectName(u"lbl_emissao")
        self.lbl_emissao.setGeometry(QRect(50, 110, 71, 20))
        self.lbl_emissao.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_vencimento = QLabel(frm_DadosValores)
        self.lbl_vencimento.setObjectName(u"lbl_vencimento")
        self.lbl_vencimento.setGeometry(QRect(20, 170, 101, 20))
        self.lbl_vencimento.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosValores)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(200, 550, 101, 91))
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
        self.txt_emissao = QLineEdit(frm_DadosValores)
        self.txt_emissao.setObjectName(u"txt_emissao")
        self.txt_emissao.setGeometry(QRect(130, 100, 361, 41))
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
        self.txt_vencimento = QLineEdit(frm_DadosValores)
        self.txt_vencimento.setObjectName(u"txt_vencimento")
        self.txt_vencimento.setGeometry(QRect(130, 160, 361, 41))
        self.txt_vencimento.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_obs = QLabel(frm_DadosValores)
        self.lbl_obs.setObjectName(u"lbl_obs")
        self.lbl_obs.setGeometry(QRect(20, 270, 101, 20))
        self.lbl_obs.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosValores)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(330, 550, 101, 91))
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
        self.textEdit = QTextEdit(frm_DadosValores)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 220, 371, 121))
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
        self.lbl_valor = QLabel(frm_DadosValores)
        self.lbl_valor.setObjectName(u"lbl_valor")
        self.lbl_valor.setGeometry(QRect(70, 370, 51, 20))
        self.lbl_valor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_valor = QLineEdit(frm_DadosValores)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setGeometry(QRect(130, 360, 371, 41))
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
        self.lbl_parcelas = QLabel(frm_DadosValores)
        self.lbl_parcelas.setObjectName(u"lbl_parcelas")
        self.lbl_parcelas.setGeometry(QRect(510, 370, 91, 20))
        self.lbl_parcelas.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_parcelas = QLineEdit(frm_DadosValores)
        self.txt_parcelas.setObjectName(u"txt_parcelas")
        self.txt_parcelas.setGeometry(QRect(590, 360, 41, 41))
        self.txt_parcelas.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_formaDePagamento = QLabel(frm_DadosValores)
        self.lbl_formaDePagamento.setObjectName(u"lbl_formaDePagamento")
        self.lbl_formaDePagamento.setGeometry(QRect(10, 430, 181, 20))
        self.lbl_formaDePagamento.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.comboFormaDePagamento = QComboBox(frm_DadosValores)
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.setObjectName(u"comboFormaDePagamento")
        self.comboFormaDePagamento.setGeometry(QRect(200, 420, 361, 31))
        self.comboFormaDePagamento.setStyleSheet(u"QComboBox {\n"
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
        self.lbl_Situacao = QLabel(frm_DadosValores)
        self.lbl_Situacao.setObjectName(u"lbl_Situacao")
        self.lbl_Situacao.setGeometry(QRect(110, 490, 81, 20))
        self.lbl_Situacao.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.comboSituacao = QComboBox(frm_DadosValores)
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.setObjectName(u"comboSituacao")
        self.comboSituacao.setGeometry(QRect(200, 480, 361, 31))
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

        self.retranslateUi(frm_DadosValores)

        QMetaObject.connectSlotsByName(frm_DadosValores)
    # setupUi

    def sairTela(self, frm_DadosValores):
        self.frm_DadosValores.close()
        self.frm_DadosValores = None

    def adicionarValores(self):
        campos_comuns = {
            "Nome": self.txt_nome.text().strip(),
            "Observacao": self.textEdit.toPlainText().strip(),
            "Valor": self.txt_valor.text().strip(),
            "Parcelas": self.txt_parcelas.text().strip(),
        }

        campos_mask = {
            "Emissão": self.txt_emissao.text().strip(),
            "Vencimento": self.txt_vencimento.text().strip(),
        }

        for campo, valor, in campos_comuns.items():
            if not valor:
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"O campo {campo} é obrigatório e não pode ficar vazio!")
                msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        
        for campo, valor in campos_mask.items():
            valor_limpo = valor.replace("R$", "").replace("/","").replace(".", "").strip()

            if not valor_limpo.isdigit():
                msg = QMessageBox()
                msg.setWindowTitle("Erro!")
                msg.setText(f"O campo '{campo}' deve conter apenas números!")
                msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
            
        valor = self.txt_valor.text().strip()
        if "R$" not in valor:
                msg = QMessageBox()
                msg.setWindowTitle("Erro!")
                msg.setText("É importante formatar o valor corretamente com R$, virgulas e pontos!")
                msg.setWindowIcon(QIcon((r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png")))
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        nome = self.txt_nome.text()
        emissao = self.txt_emissao.text()
        vencimento = self.txt_vencimento.text()
        obs = self.textEdit.toPlainText()
        valor = self.txt_valor.text()
        parcelas = self.txt_parcelas.text()
        formaDePagamento = self.comboFormaDePagamento.currentText()
        situacao = self.comboSituacao.currentText()

        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database,
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO valores(`Nome`, `Emissão`, `Vencimento`, `Observação`, `Valor`, `Parcelas`, `Forma de pagamento`, `Situação`) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nome, emissao, vencimento, obs, valor, parcelas, formaDePagamento, situacao)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'Registros inseridos')

        mycursor.close()
        mydb.close()

        self.adicionarGastos()

        self.txt_nome.setText("")
        self.txt_emissao.setText("")
        self.txt_vencimento.setText("")
        self.textEdit.setText("")
        self.txt_valor.setText("")
        self.txt_parcelas.setText("")
        self.comboFormaDePagamento.setCurrentIndex(0)
        self.comboSituacao.setCurrentIndex(0)

        # Mensagem de sucesso
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Valor adicionado com sucesso!")
        icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
        msg.setWindowIcon(QIcon(icon_path))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


    def adicionarGastos(self):

        nome = self.txt_nome.text()
        obs = self.textEdit.toPlainText()
        valor = self.txt_valor.text()
        quantidade = 1
        
        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database,
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO `banco-lucros` (`Nome`, `Valor`, `Observação`, `Quantidade`) values (%s, %s, %s, %s)"
        val = (nome, valor, obs, quantidade)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'Registros inseridos em gastos')

        mycursor.close()
        mydb.close()

    def alterarValores(self):
        
        nome = self.txt_nome.text()
        emissao = self.txt_emissao.text()
        vencimento = self.txt_vencimento.text()
        obs = self.textEdit.toPlainText()
        valor = self.txt_valor.text()
        parcelas = self.txt_parcelas.text()
        formaDePagamento = self.comboFormaDePagamento.currentText()
        situacao = self.comboSituacao.currentText()

        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )

        mycursor = mydb.cursor()
        sql = """
        UPDATE valores
        SET Nome = %s, Emissão = %s, Vencimento = %s, Observação = %s, 
                Valor = %s, Parcelas = %s, `Forma de pagamento` = %s, Situação = %s
        WHERE idValores = %s
        """
        val = (nome, emissao, vencimento, obs, valor, parcelas, formaDePagamento, situacao, Controle.idConsulta)
        mycursor.execute(sql, val)
        mydb.commit()

        msg = QMessageBox()
        msg.setWindowTitle('Sucesso!')
        msg.setText('Dívida alterada com sucesso!')
        msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosValores.close()


    def retranslateUi(self, frm_DadosValores):
        frm_DadosValores.setWindowTitle(QCoreApplication.translate("frm_DadosValores", u"Dados Valores", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosValores", u"Nome:", None))
        self.lbl_emissao.setText(QCoreApplication.translate("frm_DadosValores", u"Emiss\u00e3o:", None))
        self.lbl_vencimento.setText(QCoreApplication.translate("frm_DadosValores", u"Vencimento:", None))
        self.btn_cancelar.setText("")
        self.txt_emissao.setInputMask(QCoreApplication.translate("frm_DadosValores", u"00/00/0000", None))
        self.txt_emissao.setText(QCoreApplication.translate("frm_DadosValores", u"//", None))
        self.txt_vencimento.setInputMask(QCoreApplication.translate("frm_DadosValores", u"00/00/0000", None))
        self.lbl_obs.setText(QCoreApplication.translate("frm_DadosValores", u"Observa\u00e7\u00e3o:", None))
        self.btn_cadastrar.setText("")
        self.lbl_valor.setText(QCoreApplication.translate("frm_DadosValores", u"Valor:", None))
        self.txt_valor.setInputMask("")
        self.lbl_parcelas.setText(QCoreApplication.translate("frm_DadosValores", u"Parcelas:", None))
        self.lbl_formaDePagamento.setText(QCoreApplication.translate("frm_DadosValores", u"Forma de Pagamento:", None))
        self.comboFormaDePagamento.setItemText(0, QCoreApplication.translate("frm_DadosValores", u"Dinheiro", None))
        self.comboFormaDePagamento.setItemText(1, QCoreApplication.translate("frm_DadosValores", u"Pix", None))
        self.comboFormaDePagamento.setItemText(2, QCoreApplication.translate("frm_DadosValores", u"Cr\u00e9dito", None))
        self.comboFormaDePagamento.setItemText(3, QCoreApplication.translate("frm_DadosValores", u"D\u00e9bito", None))
        self.comboFormaDePagamento.setItemText(4, QCoreApplication.translate("frm_DadosValores", u"Boleto", None))
        self.comboFormaDePagamento.setItemText(5, QCoreApplication.translate("frm_DadosValores", u"Transfer\u00eancia banc\u00e1ria", None))

        self.lbl_Situacao.setText(QCoreApplication.translate("frm_DadosValores", u"Situa\u00e7\u00e3o:", None))
        self.comboSituacao.setItemText(0, QCoreApplication.translate("frm_DadosValores", u"PAGO", None))
        self.comboSituacao.setItemText(1, QCoreApplication.translate("frm_DadosValores", u"PENDENTE", None))

    # retranslateUi

        if Controle.tiposTelaDadosCliente == 'incluir':
                print('incluir')
                self.btn_cadastrar.clicked.connect(self.adicionarValores)
        if Controle.tiposTelaDadosCliente == 'alterar':
                print('alterar')
                self.btn_cadastrar.clicked.connect(self.alterarValores)

        self.btn_cancelar.clicked.connect(self.sairTela)

        if Controle.tiposTelaDadosCliente == 'incluir':
                print('incluindo')
                self.txt_nome.setEnabled(True)
                self.txt_emissao.setEnabled(True)
                self.txt_vencimento.setEnabled(True)
                self.textEdit.setEnabled(True)
                self.txt_valor.setEnabled(True)
                self.txt_parcelas.setEnabled(True)
                self.comboFormaDePagamento.setEnabled(True)
                self.comboSituacao.setEnabled(True)
                self.btn_cadastrar.setEnabled(True)
        elif Controle.tiposTelaDadosCliente == 'alterar':
                print('alterando')
                self.txt_nome.setEnabled(True)
                self.txt_emissao.setEnabled(True)
                self.txt_vencimento.setEnabled(True)
                self.textEdit.setEnabled(True)
                self.txt_valor.setEnabled(True)
                self.txt_parcelas.setEnabled(True)
                self.comboFormaDePagamento.setEnabled(True)
                self.comboSituacao.setEnabled(True)
                self.btn_cadastrar.setEnabled(True)

                print('conectando')

                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )

                mycursor = mydb.cursor()
                consultarSQL = "SELECT * FROM valores WHERE idValores = %s"

                mycursor.execute(consultarSQL, (Controle.idConsulta,))
                myresult = mycursor.fetchone()  # Obtém o resultado como uma tupla
                
                nome = myresult[1]
                emissao = myresult[2]
                vencimento = myresult[3]
                observacao = myresult[4]
                valor = myresult[5]
                parcelas = myresult[6]
                formaDePagamento = myresult[7]
                situacao = myresult[8]

                self.txt_nome.setText(nome)
                self.txt_emissao.setText(emissao)
                self.txt_vencimento.setText(vencimento)
                self.textEdit.setText(observacao)
                self.txt_nome.setText(nome)
                self.txt_valor.setText(valor)
                self.txt_parcelas.setText(str(parcelas))
                self.comboFormaDePagamento.setCurrentText(formaDePagamento)
                self.comboSituacao.setCurrentText(situacao)

                # Fechar o cursor e a conexão
                mycursor.close()
                mydb.close()
        
        elif Controle.tiposTelaDadosCliente == 'consultar':
                print('DadosValores:', Controle.tiposTelaDadosCliente)

                self.txt_nome.setEnabled(False)
                self.txt_emissao.setEnabled(False)
                self.txt_vencimento.setEnabled(False)
                self.textEdit.setEnabled(False)
                self.txt_valor.setEnabled(False)
                self.txt_parcelas.setEnabled(False)
                self.comboFormaDePagamento.setEnabled(False)
                self.comboSituacao.setEnabled(False)
                self.btn_cadastrar.setEnabled(False)

                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSql = """
                SELECT Nome, Emissão, Vencimento, Observação, Valor, Parcelas, `Forma de pagamento`, Situação
                FROM valores
                WHERE idValores = %s
                """

                mycursor.execute(consultaSql, (Controle.idConsulta,))
                myresult = mycursor.fetchall()

                df = pd.DataFrame(myresult, columns=["Nome", "Emissão", "Vencimento", "Observação", "Valor", "Parcelas", "Forma de pagamento", "Situação"])

                self.txt_nome.setText(str(df['Nome'][0]))
                self.txt_emissao.setText(str(df['Emissão'][0]))
                self.txt_vencimento.setText(str(df['Vencimento'][0]))
                self.textEdit.setText(str(df['Observação'][0]))
                self.txt_valor.setText(str(df['Valor'][0]))
                self.txt_parcelas.setText(str(df['Parcelas'][0]))
                formaDePagamento = str(df['Forma de pagamento'][0]) if not df.empty else ""
                situacao = str(df['Situação'][0]) if not df.empty else ""

                self.comboFormaDePagamento.setCurrentText(formaDePagamento)
                self.comboSituacao.setCurrentText(situacao)

                print(f"Forma de pagamento: {formaDePagamento}, Situação: {situacao}")




if __name__ == "__main__":
    app = QApplication([])
    frm_DadosValores = QWidget()
    ui = Ui_frm_DadosValores()
    ui.setupUi(frm_DadosValores)
    frm_DadosValores.show()
    app.exec()