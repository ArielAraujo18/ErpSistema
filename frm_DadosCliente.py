from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import icon_excluirD
import icon_cadastrar

class Ui_frm_DadosCliente(object):
    def setupUi(self, frm_DadosCliente):
        if not frm_DadosCliente.objectName():
            frm_DadosCliente.setObjectName(u"frm_DadosCliente")
        frm_DadosCliente.setFixedSize(526, 609)
        frm_DadosCliente.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsi.png"))
        frm_DadosCliente.setStyleSheet(u"QWidget {\n"
"    background-color: #eaf2f8;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosCliente)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(50, 50, 51, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosCliente)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(120, 40, 371, 41))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_celular = QLabel(frm_DadosCliente)
        self.lbl_celular.setObjectName(u"lbl_celular")
        self.lbl_celular.setGeometry(QRect(40, 100, 61, 16))
        self.lbl_celular.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_cpf = QLabel(frm_DadosCliente)
        self.lbl_cpf.setObjectName(u"lbl_cpf")
        self.lbl_cpf.setGeometry(QRect(60, 150, 41, 20))
        self.lbl_cpf.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosCliente)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(150, 500, 101, 91))
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_excluirD/excluir.png);\n"
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
        self.txt_celular = QLineEdit(frm_DadosCliente)
        self.txt_celular.setObjectName(u"txt_celular")
        self.txt_celular.setGeometry(QRect(120, 90, 371, 41))
        self.txt_celular.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_cpf = QLineEdit(frm_DadosCliente)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(120, 140, 371, 41))
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Rua = QLabel(frm_DadosCliente)
        self.lbl_Rua.setObjectName(u"lbl_Rua")
        self.lbl_Rua.setGeometry(QRect(60, 250, 41, 20))
        self.lbl_Rua.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Rua = QLineEdit(frm_DadosCliente)
        self.txt_Rua.setObjectName(u"txt_Rua")
        self.txt_Rua.setGeometry(QRect(120, 240, 371, 41))
        self.txt_Rua.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_cidade = QLabel(frm_DadosCliente)
        self.lbl_cidade.setObjectName(u"lbl_cidade")
        self.lbl_cidade.setGeometry(QRect(40, 200, 61, 20))
        self.lbl_cidade.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar_3 = QPushButton(frm_DadosCliente)
        self.btn_cadastrar_3.setObjectName(u"btn_cadastrar_3")
        self.btn_cadastrar_3.setGeometry(QRect(290, 500, 101, 91))
        self.btn_cadastrar_3.setStyleSheet(u"QPushButton {\n"
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
        self.txt_cidade = QLineEdit(frm_DadosCliente)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(120, 190, 371, 41))
        self.txt_cidade.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_bairro = QLabel(frm_DadosCliente)
        self.lbl_bairro.setObjectName(u"lbl_bairro")
        self.lbl_bairro.setGeometry(QRect(40, 300, 61, 21))
        self.lbl_bairro.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_bairro = QLineEdit(frm_DadosCliente)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(120, 290, 371, 41))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_cep = QLabel(frm_DadosCliente)
        self.lbl_cep.setObjectName(u"lbl_cep")
        self.lbl_cep.setGeometry(QRect(60, 400, 41, 21))
        self.lbl_cep.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_cep = QLineEdit(frm_DadosCliente)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(120, 390, 371, 41))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Numero = QLineEdit(frm_DadosCliente)
        self.txt_Numero.setObjectName(u"txt_Numero")
        self.txt_Numero.setGeometry(QRect(120, 340, 371, 41))
        self.txt_Numero.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Numero = QLabel(frm_DadosCliente)
        self.lbl_Numero.setObjectName(u"lbl_Numero")
        self.lbl_Numero.setGeometry(QRect(30, 350, 71, 21))
        self.lbl_Numero.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_cidade_6 = QLineEdit(frm_DadosCliente)
        self.txt_cidade_6.setObjectName(u"txt_cidade_6")
        self.txt_cidade_6.setGeometry(QRect(120, 440, 371, 41))
        self.txt_cidade_6.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_email = QLabel(frm_DadosCliente)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(40, 450, 61, 21))
        self.lbl_email.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.retranslateUi(frm_DadosCliente)

        QMetaObject.connectSlotsByName(frm_DadosCliente)
    # setupUi

    def retranslateUi(self, frm_DadosCliente):
        frm_DadosCliente.setWindowTitle(QCoreApplication.translate("frm_DadosCliente", u"Form", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosCliente", u"Nome:", None))
        self.lbl_celular.setText(QCoreApplication.translate("frm_DadosCliente", u"Celular: ", None))
        self.lbl_cpf.setText(QCoreApplication.translate("frm_DadosCliente", u"CPF:", None))
        self.btn_cancelar.setText("")
        self.txt_celular.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"(00) 0 0000-0000", None))
        self.txt_cpf.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"000.000.000-00", None))
        self.lbl_Rua.setText(QCoreApplication.translate("frm_DadosCliente", u"Rua:", None))
        self.lbl_cidade.setText(QCoreApplication.translate("frm_DadosCliente", u"Cidade:", None))
        self.btn_cadastrar_3.setText("")
        self.lbl_bairro.setText(QCoreApplication.translate("frm_DadosCliente", u"Bairro:", None))
        self.lbl_cep.setText(QCoreApplication.translate("frm_DadosCliente", u"CEP:", None))
        self.txt_cep.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"00000-000", None))
        self.lbl_Numero.setText(QCoreApplication.translate("frm_DadosCliente", u"N\u00famero:", None))
        self.txt_cidade_6.setText("")
        self.lbl_email.setText(QCoreApplication.translate("frm_DadosCliente", u"E-mail:", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosCliente = QWidget()
    ui = Ui_frm_DadosCliente()
    ui.setupUi(frm_DadosCliente)
    frm_DadosCliente.show()
    app.exec()