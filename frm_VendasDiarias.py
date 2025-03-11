from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget, QMessageBox)
import icon_consultarVendas
import icon_voltar_banco

import sys
import os
import pandas as pd
import Controle
import mysql.connector

from frm_DadosConsultasV import Ui_frm_DadosConsultasV

class Ui_Frm_VendasDiarias(object):
    def setupUi(self, Frm_VendasDiarias):
        if not Frm_VendasDiarias.objectName():
            Frm_VendasDiarias.setObjectName(u"Frm_VendasDiarias")
        Frm_VendasDiarias.setFixedSize(772, 593)
        self.Frm_VendasDiarias = Frm_VendasDiarias
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        Frm_VendasDiarias.setWindowIcon(QIcon(caminho_icone))
        Frm_VendasDiarias.setStyleSheet(u"QWidget {\n"
"    background-color: #008080;\n"
"    border-radius: 8px;\n"
"}")
        self.labe_Lucros = QLabel(Frm_VendasDiarias)
        self.labe_Lucros.setObjectName(u"labe_Lucros")
        self.labe_Lucros.setGeometry(QRect(100, 60, 281, 31))
        self.labe_Lucros.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_Visualizar = QPushButton(Frm_VendasDiarias)
        self.btn_Visualizar.setObjectName(u"btn_Visualizar")
        self.btn_Visualizar.setGeometry(QRect(50, 450, 281, 61))
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
        self.btn_voltar = QPushButton(Frm_VendasDiarias)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(680, 510, 91, 81))
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
        self.comboBox = QComboBox(Frm_VendasDiarias)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(520, 110, 161, 51))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #008080;\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #00AFAF;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #00D7D7;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(imagens/seta-baixo.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #007070;\n"
"    border: 1px solid #00AFAF;\n"
"    selection-background-color: #00D7D7;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"/* Barra de rolagem */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #005F5F;\n"
"    width: 8px;\n"
"    margin: 2px 2px 2px 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #00AFAF;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:verti"
                        "cal:hover {\n"
"    background: #00D7D7;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}")
        self.labe_Lucros_2 = QLabel(Frm_VendasDiarias)
        self.labe_Lucros_2.setObjectName(u"labe_Lucros_2")
        self.labe_Lucros_2.setGeometry(QRect(560, 70, 71, 31))
        self.labe_Lucros_2.setStyleSheet(u"QLabel {\n"
"    font-size: 22px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.tableWidget = QTableWidget(Frm_VendasDiarias)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 110, 431, 321))
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
        self.btn_consul = QPushButton(Frm_VendasDiarias)
        self.btn_consul.setObjectName(u"btn_consul")
        self.btn_consul.setGeometry(QRect(360, 440, 81, 81))
        self.btn_consul.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_consultar/consultar.png);\n"
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
        self.txt_nomeProduto = QLineEdit(Frm_VendasDiarias)
        self.txt_nomeProduto.setObjectName(u"txt_nomeProduto")
        self.txt_nomeProduto.setEnabled(False)
        self.txt_nomeProduto.setGeometry(QRect(500, 230, 211, 41))
        self.txt_nomeProduto.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc;\n"
"	color: #000000;\n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: ;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_nome = QLabel(Frm_VendasDiarias)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(460, 190, 281, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_ValorMaior = QLineEdit(Frm_VendasDiarias)
        self.txt_ValorMaior.setObjectName(u"txt_ValorMaior")
        self.txt_ValorMaior.setEnabled(False)
        self.txt_ValorMaior.setGeometry(QRect(500, 330, 211, 41))
        self.txt_ValorMaior.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc;\n"
"	color: #000000;\n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: ;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_nome_2 = QLabel(Frm_VendasDiarias)
        self.lbl_nome_2.setObjectName(u"lbl_nome_2")
        self.lbl_nome_2.setGeometry(QRect(520, 290, 181, 21))
        self.lbl_nome_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_SomaTotal = QLineEdit(Frm_VendasDiarias)
        self.txt_SomaTotal.setObjectName(u"txt_SomaTotal")
        self.txt_SomaTotal.setEnabled(False)
        self.txt_SomaTotal.setGeometry(QRect(500, 430, 211, 41))
        self.txt_SomaTotal.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc;\n"
"	color: #000000;\n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: ;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_nome_3 = QLabel(Frm_VendasDiarias)
        self.lbl_nome_3.setObjectName(u"lbl_nome_3")
        self.lbl_nome_3.setGeometry(QRect(550, 390, 121, 21))
        self.lbl_nome_3.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.retranslateUi(Frm_VendasDiarias)

        QMetaObject.connectSlotsByName(Frm_VendasDiarias)
    # setupUi

    def sairTela(self):
        self.Frm_VendasDiarias.close()

    def adicionarData(self):
        print('Conectando...')
        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )
        print('Conexão bem-sucedida!')

        mycursor = mydb.cursor()
        consultaSQL = "SELECT DISTINCT Data FROM `vendas-consulta`"  
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()
        
        self.comboBox.clear()  

        for row in myresult:
                self.comboBox.addItem(str(row[0]))  

        mycursor.close()
        mydb.close()

    def filtrarPorData(self):
        data_selecionada = self.comboBox.currentText() 
        if not data_selecionada:
                print("Nenhuma data selecionada.")
                return
        
        print(f"Buscando vendas para a data: {data_selecionada}")

        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )
        
        mycursor = mydb.cursor()
        consultaSQL = "SELECT * FROM `vendas-consulta` WHERE Data = %s"
        mycursor.execute(consultaSQL, (data_selecionada,))
        myresult = mycursor.fetchall()

        self.tableWidget.setRowCount(0)

        for row_data in myresult:
                row_number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, col_number, QTableWidgetItem(str(data)))

        mycursor.close()
        mydb.close()
        
    def visualizar(self):

        data_formatada = self.comboBox.currentText().strip() 


        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )

        mycursor = mydb.cursor()

        consulta = """
                SELECT `Nome/Produto`, 
                        CAST(REPLACE(valor, 'R$', '') AS DECIMAL(10,2)) AS valor_formatado
                FROM `vendas-consulta`
                WHERE Data = %s  -- Filtra pela data selecionada
                ORDER BY valor_formatado DESC 
                LIMIT 1
                """

        mycursor.execute(consulta, (data_formatada,))
        resultado = mycursor.fetchall()

        if resultado:
                nome_maior_divida, maior_valor = resultado[0]
                print(f'Maior valor encontrado: {nome_maior_divida} - R${maior_valor:,.2f}'.replace(",", "."))

                self.txt_nomeProduto.setText(nome_maior_divida)
                self.txt_ValorMaior.setText(f"R${maior_valor:,.2f}".replace(",", "."))

        else: 
                self.txt_nomeProduto.setText("")
                self.txt_ValorMaior.setText("")


        mycursor.close()
        mydb.close()

    def visualizarTotal(self):
        data_formatada = self.comboBox.currentText()  

        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )

        mycursor = mydb.cursor()

        consulta = "SELECT Valor, Quantidade FROM WHERE Data = %s"
        print("Query executada:", consulta, "| Data enviada:", data_formatada)

        mycursor.execute(consulta, (data_formatada,))
        resultado = mycursor.fetchall()

        print("Resultado:", resultado)

        if resultado:
                total = 0
                for valor, quantidade in resultado:
                        valor = str(valor).replace("R$", "").replace(",", ".").strip()
                        valor = float(valor) 
                        total += valor * quantidade

                self.txt_SomaTotal.setText(f"R${total:,.2f}")
        else:
                self.txt_SomaTotal.setText("R$0.00") 

    def consultar(self):
        Controle.tiposTelaDadosCliente = 'consultar'
        print('frm_VendasDiarias', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()

        if line == -1:
                msg = QMessageBox()
                msg.setWindowTitle('ERRO!')
                msg.setText('Por favor, selecione uma Venda para consultar.')
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        
        item = self.tableWidget.item(line, 0)
        if item:
                Controle.idConsulta = item.text()
                if not hasattr(self, 'frm_DadosConsultasV') or self.frm_DadosConsultasV is None or not self.frm_DadosConsultasV.isVisible():
                        self.frm_DadosConsultasV = QWidget()
                        self.ui = Ui_frm_DadosConsultasV()
                        self.ui.setupUi(self.frm_DadosConsultasV)

                        self.frm_DadosConsultasV.setAttribute(Qt.WA_DeleteOnClose)
                        self.frm_DadosConsultasV.destroyed.connect(lambda: setattr(self, 'frm_DadosConsultasV', None))

                        self.frm_DadosConsultasV.show()

        else:
            self.frm_DadosConsultasV.raise_()
            self.frm_DadosConsultasV.activateWindow() 

    def retranslateUi(self, Frm_VendasDiarias):
        Frm_VendasDiarias.setWindowTitle(QCoreApplication.translate("Frm_VendasDiarias", u"Vendas Diárias", None))
        self.labe_Lucros.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Consultar vendas", None))
        self.btn_Visualizar.setText(QCoreApplication.translate("Frm_VendasDiarias", u"VIZUALIZAR", None))
        self.btn_voltar.setText("")
        self.labe_Lucros_2.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Datas:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frm_VendasDiarias", u"idVendas", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Nome/Produto", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Data", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Valor", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Quantidade", None));
        self.btn_consul.setText("")
        self.txt_nomeProduto.setText("")
        self.lbl_nome.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Nome do produto de maior venda:", None))
        self.txt_ValorMaior.setText("")
        self.lbl_nome_2.setText(QCoreApplication.translate("Frm_VendasDiarias", u"Valor da maior venda:", None))
        self.txt_SomaTotal.setText("")
        self.lbl_nome_3.setText(QCoreApplication.translate("Frm_VendasDiarias", u"SOMA TOTAL:", None))
    # retranslateUi

        self.btn_Visualizar.clicked.connect(self.filtrarPorData)
        self.btn_Visualizar.clicked.connect(self.visualizar)
        self.adicionarData()
        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_Visualizar.clicked.connect(self.visualizarTotal)
        self.btn_consul.clicked.connect(self.consultar)
        
if __name__ == "__main__":
    app = QApplication([])
    frm_VendasDiarias = QWidget()
    ui = Ui_Frm_VendasDiarias()
    ui.setupUi(frm_VendasDiarias)
    frm_VendasDiarias.show()
    app.exec()