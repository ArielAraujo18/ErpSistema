from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import os

class Ui_frm_Login(object):
    def setupUi(self, frm_Login):
        if not frm_Login.objectName():
            frm_Login.setObjectName(u"frm_Login")
        frm_Login.setFixedSize(675, 383)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Login.setWindowIcon(QIcon(caminho_icone))
        self.frm_Login = frm_Login
        frm_Login.setStyleSheet(u"")
        self.actionCliente = QAction(frm_Login)
        self.actionCliente.setObjectName(u"actionCliente")
        self.actionFornecedor = QAction(frm_Login)
        self.actionFornecedor.setObjectName(u"actionFornecedor")
        self.actionUsu_rio_do_sistema = QAction(frm_Login)
        self.actionUsu_rio_do_sistema.setObjectName(u"actionUsu_rio_do_sistema")
        self.actionVenda = QAction(frm_Login)
        self.actionVenda.setObjectName(u"actionVenda")
        self.actionConsumo_de_produtos = QAction(frm_Login)
        self.actionConsumo_de_produtos.setObjectName(u"actionConsumo_de_produtos")
        self.actionSaldo = QAction(frm_Login)
        self.actionSaldo.setObjectName(u"actionSaldo")
        self.actionCompras_2 = QAction(frm_Login)
        self.actionCompras_2.setObjectName(u"actionCompras_2")
        self.actionPedido = QAction(frm_Login)
        self.actionPedido.setObjectName(u"actionPedido")
        self.actionCancelar_compra = QAction(frm_Login)
        self.actionCancelar_compra.setObjectName(u"actionCancelar_compra")
        self.actionCaixa = QAction(frm_Login)
        self.actionCaixa.setObjectName(u"actionCaixa")
        self.actionBanco = QAction(frm_Login)
        self.actionBanco.setObjectName(u"actionBanco")
        self.actionContas_para_pagar = QAction(frm_Login)
        self.actionContas_para_pagar.setObjectName(u"actionContas_para_pagar")
        self.actionContas_para_receber = QAction(frm_Login)
        self.actionContas_para_receber.setObjectName(u"actionContas_para_receber")
        self.actionContas_pagas = QAction(frm_Login)
        self.actionContas_pagas.setObjectName(u"actionContas_pagas")
        self.actionContas_recebidas = QAction(frm_Login)
        self.actionContas_recebidas.setObjectName(u"actionContas_recebidas")
        self.actionGeral = QAction(frm_Login)
        self.actionGeral.setObjectName(u"actionGeral")
        self.actionResumido = QAction(frm_Login)
        self.actionResumido.setObjectName(u"actionResumido")
        self.actionGeral_3 = QAction(frm_Login)
        self.actionGeral_3.setObjectName(u"actionGeral_3")
        self.actionResumido_2 = QAction(frm_Login)
        self.actionResumido_2.setObjectName(u"actionResumido_2")
        self.centralwidget = QWidget(frm_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #FFFFE0;")
        self.lbl_senha = QLabel(self.centralwidget)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(50, 170, 111, 31))
        self.lbl_senha.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(self.centralwidget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(190, 290, 141, 61))
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_alt/consultar.png);\n"
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
        self.txt_usuario = QLineEdit(self.centralwidget)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(180, 60, 471, 61))
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_senha = QLineEdit(self.centralwidget)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(180, 160, 471, 61))
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_usuario = QLabel(self.centralwidget)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(30, 80, 131, 31))
        self.lbl_usuario.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_entrar = QPushButton(self.centralwidget)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(380, 290, 141, 61))
        self.btn_entrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_alt/consultar.png);\n"
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
        frm_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_Login)

        QMetaObject.connectSlotsByName(frm_Login)
    # setupUi

    def sairTela(self):
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