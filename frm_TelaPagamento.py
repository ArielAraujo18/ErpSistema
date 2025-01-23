from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import icon_pagamentoTe

class Ui_frm_TelaPagamento(object):
    def setupUi(self, frm_TelaPagamento):
        if not frm_TelaPagamento.objectName():
            frm_TelaPagamento.setObjectName(u"frm_TelaPagamento")
        frm_TelaPagamento.setFixedSize(524, 761)
        frm_TelaPagamento.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        frm_TelaPagamento.setStyleSheet(u"QWidget{\n"
"	background-color: #2E8B57;\n"
"}")
        self.label = QLabel(frm_TelaPagamento)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 211, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Dinheiro = QLineEdit(frm_TelaPagamento)
        self.txt_Dinheiro.setObjectName(u"txt_Dinheiro")
        self.txt_Dinheiro.setGeometry(QRect(220, 80, 281, 41))
        self.txt_Dinheiro.setStyleSheet(u"QLineEdit {\n"
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
        self.label_2 = QLabel(frm_TelaPagamento)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 191, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Cheque = QLineEdit(frm_TelaPagamento)
        self.txt_Cheque.setObjectName(u"txt_Cheque")
        self.txt_Cheque.setGeometry(QRect(220, 320, 281, 41))
        self.txt_Cheque.setStyleSheet(u"QLineEdit {\n"
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
        self.label_3 = QLabel(frm_TelaPagamento)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 320, 151, 41))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.label_4 = QLabel(frm_TelaPagamento)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 151, 41))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Cartao = QLineEdit(frm_TelaPagamento)
        self.txt_Cartao.setObjectName(u"txt_Cartao")
        self.txt_Cartao.setGeometry(QRect(220, 160, 281, 41))
        self.txt_Cartao.setStyleSheet(u"QLineEdit {\n"
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
        self.label_5 = QLabel(frm_TelaPagamento)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 250, 71, 31))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Pix = QLineEdit(frm_TelaPagamento)
        self.txt_Pix.setObjectName(u"txt_Pix")
        self.txt_Pix.setGeometry(QRect(220, 240, 281, 41))
        self.txt_Pix.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_Total = QLineEdit(frm_TelaPagamento)
        self.txt_Total.setObjectName(u"txt_Total")
        self.txt_Total.setEnabled(False)
        self.txt_Total.setGeometry(QRect(250, 460, 271, 41))
        self.txt_Total.setStyleSheet(u"QLineEdit {\n"
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
        self.label_6 = QLabel(frm_TelaPagamento)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 460, 241, 41))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Troco = QLineEdit(frm_TelaPagamento)
        self.txt_Troco.setObjectName(u"txt_Troco")
        self.txt_Troco.setEnabled(False)
        self.txt_Troco.setGeometry(QRect(250, 530, 271, 41))
        self.txt_Troco.setStyleSheet(u"QLineEdit {\n"
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
        self.label_7 = QLabel(frm_TelaPagamento)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 530, 131, 41))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.btn_pagamento = QPushButton(frm_TelaPagamento)
        self.btn_pagamento.setObjectName(u"btn_pagamento")
        self.btn_pagamento.setGeometry(QRect(80, 620, 381, 121))
        self.btn_pagamento.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_pagamento/forma-de-pagamento AA (2).png);\n"
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

        self.retranslateUi(frm_TelaPagamento)

        QMetaObject.connectSlotsByName(frm_TelaPagamento)
    # setupUi

    def retranslateUi(self, frm_TelaPagamento):
        frm_TelaPagamento.setWindowTitle(QCoreApplication.translate("frm_TelaPagamento", u"Pagamento", None))
        self.label.setText(QCoreApplication.translate("frm_TelaPagamento", u"PAGAMENTO", None))
        self.label_2.setText(QCoreApplication.translate("frm_TelaPagamento", u"DINHEIRO:", None))
        self.label_3.setText(QCoreApplication.translate("frm_TelaPagamento", u"CHEQUE:", None))
        self.label_4.setText(QCoreApplication.translate("frm_TelaPagamento", u"CART\u00c3O:", None))
        self.label_5.setText(QCoreApplication.translate("frm_TelaPagamento", u"PIX:", None))
        self.label_6.setText(QCoreApplication.translate("frm_TelaPagamento", u"VALOR TOTAL:", None))
        self.txt_Troco.setText("")
        self.label_7.setText(QCoreApplication.translate("frm_TelaPagamento", u"TROCO:", None))
        self.btn_pagamento.setText("")
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_TelaPagamento = QWidget()
    ui = Ui_frm_TelaPagamento()
    ui.setupUi(frm_TelaPagamento)
    frm_TelaPagamento.show()
    app.exec()