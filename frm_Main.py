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

from frm_cliente_ui import Ui_frm_Cliente
from frm_Fornecedor import Ui_frm_Fornecedor
from frm_Produtos import Ui_frm_Produtos
from frm_Vendas import Ui_Frm_Vendas
from frm_Contas import Ui_frm_Contas

import sys
import icon_cliente
import icon_sair
import icon_caixa
import icon_receber
import icon_bancos
import icon_pagar
import icon_vendas
import icon_produtos
import icon_fornecedor


class Ui_frm_Main(object):
    def setupUi(self, frm_Main):
        if not frm_Main.objectName():
            frm_Main.setObjectName(u"frm_Main")
        frm_Main.setFixedSize(642, 294)
        frm_Main.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
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
        self.btn_sair.setGeometry(QRect(560, 0, 81, 71))
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
        self.label.setGeometry(QRect(180, 140, 301, 31))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        frm_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 642, 34))
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
        self.menuOpera_es = QMenu(self.menubar)
        self.menuOpera_es.setObjectName(u"menuOpera_es")
        self.menuSa_da_de_produtos = QMenu(self.menuOpera_es)
        self.menuSa_da_de_produtos.setObjectName(u"menuSa_da_de_produtos")
        self.menuEstoque = QMenu(self.menuOpera_es)
        self.menuEstoque.setObjectName(u"menuEstoque")
        self.menuFinanceiro = QMenu(self.menubar)
        self.menuFinanceiro.setObjectName(u"menuFinanceiro")
        self.menuConsultas = QMenu(self.menubar)
        self.menuConsultas.setObjectName(u"menuConsultas")
        self.menuVendas = QMenu(self.menuConsultas)
        self.menuVendas.setObjectName(u"menuVendas")
        self.menuConsumos = QMenu(self.menuConsultas)
        self.menuConsumos.setObjectName(u"menuConsumos")
        frm_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_Main)
        self.statusbar.setObjectName(u"statusbar")
        frm_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuOpera_es.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menuCadastros.addAction(self.actionCliente)
        self.menuCadastros.addAction(self.actionFornecedor)
        self.menuOpera_es.addAction(self.menuSa_da_de_produtos.menuAction())
        self.menuOpera_es.addAction(self.menuEstoque.menuAction())
        self.menuSa_da_de_produtos.addAction(self.actionVenda)
        self.menuSa_da_de_produtos.addAction(self.actionConsumo_de_produtos)
        self.menuFinanceiro.addAction(self.actionCaixa)
        self.menuFinanceiro.addAction(self.actionBanco)
        self.menuFinanceiro.addAction(self.actionContas_para_pagar)
        self.menuFinanceiro.addAction(self.actionContas_para_receber)
        self.menuFinanceiro.addAction(self.actionContas_pagas)
        self.menuFinanceiro.addAction(self.actionContas_recebidas)
        self.menuConsultas.addAction(self.menuVendas.menuAction())
        self.menuConsultas.addAction(self.menuConsumos.menuAction())
        self.menuVendas.addAction(self.actionGeral)
        self.menuVendas.addAction(self.actionResumido)
        self.menuConsumos.addAction(self.actionGeral_3)
        self.menuConsumos.addAction(self.actionResumido_2)

        self.retranslateUi(frm_Main)

        QMetaObject.connectSlotsByName(frm_Main)
    # setupUi

    def telaCliente(self):
        #Verifica se o atributo existe e não é None
        if not hasattr(self, 'frm_Cliente') or self.frm_Cliente is None or not self.frm_Cliente.isVisible():
                #Cria a tela somente se não estiver aberta
                self.frm_Cliente = QWidget()
                self.ui = Ui_frm_Cliente()
                self.ui.setupUi(self.frm_Cliente)

                #Configurações para garantir a remoção da referência ao fechar a janela
                self.frm_Cliente.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Cliente.destroyed.connect(lambda: setattr(self, 'frm_Cliente', None))

                #Mostra a tela  
                self.frm_Cliente.show()
        else:
                #Traz a janela existente
                self.frm_Cliente.raise_()
                self.frm_Cliente.activateWindow()



    def telaFornecedor(self):
         if not hasattr(self, 'frm_Fornecedor') or self.frm_Fornecedor is None or not self.frm_Fornecedor.isVisible():
                self.frm_Fornecedor = QWidget()
                self.ui = Ui_frm_Fornecedor()
                self.ui.setupUi(self.frm_Fornecedor)
                
                #Configurações para garantir a remoção da referência ao fechar a janela
                self.frm_Fornecedor.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Fornecedor.destroyed.connect(lambda: setattr(self, 'frm_Fornecedor', None))

                #Mostra a tela
                self.frm_Fornecedor.show()

         else:
                self.frm_Fornecedor.raise_()
                self.frm_Fornecedor.activateWindow()


    def telaProdutos(self):
         if not hasattr(self, 'frm_Produtos') or self.frm_Produtos is None or not self.frm_Produtos.isVisible():
                self.frm_Produtos = QWidget()
                self.ui = Ui_frm_Produtos()
                self.ui.setupUi(self.frm_Produtos)

                #Config para garantir a remoção total da tela ao ser fechada
                self.frm_Produtos.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_Produtos.destroyed.connect(lambda: setattr(self, 'frm_Produtos', None))

                self.frm_Produtos.show()
         else:
                self.frm_Produtos.raise_()
                self.frm_Produtos.activateWindow()


    def sairSistema(self):
        sys.exit()   

        QMetaObject.connectSlotsByName(frm_Main)

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
         if not hasattr(self, 'frm_Contas') or self.frm_Contas is None or not self.frm_Contas.isVisible():
                self.frm_Contas = QWidget()
                self.ui = Ui_frm_Contas()
                self.ui.setupUi(self.frm_Contas)
                self.frm_Contas.show()
         else:
               self.frm_Contas.raise_()
               self.frm_Contas.activateWindow()

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
        self.menuCadastros.setTitle(QCoreApplication.translate("frm_Main", u"Cadastros", None))
        self.menuOpera_es.setTitle(QCoreApplication.translate("frm_Main", u"Opera\u00e7\u00f5es", None))
        self.menuSa_da_de_produtos.setTitle(QCoreApplication.translate("frm_Main", u"Sa\u00edda de produtos", None))
        self.menuEstoque.setTitle(QCoreApplication.translate("frm_Main", u"Estoque", None))
        self.menuFinanceiro.setTitle(QCoreApplication.translate("frm_Main", u"Financeiro", None))
        self.menuConsultas.setTitle(QCoreApplication.translate("frm_Main", u"Consultas", None))
        self.menuVendas.setTitle(QCoreApplication.translate("frm_Main", u"Vendas", None))
        self.menuConsumos.setTitle(QCoreApplication.translate("frm_Main", u"Consumos", None))
    # retranslateUi
         ##Botão##
        self.btn_sair.clicked.connect(self.sairSistema)
        self.btn_cliente.clicked.connect(self.telaCliente)
        self.btn_fornecedor.clicked.connect(self.telaFornecedor)        
        self.btn_produtos.clicked.connect(self.telaProdutos)
        self.btn_vendas.clicked.connect(self.telaVendas)
        self.btn_pagar.clicked.connect(self.telaContas)

        #action
        self.actionCliente.triggered.connect(self.telaCliente)
        self.actionFornecedor.triggered.connect(self.telaFornecedor)

if __name__ == "__main__":
    app = QApplication([])
    frm_Main = QMainWindow()
    ui = Ui_frm_Main()
    ui.setupUi(frm_Main)
    frm_Main.show()
    app.exec()