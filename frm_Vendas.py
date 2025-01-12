from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)


import mysql.connector
import pandas as pd


import icon_addCarrinho
import icon_voltarVenda
import icon_att
import icon_pagamento
import icon_excluirCart

class Ui_Frm_Vendas(object):
    def setupUi(self, Frm_Vendas):
        if not Frm_Vendas.objectName():
            Frm_Vendas.setObjectName(u"Frm_Vendas")
        Frm_Vendas.setFixedSize(1422, 739)
        self.Frm_Vendas = Frm_Vendas
        Frm_Vendas.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        Frm_Vendas.setStyleSheet(u"QWidget{\n"
"	background-color: #2E8B57;\n"
"}")
        self.label = QLabel(Frm_Vendas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 191, 21))
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
        self.label_2.setGeometry(QRect(560, 10, 271, 81))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 65px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.comboProd = QComboBox(Frm_Vendas)
        self.comboProd.setObjectName(u"comboProd")
        self.comboProd.setGeometry(QRect(0, 110, 701, 31))
        self.comboProd.setStyleSheet(u"QComboBox {\n"
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
"\n"
"")
        self.label_3 = QLabel(Frm_Vendas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 121, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txtQtd = QLineEdit(Frm_Vendas)
        self.txtQtd.setObjectName(u"txtQtd")
        self.txtQtd.setGeometry(QRect(0, 200, 241, 41))
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
        self.label_4.setGeometry(QRect(290, 170, 71, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txtValor = QLineEdit(Frm_Vendas)
        self.txtValor.setObjectName(u"txtValor")
        self.txtValor.setGeometry(QRect(290, 200, 241, 41))
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
        self.label_5.setGeometry(QRect(10, 410, 141, 21))
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
        self.txtIdProduto.setGeometry(QRect(0, 440, 241, 41))
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
        self.label_6.setGeometry(QRect(290, 410, 121, 21))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Qtd = QLineEdit(Frm_Vendas)
        self.txt_Qtd.setObjectName(u"txt_Qtd")
        self.txt_Qtd.setEnabled(True)
        self.txt_Qtd.setGeometry(QRect(290, 440, 241, 41))
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
        self.label_7.setGeometry(QRect(10, 500, 81, 21))
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
        self.txt_idCliente.setGeometry(QRect(0, 530, 91, 41))
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
        self.label_8.setGeometry(QRect(980, 100, 191, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.btn_excluirCarrinho = QPushButton(Frm_Vendas)
        self.btn_excluirCarrinho.setObjectName(u"btn_excluirCarrinho")
        self.btn_excluirCarrinho.setGeometry(QRect(280, 300, 101, 71))
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
        self.btn_addCarrinho.setGeometry(QRect(100, 300, 101, 71))
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
        if (self.carrinho.columnCount() < 7):
            self.carrinho.setColumnCount(7)
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
        self.carrinho.setObjectName(u"carrinho")
        self.carrinho.setGeometry(QRect(720, 160, 701, 361))
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
        self.frame.setGeometry(QRect(900, 550, 371, 111))
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
        self.comboCliente.setObjectName(u"comboCliente")
        self.comboCliente.setGeometry(QRect(100, 530, 511, 41))
        self.comboCliente.setStyleSheet(u"QComboBox {\n"
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
        self.btn_pagamento = QPushButton(Frm_Vendas)
        self.btn_pagamento.setObjectName(u"btn_pagamento")
        self.btn_pagamento.setGeometry(QRect(120, 600, 381, 121))
        self.btn_pagamento.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/iconPagar/forma-de-pagamento AA (2).png);\n"
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
        self.btn_atualizar.setGeometry(QRect(560, 200, 31, 31))
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
        self.btn_voltar.setGeometry(QRect(1330, 660, 91, 81))
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

        self.retranslateUi(Frm_Vendas)

        QMetaObject.connectSlotsByName(Frm_Vendas)
    # setupUi

    ##Funções

    def sairTela(self, Frm_Vendas):
        self.Frm_Vendas.close()
        self.Frm_Vendas = None

    def carregarComboBoxProduto(self):
        mydb = mysql.connector.connect(
                host='localhost',
                user='Ariel',
                password='IRani18@#',
                database='sistema'
                )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT idProdutos, Nome FROM produtos")
        resultados = mycursor.fetchall()

        self.comboProd.clear()

        #Adicionando os produtos na combobox
        for produtos in resultados:
            print('Adicionando na combobox')
            produtos_id, produtos_nome = produtos
            self.comboProd.addItem(produtos_nome, produtos_id)

        #Atualiza o line Edit do produto para mudar de acordo com o produto selecionado
        self.comboProd.currentIndexChanged.connect(self.atualizarCampoProdutos)

        mycursor.close()
        mydb.close()

    def carregarComboBoxCliente(self):
        mydb = mysql.connector.connect(
                host='localhost',
                user='Ariel',
                password='IRani18@#',
                database='sistema'
        )
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT idCliente, Nome FROM cliente")
        resultados = mycursor.fetchall()

        self.comboCliente.clear()

        for clientes in resultados:
            print('Adicionando na comboBox')
            cliente_id, cliente_nome = clientes
            self.comboCliente.addItem(cliente_nome, cliente_id)

        #Atualizar o LineEdit do cliente para mudar de acordo com o cliente selecionado
        self.comboCliente.currentIndexChanged.connect(self.atualizarCampoCliente)

        mycursor.close()
        mydb.close()

    def atualizarCampoCliente(self):
        
        #Retorna o dado Oculto 
        cliente_id = self.comboCliente.currentData()
        if cliente_id:
            self.txt_idCliente.setText(str(cliente_id))
        else: 
            self.txt_idCliente.clear

    def atualizarCampoProdutos(self):
        produtos_id = self.comboProd.currentData()
        if produtos_id:
            self.txtIdProduto.setText(str(produtos_id))
        else:
            self.txtIdProduto.clear


    def retranslateUi(self, Frm_Vendas):
        Frm_Vendas.setWindowTitle(QCoreApplication.translate("Frm_Vendas", u"Vendas", None))
        self.label.setText(QCoreApplication.translate("Frm_Vendas", u"NOME DO PRODUTO: ", None))
        self.label_2.setText(QCoreApplication.translate("Frm_Vendas", u"VENDAS", None))
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
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frm_Vendas", u"Quantidade", None));
        ___qtablewidgetitem2 = self.carrinho.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frm_Vendas", u"Valor", None));
        ___qtablewidgetitem3 = self.carrinho.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frm_Vendas", u"IdProduto", None));
        ___qtablewidgetitem4 = self.carrinho.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frm_Vendas", u"IdCliente", None));
        ___qtablewidgetitem5 = self.carrinho.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frm_Vendas", u"Cliente", None));
        ___qtablewidgetitem6 = self.carrinho.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frm_Vendas", u"Total", None));
        self.label_9.setText(QCoreApplication.translate("Frm_Vendas", u"QUANTIDADE DE ITENS:", None))
        self.lblQtd.setText(QCoreApplication.translate("Frm_Vendas", u"0000000", None))
        self.label_11.setText(QCoreApplication.translate("Frm_Vendas", u"VALOR TOTAL:", None))
        self.lblValor.setText(QCoreApplication.translate("Frm_Vendas", u"0000000", None))
        self.btn_pagamento.setText("")
        self.btn_atualizar.setText("")
        self.btn_voltar.setText("")
    # retranslateUi

        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_atualizar.clicked.connect(self.carregarComboBoxProduto)
        self.btn_atualizar.clicked.connect(self.carregarComboBoxCliente)


if __name__ == "__main__":
    app = QApplication([])
    frm_Vendas = QWidget()
    ui = Ui_Frm_Vendas()
    ui.setupUi(frm_Vendas)
    frm_Vendas.show()
    app.exec()
