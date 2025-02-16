from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Frm_Bancos(object):
    def setupUi(self, Frm_Bancos):
        if not Frm_Bancos.objectName():
            Frm_Bancos.setObjectName(u"Frm_Bancos")
        Frm_Bancos.setFixedSize(1254, 860)
        self.frm_Bancos = frm_Bancos
        frm_Bancos.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        Frm_Bancos.setStyleSheet(u"QWidget {\n"
"    background-color: #FA8072;\n"
"    border-radius: 8px;\n"
"}")
        self.label_Bancos = QLabel(Frm_Bancos)
        self.label_Bancos.setObjectName(u"label_Bancos")
        self.label_Bancos.setGeometry(QRect(590, 20, 141, 31))
        self.label_Bancos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.label_Gastos = QLabel(Frm_Bancos)
        self.label_Gastos.setObjectName(u"label_Gastos")
        self.label_Gastos.setGeometry(QRect(200, 180, 151, 31))
        self.label_Gastos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.labe_Lucros = QLabel(Frm_Bancos)
        self.labe_Lucros.setObjectName(u"labe_Lucros")
        self.labe_Lucros.setGeometry(QRect(910, 180, 151, 31))
        self.labe_Lucros.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.tableLucros = QTableWidget(Frm_Bancos)
        if (self.tableLucros.columnCount() < 4):
            self.tableLucros.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableLucros.setObjectName(u"tableLucros")
        self.tableLucros.setGeometry(QRect(700, 230, 521, 271))
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
        self.btn_Visualizar = QPushButton(Frm_Bancos)
        self.btn_Visualizar.setObjectName(u"btn_Visualizar")
        self.btn_Visualizar.setGeometry(QRect(490, 570, 321, 71))
        self.btn_Visualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #000000;\n"
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
        self.txt_gastos = QLineEdit(Frm_Bancos)
        self.txt_gastos.setObjectName(u"txt_gastos")
        self.txt_gastos.setEnabled(False)
        self.txt_gastos.setGeometry(QRect(320, 710, 281, 41))
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
        self.label_SomaGastos = QLabel(Frm_Bancos)
        self.label_SomaGastos.setObjectName(u"label_SomaGastos")
        self.label_SomaGastos.setGeometry(QRect(30, 710, 281, 41))
        self.label_SomaGastos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_lucros = QLineEdit(Frm_Bancos)
        self.txt_lucros.setObjectName(u"txt_lucros")
        self.txt_lucros.setEnabled(False)
        self.txt_lucros.setGeometry(QRect(930, 710, 281, 41))
        self.txt_lucros.setStyleSheet(u"QLineEdit {\n"
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
        self.label_SomaLucros = QLabel(Frm_Bancos)
        self.label_SomaLucros.setObjectName(u"label_SomaLucros")
        self.label_SomaLucros.setGeometry(QRect(640, 710, 271, 41))
        self.label_SomaLucros.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.tableGastos = QTableWidget(Frm_Bancos)
        if (self.tableGastos.columnCount() < 5):
            self.tableGastos.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableGastos.setObjectName(u"tableGastos")
        self.tableGastos.setGeometry(QRect(50, 230, 521, 271))
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

        self.retranslateUi(Frm_Bancos)

        QMetaObject.connectSlotsByName(Frm_Bancos)
    # setupUi

    def retranslateUi(self, Frm_Bancos):
        Frm_Bancos.setWindowTitle(QCoreApplication.translate("Frm_Bancos", u"Bancos", None))
        self.label_Bancos.setText(QCoreApplication.translate("Frm_Bancos", u"BANCOS", None))
        self.label_Gastos.setText(QCoreApplication.translate("Frm_Bancos", u"GASTOS:", None))
        self.labe_Lucros.setText(QCoreApplication.translate("Frm_Bancos", u"LUCROS:", None))
        ___qtablewidgetitem = self.tableLucros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frm_Bancos", u"Nome/Produtos", None));
        ___qtablewidgetitem1 = self.tableLucros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frm_Bancos", u"Valor", None));
        ___qtablewidgetitem2 = self.tableLucros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frm_Bancos", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem3 = self.tableLucros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frm_Bancos", u"Quantidade", None));
        self.btn_Visualizar.setText(QCoreApplication.translate("Frm_Bancos", u"VIZUALIZAR", None))
        self.label_SomaGastos.setText(QCoreApplication.translate("Frm_Bancos", u"Soma dos gastos:", None))
        self.label_SomaLucros.setText(QCoreApplication.translate("Frm_Bancos", u"Soma dos lucros:", None))
        ___qtablewidgetitem4 = self.tableGastos.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frm_Bancos", u"Nome", None));
        ___qtablewidgetitem5 = self.tableGastos.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frm_Bancos", u"Fornecedor", None));
        ___qtablewidgetitem6 = self.tableGastos.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frm_Bancos", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem7 = self.tableGastos.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Frm_Bancos", u"Valor", None));
        ___qtablewidgetitem8 = self.tableGastos.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Frm_Bancos", u"Total", None));
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_Bancos = QWidget()
    ui = Ui_Frm_Bancos()
    ui.setupUi(frm_Bancos)
    frm_Bancos.show()
    app.exec()