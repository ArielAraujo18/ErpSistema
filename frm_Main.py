from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget, QMessageBox)

import sys
import Controle
import os

import icon_cliente
import icon_back
import icon_ConsultaVendas
import icon_tarefas
import icon_sair
import icon_caixa
import icon_receber
import icon_bancos
import icon_pagar
import icon_vendas
import icon_produtos
import icon_fornecedor

from frm_cliente_ui import Ui_frm_Cliente
from frm_Fornecedor import Ui_frm_Fornecedor
from frm_Produtos import Ui_frm_Produtos
from frm_Vendas import Ui_Frm_Vendas
from frm_Contas import Ui_frm_Contas
from frm_ValoresAReceber import Ui_frm_ValoresAReceber
from frm_Tarefas import Ui_frm_Tarefas
from frm_Bancos import Ui_Frm_Bancos
from frm_Login import Ui_frm_Login

class Ui_frm_Main(object):
    def setupUi(self, frm_Main):
        if not frm_Main.objectName():
            frm_Main.setObjectName(u"frm_Main")
        frm_Main.setFixedSize(723, 453)
        self.frm_Main = frm_Main
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Main.setWindowIcon(QIcon(caminho_icone))
        frm_Main.setStyleSheet(u"")
        self.actionCliente = QAction(frm_Main)
        self.actionCliente.setObjectName(u"actionCliente")
        self.actionFornecedor = QAction(frm_Main)
        self.actionFornecedor.setObjectName(u"actionFornecedor")
        self.actionUsu_rio_do_sistema = QAction(frm_Main)
        self.actionUsu_rio_do_sistema.setObjectName(u"actionUsu_rio_do_sistema")
        self.actionVenda = QAction(frm_Main)
        self.actionVenda.setObjectName(u"actionVenda")
        self.actionConsumo_de_produtos = QAction(frm_Main)
        self.actionConsumo_de_produtos.setObjectName(u"actionConsumo_de_produtos")
        self.actionSaldo = QAction(frm_Main)
        self.actionSaldo.setObjectName(u"actionSaldo")
        self.actionCompras_2 = QAction(frm_Main)
        self.actionCompras_2.setObjectName(u"actionCompras_2")
        self.actionPedido = QAction(frm_Main)
        self.actionPedido.setObjectName(u"actionPedido")
        self.actionCancelar_compra = QAction(frm_Main)
        self.actionCancelar_compra.setObjectName(u"actionCancelar_compra")
        self.actionCaixa = QAction(frm_Main)
        self.actionCaixa.setObjectName(u"actionCaixa")
        self.actionBanco = QAction(frm_Main)
        self.actionBanco.setObjectName(u"actionBanco")
        self.actionContas_para_pagar = QAction(frm_Main)
        self.actionContas_para_pagar.setObjectName(u"actionContas_para_pagar")
        self.actionContas_para_receber = QAction(frm_Main)
        self.actionContas_para_receber.setObjectName(u"actionContas_para_receber")
        self.actionContas_pagas = QAction(frm_Main)
        self.actionContas_pagas.setObjectName(u"actionContas_pagas")
        self.actionContas_recebidas = QAction(frm_Main)
        self.actionContas_recebidas.setObjectName(u"actionContas_recebidas")
        self.actionGeral = QAction(frm_Main)
        self.actionGeral.setObjectName(u"actionGeral")
        self.actionResumido = QAction(frm_Main)
        self.actionResumido.setObjectName(u"actionResumido")
        self.actionGeral_3 = QAction(frm_Main)
        self.actionGeral_3.setObjectName(u"actionGeral_3")
        self.actionResumido_2 = QAction(frm_Main)
        self.actionResumido_2.setObjectName(u"actionResumido_2")
        self.centralwidget = QWidget(frm_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #2c2c2c;")
        self.btn_cliente = QPushButton(self.centralwidget)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setGeometry(QRect(0, 0, 81, 71))
        self.btn_cliente.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_cli/cliente.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_receber = QPushButton(self.centralwidget)
        self.btn_receber.setObjectName(u"btn_receber")
        self.btn_receber.setGeometry(QRect(480, 0, 81, 71))
        self.btn_receber.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_receb/receber.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa; \n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_produtos = QPushButton(self.centralwidget)
        self.btn_produtos.setObjectName(u"btn_produtos")
        self.btn_produtos.setGeometry(QRect(160, 0, 81, 71))
        self.btn_produtos.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_prod/produtos.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_vendas = QPushButton(self.centralwidget)
        self.btn_vendas.setObjectName(u"btn_vendas")
        self.btn_vendas.setGeometry(QRect(240, 0, 81, 71))
        self.btn_vendas.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px; \n"
"	background-image: url(:/icon_vend/venda.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_pagar = QPushButton(self.centralwidget)
        self.btn_pagar.setObjectName(u"btn_pagar")
        self.btn_pagar.setGeometry(QRect(320, 0, 81, 71))
        self.btn_pagar.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"	background-image:url(:/icon_cont/contasPagar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa; \n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_bancos = QPushButton(self.centralwidget)
        self.btn_bancos.setObjectName(u"btn_bancos")
        self.btn_bancos.setGeometry(QRect(400, 0, 81, 71))
        self.btn_bancos.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"	background-image:url(:/icon_bank/banco.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa; \n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_fornecedor = QPushButton(self.centralwidget)
        self.btn_fornecedor.setObjectName(u"btn_fornecedor")
        self.btn_fornecedor.setGeometry(QRect(80, 0, 81, 71))
        self.btn_fornecedor.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"	background-image:url(:/icon_forn/fornecedor.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa; \n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_sair = QPushButton(self.centralwidget)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(640, 0, 81, 71))
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_sair/sair.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 270, 251, 31))
        font = QFont()
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"}")
        self.btn_produtos_2 = QPushButton(self.centralwidget)
        self.btn_produtos_2.setObjectName(u"btn_produtos_2")
        self.btn_produtos_2.setGeometry(QRect(560, 0, 81, 71))
        self.btn_produtos_2.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_tarefas/Adobe_Express_-_file-removebg-preview.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0;\n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 380, 81, 21))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 14px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 140, 81, 121))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background: url(:/icon_avs/avsIconLogo.png);\n"
"	background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 310, 201, 20))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}")
        self.lbl_login = QLabel(self.centralwidget)
        self.lbl_login.setObjectName(u"lbl_login")
        self.lbl_login.setGeometry(QRect(10, 370, 131, 21))
        self.lbl_login.setStyleSheet(u"QLabel {\n"
"    font-size: 14px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        frm_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 723, 35))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #2E3440;\n"
"    color: white;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {   \n"
"    background: #3B4252;    \n"
"    color: #88C0D0;          \n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #2E3440;\n"
"    color: white; \n"
"    border: 1px solid #4C566A;\n"
"}\n"
"\n"
"QMenu::item:selected {      \n"
"    background-color: #3B4252;\n"
"    color: #A3BE8C;\n"
"}\n"
"")
        self.menuCadastros = QMenu(self.menubar)
        self.menuCadastros.setObjectName(u"menuCadastros")
        self.menuFinanceiro = QMenu(self.menubar)
        self.menuFinanceiro.setObjectName(u"menuFinanceiro")
        frm_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_Main)
        self.statusbar.setObjectName(u"statusbar")
        frm_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menuCadastros.addAction(self.actionCliente)
        self.menuCadastros.addAction(self.actionFornecedor)
        self.menuFinanceiro.addAction(self.actionCaixa)
        self.menuFinanceiro.addAction(self.actionBanco)
        self.menuFinanceiro.addAction(self.actionContas_para_pagar)
        self.menuFinanceiro.addAction(self.actionContas_para_receber)
        self.menuFinanceiro.addAction(self.actionContas_pagas)
        self.menuFinanceiro.addAction(self.actionContas_recebidas)

        self.retranslateUi(frm_Main)

        QMetaObject.connectSlotsByName(frm_Main)
    # setupUi

    def login(self):
        self.lbl_login.setText(Controle.login)

    def telaCliente(self):
        if not hasattr(self, 'frm_Cliente') or self.frm_Cliente is None or not self.frm_Cliente.isVisible():
                self.frm_Cliente = QWidget()
                self.ui = Ui_frm_Cliente()
                self.ui.setupUi(self.frm_Cliente)

                self.frm_Cliente.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Cliente.destroyed.connect(lambda: setattr(self, 'frm_Cliente', None))

                self.frm_Cliente.show()
        else:
                self.frm_Cliente.raise_()
                self.frm_Cliente.activateWindow()



    def telaFornecedor(self):
         if not hasattr(self, 'frm_Fornecedor') or self.frm_Fornecedor is None or not self.frm_Fornecedor.isVisible():
                self.frm_Fornecedor = QWidget()
                self.ui = Ui_frm_Fornecedor()
                self.ui.setupUi(self.frm_Fornecedor)
                
                self.frm_Fornecedor.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Fornecedor.destroyed.connect(lambda: setattr(self, 'frm_Fornecedor', None))

                self.frm_Fornecedor.show()

         else:
                self.frm_Fornecedor.raise_()
                self.frm_Fornecedor.activateWindow()


    def telaProdutos(self):
         if not hasattr(self, 'frm_Produtos') or self.frm_Produtos is None or not self.frm_Produtos.isVisible():
                self.frm_Produtos = QWidget()
                self.ui = Ui_frm_Produtos()
                self.ui.setupUi(self.frm_Produtos)

                self.frm_Produtos.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Produtos.destroyed.connect(lambda: setattr(self, 'frm_Produtos', None))

                self.frm_Produtos.show()
         else:
                self.frm_Produtos.raise_()
                self.frm_Produtos.activateWindow()


    def sairSistema(self):
        if not hasattr(self, 'frm_Login') or self.frm_Login is None or not self.frm_Login.isVisible():
                self.frm_Login = QMainWindow()
                self.ui = Ui_frm_Login()
                self.ui.setupUi(self.frm_Login)
                self.frm_Login.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Login.destroyed.connect(lambda: setattr(self, 'frm_Login', None))

                #Abre a tela
                self.frm_Login.show()

        else:

                self.frm_Login.raise_()
                self.frm_Login.activateWindow()


        self.frm_Main.close()
        

    def telaVendas(self):
         if not hasattr(self, 'frm_Vendas') or self.frm_Vendas is None or not self.frm_Vendas.isVisible():
                self.frm_Vendas = QWidget()
                self.ui = Ui_Frm_Vendas()
                self.ui.setupUi(self.frm_Vendas)

                self.frm_Vendas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Vendas.destroyed.connect(lambda: setattr(self, 'frm_Vendas', None))

                self.frm_Vendas.show()

         else:
               self.frm_Vendas.raise_()
               self.frm_Vendas.activateWindow()

    def telaContas(self):
        if Controle.login == 'Usuário':
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText("Você não tem permissão para acessar esse frame!")
                msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
         
        if not hasattr(self, 'frm_Contas') or self.frm_Contas is None or not self.frm_Contas.isVisible():

                self.frm_Contas = QWidget()
                self.ui = Ui_frm_Contas()
                self.ui.setupUi(self.frm_Contas)

                self.frm_Contas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Contas.destroyed.connect(lambda: setattr(self, 'frm_Contas', None))

                self.frm_Contas.show()
        else:
               self.frm_Contas.raise_()
               self.frm_Contas.activateWindow()

    def telaValores(self):
        if not hasattr(self, 'frm_ValoresAReceber') or self.frm_ValoresAReceber is None or not self.frm_ValoresAReceber.isVisible():

                self.frm_ValoresAReceber = QWidget()
                self.ui = Ui_frm_ValoresAReceber()
                self.ui.setupUi(self.frm_ValoresAReceber)

                self.frm_ValoresAReceber.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_ValoresAReceber.destroyed.connect(lambda: setattr(self, 'frm_ValoresAReceber', None))

                self.frm_ValoresAReceber.show()
        else:
               self.frm_ValoresAReceber.raise_()
               self.frm_ValoresAReceber.activateWindow()

    def telaTarefas(self):
        if not hasattr(self, 'frm_Tarefas') or self.frm_Tarefas is None or not self.frm_Tarefas.isVisible():

                self.frm_Tarefas = QWidget()
                self.ui = Ui_frm_Tarefas()
                self.ui.setupUi(self.frm_Tarefas)

                self.frm_Tarefas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Tarefas.destroyed.connect(lambda: setattr(self, 'frm_Tarefas', None))

                self.frm_Tarefas.show()

        else:
              self.frm_Tarefas.raise_()
              self.frm_Tarefas.activateWindow()

    def TelaBancos(self):
        if Controle.login == 'Usuário':
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText("Você não tem permissão para acessar esse frame!")
                msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return

        if not hasattr(self, 'frm_Bancos') or self.Frm_Bancos is None or not self.Frm_Bancos.isVisible():
                self.Frm_Bancos = QWidget()
                self.ui = Ui_Frm_Bancos()
                self.ui.setupUi(self.Frm_Bancos)

                self.Frm_Bancos.setAttribute(Qt.WA_DeleteOnClose)
                self.Frm_Bancos.destroyed.connect(lambda: setattr(self, 'Frm_Bancos', None))

                self.Frm_Bancos.show()
       
        else:

                self.Frm_Bancos.raise_()
                self.Frm_Bancos.activateWindow()

    def retranslateUi(self, frm_Main):
        frm_Main.setWindowTitle(QCoreApplication.translate("frm_Main", u"Tela Principal", None))
        self.actionCliente.setText(QCoreApplication.translate("frm_Main", u"Cliente", None))
        self.actionFornecedor.setText(QCoreApplication.translate("frm_Main", u"Fornecedor", None))
        self.actionUsu_rio_do_sistema.setText(QCoreApplication.translate("frm_Main", u"Usu\u00e1rio", None))
        self.actionVenda.setText(QCoreApplication.translate("frm_Main", u"Venda", None))
        self.actionConsumo_de_produtos.setText(QCoreApplication.translate("frm_Main", u"Consumo de produtos", None))
        self.actionSaldo.setText(QCoreApplication.translate("frm_Main", u"Saldo", None))
        self.actionCompras_2.setText(QCoreApplication.translate("frm_Main", u"Compras", None))
        self.actionPedido.setText(QCoreApplication.translate("frm_Main", u"Pedido", None))
        self.actionCancelar_compra.setText(QCoreApplication.translate("frm_Main", u"Cancelar", None))
        self.actionCaixa.setText(QCoreApplication.translate("frm_Main", u"Caixa", None))
        self.actionBanco.setText(QCoreApplication.translate("frm_Main", u"Banco", None))
        self.actionContas_para_pagar.setText(QCoreApplication.translate("frm_Main", u"Contas para pagar", None))
        self.actionContas_para_receber.setText(QCoreApplication.translate("frm_Main", u"Contas para receber", None))
        self.actionContas_pagas.setText(QCoreApplication.translate("frm_Main", u"Contas pagas", None))
        self.actionContas_recebidas.setText(QCoreApplication.translate("frm_Main", u"Contas recebidas", None))
        self.actionGeral.setText(QCoreApplication.translate("frm_Main", u"Geral", None))
        self.actionResumido.setText(QCoreApplication.translate("frm_Main", u"Resumido", None))
        self.actionGeral_3.setText(QCoreApplication.translate("frm_Main", u"Geral", None))
        self.actionResumido_2.setText(QCoreApplication.translate("frm_Main", u"Resumido", None))
        self.btn_cliente.setText("")
        self.btn_receber.setText("")
        self.btn_produtos.setText("")
        self.btn_vendas.setText("")
        self.btn_pagar.setText("")
        self.btn_bancos.setText("")
        self.btn_fornecedor.setText("")
        self.btn_sair.setText("")
        self.label.setText(QCoreApplication.translate("frm_Main", u"AVS-SOFTWARES", None))
        self.btn_produtos_2.setText("")
        self.label_2.setText(QCoreApplication.translate("frm_Main", u"Vers\u00e3o: 1.1", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("frm_Main", u"SOFTWARE E TECNOLOGIA", None))
        self.lbl_login.setText(QCoreApplication.translate("frm_Main", u"Login", None))
        self.menuCadastros.setTitle(QCoreApplication.translate("frm_Main", u"Cadastros", None))
        self.menuFinanceiro.setTitle(QCoreApplication.translate("frm_Main", u"Financeiro", None))
    # retranslateUi
        self.login()

        self.btn_sair.clicked.connect(self.sairSistema)
        self.btn_cliente.clicked.connect(self.telaCliente)
        self.btn_fornecedor.clicked.connect(self.telaFornecedor)        
        self.btn_produtos.clicked.connect(self.telaProdutos)
        self.btn_vendas.clicked.connect(self.telaVendas)
        self.btn_pagar.clicked.connect(self.telaContas)
        self.btn_receber.clicked.connect(self.telaValores)
        self.btn_produtos_2.clicked.connect(self.telaTarefas) #Esqueci de mudar o nome do btn
        self.btn_bancos.clicked.connect(self.TelaBancos)

        #Action

        self.actionCliente.triggered.connect(self.telaCliente)
        self.actionFornecedor.triggered.connect(self.telaFornecedor)
        self.actionCaixa.triggered.connect(self.telaVendas)
        self.actionBanco.triggered.connect(self.TelaBancos)
        self.actionContas_para_pagar.triggered.connect(self.telaContas)
        self.actionContas_para_receber.triggered.connect(self.telaValores)

if __name__ == "__main__":
    app = QApplication([])
    frm_Main = QMainWindow()
    ui = Ui_frm_Main()
    ui.setupUi(frm_Main)
    frm_Main.show()
    app.exec()