from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox)

import icon_consultadiaria


class Ui_frm_Bancos(object):
    def setupUi(self, frm_Bancos):
        if not frm_Bancos.objectName():
            frm_Bancos.setObjectName(u"frm_Bancos")
        frm_Bancos.resize(1045, 660)
        frm_Bancos.setStyleSheet(u"background-color: #2c2c2c;")
        self.verticalLayout = QVBoxLayout(frm_Bancos)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(frm_Bancos)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_4 = QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableGastos = QTableWidget(self.widget_10)
        if (self.tableGastos.columnCount() < 5):
            self.tableGastos.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableGastos.setObjectName(u"tableGastos")
        self.tableGastos.setStyleSheet(u"QTableWidget, QTableView {\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 5px; \n"
"    gridline-color: #dcdcdc; \n"
"    background-color: #ffffff; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; \n"
"    color: #333333;\n"
"    font-weight: bold; \n"
"    border: 1px solid #dcdcdc; \n"
"    padding: 4px; \n"
"}\n"
"\n"
"QTableWidget::item:selected, QTableView::item:selected {\n"
"    background-color: #b3d9ff; \n"
"    color: #000000;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f0f0f0; \n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #f0f0f0;\n"
"    width: 12px; \n"
"    margin: 2px 0 2px 0; \n"
"    border: none; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #b0bec5; \n"
"    min-height: 20px; \n"
"    border-radius: 6px; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar:"
                        ":add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; \n"
"    height: 0px; \n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; \n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #f0f0f0; \n"
"    height: 12px; \n"
"    margin: 0 2px 0 2px; \n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #b0bec5;\n"
"    min-width: 20px; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.tableGastos)


        self.verticalLayout_3.addWidget(self.widget_10)


        self.horizontalLayout.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_17 = QVBoxLayout(self.widget_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_20 = QWidget(self.widget_7)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_2 = QVBoxLayout(self.widget_20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_18 = QVBoxLayout(self.widget_21)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_4 = QLabel(self.widget_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_22)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_2.addWidget(self.widget_22)


        self.verticalLayout_17.addWidget(self.widget_20)

        self.widget_19 = QWidget(self.widget_7)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_16 = QVBoxLayout(self.widget_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_consultaD = QPushButton(self.widget_19)
        self.btn_consultaD.setObjectName(u"btn_consultaD")
        self.btn_consultaD.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #000000;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_consulta/consulta.png); \n"
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

        self.verticalLayout_16.addWidget(self.btn_consultaD, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.widget_19)


        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_6 = QVBoxLayout(self.widget_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableLucros = QTableWidget(self.widget_12)
        if (self.tableLucros.columnCount() < 5):
            self.tableLucros.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableLucros.setObjectName(u"tableLucros")
        self.tableLucros.setStyleSheet(u"QTableWidget, QTableView {\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 5px; \n"
"    gridline-color: #dcdcdc; \n"
"    background-color: #ffffff; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; \n"
"    color: #333333;\n"
"    font-weight: bold; \n"
"    border: 1px solid #dcdcdc; \n"
"    padding: 4px; \n"
"}\n"
"\n"
"QTableWidget::item:selected, QTableView::item:selected {\n"
"    background-color: #b3d9ff; \n"
"    color: #000000;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f0f0f0; \n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #f0f0f0;\n"
"    width: 12px; \n"
"    margin: 2px 0 2px 0; \n"
"    border: none; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #b0bec5; \n"
"    min-height: 20px; \n"
"    border-radius: 6px; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar:"
                        ":add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; \n"
"    height: 0px; \n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; \n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #f0f0f0; \n"
"    height: 12px; \n"
"    margin: 0 2px 0 2px; \n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #b0bec5;\n"
"    min-width: 20px; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.tableLucros)


        self.verticalLayout_5.addWidget(self.widget_12)


        self.horizontalLayout.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(frm_Bancos)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_4)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_8 = QVBoxLayout(self.widget_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_SomaGastos = QLabel(self.widget_14)
        self.label_SomaGastos.setObjectName(u"label_SomaGastos")
        self.label_SomaGastos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.label_SomaGastos, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.widget_14)

        self.widget_13 = QWidget(self.widget_4)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_13 = QVBoxLayout(self.widget_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.txt_gastos = QLineEdit(self.widget_13)
        self.txt_gastos.setObjectName(u"txt_gastos")
        self.txt_gastos.setEnabled(False)
        self.txt_gastos.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_13.addWidget(self.txt_gastos)


        self.verticalLayout_7.addWidget(self.widget_13)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_3)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_12 = QVBoxLayout(self.widget_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_SomaGastos_3 = QLabel(self.widget_16)
        self.label_SomaGastos_3.setObjectName(u"label_SomaGastos_3")
        self.label_SomaGastos_3.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.label_SomaGastos_3, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_11.addWidget(self.widget_16)

        self.widget_15 = QWidget(self.widget_3)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_14 = QVBoxLayout(self.widget_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.txt_total = QLineEdit(self.widget_15)
        self.txt_total.setObjectName(u"txt_total")
        self.txt_total.setEnabled(False)
        self.txt_total.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_14.addWidget(self.txt_total)


        self.verticalLayout_11.addWidget(self.widget_15)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.widget_5)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_10 = QVBoxLayout(self.widget_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_SomaGastos_2 = QLabel(self.widget_18)
        self.label_SomaGastos_2.setObjectName(u"label_SomaGastos_2")
        self.label_SomaGastos_2.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.label_SomaGastos_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.widget_18, 0, Qt.AlignBottom)

        self.widget_17 = QWidget(self.widget_5)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_15 = QVBoxLayout(self.widget_17)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.txt_rendimentos = QLineEdit(self.widget_17)
        self.txt_rendimentos.setObjectName(u"txt_rendimentos")
        self.txt_rendimentos.setEnabled(False)
        self.txt_rendimentos.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_15.addWidget(self.txt_rendimentos)


        self.verticalLayout_9.addWidget(self.widget_17)


        self.horizontalLayout_2.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(frm_Bancos)

        QMetaObject.connectSlotsByName(frm_Bancos)
    # setupUi

    def retranslateUi(self, frm_Bancos):
        frm_Bancos.setWindowTitle(QCoreApplication.translate("frm_Bancos", u"Bancos", None))
        self.label_2.setText(QCoreApplication.translate("frm_Bancos", u"DESPESAS", None))
        ___qtablewidgetitem = self.tableGastos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Bancos", u"Nome", None));
        ___qtablewidgetitem1 = self.tableGastos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Bancos", u"Fornecedor", None));
        ___qtablewidgetitem2 = self.tableGastos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Bancos", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem3 = self.tableGastos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Bancos", u"Quantidade", None));
        ___qtablewidgetitem4 = self.tableGastos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Bancos", u"Valor", None));
        self.label_4.setText(QCoreApplication.translate("frm_Bancos", u"BANCOS", None))
        self.btn_consultaD.setText(QCoreApplication.translate("frm_Bancos", u"\u3164\u3164\n"
"\u3164\u3164\n"
"", None))
        self.label_3.setText(QCoreApplication.translate("frm_Bancos", u"RENDIMENTOS", None))
        ___qtablewidgetitem5 = self.tableLucros.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_Bancos", u"Nome", None));
        ___qtablewidgetitem6 = self.tableLucros.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_Bancos", u"Fornecedor", None));
        ___qtablewidgetitem7 = self.tableLucros.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_Bancos", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem8 = self.tableLucros.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_Bancos", u"Quantidade", None));
        ___qtablewidgetitem9 = self.tableLucros.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("frm_Bancos", u"Valor", None));
        self.label_SomaGastos.setText(QCoreApplication.translate("frm_Bancos", u"Soma dos gastos:", None))
        self.label_SomaGastos_3.setText(QCoreApplication.translate("frm_Bancos", u"Soma dos gastos:", None))
        self.label_SomaGastos_2.setText(QCoreApplication.translate("frm_Bancos", u"Soma dos gastos:", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_Bancos = QWidget()
    ui = Ui_frm_Bancos()
    ui.setupUi(frm_Bancos)
    frm_Bancos.show()
    app.exec()
    
    
