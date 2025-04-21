from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget, QMessageBox)
import icon_addCarrinho
import icon_PagamentoV
import icon_voltarVenda
import icon_att
import icon_excluirCart

from frm_TelaPagamento import Ui_frm_TelaPagamento
from datetime import date

import os
import Controle
import mysql.connector
import pandas as pd

class Ui_Frm_Vendas(object):
    def setupUi(self, Frm_Vendas):
        if not Frm_Vendas.objectName():
            Frm_Vendas.setObjectName(u"Frm_Vendas")
        Frm_Vendas.setFixedSize(1302, 673)
        self.Frm_Vendas = Frm_Vendas
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        Frm_Vendas.setWindowIcon(QIcon(caminho_icone))
        Frm_Vendas.setStyleSheet(u"QWidget{\n"
"	background-color: #2E8B57;\n"
"}")
        self.label = QLabel(Frm_Vendas)
        self.Frm_Vendas.closeEvent = self.FecharTela
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 191, 21))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.label_2 = QLabel(Frm_Vendas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 0, 271, 81))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 65px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.comboProd = QComboBox(Frm_Vendas)
        self.comboProd.addItem("")
        self.comboProd.setObjectName(u"comboProd")
        self.comboProd.setGeometry(QRect(0, 90, 331, 41))
        self.comboProd.setStyleSheet(u"QComboBox {\n"
"    background-color: #2c3e50;\n"
"    color: #ecf0f1;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 18px;\n"
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
"\n"
"")
        self.label_3 = QLabel(Frm_Vendas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 121, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txtQtd = QLineEdit(Frm_Vendas)
        self.txtQtd.setObjectName(u"txtQtd")
        self.txtQtd.setGeometry(QRect(0, 180, 241, 41))
        self.txtQtd.setStyleSheet(u"QLineEdit {\n"
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
        self.label_4 = QLabel(Frm_Vendas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 150, 71, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txtValor = QLineEdit(Frm_Vendas)
        self.txtValor.setObjectName(u"txtValor")
        self.txtValor.setEnabled(False)
        self.txtValor.setGeometry(QRect(290, 180, 241, 41))
        self.txtValor.setStyleSheet(u"QLineEdit {\n"
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
        self.label_5 = QLabel(Frm_Vendas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 390, 141, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txtIdProduto = QLineEdit(Frm_Vendas)
        self.txtIdProduto.setObjectName(u"txtIdProduto")
        self.txtIdProduto.setEnabled(False)
        self.txtIdProduto.setGeometry(QRect(0, 420, 241, 41))
        self.txtIdProduto.setStyleSheet(u"QLineEdit {\n"
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
        self.label_6 = QLabel(Frm_Vendas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 390, 121, 21))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Qtd = QLineEdit(Frm_Vendas)
        self.txt_Qtd.setObjectName(u"txt_Qtd")
        self.txt_Qtd.setEnabled(False)
        self.txt_Qtd.setGeometry(QRect(290, 420, 241, 41))
        self.txt_Qtd.setStyleSheet(u"QLineEdit {\n"
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
        self.label_7 = QLabel(Frm_Vendas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 480, 81, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_idCliente = QLineEdit(Frm_Vendas)
        self.txt_idCliente.setObjectName(u"txt_idCliente")
        self.txt_idCliente.setEnabled(False)
        self.txt_idCliente.setGeometry(QRect(0, 510, 91, 41))
        self.txt_idCliente.setStyleSheet(u"QLineEdit {\n"
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
        self.label_8 = QLabel(Frm_Vendas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(830, 110, 191, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.btn_excluirCarrinho = QPushButton(Frm_Vendas)
        self.btn_excluirCarrinho.setObjectName(u"btn_excluirCarrinho")
        self.btn_excluirCarrinho.setGeometry(QRect(280, 280, 101, 71))
        self.btn_excluirCarrinho.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/exitCart/excluir carrinho.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_addCarrinho = QPushButton(Frm_Vendas)
        self.btn_addCarrinho.setObjectName(u"btn_addCarrinho")
        self.btn_addCarrinho.setGeometry(QRect(100, 280, 101, 71))
        self.btn_addCarrinho.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_addCart/adicionar-ao-carrinho (1).png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.carrinho = QTableWidget(Frm_Vendas)
        if (self.carrinho.columnCount() < 8):
            self.carrinho.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.carrinho.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.carrinho.setObjectName(u"carrinho")
        self.carrinho.setGeometry(QRect(600, 160, 701, 361))
        self.carrinho.setStyleSheet(u"QTableWidget, QTableView {\n"
"    border: 2px solid #C0C0C0;  \n"
"    border-radius: 8px;  \n"
"    gridline-color: #C0C0C0;  \n"
"    background-color: #FAFAFA;  \n"
"    font-size: 14px;  \n"
"    color: #333333;  \n"
"    selection-background-color: #FFD700;  \n"
"    selection-color: #000000;  \n"
"    alternate-background-color: #F5F5F5;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #EAEAEA;  \n"
"    color: #333333;  \n"
"    font-weight: bold;  \n"
"    border: 1px solid #C0C0C0;  \n"
"    padding: 6px;  \n"
"    border-radius: 4px;  \n"
"}\n"
"\n"
"QTableWidget::item:selected, QTableView::item:selected {\n"
"    background-color: #FFD700;  \n"
"    color: #000000;  \n"
"    border: 1px solid #C0C0C0;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #EAEAEA;  \n"
"    border: 1px solid #C0C0C0;  \n"
"    border-radius: 8px 0 0 0;\n"
"}\n"
"\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: #F0F0F0;  \n"
"    border: none;  \n"
"    border-radi"
                        "us: 6px;  \n"
"    margin: 2px;  \n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #B0BEC5;  \n"
"    border-radius: 6px;  \n"
"    min-height: 20px;  \n"
"    min-width: 20px;  \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {\n"
"    background: #90A4AE;  \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, \n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;  \n"
"    height: 0px;  \n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.frame = QFrame(Frm_Vendas)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(760, 540, 371, 111))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color:  #FFFFFF;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 201, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.lblQtd = QLabel(self.frame)
        self.lblQtd.setObjectName(u"lblQtd")
        self.lblQtd.setGeometry(QRect(250, 20, 111, 21))
        self.lblQtd.setFont(font)
        self.lblQtd.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color:  #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 60, 131, 21))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.lblValor = QLabel(self.frame)
        self.lblValor.setObjectName(u"lblValor")
        self.lblValor.setGeometry(QRect(250, 60, 111, 21))
        self.lblValor.setFont(font)
        self.lblValor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color:  #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.comboCliente = QComboBox(Frm_Vendas)
        self.comboCliente.addItem("")
        self.comboCliente.setObjectName(u"comboCliente")
        self.comboCliente.setGeometry(QRect(110, 510, 331, 41))
        self.comboCliente.setStyleSheet(u"QComboBox {\n"
"    background-color: #2c3e50;\n"
"    color: #ecf0f1;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 18px;\n"
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
        self.btn_pagamento = QPushButton(Frm_Vendas)
        self.btn_pagamento.setObjectName(u"btn_pagamento")
        self.btn_pagamento.setGeometry(QRect(50, 580, 381, 91))
        self.btn_pagamento.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_Pagar/forma-de-pagamento AA (2).png);\n"
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
"    background-color: #e8dfcf;\n"
"    border-color: #b39b8d;\n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.btn_atualizar = QPushButton(Frm_Vendas)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setGeometry(QRect(540, 200, 31, 31))
        self.btn_atualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_atualizar/atualizar (1).png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFFFFF;\n"
"    box-shadow: none; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}\n"
"")
        self.btn_voltar = QPushButton(Frm_Vendas)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(1210, 590, 91, 81))
        self.btn_voltar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_voltarVendas/retornar.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #83C5BE;\n"
"    box-shadow: none; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}")
        self.label_10 = QLabel(Frm_Vendas)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(540, 600, 131, 21))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txtQtd_2 = QLineEdit(Frm_Vendas)
        self.txtQtd_2.setObjectName(u"txtQtd_2")
        self.txtQtd_2.setEnabled(False)
        self.txtQtd_2.setGeometry(QRect(530, 630, 141, 41))
        self.txtQtd_2.setStyleSheet(u"QLineEdit {\n"
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

        self.retranslateUi(Frm_Vendas)

        QMetaObject.connectSlotsByName(Frm_Vendas)
    # setupUi

    def sairTela(self, Frm_Vendas):
        self.Frm_Vendas.close()
        self.Frm_Vendas = None

    def carregarComboBoxProduto(self):
        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT idProdutos, Nome, Valor FROM produtos")
        resultados = mycursor.fetchall()

        self.comboProd.clear()
        self.produtos_info = {} 

        for produtos_id, produtos_nome, produtos_valor in resultados:
                if produtos_valor is None:
                        produtos_valor = "0.00"
                else:
                        produtos_valor = str(produtos_valor).replace("R$", "").replace(",", ".").strip() 

                produtos_valor = float(produtos_valor)

                self.comboProd.addItem(produtos_nome, produtos_id)
                self.produtos_info[produtos_id] = produtos_valor

        self.comboProd.currentIndexChanged.connect(self.atualizarCampoProdutos)

        mycursor.close()
        mydb.close()

        if self.comboProd.count() > 0:
                self.comboProd.setCurrentIndex(0)
                self.atualizarCampoProdutos()

    def carregarComboBoxCliente(self):
        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT idCliente, Nome FROM cliente")
        resultados = mycursor.fetchall()

        self.comboCliente.clear()

        for clientes in resultados:
            print('Adicionando na comboBox')
            cliente_id, cliente_nome = clientes
            self.comboCliente.addItem(cliente_nome, cliente_id)

        self.comboCliente.currentIndexChanged.connect(self.atualizarCampoCliente)

        mycursor.close()
        mydb.close()

    def atualizarCampoCliente(self):
        
        self.atualizarTabela()
        cliente_id = self.comboCliente.currentData()
        if cliente_id:
            self.txt_idCliente.setText(str(cliente_id))
        else: 
            self.txt_idCliente.clear

    def atualizarCampoProdutos(self):
        produtos_id = self.comboProd.currentData()
        self.atualizarTabela()
        
        if produtos_id is not None:
                produtos_valor = self.produtos_info.get(produtos_id, 0.0)
                
                self.txtIdProduto.setText(str(produtos_id))
                self.txtValor.setText(f"R$ {produtos_valor:.2f}".replace(".", ","))
        else:
                self.txtValor.clear()
                self.txtIdProduto.clear()


    def adicionarAoCarrinho(self):
        produto = self.comboProd.currentText()
        data = self.txtQtd_2.text() #campo data
        quantidade = self.txtQtd.text()
        quantidadee = self.txt_Qtd.text()
        valor = self.txtValor.text().replace("R$", "").replace(",", ".").strip()
        idProduto = self.txtIdProduto.text()
        idCliente = self.txt_idCliente.text()
        cliente = self.comboCliente.currentText()

        quantidade = int(quantidade) if quantidade.isdigit() else 1
        valor = float(valor) if valor else 0.0
        total = valor

        campos_comuns = {
                "Valor": valor,
                "IdProduto": idProduto,
                "Quantidade": quantidade,
                "Quantidade2": quantidadee,
                "idCliente": idCliente,
                "data": data
        }

        campos_combo = {
                "Cliente": cliente,
                "Produto": produto
        }

        for campo, preenchido in campos_comuns.items():
                if not preenchido: 
                        msg = QMessageBox()
                        msg.setWindowTitle("ERRO!")
                        msg.setText(f"O campo '{campo}' é obrigatório e não pode ficar vazio!")
                        icon_path = r"C:\\Users\\Ariel\\PycharmProjects\\Scripts\\Sistema\\avsIcon.png"
                        msg.setWindowIcon(QIcon(icon_path))
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec()
                        return

        for campo, preenchido in campos_combo.items():
                if not preenchido:
                        msg = QMessageBox()
                        msg.setWindowTitle("ERRO!")
                        msg.setText(f"O campo '{campo}' deve estar preenchido!")
                        icon_path = r"C:\\Users\\Ariel\\PycharmProjects\\Scripts\\Sistema\\avsIcon.png"
                        msg.setWindowIcon(QIcon(icon_path))
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec()
                        return

        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )

        mycursor = mydb.cursor()
        sql = """
                INSERT INTO vendas 
                (`Produto`, `Data`, `Quantidade`, `Valor`, `IdProduto`, `IdCliente`, `Cliente`, `Total`) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (produto, data, quantidade, valor, idProduto, idCliente, cliente, total)
        mycursor.execute(sql, val)
        mydb.commit()

        self.carregarComboBoxCliente()
        self.carregarComboBoxProduto()
        self.atualizarTabela()
        
        print(mycursor.rowcount, 'Registro(s) inserido(s)')

        mycursor.close()
        mydb.close()

        self.txtQtd.setText("")
        self.txtValor.setText("")
        self.txtIdProduto.setText("")
        self.txt_idCliente.setText("")

        self.atualizarTot()

        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Produto adicionado com sucesso!")
        icon_path = r"C:\\Users\\Ariel\\PycharmProjects\\Scripts\\Sistema\\avsIcon.png"
        msg.setWindowIcon(QIcon(icon_path))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def configurarSincronizaçãoQtd(self):
         self.txtQtd.textChanged.connect(self.sincronizarQtd)

    def sincronizarQtd(self):
         quantidade = self.txtQtd.text()
         self.txt_Qtd.setText(quantidade)

    def atualizarTabela(self):
         mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
         mycursor = mydb.cursor()
         mycursor.execute("SELECT * FROM vendas")
         resultados = mycursor.fetchall()

         self.carrinho.setRowCount(0)

         for linha1, linhaD in enumerate(resultados):
              self.carrinho.insertRow(linha1)
              for coluna, dado in enumerate (linhaD):
                   self.carrinho.setItem(linha1, coluna, QTableWidgetItem(str(dado)))

    def atualizarTot(self):

         total = 0.0
         totalqtd = 0
         for linha in range(self.carrinho.rowCount()):
              item = self.carrinho.item(linha, 7)
              quantidade = self.carrinho.item(linha, 2)
              print(f"Linha {linha}: Preço = {item.text() if item else 'None'}, Quantidade = {quantidade.text() if quantidade else 'None'}")
              if item and quantidade:
                   precouni = float(item.text().replace(',', '.').replace('R$', '').strip())
                   qtd = int(quantidade.text().strip())
                   totalqtd += qtd
                   total += precouni * qtd
                   Controle.totalDaVenda = total
                   Controle.totalItens = totalqtd
                   print(Controle.totalDaVenda)
                  

         self.lblValor.setText(f"R$ {total:,.2f}")
         self.lblQtd.setText(str(totalqtd))
         print(f"Total calculado: R$ {total:.2f}")

    def excluirDaTabela(self):
         line = self.carrinho.currentRow()

         if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('Por favor, selecione um item para excluir.')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 

         item = self.carrinho.item(line, 0)

         if item:
              produto = item.text()
              mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
              mycursor = mydb.cursor()
              sql = "DELETE FROM vendas WHERE Produto = %s"
              mycursor.execute(sql, (produto,))
              mydb.commit()

              msg = QMessageBox()
              msg.setWindowTitle('Produto excluído')
              msg.setText('Produto excluído com sucesso!')
              msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
              msg.setIcon(QMessageBox.Information)
              msg.setStandardButtons(QMessageBox.Ok)
              msg.exec()

              mycursor.execute("SELECT * FROM vendas")
              myresult = mycursor.fetchall()
              df = pd.DataFrame(myresult, columns=['Produto', 'Quantidade', 'Valor', 'IdProduto', 'IdCliente', 'Cliente', 'Total'])
              self.all_data = df

              numRows = len(self.all_data.index)
              self.carrinho.setColumnCount(len(self.all_data.columns))
              self.carrinho.setRowCount(numRows)
              self.carrinho.setHorizontalHeaderLabels(self.all_data.columns)

              for i in range(numRows):
                   for j in range(len(self.all_data.columns)):
                        self.carrinho.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

              self.carrinho.resizeColumnsToContents()

              for row in range(self.carrinho.rowCount()):
                   self.carrinho.resizeRowsToContents()

              mydb.close()

         else:
    
              msg = QMessageBox()
              msg.setWindowTitle('Erro seleção')
              msg.setText('Produto não selecionado!')
              msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
              msg.setIcon(QMessageBox.Warning)
              msg.setStandardButtons(QMessageBox.Ok)
              msg.exec()

    def excluirDaTabela(self):
         line = self.carrinho.currentRow()

         if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('Por favor, selecione um item para excluir.')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 

         item = self.carrinho.item(line, 0)

         if item:
              produto = item.text()
              mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
              mycursor = mydb.cursor()
              sql = "DELETE FROM vendas WHERE Produto = %s"
              mycursor.execute(sql, (produto,))
              mydb.commit()

              msg = QMessageBox()
              msg.setWindowTitle('Produto excluído')
              msg.setText('Produto excluído com sucesso!')
              msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
              msg.setIcon(QMessageBox.Information)
              msg.setStandardButtons(QMessageBox.Ok)
              msg.exec()

              mycursor.execute("SELECT * FROM vendas")
              myresult = mycursor.fetchall()
              df = pd.DataFrame(myresult, columns=['Produto', 'Data', 'Quantidade', 'Valor', 'IdProduto', 'IdCliente', 'Cliente', 'Total'])
              self.all_data = df

              numRows = len(self.all_data.index)
              self.carrinho.setColumnCount(len(self.all_data.columns))
              self.carrinho.setRowCount(numRows)
              self.carrinho.setHorizontalHeaderLabels(self.all_data.columns)

              for i in range(numRows):
                   for j in range(len(self.all_data.columns)):
                        self.carrinho.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

              self.carrinho.resizeColumnsToContents()

              for row in range(self.carrinho.rowCount()):
                   self.carrinho.resizeRowsToContents()

              mydb.close()

         else:
    
              msg = QMessageBox()
              msg.setWindowTitle('Erro seleção')
              msg.setText('Produto não selecionado!')
              msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
              msg.setIcon(QMessageBox.Warning)
              msg.setStandardButtons(QMessageBox.Ok)
              msg.exec()

    def FecharTela(self, event):
        resposta = QMessageBox(self.Frm_Vendas)
        resposta.setWindowTitle('Fechar o PDV')
        resposta.setText('Deseja fechar o PDV e limpar o carrinho?')
        resposta.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
        resposta.setIcon(QMessageBox.Warning)
        resposta.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        resposta.exec()

        if resposta.clickedButton() == resposta.button(QMessageBox.Yes):
                mydb = mysql.connector.connect(
                        host=Controle.host,
                        user=Controle.user,
                        password=Controle.password,
                        database=Controle.database
                )
                mycursor = mydb.cursor()
                mycursor.execute("DELETE FROM vendas")
                mydb.commit()
                
                print('Banco de dados e carrinho limpos com sucesso!')
                event.accept()
        else:
                event.ignore()

    def pagamentoTela(self):
         if not hasattr(self, 'frm_TelaPagamento') or self.frm_TelaPagamento is None or not self.frm_TelaPagamento.isVisible():
                self.frm_TelaPagamento = QWidget()
                self.ui = Ui_frm_TelaPagamento()
                self.ui.setupUi(self.frm_TelaPagamento)

                self.frm_TelaPagamento.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_TelaPagamento.destroyed.connect(lambda: setattr(self, 'frm_TelaPagamento', None))

                self.frm_TelaPagamento.show()

         else: 
               self.frm_TelaPagamento.raise_()
               self.frm_TelaPagamento.activateWindow()

    def atualizarDados(self, cliente_id=None):
        self.carregarComboBoxCliente()
        self.carregarComboBoxProduto()

        data = date.today()
        self.txtQtd_2.setText(f'{data.strftime("%Y/%m/%d")}') 

        if cliente_id is not None:
                index = self.comboCliente.findData(cliente_id)
                if index != -1:
                        self.comboCliente.setCurrentIndex(index)
        else:
                if self.comboCliente.count() > 0:
                        self.comboCliente.setCurrentIndex(0)

    def retranslateUi(self, Frm_Vendas):
        Frm_Vendas.setWindowTitle(QCoreApplication.translate("Frm_Vendas", u"Vendas", None))
        self.label.setText(QCoreApplication.translate("Frm_Vendas", u"NOME DO PRODUTO: ", None))
        self.label_2.setText(QCoreApplication.translate("Frm_Vendas", u"VENDAS", None))
        self.comboProd.setItemText(0, QCoreApplication.translate("Frm_Vendas", u"Nenhum selecionado", None))

        self.label_3.setText(QCoreApplication.translate("Frm_Vendas", u"QUANTIDADE:", None))
        self.label_4.setText(QCoreApplication.translate("Frm_Vendas", u"VALOR:", None))
        self.label_5.setText(QCoreApplication.translate("Frm_Vendas", u"ID DO PRODUTO:", None))
        self.label_6.setText(QCoreApplication.translate("Frm_Vendas", u"QUANTIDADE:", None))
        self.label_7.setText(QCoreApplication.translate("Frm_Vendas", u"CLIENTE:", None))
        self.label_8.setText(QCoreApplication.translate("Frm_Vendas", u"CARRINHO:", None))
        self.btn_excluirCarrinho.setText("")
        self.btn_addCarrinho.setText("")
        ___qtablewidgetitem = self.carrinho.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frm_Vendas", u"Produto", None));
        ___qtablewidgetitem1 = self.carrinho.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frm_Vendas", u"Data", None));
        ___qtablewidgetitem2 = self.carrinho.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frm_Vendas", u"Quantidade", None));
        ___qtablewidgetitem3 = self.carrinho.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frm_Vendas", u"Valor", None));
        ___qtablewidgetitem4 = self.carrinho.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frm_Vendas", u"IdProduto", None));
        ___qtablewidgetitem5 = self.carrinho.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frm_Vendas", u"IdCliente", None));
        ___qtablewidgetitem6 = self.carrinho.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frm_Vendas", u"Cliente", None));
        ___qtablewidgetitem7 = self.carrinho.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Frm_Vendas", u"Total", None));
        self.label_9.setText(QCoreApplication.translate("Frm_Vendas", u"QUANTIDADE DE ITENS:", None))
        self.lblQtd.setText(QCoreApplication.translate("Frm_Vendas", u"0000000", None))
        self.label_11.setText(QCoreApplication.translate("Frm_Vendas", u"VALOR TOTAL:", None))
        self.lblValor.setText(QCoreApplication.translate("Frm_Vendas", u"0000000", None))
        self.comboCliente.setItemText(0, QCoreApplication.translate("Frm_Vendas", u"Nenhum selecionado", None))

        self.btn_pagamento.setText("")
        self.btn_atualizar.setText("")
        self.btn_voltar.setText("")
        self.label_10.setText(QCoreApplication.translate("Frm_Vendas", u"Data da venda:", None))
    # retranslateUi
        	
        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_atualizar.clicked.connect(self.carregarComboBoxProduto)
        self.btn_atualizar.clicked.connect(self.carregarComboBoxCliente)
        self.btn_atualizar.clicked.connect(self.atualizarDados)
        self.btn_addCarrinho.clicked.connect(self.adicionarAoCarrinho)
        self.btn_excluirCarrinho.clicked.connect(self.excluirDaTabela)
        self.btn_pagamento.clicked.connect(self.pagamentoTela)

        self.configurarSincronizaçãoQtd()

if __name__ == "__main__":
    app = QApplication([])
    frm_Vendas = QWidget()
    ui = Ui_Frm_Vendas()
    ui.setupUi(frm_Vendas)
    frm_Vendas.show()
    app.exec()