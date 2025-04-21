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

from frm_VendasDiarias import Ui_Frm_VendasDiarias

import mysql.connector
import pandas as pd
import Controle
import os

import icon_consultarBancos
import icon_voltar

class Ui_Frm_Bancos(object):
    def setupUi(self, Frm_Bancos):
        if not Frm_Bancos.objectName():
            Frm_Bancos.setObjectName(u"Frm_Bancos")
        Frm_Bancos.setFixedSize(1192, 641)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        Frm_Bancos.setWindowIcon(QIcon(caminho_icone))
        self.Frm_Bancos = Frm_Bancos
        Frm_Bancos.setStyleSheet(u"QWidget {\n"
"    background-color: #FA8072;\n"
"    border-radius: 8px;\n"
"}")
        self.label_Bancos = QLabel(Frm_Bancos)
        self.label_Bancos.setObjectName(u"label_Bancos")
        self.label_Bancos.setGeometry(QRect(530, 10, 141, 31))
        self.label_Bancos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.label_Gastos = QLabel(Frm_Bancos)
        self.label_Gastos.setObjectName(u"label_Gastos")
        self.label_Gastos.setGeometry(QRect(160, 50, 151, 31))
        self.label_Gastos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.labe_Lucros = QLabel(Frm_Bancos)
        self.labe_Lucros.setObjectName(u"labe_Lucros")
        self.labe_Lucros.setGeometry(QRect(870, 50, 151, 31))
        self.labe_Lucros.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.tableLucros = QTableWidget(Frm_Bancos)
        if (self.tableLucros.columnCount() < 4):
            self.tableLucros.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableLucros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableLucros.setObjectName(u"tableLucros")
        self.tableLucros.setGeometry(QRect(660, 100, 521, 271))
        self.tableLucros.setStyleSheet(u"QTableWidget, QTableView {\n"
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
        self.btn_Visualizar = QPushButton(Frm_Bancos)
        self.btn_Visualizar.setObjectName(u"btn_Visualizar")
        self.btn_Visualizar.setGeometry(QRect(440, 390, 321, 71))
        self.btn_Visualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #000000;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
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
        self.txt_gastos = QLineEdit(Frm_Bancos)
        self.txt_gastos.setObjectName(u"txt_gastos")
        self.txt_gastos.setEnabled(False)
        self.txt_gastos.setGeometry(QRect(300, 490, 281, 41))
        self.txt_gastos.setStyleSheet(u"QLineEdit {\n"
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
        self.label_SomaGastos = QLabel(Frm_Bancos)
        self.label_SomaGastos.setObjectName(u"label_SomaGastos")
        self.label_SomaGastos.setGeometry(QRect(10, 490, 281, 41))
        self.label_SomaGastos.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_lucros = QLineEdit(Frm_Bancos)
        self.txt_lucros.setObjectName(u"txt_lucros")
        self.txt_lucros.setEnabled(False)
        self.txt_lucros.setGeometry(QRect(900, 490, 281, 41))
        self.txt_lucros.setStyleSheet(u"QLineEdit {\n"
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
        self.label_SomaLucros = QLabel(Frm_Bancos)
        self.label_SomaLucros.setObjectName(u"label_SomaLucros")
        self.label_SomaLucros.setGeometry(QRect(620, 490, 271, 41))
        self.label_SomaLucros.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.tableGastos = QTableWidget(Frm_Bancos)
        if (self.tableGastos.columnCount() < 5):
            self.tableGastos.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableGastos.setObjectName(u"tableGastos")
        self.tableGastos.setGeometry(QRect(10, 100, 521, 271))
        self.tableGastos.setStyleSheet(u"QTableWidget, QTableView {\n"
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
        self.txt_gastos_2 = QLineEdit(Frm_Bancos)
        self.txt_gastos_2.setObjectName(u"txt_gastos_2")
        self.txt_gastos_2.setEnabled(False)
        self.txt_gastos_2.setGeometry(QRect(620, 560, 281, 51))
        self.txt_gastos_2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 32px; \n"
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
        self.label_SomaGastos_2 = QLabel(Frm_Bancos)
        self.label_SomaGastos_2.setObjectName(u"label_SomaGastos_2")
        self.label_SomaGastos_2.setGeometry(QRect(350, 570, 261, 41))
        self.label_SomaGastos_2.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_voltar = QPushButton(Frm_Bancos)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(1100, 560, 91, 81))
        self.btn_voltar.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_volt/retornar.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_voltar_2 = QPushButton(Frm_Bancos)
        self.btn_voltar_2.setObjectName(u"btn_voltar_2")
        self.btn_voltar_2.setGeometry(QRect(550, 100, 91, 81))
        self.btn_voltar_2.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/icon_BancosCon/consultar.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")

        self.retranslateUi(Frm_Bancos)

        QMetaObject.connectSlotsByName(Frm_Bancos)
    # setupUi

    def tabelaGastos(self):

        print('Conectando...')
        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
        print('Conexão bem-sucedida!')
        mycursor = mydb.cursor()

        consultaSQL = "SELECT * FROM `banco-gastos`"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        #criando dataframe
        df = pd.DataFrame(myresult, columns=["Nome", "Fornecedor", "Observação", "Valor", "Quantidade"])
        self.all_data = df

        #config da tabela
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableGastos.setColumnCount(numCols)
        self.tableGastos.setRowCount(numRows)
        self.tableGastos.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
                for j in range(numCols):
                        self.tableGastos.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
                        
        self.tableGastos.resizeColumnsToContents()
        self.tableGastos.resizeRowsToContents()

        mycursor.close()

    def tabelaLucros(self):

        mydb = mysql.connector.connect(
        host = Controle.host,
        user = Controle.user,
        password = Controle.password,
        database = Controle.database
        )
        print('Conexão bem-sucedida!')
        mycursor = mydb.cursor()

        consultaSQL = "SELECT * FROM `banco-lucros`"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["Nome", "Valor", "Observação", "Quantidade"])

        df.replace('', pd.NA, inplace=True) 
        df = df.dropna(how='any') 

        self.all_data = df

        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableLucros.setColumnCount(numCols)
        self.tableLucros.setRowCount(numRows)
        self.tableLucros.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
                for j in range(numCols):
                        self.tableLucros.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableLucros.resizeColumnsToContents()
        self.tableLucros.resizeRowsToContents()

        mycursor.close()

    def sairTela(self):
        self.Frm_Bancos.close()
        self.Frm_Bancos = None

    def SomaLucros(self):
        import re

        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )
        cursor = mydb.cursor()

        sql = "SELECT Valor, Quantidade FROM `banco-lucros`"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        cursor.close()
        mydb.close()

        valores = []
        for row in resultado:
                valor_raw = row[0]
                quantidade = row[1]

                if valor_raw is not None and str(valor_raw).strip() != "" and \
                quantidade is not None and str(quantidade).strip() != "":
                        
                        if isinstance(valor_raw, (float, int)):
                                valor_unitario = float(valor_raw)
                        else:
                                valor_str = str(valor_raw).replace("R$", "").strip()
                                valor_str = re.sub(r'\.(?=\d{3}(,|$))', '', valor_str)
                                valor_str = valor_str.replace(",", ".")
                                valor_unitario = float(valor_str)

                        total_item = valor_unitario * int(quantidade)
                        valores.append(total_item)

        somaL = sum(valores)
        self.txt_lucros.setText(f"R${somaL:,.2f}")
        Controle.somaLucros = somaL

    def SomaGastos(self):
        import re

        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )
        cursor = mydb.cursor()

        sql = "SELECT Valor FROM `banco-gastos`"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        cursor.close()
        mydb.close()

        valores = []
        for row in resultado:
                valor_raw = row[0]

                if valor_raw is not None and str(valor_raw).strip() != "":
                        if isinstance(valor_raw, (float, int)):
                                valor = float(valor_raw)
                        else:
                                valor_str = str(valor_raw).replace("R$", "").strip()
                                valor_str = re.sub(r'\.(?=\d{3}(,|$))', '', valor_str)
                                valor_str = valor_str.replace(",", ".")
                                valor = float(valor_str)

                valores.append(valor)

        somag = sum(valores)
        self.txt_gastos.setText(f"R${somag:,.2f}")
        Controle.somaGastos = somag

    def somaTotal(self):
        somaLucros = Controle.somaLucros
        somaGastos = Controle.somaGastos

        if isinstance(somaLucros, str):
                somaLucros = float(somaLucros.replace("R$", "").replace(".", "").replace(",", "."))
        
        if isinstance(somaGastos, str):
                somaGastos = float(somaGastos.replace("R$", "").replace(".", "").replace(",", "."))
        
        somaTotal = somaLucros - somaGastos 

        print(f"Soma Total (Lucros - Gastos): R$ {somaTotal:,.2f}")

        self.txt_gastos_2.setText(f"R$ {somaTotal:,.2f}")

    def atualizar_bancos(self):

        mydb = mysql.connector.connect(
            host=Controle.host,
            user=Controle.user,
            password=Controle.password,
            database=Controle.database
        )

        mycursor = mydb.cursor()

        mycursor.execute("""
            SELECT nome, valor FROM bancos
            WHERE Situação != 'PENDENTE'
        """)

        resultado = mycursor.fetchall()

        if resultado:
            for nome, valor in resultado:
                self.txt_NomeBanco.setText(nome) 
                self.txt_ValorBanco.setText(f"R${float(valor.replace('R$', '').replace(',', '.').strip()):,.2f}")
        else:
            self.txt_NomeBanco.setText("")
            self.txt_ValorBanco.setText("")

        mycursor.close()
        mydb.close()

    def consultar(self):
        if not hasattr(self, 'Frm_VendasDiarias') or self.frm_VendasDiarias is None or not self.Frm_VendasDiarias.isVisible():
                self.frm_VendasDiarias = QWidget()
                self.ui = Ui_Frm_VendasDiarias()
                self.ui.setupUi(self.frm_VendasDiarias)

                self.frm_VendasDiarias.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_VendasDiarias.destroyed.connect(lambda: setattr(self, 'Frm_Vendas Diarias', None))

                self.frm_VendasDiarias.show()
        else:
                self.frm_VendasDiarias.raise_()
                self.frm_VendasDiarias.activateWindow()

    def retranslateUi(self, Frm_Bancos):
        Frm_Bancos.setWindowTitle(QCoreApplication.translate("Frm_Bancos", u"Bancos", None))
        self.label_Bancos.setText(QCoreApplication.translate("Frm_Bancos", u"BANCOS", None))
        self.label_Gastos.setText(QCoreApplication.translate("Frm_Bancos", u"GASTOS:", None))
        self.labe_Lucros.setText(QCoreApplication.translate("Frm_Bancos", u"LUCROS:", None))
        ___qtablewidgetitem = self.tableLucros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frm_Bancos", u"Nome/Produtos", None));
        ___qtablewidgetitem1 = self.tableLucros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frm_Bancos", u"Valor", None));
        ___qtablewidgetitem2 = self.tableLucros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frm_Bancos", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem3 = self.tableLucros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frm_Bancos", u"Quantidade", None));
        self.btn_Visualizar.setText(QCoreApplication.translate("Frm_Bancos", u"VIZUALIZAR", None))
        self.label_SomaGastos.setText(QCoreApplication.translate("Frm_Bancos", u"Soma dos gastos:", None))
        self.label_SomaLucros.setText(QCoreApplication.translate("Frm_Bancos", u"Soma dos lucros:", None))
        ___qtablewidgetitem4 = self.tableGastos.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frm_Bancos", u"Nome", None));
        ___qtablewidgetitem5 = self.tableGastos.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Frm_Bancos", u"Fornecedor", None));
        ___qtablewidgetitem6 = self.tableGastos.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Frm_Bancos", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem7 = self.tableGastos.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Frm_Bancos", u"Valor", None));
        ___qtablewidgetitem8 = self.tableGastos.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Frm_Bancos", u"Total", None));
        self.txt_gastos_2.setText(QCoreApplication.translate("Frm_Bancos", u"R$", None))
        self.label_SomaGastos_2.setText(QCoreApplication.translate("Frm_Bancos", u"Resultado Final:", None))
        self.btn_voltar.setText("")
        self.btn_voltar_2.setText("")
    # retranslateUi
        self.btn_Visualizar.clicked.connect(self.tabelaGastos)
        self.btn_Visualizar.clicked.connect(self.tabelaLucros)
        self.btn_Visualizar.clicked.connect(self.SomaLucros)
        self.btn_Visualizar.clicked.connect(self.SomaGastos)
        self.btn_Visualizar.clicked.connect(self.somaTotal)
        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_voltar_2.clicked.connect(self.consultar)

if __name__ == "__main__":
    app = QApplication([])
    frm_Bancos = QWidget()
    ui = Ui_Frm_Bancos()
    ui.setupUi(frm_Bancos)
    frm_Bancos.show()
    app.exec()

