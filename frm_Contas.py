from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget, QMessageBox)
import icon_adicionar
import icon_attConta
import icon_consultar
import icon_excluir
import icon_filtro
import icon_pesquisar
import icon_voltar
import icon_alterar

import pandas as pd
import Controle
import mysql.connector
import os

from frm_DadosContas import Ui_frm_DadosContas
#testando

class Ui_frm_Contas(object):
    def setupUi(self, frm_Contas):
        if not frm_Contas.objectName():
            frm_Contas.setObjectName(u"frm_Contas")
        frm_Contas.setFixedSize(953, 593)
        self.frm_Contas = frm_Contas
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Contas.setWindowIcon(QIcon(caminho_icone))
        frm_Contas.setStyleSheet(u"QWidget{\n"
"	background-color: #4E342E;\n"
"\n"
"}")
        self.btn_Add = QPushButton(frm_Contas)
        self.btn_Add.setObjectName(u"btn_Add")
        self.btn_Add.setGeometry(QRect(0, 0, 91, 81))
        self.btn_Add.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_add/adicionar.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6CBA8; \n"
"    color: #5D3A00;\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C19A6B; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px;\n"
"    padding-left: 2px;\n"
"}")
        self.btn_voltar = QPushButton(frm_Contas)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(860, 510, 91, 81))
        self.btn_voltar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_volt/retornar.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #83C5BE;\n"
"    box-shadow: none; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}")
        self.btn_consul = QPushButton(frm_Contas)
        self.btn_consul.setObjectName(u"btn_consul")
        self.btn_consul.setGeometry(QRect(180, 0, 91, 81))
        self.btn_consul.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_alt/consultar.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6CBA8; \n"
"    color: #5D3A00;\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C19A6B; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px;\n"
"    padding-left: 2px;\n"
"}")
        self.btn_alterar = QPushButton(frm_Contas)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setGeometry(QRect(90, 0, 91, 81))
        self.btn_alterar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_alt/alterar.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6CBA8; \n"
"    color: #5D3A00;\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C19A6B; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px;\n"
"    padding-left: 2px;\n"
"}\n"
"")
        self.btn_excluir = QPushButton(frm_Contas)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(0, 510, 91, 81))
        self.btn_excluir.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_exc/excluir.png);\n"
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
        self.btn_pesquisar = QPushButton(frm_Contas)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setGeometry(QRect(540, 110, 21, 21))
        self.btn_pesquisar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_pesq/pesquisar.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFFFFF;\n"
"    box-shadow: none; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}\n"
"")
        self.lbl_Contas = QLabel(frm_Contas)
        self.lbl_Contas.setObjectName(u"lbl_Contas")
        self.lbl_Contas.setGeometry(QRect(0, 110, 161, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_Contas.setFont(font)
        self.lbl_Contas.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeContas = QLineEdit(frm_Contas)
        self.txt_nomeContas.setObjectName(u"txt_nomeContas")
        self.txt_nomeContas.setGeometry(QRect(160, 100, 371, 41))
        font1 = QFont()
        self.txt_nomeContas.setFont(font1)
        self.txt_nomeContas.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.btn_filtro = QPushButton(frm_Contas)
        self.btn_filtro.setObjectName(u"btn_filtro")
        self.btn_filtro.setGeometry(QRect(540, 80, 21, 21))
        self.btn_filtro.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 10px;\n"
"    color: #FFFFFF; \n"
"    background-image: url(:/icon_filt/filtro.png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFFFFF;\n"
"    box-shadow: none; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}\n"
"")
        self.tableWidget = QTableWidget(frm_Contas)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 170, 581, 321))
        self.tableWidget.setStyleSheet(u"QTableWidget, QTableView {\n"
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
        self.lbl_SomaDasDividas = QLabel(frm_Contas)
        self.lbl_SomaDasDividas.setObjectName(u"lbl_SomaDasDividas")
        self.lbl_SomaDasDividas.setGeometry(QRect(690, 140, 151, 16))
        self.lbl_SomaDasDividas.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_SomaDividas = QLineEdit(frm_Contas)
        self.txt_SomaDividas.setObjectName(u"txt_SomaDividas")
        self.txt_SomaDividas.setEnabled(False)
        self.txt_SomaDividas.setGeometry(QRect(610, 170, 321, 41))
        self.txt_SomaDividas.setFont(font1)
        self.txt_SomaDividas.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_MaiorDivida = QLineEdit(frm_Contas)
        self.txt_MaiorDivida.setObjectName(u"txt_MaiorDivida")
        self.txt_MaiorDivida.setEnabled(False)
        self.txt_MaiorDivida.setGeometry(QRect(610, 260, 321, 41))
        self.txt_MaiorDivida.setFont(font1)
        self.txt_MaiorDivida.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_MaiorDivida = QLabel(frm_Contas)
        self.lbl_MaiorDivida.setObjectName(u"lbl_MaiorDivida")
        self.lbl_MaiorDivida.setGeometry(QRect(710, 230, 111, 16))
        self.lbl_MaiorDivida.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_MaiorValor = QLineEdit(frm_Contas)
        self.txt_MaiorValor.setObjectName(u"txt_MaiorValor")
        self.txt_MaiorValor.setEnabled(False)
        self.txt_MaiorValor.setGeometry(QRect(610, 350, 321, 41))
        self.txt_MaiorValor.setFont(font1)
        self.txt_MaiorValor.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"    color: #000000; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.label_3 = QLabel(frm_Contas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 320, 181, 16))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_atualizar = QPushButton(frm_Contas)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setGeometry(QRect(870, 130, 31, 31))
        self.btn_atualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 14px;\n"
"    color: #FFFFFF; \n"
"    background-image:url(:/icon_attConta/atualizar (1).png); \n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"    font-size: 14px; \n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); \n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFFFFF;\n"
"    box-shadow: none; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}\n"
"")

        self.retranslateUi(frm_Contas)

        QMetaObject.connectSlotsByName(frm_Contas)
    # setupUi

    def sairTela(self, frm_Contas):
        self.frm_Contas.close()
        self.frm_Contas = None

    def consultarGeral(self):
        print("Conectando")
        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database
        )
        print("Conexão bem sucedida")
        mycursor = mydb.cursor()
        nomeConsulta = self.txt_nomeContas.text()
        consultaSQL = "SELECT * FROM contas WHERE Nome LIKE '" + nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idContas", "Nome", "Emissão", "Vencimento", "Fornecedor", "Observação", "Valor", "Parcelas", "Forma de pagamento", "Situação"])
        self.all_data = df

        #Criando a tabela
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(numCols):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        mydb.close()

    def pesquisarContas(self):
        print("Conectando")
        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database
        )

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeContas.text()
        consultaSQL = "SELECT * FROM contas WHERE nome LIKE     %s"
        mycursor.execute(consultaSQL, ('%' + nomeConsulta + '%',))

        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idContas","Nome", "Emissão", "Vencimento", "Fornecedor", "Observação", "Valor", "Parcelas", "Forma de pagamento", "Situação"])
        self.all_data = df

        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(numCols):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
        mydb.close()

    def cadastrarContas(self):
        Controle.tiposTelaDadosCliente = "incluir"
        if not hasattr(self, 'frm_DadosContas') or self.frm_DadosContas is None or not self.frm_DadosContas.isVisible():

            self.frm_DadosContas = QWidget()
            self.ui = Ui_frm_DadosContas()
            self.ui.setupUi(self.frm_DadosContas)

            self.frm_DadosContas.setAttribute(Qt.WA_DeleteOnClose)
            self.frm_DadosContas.destroyed.connect(lambda: setattr(self, 'frm_DadosContas', None))

            self.frm_DadosContas.show()
        
        else:
            self.frm_DadosContas.raise_()
            self.frm_DadosContas.activateWindow()

    def alterarContas(self):
        Controle.tiposTelaDadosCliente = 'alterar'
        print('frm_DadosContas', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()
    
        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro de Seleção')
            msg.setText('Por favor, selecione alguma conta para alterar')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return #Retorna e não prossegue
        
        item = self.tableWidget.item(line, 0)
        
        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosContas') or self.frm_DadosContas is None or not self.frm_DadosContas.isVisible():
                self.frm_DadosContas = QWidget()
                self.ui = Ui_frm_DadosContas()
                self.ui.setupUi(self.frm_DadosContas)

                self.frm_DadosContas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosContas.destroyed.connect(lambda: setattr(self, 'frm_DadosContas', None))

                self.frm_DadosContas.show()
            
            else:
                self.frm_DadosContas.raise_()
                self.frm_DadosContas.activateWindow()

    def excluirContas(self):

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('Por favor, selecione uma conta para excluir.')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return #Retorna se a codição for falsa

        item = self.tableWidget.item(line, 0)

        if item:
            idConta = item.text()
            mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
            )

            mycursor = mydb.cursor()
            sql = "DELETE FROM contas WHERE idContas = %s"
            mycursor.execute(sql, (idConta,))
            mydb.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Conta excluída')
            msg.setText('Conta excluída com sucesso!')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

            mycursor.execute("SELECT * FROM contas")
            myresult = mycursor.fetchall()
            df = pd.DataFrame(myresult, columns=['idContas', 'Nome', 'Emissão', 'Vencimento', 'Fornecedor', 'Observação', 'Valor', 'Parcelas', 'Forma de pagamento', 'Situação'])
            self.all_data = df

            numRows = len(self.all_data.index)
            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(numRows)
            self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(numRows):
                for j in range(len(self.all_data.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
            
            self.tableWidget.resizeRowsToContents()


            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.resizeRowsToContents()

            mydb.close()

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Erro seleção')
            msg.setText('Conta não selecionada!')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def consultarContas(self):
        Controle.tiposTelaDadosCliente = 'consultar'
        print('frm_Contas', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()
        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('ERRO!')
            msg.setText('Por favor, selecione uma Conta para consultar.')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
        
        item = self.tableWidget.item(line, 0)
        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosContas') or self.frm_DadosContas is None or not self.frm_DadosContas.isVisible():
                self.frm_DadosContas = QWidget()
                self.ui = Ui_frm_DadosContas()
                self.ui.setupUi(self.frm_DadosContas)

                self.frm_DadosContas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosContas.destroyed.connect(lambda: setattr(self, 'frm_DadosContas', None))

                self.frm_DadosContas.show()
            
            else:
                self.frm_DadosContas.raise_()
                self.frm_DadosContas.activateWindow()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Erro de Seleção")
            msg.setText("Não foi possível obter o ID da conta selecionada.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def visualizar(self):
        mydb = mysql.connector.connect(
            host=Controle.host,
            user=Controle.user,
            password=Controle.password,
            database=Controle.database
        )

        mycursor = mydb.cursor()

        # Ajuste na query para desconsiderar valores com 'pago'
        mycursor.execute("""
            SELECT nome, valor FROM contas 
            WHERE Situação != 'pago' 
            ORDER BY CAST(REPLACE(valor, 'R$', '') AS DECIMAL(10,2)) DESC 
            LIMIT 1
        """)
        resultado = mycursor.fetchone()

        if resultado:
            nome_maior_divida, maior_valor = resultado
            
            print(f"Maior dívida encontrada: {nome_maior_divida} - {maior_valor}")  # Debug

            # Removendo "R$" e garantindo que seja número
            maior_valor = float(maior_valor.replace("R$", "").replace(",", ".").strip())  # Substitui a vírgula por ponto

            # Atualiza os campos de texto
            self.txt_MaiorDivida.setText(nome_maior_divida)
            self.txt_MaiorValor.setText(f"R${maior_valor:,.2f}".replace(",", "."))  # Formato correto
        else:
            # Caso não tenha nenhuma dívida pendente, limpar os campos
            self.txt_MaiorDivida.setText("")
            self.txt_MaiorValor.setText("")

        mycursor.close()

    def calcular_total_dividas(self):
        conexao = mysql.connector.connect(
            host=Controle.host,
            user=Controle.user,
            password=Controle.password,
            database=Controle.database
        )

        cursor = conexao.cursor()

        # Query para somar todos os valores, ignorando as contas com a situação 'pago'
        cursor.execute("""
            SELECT SUM(CAST(REPLACE(valor, 'R$', '') AS DECIMAL(10,2))) 
            FROM contas 
            WHERE Situação != 'pago'
        """)
        total_dividas = cursor.fetchone()[0]  # Pega o resultado da soma

        if total_dividas is None:  
            total_dividas = 0.0  # Caso não tenha nenhuma dívida, define como 0

        print(f"Total de dívidas: R${total_dividas:,.2f}")  # Debug

        # Exibir no campo de texto
        self.txt_SomaDividas.setText(f"R${total_dividas:,.2f}".replace(",", "."))  

        cursor.close()
        conexao.close()



    def retranslateUi(self, frm_Contas):
        frm_Contas.setWindowTitle(QCoreApplication.translate("frm_Contas", u"Contas", None))
        self.btn_Add.setText("")
        self.btn_voltar.setText("")
        self.btn_consul.setText("")
        self.btn_alterar.setText("")
        self.btn_excluir.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_Contas.setText(QCoreApplication.translate("frm_Contas", u"Contas para pagar:", None))
        self.btn_filtro.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Contas", u"idContas", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Contas", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Contas", u"Emiss\u00e3o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Contas", u"Vencimento", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Contas", u"Fornecedor", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_Contas", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_Contas", u"Valor", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_Contas", u"Parcelas", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_Contas", u"Forma de pagamento", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("frm_Contas", u"Situa\u00e7\u00e3o", None));
        self.lbl_SomaDasDividas.setText(QCoreApplication.translate("frm_Contas", u"Soma das D\u00edvidas:", None))
        self.lbl_MaiorDivida.setText(QCoreApplication.translate("frm_Contas", u"Maior D\u00edvida:", None))
        self.label_3.setText(QCoreApplication.translate("frm_Contas", u"Valor da maior d\u00edvida:", None))
        self.btn_atualizar.setText("")
    # retranslateUi

        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_filtro.clicked.connect(self.consultarGeral)
        self.btn_pesquisar.clicked.connect(self.pesquisarContas)
        self.btn_Add.clicked.connect(self.cadastrarContas)
        self.btn_alterar.clicked.connect(self.alterarContas)
        self.btn_excluir.clicked.connect(self.excluirContas)
        self.btn_consul.clicked.connect(self.consultarContas)
        self.btn_atualizar.clicked.connect(self.visualizar)
        self.btn_atualizar.clicked.connect(self.calcular_total_dividas)

if __name__ == "__main__":
    app = QApplication([])
    frm_Contas = QWidget()
    ui = Ui_frm_Contas()
    ui.setupUi(frm_Contas)
    frm_Contas.show()
    app.exec()