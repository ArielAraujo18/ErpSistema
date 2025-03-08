from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import icon_cadastrar
import icon_cancelar

import os
import sys

class Ui_frm_DadosConsultasV(object):
    def setupUi(self, frm_DadosConsultasV):
        if not frm_DadosConsultasV.objectName():
            frm_DadosConsultasV.setObjectName(u"frm_DadosConsultasV")
        frm_DadosConsultasV.setFixedSize(513, 394)
        self.frm_DadosConsultasV = frm_DadosConsultasV
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_DadosConsultasV.setWindowIcon(QIcon(caminho_icone))
        frm_DadosConsultasV.setStyleSheet(u"QWidget {\n"
"    background-color: #008080;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosConsultasV)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(10, 50, 131, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosConsultasV)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(140, 40, 361, 41))
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
        self.lbl_qtd = QLabel(frm_DadosConsultasV)
        self.lbl_qtd.setObjectName(u"lbl_qtd")
        self.lbl_qtd.setGeometry(QRect(30, 230, 101, 20))
        self.lbl_qtd.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_Valor = QLabel(frm_DadosConsultasV)
        self.lbl_Valor.setObjectName(u"lbl_Valor")
        self.lbl_Valor.setGeometry(QRect(80, 170, 51, 16))
        self.lbl_Valor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosConsultasV)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(210, 300, 101, 91))
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
        self.txt_qtd = QLineEdit(frm_DadosConsultasV)
        self.txt_qtd.setObjectName(u"txt_qtd")
        self.txt_qtd.setGeometry(QRect(140, 220, 361, 41))
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
        self.txt_valor = QLineEdit(frm_DadosConsultasV)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setGeometry(QRect(140, 160, 361, 41))
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
        self.txt_nome_2 = QLineEdit(frm_DadosConsultasV)
        self.txt_nome_2.setObjectName(u"txt_nome_2")
        self.txt_nome_2.setGeometry(QRect(140, 100, 101, 41))
        self.txt_nome_2.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_nome_2 = QLabel(frm_DadosConsultasV)
        self.lbl_nome_2.setObjectName(u"lbl_nome_2")
        self.lbl_nome_2.setGeometry(QRect(80, 110, 51, 21))
        self.lbl_nome_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.retranslateUi(frm_DadosConsultasV)

        QMetaObject.connectSlotsByName(frm_DadosConsultasV)
    # setupUi

    def retranslateUi(self, frm_DadosConsultasV):
        frm_DadosConsultasV.setWindowTitle(QCoreApplication.translate("frm_DadosConsultasV", u"Dados Consultas", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosConsultasV", u"Nome/Produto:", None))
        self.lbl_qtd.setText(QCoreApplication.translate("frm_DadosConsultasV", u"Quantidade:", None))
        self.lbl_Valor.setText(QCoreApplication.translate("frm_DadosConsultasV", u"Valor:", None))
        self.btn_cancelar.setText("")
        self.txt_qtd.setInputMask(QCoreApplication.translate("frm_DadosConsultasV", u"00000000000000000000000000000000000000000000000000", None))
        self.txt_qtd.setText("")
        self.txt_valor.setInputMask(QCoreApplication.translate("frm_DadosConsultasV", u"R$", None))
        self.txt_nome_2.setInputMask(QCoreApplication.translate("frm_DadosConsultasV", u"00/00/0000", None))
        self.txt_nome_2.setText(QCoreApplication.translate("frm_DadosConsultasV", u"//", None))
        self.lbl_nome_2.setText(QCoreApplication.translate("frm_DadosConsultasV", u"Data:", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosConsultasV = QWidget()
    ui = Ui_frm_DadosConsultasV()
    ui.setupUi(frm_DadosConsultasV)
    frm_DadosConsultasV.show()
    app.exec()