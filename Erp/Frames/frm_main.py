from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(975, 567)
        self.actionCliente = QAction(frm_main)
        self.actionCliente.setObjectName(u"actionCliente")
        self.actionFornecedor = QAction(frm_main)
        self.actionFornecedor.setObjectName(u"actionFornecedor")
        self.actionProdutos = QAction(frm_main)
        self.actionProdutos.setObjectName(u"actionProdutos")
        self.actionTarefas = QAction(frm_main)
        self.actionTarefas.setObjectName(u"actionTarefas")
        self.actionBanco = QAction(frm_main)
        self.actionBanco.setObjectName(u"actionBanco")
        self.actionContas_pagar = QAction(frm_main)
        self.actionContas_pagar.setObjectName(u"actionContas_pagar")
        self.actionContas_receber = QAction(frm_main)
        self.actionContas_receber.setObjectName(u"actionContas_receber")
        self.actionFuncion_rio = QAction(frm_main)
        self.actionFuncion_rio.setObjectName(u"actionFuncion_rio")
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #2c2c2c;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_cliente = QPushButton(self.widget_5)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_cliente/cliente.png);\n"
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

        self.verticalLayout_2.addWidget(self.btn_cliente)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_fornecedor = QPushButton(self.widget_7)
        self.btn_fornecedor.setObjectName(u"btn_fornecedor")
        self.btn_fornecedor.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_fornecedor/fornecedor.png);\n"
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

        self.verticalLayout_3.addWidget(self.btn_fornecedor)


        self.horizontalLayout_2.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_produtos = QPushButton(self.widget_6)
        self.btn_produtos.setObjectName(u"btn_produtos")
        self.btn_produtos.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_produtos/produtos.png);\n"
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

        self.verticalLayout_4.addWidget(self.btn_produtos)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_tarefas = QPushButton(self.widget_8)
        self.btn_tarefas.setObjectName(u"btn_tarefas")
        self.btn_tarefas.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_tarefas/tarefa.png);\n"
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

        self.verticalLayout_6.addWidget(self.btn_tarefas)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.widget_14 = QWidget(self.widget_4)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_11 = QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.horizontalLayout_3.addWidget(self.widget_14)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_vendas = QPushButton(self.widget_9)
        self.btn_vendas.setObjectName(u"btn_vendas")
        self.btn_vendas.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_vendas/vendas.png);\n"
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

        self.verticalLayout_5.addWidget(self.btn_vendas)


        self.horizontalLayout_3.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_12 = QWidget(self.widget_3)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_7 = QVBoxLayout(self.widget_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_pagar = QPushButton(self.widget_12)
        self.btn_pagar.setObjectName(u"btn_pagar")
        self.btn_pagar.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_pagar/pagar.png);\n"
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

        self.verticalLayout_7.addWidget(self.btn_pagar)


        self.horizontalLayout_4.addWidget(self.widget_12)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_receber = QPushButton(self.widget_10)
        self.btn_receber.setObjectName(u"btn_receber")
        self.btn_receber.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_receber/receber.png);\n"
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

        self.verticalLayout_8.addWidget(self.btn_receber)


        self.horizontalLayout_4.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_bancos = QPushButton(self.widget_11)
        self.btn_bancos.setObjectName(u"btn_bancos")
        self.btn_bancos.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px;\n"
"	background-image: url(:/icon_bancos/bancos.png);\n"
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

        self.verticalLayout_9.addWidget(self.btn_bancos)


        self.horizontalLayout_4.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.frame)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	background: url(:/icon_logoInicial/AvsLogo.png);\n"
"	background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}")

        self.verticalLayout_10.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_2)

        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 31))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #2c2c2c;\n"
"    color: #ffffff;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px 12px;\n"
"    margin: 2px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { \n"
"    background: #444444; \n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #555555;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #2c2c2c;\n"
"    color: #ffffff;\n"
"    border: 1px solid #444444;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background: transparent;\n"
"    padding: 6px 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background: #444444;\n"
"}\n"
"")
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuFinanceiro = QMenu(self.menubar)
        self.menuFinanceiro.setObjectName(u"menuFinanceiro")
        self.menuPDV = QMenu(self.menubar)
        self.menuPDV.setObjectName(u"menuPDV")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"QStatusBar {\n"
"    background-color: #2c2c2c;\n"
"    color: #ffffff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border-top: 1px solid #444444;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 2px 6px;\n"
"}\n"
"")
        frm_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menubar.addAction(self.menuPDV.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuCadastro.addSeparator()
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.actionCliente)
        self.menuCadastro.addAction(self.actionFornecedor)
        self.menuCadastro.addAction(self.actionProdutos)
        self.menuCadastro.addAction(self.actionTarefas)
        self.menuCadastro.addAction(self.actionFuncion_rio)
        self.menuFinanceiro.addAction(self.actionBanco)
        self.menuFinanceiro.addAction(self.actionContas_pagar)
        self.menuFinanceiro.addAction(self.actionContas_receber)

        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def botaoCliente(self):
        print('oi')

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.actionCliente.setText(QCoreApplication.translate("frm_main", u"Cliente", None))
        self.actionFornecedor.setText(QCoreApplication.translate("frm_main", u"Fornecedor", None))
        self.actionProdutos.setText(QCoreApplication.translate("frm_main", u"Produtos", None))
        self.actionTarefas.setText(QCoreApplication.translate("frm_main", u"Tarefas", None))
        self.actionBanco.setText(QCoreApplication.translate("frm_main", u"Banco", None))
        self.actionContas_pagar.setText(QCoreApplication.translate("frm_main", u"Contas a pagar", None))
        self.actionContas_receber.setText(QCoreApplication.translate("frm_main", u"Contas a receber", None))
        self.actionFuncion_rio.setText(QCoreApplication.translate("frm_main", u"Funcion\u00e1rio", None))
        self.btn_cliente.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_fornecedor.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_produtos.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_tarefas.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_vendas.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_pagar.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_receber.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.btn_bancos.setText(QCoreApplication.translate("frm_main", u"\u3164\u3164\n"
"\u3164\u3164\u3164\u3164\u3164\u3164\u3164", None))
        self.label.setText(QCoreApplication.translate("frm_main", u"<html><head/><body><p>\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164</p><p>\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164</p><p>\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164\u3164</p></body></html>", None))
        self.menuCadastro.setTitle(QCoreApplication.translate("frm_main", u"Cadastro", None))
        self.menuFinanceiro.setTitle(QCoreApplication.translate("frm_main", u"Financeiro", None))
        self.menuPDV.setTitle(QCoreApplication.translate("frm_main", u"PDV", None))
        self.menuSobre.setTitle(QCoreApplication.translate("frm_main", u"Sobre", None))
    # retranslateUi
        self.btn_cliente.clicked.connect(self.botaoCliente)

if __name__ == "__main__":
    app = QApplication([])
    frm_Main = QMainWindow()
    ui = Ui_frm_main()
    ui.setupUi(frm_Main)
    frm_Main.show()
    app.exec()