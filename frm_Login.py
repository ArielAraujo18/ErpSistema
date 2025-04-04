from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import os

class Ui_frm_Login(object):
    def setupUi(self, frm_Login):
        if not frm_Login.objectName():
            frm_Login.setObjectName(u"frm_Login")
        frm_Login.setFixedSize(674, 791)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Login.setWindowIcon(QIcon(caminho_icone))
        self.frm_Login = frm_Login
        frm_Login.setStyleSheet(u"QWidget {\n"
"    background-color: #2F4F4F;\n"
"}")
        self.centralwidget = QWidget(frm_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #FFFFE0;")
        self.lbl_senha = QLabel(self.centralwidget)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(50, 170, 111, 31))
        self.lbl_senha.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Usuario = QLineEdit(self.centralwidget)
        self.txt_Usuario.setObjectName(u"txt_Usuario")
        self.txt_Usuario.setGeometry(QRect(150, 240, 511, 51))
        font1 = QFont()
        self.txt_Usuario.setFont(font1)
        self.txt_Usuario.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_senha = QLabel(self.centralwidget)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(30, 330, 111, 31))
        self.lbl_senha.setFont(font)
        self.lbl_senha.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Senha = QLineEdit(self.centralwidget)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(150, 320, 511, 51))
        self.txt_Senha.setFont(font1)
        self.txt_Senha.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Senha.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 570, 81, 121))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background: url(:/icon_login/avsIconLogo.png);\n"
"	background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 700, 251, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 740, 201, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 70, 401, 81))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    font-size: 60px;\n"
"    font-weight: bold;\n"
"    color: #FFA500;\n"
"    padding: 10px;\n"
"    border-radius: 8px;\n"
"}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 410, 481, 91))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #007BFF; \n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 410, 141, 91))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #6c757d; \n"
"    color: white; \n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a6268; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #495057; \n"
"}")
        frm_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_Login)

        QMetaObject.connectSlotsByName(frm_Login)
    # setupUi

    def voltar(self):
        self.frm_Login.close()

    def retranslateUi(self, frm_Login):
        frm_Login.setWindowTitle(QCoreApplication.translate("frm_Login", u"Login", None))
        self.actionCliente.setText(QCoreApplication.translate("frm_Login", u"Cliente", None))
        self.actionFornecedor.setText(QCoreApplication.translate("frm_Login", u"Fornecedor", None))
        self.actionUsu_rio_do_sistema.setText(QCoreApplication.translate("frm_Login", u"Usu\u00e1rio", None))
        self.actionVenda.setText(QCoreApplication.translate("frm_Login", u"Venda", None))
        self.actionConsumo_de_produtos.setText(QCoreApplication.translate("frm_Login", u"Consumo de produtos", None))
        self.actionSaldo.setText(QCoreApplication.translate("frm_Login", u"Saldo", None))
        self.actionCompras_2.setText(QCoreApplication.translate("frm_Login", u"Compras", None))
        self.actionPedido.setText(QCoreApplication.translate("frm_Login", u"Pedido", None))
        self.actionCancelar_compra.setText(QCoreApplication.translate("frm_Login", u"Cancelar", None))
        self.actionCaixa.setText(QCoreApplication.translate("frm_Login", u"Caixa", None))
        self.actionBanco.setText(QCoreApplication.translate("frm_Login", u"Banco", None))
        self.actionContas_para_pagar.setText(QCoreApplication.translate("frm_Login", u"Contas para pagar", None))
        self.actionContas_para_receber.setText(QCoreApplication.translate("frm_Login", u"Contas para receber", None))
        self.actionContas_pagas.setText(QCoreApplication.translate("frm_Login", u"Contas pagas", None))
        self.actionContas_recebidas.setText(QCoreApplication.translate("frm_Login", u"Contas recebidas", None))
        self.actionGeral.setText(QCoreApplication.translate("frm_Login", u"Geral", None))
        self.actionResumido.setText(QCoreApplication.translate("frm_Login", u"Resumido", None))
        self.actionGeral_3.setText(QCoreApplication.translate("frm_Login", u"Geral", None))
        self.actionResumido_2.setText(QCoreApplication.translate("frm_Login", u"Resumido", None))
        self.lbl_senha.setText(QCoreApplication.translate("frm_Login", u"Senha:", None))
        self.btn_cancelar.setText(QCoreApplication.translate("frm_Login", u"CANCELAR", None))
        self.lbl_usuario.setText(QCoreApplication.translate("frm_Login", u"Usu\u00e1rio:", None))
        self.btn_entrar.setText(QCoreApplication.translate("frm_Login", u"ENTRAR", None))
    # retranslateUi
        self.btn_cancelar.clicked.connect(self.sairTela)

if __name__ == "__main__":
    app = QApplication([])
    frm_Login = QMainWindow()
    ui = Ui_frm_Login()
    ui.setupUi(frm_Login)
    frm_Login.show()
    app.exec()