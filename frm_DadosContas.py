from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget, QMessageBox)

import Controle
import pandas as pd
import mysql.connector

import icon_cadastrar
import icon_cancelar

class Ui_frm_DadosContas(object):
    def setupUi(self, frm_DadosContas):
        if not frm_DadosContas.objectName():
            frm_DadosContas.setObjectName(u"frm_DadosContas")
        frm_DadosContas.setFixedSize(638, 795)
        self.frm_DadosContas = frm_DadosContas
        frm_DadosContas.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        frm_DadosContas.setStyleSheet(u"QWidget {\n"
"    background-color: #4E342E;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosContas)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(70, 50, 61, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosContas)
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
        self.lbl_emissao = QLabel(frm_DadosContas)
        self.lbl_emissao.setObjectName(u"lbl_emissao")
        self.lbl_emissao.setGeometry(QRect(50, 110, 71, 20))
        self.lbl_emissao.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_vencimento = QLabel(frm_DadosContas)
        self.lbl_vencimento.setObjectName(u"lbl_vencimento")
        self.lbl_vencimento.setGeometry(QRect(20, 170, 101, 20))
        self.lbl_vencimento.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosContas)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(210, 670, 101, 91))
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
        self.txt_emissao = QLineEdit(frm_DadosContas)
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
        self.txt_vencimento = QLineEdit(frm_DadosContas)
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
        self.lbl_Fornecedor = QLabel(frm_DadosContas)
        self.lbl_Fornecedor.setObjectName(u"lbl_Fornecedor")
        self.lbl_Fornecedor.setGeometry(QRect(20, 230, 101, 20))
        self.lbl_Fornecedor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_obs = QLabel(frm_DadosContas)
        self.lbl_obs.setObjectName(u"lbl_obs")
        self.lbl_obs.setGeometry(QRect(20, 340, 101, 20))
        self.lbl_obs.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosContas)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(340, 670, 101, 91))
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
        self.textEdit = QTextEdit(frm_DadosContas)
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
        self.lbl_maxCarac = QLabel(frm_DadosContas)
        self.lbl_maxCarac.setObjectName(u"lbl_maxCarac")
        self.lbl_maxCarac.setGeometry(QRect(410, 410, 111, 16))
        self.lbl_maxCarac.setStyleSheet(u"QLabel {\n"
"    font-size: 10px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_contador = QLabel(frm_DadosContas)
        self.lbl_contador.setObjectName(u"lbl_contador")
        self.lbl_contador.setGeometry(QRect(470, 270, 21, 20))
        self.comboFornecedor = QComboBox(frm_DadosContas)
        self.comboFornecedor.addItem("")
        self.comboFornecedor.setObjectName(u"comboFornecedor")
        self.comboFornecedor.setGeometry(QRect(130, 230, 361, 31))
        self.comboFornecedor.setStyleSheet(u"QComboBox {\n"
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
        self.lbl_valor = QLabel(frm_DadosContas)
        self.lbl_valor.setObjectName(u"lbl_valor")
        self.lbl_valor.setGeometry(QRect(60, 450, 51, 20))
        self.lbl_valor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_valor = QLineEdit(frm_DadosContas)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setGeometry(QRect(120, 440, 371, 41))
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
        self.lbl_parcelas = QLabel(frm_DadosContas)
        self.lbl_parcelas.setObjectName(u"lbl_parcelas")
        self.lbl_parcelas.setGeometry(QRect(500, 450, 91, 20))
        self.lbl_parcelas.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_parcelas = QLineEdit(frm_DadosContas)
        self.txt_parcelas.setObjectName(u"txt_parcelas")
        self.txt_parcelas.setGeometry(QRect(580, 440, 51, 41))
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
        self.lbl_formaDePagamento = QLabel(frm_DadosContas)
        self.lbl_formaDePagamento.setObjectName(u"lbl_formaDePagamento")
        self.lbl_formaDePagamento.setGeometry(QRect(10, 520, 181, 20))
        self.lbl_formaDePagamento.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.comboFormaDePagamento = QComboBox(frm_DadosContas)
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.addItem("")
        self.comboFormaDePagamento.setObjectName(u"comboFormaDePagamento")
        self.comboFormaDePagamento.setGeometry(QRect(200, 520, 361, 31))
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
        self.lbl_Situacao = QLabel(frm_DadosContas)
        self.lbl_Situacao.setObjectName(u"lbl_Situacao")
        self.lbl_Situacao.setGeometry(QRect(110, 580, 81, 20))
        self.lbl_Situacao.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.comboSituacao = QComboBox(frm_DadosContas)
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.setObjectName(u"comboSituacao")
        self.comboSituacao.setGeometry(QRect(200, 580, 361, 31))
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

        self.retranslateUi(frm_DadosContas)

        QMetaObject.connectSlotsByName(frm_DadosContas)
    # setupUi

    def adiconarContas(self):
        #Definição dos campos
        campos_comuns = {
            "Nome": self.txt_nome.text().strip(),
            "Observação": self.textEdit.toPlainText().strip(),
            "Parcelas": self.txt_parcelas.text().strip(),
            "Valor": self.txt_valor.text().strip(),
        }
        campos_mask = {
            "Emissão": self.txt_emissao.text().strip(),
            "Vencimento": self.txt_vencimento.text().strip(),
        }

        for campo, valor in campos_comuns.items():
            if not valor: #Verifica se o campo está vazio
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
        fornecedor = self.comboFornecedor.currentText()
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

        sql = "INSERT INTO contas(`Nome`, `Emissão`, `Vencimento`, `Fornecedor`, `Observação`, `Valor`, `Parcelas`, `Forma de pagamento`, `Situação`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nome, emissao, vencimento, fornecedor, obs, valor, parcelas, formaDePagamento, situacao)
        mycursor.execute(sql, val)
        mydb.commit()

        self.carregarFornecedores()
        
        print(mycursor.rowcount, 'Registros inseridos')

        mycursor.close()
        mydb.close()

        self.txt_nome.setText("")
        self.txt_emissao.setText("")
        self.txt_vencimento.setText("")
        self.textEdit.setText("")
        self.txt_valor.setText("")
        self.txt_parcelas.setText("")
        self.comboFornecedor.setCurrentIndex(0)
        self.comboFormaDePagamento.setCurrentIndex(0)
        self.comboSituacao.setCurrentIndex(0)

        # Mensagem de sucesso
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Dívida adicionada com sucesso!")
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

        #Query para nomes dos fornecedores
        mycursor.execute("SELECT `Razão Social` FROM fornecedor")
        resultados = mycursor.fetchall()

        for fornecedor in resultados:
            print(f"Adicionado fornecedor: {fornecedor[0]}")
            self.comboFornecedor.addItem(fornecedor[0])

        mycursor.close()
        mydb.close()

    def sairTela(self, frm_DadosContas):
        self.frm_DadosContas.close()

    def alterarContas(self):
        nome = self.txt_nome.text()
        emissao = self.txt_emissao.text()
        vencimento = self.txt_vencimento.text()
        fornecedor = self.comboFornecedor.currentText()
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
        UPDATE contas
        SET Nome = %s, Emissão = %s, Vencimento = %s, Fornecedor = %s, Observação = %s, 
                Valor = %s, Parcelas = %s, `Forma de pagamento` = %s, Situação = %s
        WHERE idContas = %s
        """
        val = (nome, emissao, vencimento, fornecedor, obs, valor, parcelas, formaDePagamento, situacao, Controle.idConsulta)
        mycursor.execute(sql, val)
        mydb.commit()

        msg = QMessageBox()
        msg.setWindowTitle('Sucesso!')
        msg.setText('Dívida alterada com sucesso!')
        msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosContas.close()


    def retranslateUi(self, frm_DadosContas):
        frm_DadosContas.setWindowTitle(QCoreApplication.translate("frm_DadosContas", u"Dados Contas", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosContas", u"Nome:", None))
        self.lbl_emissao.setText(QCoreApplication.translate("frm_DadosContas", u"Emiss\u00e3o:", None))
        self.lbl_vencimento.setText(QCoreApplication.translate("frm_DadosContas", u"Vencimento:", None))
        self.btn_cancelar.setText("")
        self.txt_emissao.setInputMask(QCoreApplication.translate("frm_DadosContas", u"00/00/0000", None))
        self.txt_emissao.setText(QCoreApplication.translate("frm_DadosContas", u"//", None))
        self.txt_vencimento.setInputMask(QCoreApplication.translate("frm_DadosContas", u"00/00/0000", None))
        self.lbl_Fornecedor.setText(QCoreApplication.translate("frm_DadosContas", u"Fornecedor:", None))
        self.lbl_obs.setText(QCoreApplication.translate("frm_DadosContas", u"Observa\u00e7\u00e3o:", None))
        self.btn_cadastrar.setText("")
        self.lbl_maxCarac.setText(QCoreApplication.translate("frm_DadosContas", u"max: 500 caracteres", None))
        self.lbl_contador.setText(QCoreApplication.translate("frm_DadosContas", u"000", None))
        self.comboFornecedor.setItemText(0, QCoreApplication.translate("frm_DadosContas", u"Nenhum", None))

        self.lbl_valor.setText(QCoreApplication.translate("frm_DadosContas", u"Valor:", None))
        self.txt_valor.setInputMask("")
        self.lbl_parcelas.setText(QCoreApplication.translate("frm_DadosContas", u"Parcelas:", None))
        self.lbl_formaDePagamento.setText(QCoreApplication.translate("frm_DadosContas", u"Forma de Pagamento:", None))
        self.comboFormaDePagamento.setItemText(0, QCoreApplication.translate("frm_DadosContas", u"Dinheiro", None))
        self.comboFormaDePagamento.setItemText(1, QCoreApplication.translate("frm_DadosContas", u"Pix", None))
        self.comboFormaDePagamento.setItemText(2, QCoreApplication.translate("frm_DadosContas", u"Cr\u00e9dito", None))
        self.comboFormaDePagamento.setItemText(3, QCoreApplication.translate("frm_DadosContas", u"D\u00e9bito", None))
        self.comboFormaDePagamento.setItemText(4, QCoreApplication.translate("frm_DadosContas", u"Boleto", None))
        self.comboFormaDePagamento.setItemText(5, QCoreApplication.translate("frm_DadosContas", u"Transfer\u00eancia banc\u00e1ria", None))

        self.lbl_Situacao.setText(QCoreApplication.translate("frm_DadosContas", u"Situa\u00e7\u00e3o:", None))
        self.comboSituacao.setItemText(0, QCoreApplication.translate("frm_DadosContas", u"PAGO", None))
        self.comboSituacao.setItemText(1, QCoreApplication.translate("frm_DadosContas", u"PENDENTE", None))

        if Controle.tiposTelaDadosCliente == 'incluir':
             print("incluir")
             self.btn_cadastrar.clicked.connect(self.adiconarContas)
        if Controle.tiposTelaDadosCliente == 'alterar':
             print('alterando')
             self.btn_cadastrar.clicked.connect(self.alterarContas)
        
        self.btn_cancelar.clicked.connect(self.sairTela)

        #Condições da tela
        if Controle.tiposTelaDadosCliente == 'incluir':
                self.carregarFornecedores()
                self.txt_nome.setEnabled(True)
                self.txt_emissao.setEnabled(True)
                self.txt_vencimento.setEnabled(True)
                self.comboFornecedor.setEnabled(True)
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
                self.comboFornecedor.setEnabled(True)
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
                consultarSQL = "SELECT * FROM contas WHERE idContas = %s"
                
                mycursor.execute(consultarSQL, (Controle.idConsulta,))
                myresult = mycursor.fetchone()  # Obtém o resultado como uma tupla

                nome = myresult[1]
                emissao = myresult[2]
                vencimento = myresult[3]
                fornecedor = myresult[4]
                observacao = myresult[5]
                valor = myresult[6]
                parcelas = myresult[7]
                formaDePagamento = myresult[8]
                situacao = myresult[9]

                self.txt_nome.setText(nome)
                self.txt_emissao.setText(emissao)
                self.txt_vencimento.setText(vencimento)
                self.textEdit.setText(observacao)
                self.txt_nome.setText(nome)
                self.txt_valor.setText(valor)
                self.txt_parcelas.setText(str(parcelas))
                self.comboFormaDePagamento.setCurrentText(formaDePagamento)
                self.comboSituacao.setCurrentText(situacao)

                mycursor.execute("SELECT `Razão Social` FROM fornecedor")
                fornecedores = mycursor.fetchall()
                
                # Adicionar todos os fornecedores à ComboBox
                for fornecedor_item in fornecedores:
                        self.comboFornecedor.addItem(fornecedor_item[0])
                
                # Definir o fornecedor atual na ComboBox
                self.comboFornecedor.setCurrentText(fornecedor)
                
                # Fechar o cursor e a conexão
                mycursor.close()
                mydb.close()
        
        elif Controle.tiposTelaDadosCliente == 'consultar':
                print('DadosContas:', Controle.tiposTelaDadosCliente)

                self.txt_nome.setEnabled(False)
                self.txt_emissao.setEnabled(False)
                self.txt_vencimento.setEnabled(False)
                self.comboFornecedor.setEnabled(False)
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
                SELECT Nome, Emissão, Vencimento, Fornecedor, Observação, Valor, Parcelas, `Forma de pagamento`, Situação
                FROM contas
                WHERE idContas = %s
                """

                mycursor.execute(consultaSql, (Controle.idConsulta,))
                myresult = mycursor.fetchall()

                df = pd.DataFrame(myresult, columns=["Nome", "Emissão", "Vencimento", "Fornecedor", "Observação", "Valor", "Parcelas", "Forma de pagamento", "Situação"])

                self.txt_nome.setText(str(df['Nome'][0]))
                self.txt_emissao.setText(str(df['Emissão'][0]))
                self.txt_vencimento.setText(str(df['Vencimento'][0]))
                fornecedor = str(df['Fornecedor'][0]) if not df.empty else ""
                self.textEdit.setText(str(df['Observação'][0]))
                self.txt_valor.setText(str(df['Valor'][0]))
                self.txt_parcelas.setText(str(df['Parcelas'][0]))

                formaDePagamento = str(df['Forma de pagamento'][0]) if not df.empty else ""
                situacao = str(df['Situação'][0]) if not df.empty else ""

                self.comboFornecedor.setCurrentText(fornecedor)
                self.comboFormaDePagamento.setCurrentText(formaDePagamento)
                self.comboSituacao.setCurrentText(situacao)


if __name__ == "__main__":
    app = QApplication([])
    frm_DadosContas = QWidget()
    ui = Ui_frm_DadosContas()
    ui.setupUi(frm_DadosContas)
    frm_DadosContas.show()
    app.exec()