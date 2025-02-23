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

from frm_DadosValores import Ui_frm_DadosValores

import mysql.connector
import Controle
import pandas as pd
import os

import icon_adicionar
import icon_attValores
import icon_consultar
import icon_excluir
import icon_filtro
import icon_pesquisar
import icon_voltar
import icon_alterar

class Ui_frm_ValoresAReceber(object):
    def setupUi(self, frm_ValoresAReceber):
        if not frm_ValoresAReceber.objectName():
            frm_ValoresAReceber.setObjectName(u"frm_ValoresAReceber")
        frm_ValoresAReceber.setFixedSize(952, 593)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_ValoresAReceber.setWindowIcon(QIcon(caminho_icone))
        self.frm_ValoresAReceber = frm_ValoresAReceber
        frm_ValoresAReceber.setStyleSheet(u"QWidget{\n"
"	background-color: #40E0D0;\n"
"\n"
"}")
        self.btn_Add = QPushButton(frm_ValoresAReceber)
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
        self.btn_voltar = QPushButton(frm_ValoresAReceber)
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
        self.btn_consul = QPushButton(frm_ValoresAReceber)
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
        self.btn_alterar = QPushButton(frm_ValoresAReceber)
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
        self.btn_excluir = QPushButton(frm_ValoresAReceber)
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
        self.btn_pesquisar = QPushButton(frm_ValoresAReceber)
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
        self.lbl_Contas = QLabel(frm_ValoresAReceber)
        self.lbl_Contas.setObjectName(u"lbl_Contas")
        self.lbl_Contas.setGeometry(QRect(10, 110, 151, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_Contas.setFont(font)
        self.lbl_Contas.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeContas = QLineEdit(frm_ValoresAReceber)
        self.txt_nomeContas.setObjectName(u"txt_nomeContas")
        self.txt_nomeContas.setGeometry(QRect(170, 100, 361, 41))
        font1 = QFont()
        self.txt_nomeContas.setFont(font1)
        self.txt_nomeContas.setStyleSheet(u"QLineEdit {\n"
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
        self.btn_filtro = QPushButton(frm_ValoresAReceber)
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
        self.tableWidget = QTableWidget(frm_ValoresAReceber)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
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
        self.txt_MaiorValorAReceber = QLineEdit(frm_ValoresAReceber)
        self.txt_MaiorValorAReceber.setObjectName(u"txt_MaiorValorAReceber")
        self.txt_MaiorValorAReceber.setEnabled(False)
        self.txt_MaiorValorAReceber.setGeometry(QRect(610, 370, 321, 41))
        self.txt_MaiorValorAReceber.setFont(font1)
        self.txt_MaiorValorAReceber.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_MaiorValor = QLabel(frm_ValoresAReceber)
        self.lbl_MaiorValor.setObjectName(u"lbl_MaiorValor")
        self.lbl_MaiorValor.setGeometry(QRect(680, 340, 181, 16))
        self.lbl_MaiorValor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_NomeDoMaiorValorReceber = QLineEdit(frm_ValoresAReceber)
        self.txt_NomeDoMaiorValorReceber.setObjectName(u"txt_NomeDoMaiorValorReceber")
        self.txt_NomeDoMaiorValorReceber.setEnabled(False)
        self.txt_NomeDoMaiorValorReceber.setGeometry(QRect(610, 280, 321, 41))
        self.txt_NomeDoMaiorValorReceber.setFont(font1)
        self.txt_NomeDoMaiorValorReceber.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_NomeMaiorValor = QLabel(frm_ValoresAReceber)
        self.lbl_NomeMaiorValor.setObjectName(u"lbl_NomeMaiorValor")
        self.lbl_NomeMaiorValor.setGeometry(QRect(640, 250, 261, 20))
        self.lbl_NomeMaiorValor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_SomaDosValores = QLineEdit(frm_ValoresAReceber)
        self.txt_SomaDosValores.setObjectName(u"txt_SomaDosValores")
        self.txt_SomaDosValores.setEnabled(False)
        self.txt_SomaDosValores.setGeometry(QRect(610, 190, 321, 41))
        self.txt_SomaDosValores.setFont(font1)
        self.txt_SomaDosValores.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_SomaDosValores = QLabel(frm_ValoresAReceber)
        self.lbl_SomaDosValores.setObjectName(u"lbl_SomaDosValores")
        self.lbl_SomaDosValores.setGeometry(QRect(690, 160, 151, 16))
        self.lbl_SomaDosValores.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_atualizar = QPushButton(frm_ValoresAReceber)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setGeometry(QRect(860, 150, 31, 31))
        self.btn_atualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #EDE7F6;\n"
"    border: 2px solid #83C5BE; \n"
"    border-radius: 14px;\n"
"    color: #FFFFFF; \n"
"    background-image:url(:/icon_attValor/atualizar (1).png); \n"
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

        self.retranslateUi(frm_ValoresAReceber)

        QMetaObject.connectSlotsByName(frm_ValoresAReceber)
    # setupUi

    def sairTela(self, frm_ValoresAReceber):
        self.frm_ValoresAReceber.close()
        self.frm_ValoresAReceber = None

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
        nomeConsulta = self.txt_nomeContas.text() #Esqueci de trocar o nome da variavel
        consultaSQL = "SELECT * FROM valores WHERE Nome LIKE '" + nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idValores", "Nome", "Emissão", "Vencimento", "Observação", "Valor", "Parcelas", "Forma de pagamento", "Situação"])
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

    def pesquisarValores(self):

        print("Conectando")
        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database
        )

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeContas.text() #Esqueci de mudar o nome da variavel
        consultaSQL = "SELECT * FROM valores WHERE nome LIKE     %s"
        mycursor.execute(consultaSQL, ('%' + nomeConsulta + '%',))

        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idValores", "Nome", "Emissão", "Vencimento", "Observação", "Valor", "Parcelas", "Forma de pagamento", "Situação"])
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

    def cadastrarValores(self):
        Controle.tiposTelaDadosCliente = 'incluir'
        if not hasattr(self, 'frm_DadosValores') or self.frm_DadosValores is None or not self.frm_ValoresAReceber.isVisible():

            self.frm_DadosValores = QWidget()
            self.ui = Ui_frm_DadosValores()
            self.ui.setupUi(self.frm_DadosValores)

            self.frm_DadosValores.setAttribute(Qt.WA_DeleteOnClose)
            self.frm_DadosValores.destroyed.connect(lambda: setattr(self, 'frm_DadosValores', None))

            self.frm_DadosValores.show()

        else:
            self.frm_DadosValores.raise_()
            self.frm_DadosValores.activateWindow()

    def alterarValores(self):
        
        Controle.tiposTelaDadosCliente = 'alterar'
        print('frm_DadosValores', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle("Erro de seleção")
            msg.setText('Por favor selecione um valor para alterar')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
        
        item = self.tableWidget.item(line, 0)

        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosValores') or self.frm_DadosValores is None or not self.frm_ValoresAReceber.isVisible():

                self.frm_DadosValores = QWidget()
                self.ui = Ui_frm_DadosValores()
                self.ui.setupUi(self.frm_DadosValores)

                self.frm_DadosValores.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosValores.destroyed.connect(lambda: setattr(self, 'frm_DadosValores', None))

                self.frm_DadosValores.show()

            else:
                self.frm_DadosValores.raise_()
                self.frm_DadosValores.activateWindow()

    def excluirContas(self):

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('Por favor, selecione um valor para excluir.')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return #Retorna se a codição for falsa
        
        item = self.tableWidget.item(line, 0)

        if item:
            idValor = item.text()
            mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
            )

            mycursor = mydb.cursor()
            sql = "DELETE FROM valores WHERE idValores = %s"
            mycursor.execute(sql, (idValor,))
            mydb.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Conta excluída')
            msg.setText('Conta excluída com sucesso!')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

            mycursor.execute("SELECT * FROM valores")
            myresult = mycursor.fetchall()
            df = pd.DataFrame(myresult, columns=['idValores', 'Nome', 'Emissão', 'Vencimento', 'Observação', 'Valor', 'Parcelas', 'Forma de pagamento', 'Situação'])
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
            msg.setText('Valor não selecionado!')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def consultarValores(self):
        Controle.tiposTelaDadosCliente = 'consultar'
        print('frm_DadosValores', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()
        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('ERRO!')
            msg.setText('Por favor, selecione um Valor para consultar')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
    
        item = self.tableWidget.item(line, 0)
        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosValores') or self.frm_DadosValores is None or not self.frm_ValoresAReceber.isVisible():

                self.frm_DadosValores = QWidget()
                self.ui = Ui_frm_DadosValores()
                self.ui.setupUi(self.frm_DadosValores)

                self.frm_DadosValores.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosValores.destroyed.connect(lambda: setattr(self, 'frm_DadosValores', None))

                self.frm_DadosValores.show()

            else:
                self.frm_DadosValores.raise_()
                self.frm_DadosValores.activateWindow()

    def retranslateUi(self, frm_ValoresAReceber):
        frm_ValoresAReceber.setWindowTitle(QCoreApplication.translate("frm_ValoresAReceber", u"Valores a receber", None))
        self.btn_Add.setText("")
        self.btn_voltar.setText("")
        self.btn_consul.setText("")
        self.btn_alterar.setText("")
        self.btn_excluir.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_Contas.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Valores a receber:", None))
        self.btn_filtro.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_ValoresAReceber", u"idValores", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Emiss\u00e3o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Vencimento", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Valor", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Parcelas", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Forma de pagamento", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Situa\u00e7\u00e3o", None));
        self.lbl_MaiorValor.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Maior valor a receber:", None))
        self.lbl_NomeMaiorValor.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Nome do maior valor \u00e1 receber:", None))
        self.lbl_SomaDosValores.setText(QCoreApplication.translate("frm_ValoresAReceber", u"Soma dos valores:", None))
        self.btn_atualizar.setText("")
    # retranslateUi

        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_filtro.clicked.connect(self.consultarGeral)
        self.btn_pesquisar.clicked.connect(self.pesquisarValores)
        self.btn_Add.clicked.connect(self.cadastrarValores)
        self.btn_alterar.clicked.connect(self.alterarValores)
        self.btn_excluir.clicked.connect(self.excluirContas)
        self.btn_consul.clicked.connect(self.consultarValores)


if __name__ == "__main__":
    app = QApplication([])
    frm_ValoresAReceber = QWidget()
    ui = Ui_frm_ValoresAReceber()
    ui.setupUi(frm_ValoresAReceber)
    frm_ValoresAReceber.show()
    app.exec()