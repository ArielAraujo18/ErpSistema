from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QMessageBox)

import icon_adiconarCarrinho
import icon_removerCarrinho

#from frm_TelaPagamento import Ui_frm_TelaPagamento
from datetime import date

import os
import Controle
import mysql.connector
import pandas as pd

class Ui_frm_Vendas(object):
    def setupUi(self, frm_Vendas):
        if not frm_Vendas.objectName():
            frm_Vendas.setObjectName(u"frm_Vendas")
        frm_Vendas.resize(1250, 678)
        self.frm_Vendas = frm_Vendas
        frm_Vendas.setStyleSheet(u"background-color: #2c2c2c;")
        self.gridLayout = QGridLayout(frm_Vendas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(frm_Vendas)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label)

        self.comboProd = QComboBox(self.widget_7)
        self.comboProd.addItem("")
        self.comboProd.setObjectName(u"comboProd")
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

        self.horizontalLayout_3.addWidget(self.comboProd)


        self.horizontalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.txt_idProd = QLineEdit(self.widget_8)
        self.txt_idProd.setObjectName(u"txt_idProd")
        self.txt_idProd.setEnabled(False)
        self.txt_idProd.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_4.addWidget(self.txt_idProd)


        self.horizontalLayout_2.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignVCenter)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.txtQtd = QLineEdit(self.widget_9)
        self.txtQtd.setObjectName(u"txtQtd")
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

        self.horizontalLayout_8.addWidget(self.txtQtd)


        self.horizontalLayout_5.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.txtValor = QLineEdit(self.widget_10)
        self.txtValor.setObjectName(u"txtValor")
        self.txtValor.setEnabled(False)
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

        self.horizontalLayout_7.addWidget(self.txtValor)


        self.horizontalLayout_5.addWidget(self.widget_10)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.widget_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.txt_idCliente = QLineEdit(self.widget_16)
        self.txt_idCliente.setObjectName(u"txt_idCliente")
        self.txt_idCliente.setEnabled(False)
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

        self.horizontalLayout_11.addWidget(self.txt_idCliente, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_11)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_7 = QLabel(self.widget_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.comboCliente = QComboBox(self.widget_17)
        self.comboCliente.addItem("")
        self.comboCliente.setObjectName(u"comboCliente")
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

        self.horizontalLayout_13.addWidget(self.comboCliente)


        self.horizontalLayout_10.addWidget(self.widget_17)


        self.horizontalLayout_9.addWidget(self.widget_11)

        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_10)

        self.txtDataVenda = QLineEdit(self.frame)
        self.txtDataVenda.setObjectName(u"txtDataVenda")
        self.txtDataVenda.setEnabled(False)
        self.txtDataVenda.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_14.addWidget(self.txtDataVenda)


        self.horizontalLayout_9.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_2 = QVBoxLayout(self.widget_14)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.verticalLayout_2.addWidget(self.label_13)


        self.horizontalLayout_12.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_3 = QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lblQtd_2 = QLabel(self.widget_15)
        self.lblQtd_2.setObjectName(u"lblQtd_2")
        self.lblQtd_2.setFont(font)
        self.lblQtd_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.verticalLayout_3.addWidget(self.lblQtd_2)

        self.lblValor_2 = QLabel(self.widget_15)
        self.lblValor_2.setObjectName(u"lblValor_2")
        self.lblValor_2.setFont(font)
        self.lblValor_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")

        self.verticalLayout_3.addWidget(self.lblValor_2)


        self.horizontalLayout_12.addWidget(self.widget_15)


        self.horizontalLayout.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_addCarrinho = QPushButton(self.widget_13)
        self.btn_addCarrinho.setObjectName(u"btn_addCarrinho")
        self.btn_addCarrinho.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_adicionarCarrinho/adicionarCarrinho.png);\n"
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

        self.horizontalLayout_15.addWidget(self.btn_addCarrinho)

        self.btn_excluirCarrinho = QPushButton(self.widget_13)
        self.btn_excluirCarrinho.setObjectName(u"btn_excluirCarrinho")
        self.btn_excluirCarrinho.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_removerCarrinho/RemoverCarrinho.png);\n"
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

        self.horizontalLayout_15.addWidget(self.btn_excluirCarrinho)


        self.horizontalLayout.addWidget(self.widget_13)


        self.verticalLayout.addWidget(self.widget_6)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget = QWidget(frm_Vendas)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.carrinho = QTableWidget(self.widget)
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

        self.horizontalLayout_6.addWidget(self.carrinho)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)


        self.retranslateUi(frm_Vendas)

        QMetaObject.connectSlotsByName(frm_Vendas)
    # setupUi
    def sairTela(self, frm_Vendas):
        self.frm_Vendas.close()
        self.frm_Vendas = None

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
        """
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
        """

    def retranslateUi(self, frm_Vendas):
        frm_Vendas.setWindowTitle(QCoreApplication.translate("frm_Vendas", u"VENDAS (PDV)", None))
        self.label.setText(QCoreApplication.translate("frm_Vendas", u"NOME DO PRODUTO: ", None))
        self.comboProd.setItemText(0, QCoreApplication.translate("frm_Vendas", u"Nenhum selecionado", None))

        self.label_6.setText(QCoreApplication.translate("frm_Vendas", u"ID DO PRODUTO:", None))
        self.label_4.setText(QCoreApplication.translate("frm_Vendas", u"QUANTIDADE:", None))
        self.label_5.setText(QCoreApplication.translate("frm_Vendas", u"VALOR:", None))
        self.label_8.setText(QCoreApplication.translate("frm_Vendas", u"ID CLIENTE:", None))
        self.label_7.setText(QCoreApplication.translate("frm_Vendas", u"CLIENTE:", None))
        self.comboCliente.setItemText(0, QCoreApplication.translate("frm_Vendas", u"Nenhum selecionado", None))

        self.label_10.setText(QCoreApplication.translate("frm_Vendas", u"Data da venda:", None))
        self.label_12.setText(QCoreApplication.translate("frm_Vendas", u"QUANTIDADE DE ITENS:", None))
        self.label_13.setText(QCoreApplication.translate("frm_Vendas", u"VALOR TOTAL:", None))
        self.lblQtd_2.setText(QCoreApplication.translate("frm_Vendas", u"0000000", None))
        self.lblValor_2.setText(QCoreApplication.translate("frm_Vendas", u"0000000", None))
        self.btn_addCarrinho.setText(QCoreApplication.translate("frm_Vendas", u"\n"
"\u3164\u3164\u3164\u3164\n"
"\u3164\u3164", None))
        self.btn_excluirCarrinho.setText(QCoreApplication.translate("frm_Vendas", u"\u3164\u3164\n"
"\u3164\u3164\n"
"\u3164\u3164", None))
        ___qtablewidgetitem = self.carrinho.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Vendas", u"Produto", None));
        ___qtablewidgetitem1 = self.carrinho.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Vendas", u"Data", None));
        ___qtablewidgetitem2 = self.carrinho.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Vendas", u"Quantidade", None));
        ___qtablewidgetitem3 = self.carrinho.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Vendas", u"Valor", None));
        ___qtablewidgetitem4 = self.carrinho.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Vendas", u"IdProduto", None));
        ___qtablewidgetitem5 = self.carrinho.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_Vendas", u"IdCliente", None));
        ___qtablewidgetitem6 = self.carrinho.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_Vendas", u"Cliente", None));
        ___qtablewidgetitem7 = self.carrinho.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_Vendas", u"Total", None));
        # retranslateUi

        #self.btn_voltar.clicked.connect(self.sairTela)
        #self.btn_atualizar.clicked.connect(self.carregarComboBoxProduto)
        #self.btn_atualizar.clicked.connect(self.carregarComboBoxCliente)
        #self.btn_atualizar.clicked.connect(self.atualizarDados)
        self.carregarComboBoxCliente()
        self.carregarComboBoxProduto()
        self.btn_addCarrinho.clicked.connect(self.adicionarAoCarrinho)
        self.btn_excluirCarrinho.clicked.connect(self.excluirDaTabela)
        #self.btn_pagamento.clicked.connect(self.pagamentoTela)

if __name__ == "__main__":
    app = QApplication([])
    frm_Vendas = QWidget()
    ui = Ui_frm_Vendas()
    ui.setupUi(frm_Vendas)
    frm_Vendas.show()
    app.exec()