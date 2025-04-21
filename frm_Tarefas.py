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
from frm_DadosTarefas import Ui_frm_DadosTarefas

import mysql.connector
import pandas as pd
import Controle
import os

import icon_adicionar
import icon_consultar
import icon_excluir
import icon_filtro
import icon_pesquisar
import icon_voltar
import icon_alterar

class Ui_frm_Tarefas(object):
    def setupUi(self, frm_Tarefas):
        if not frm_Tarefas.objectName():
            frm_Tarefas.setObjectName(u"frm_Tarefas")
        frm_Tarefas.setFixedSize(581, 593)
        self.frm_Tarefas = frm_Tarefas
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Tarefas.setWindowIcon(QIcon(caminho_icone))
        frm_Tarefas.setStyleSheet(u"QWidget{\n"
"	background-color: #001F3F;\n"
"\n"
"}")
        self.btn_Add = QPushButton(frm_Tarefas)
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
        self.btn_voltar = QPushButton(frm_Tarefas)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(490, 510, 91, 81))
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
        self.btn_consul = QPushButton(frm_Tarefas)
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
        self.btn_alterar = QPushButton(frm_Tarefas)
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
        self.btn_excluir = QPushButton(frm_Tarefas)
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
        self.btn_pesquisar = QPushButton(frm_Tarefas)
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
        self.lbl_Tarefas = QLabel(frm_Tarefas)
        self.lbl_Tarefas.setObjectName(u"lbl_Tarefas")
        self.lbl_Tarefas.setGeometry(QRect(10, 110, 81, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_Tarefas.setFont(font)
        self.lbl_Tarefas.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeTarefas = QLineEdit(frm_Tarefas)
        self.txt_nomeTarefas.setObjectName(u"txt_nomeTarefas")
        self.txt_nomeTarefas.setGeometry(QRect(100, 100, 431, 41))
        font1 = QFont()
        self.txt_nomeTarefas.setFont(font1)
        self.txt_nomeTarefas.setStyleSheet(u"QLineEdit {\n"
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
        self.btn_filtro = QPushButton(frm_Tarefas)
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
        self.tableWidget = QTableWidget(frm_Tarefas)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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

        self.retranslateUi(frm_Tarefas)

        QMetaObject.connectSlotsByName(frm_Tarefas)
    # setupUi

    def sairTela(self):
        self.frm_Tarefas.close()
        self.frm_Tarefas = None

    def consultarGeral(self):

        print('Conectando...')
        mydb = mysql.connector.connect(
        host=Controle.host,
        user=Controle.user,
        password=Controle.password,
        database=Controle.database
        )
        print("Conexão bem-sucedida")

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeTarefas.text()

        consultaSQL = "SELECT * FROM tarefas WHERE Nome LIKE %s"

        mycursor.execute(consultaSQL, (nomeConsulta + '%',))
        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idTarefas", "Nome", "Início", "Fim", "Observação", "Situação"])
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

    def pesquisarGeral(self):

        print("Conectando")
        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database
        )

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeTarefas.text()
        consultaSQL = "SELECT * FROM tarefas WHERE Nome LIKE    %s"
        mycursor.execute(consultaSQL, ('%' + nomeConsulta + '%',))

        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idTarefas","Nome","Início","Fim","Observação","Situação"])
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

    def cadastrarTarefas(self):
        Controle.tiposTelaDadosCliente = "incluir"
        if not hasattr(self, 'frm_DadosTarefas') or self.frm_DadosTarefas is None or not self.frm_DadosTarefas.isVisible():
            self.frm_DadosTarefas = QWidget()
            self.ui = Ui_frm_DadosTarefas()
            self.ui.setupUi(self.frm_DadosTarefas)

            self.frm_DadosTarefas.setAttribute(Qt.WA_DeleteOnClose)
            self.frm_DadosTarefas.destroyed.connect(lambda: setattr(self, 'frm_DadosTarefas', None))

            self.frm_DadosTarefas.show()

        else:
            self.frm_DadosTarefas.raise_()
            self.frm_DadosTarefas.activateWindow()
    
    def alterarTarefas(self):
        Controle.tiposTelaDadosCliente = 'alterar'
        print('frm_DadosTarefas', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro de seleção')
            msg.setText('Por favor, selecione alguma tarefa para alterar')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        item = self.tableWidget.item(line, 0)

        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosTarefas') or self.frm_DadosTarefas is None or not self.frm_DadosTarefas.isVisible():
                self.frm_DadosTarefas = QWidget()
                self.ui = Ui_frm_DadosTarefas()
                self.ui.setupUi(self.frm_DadosTarefas)

                self.frm_DadosTarefas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosTarefas.destroyed.connect(lambda: setattr(self, 'frm_DadosTarefas', None))

                self.frm_DadosTarefas.show()

        else:
            self.frm_DadosTarefas.raise_()
            self.frm_DadosTarefas.activateWindow() 
    
    def consultarTarefas(self):
        Controle.tiposTelaDadosCliente = 'consultar'
        print('frm_Tarefas', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()
        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('ERRO!')
            msg.setText('Por favor, selecione uma Tarefa para consultar.')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
        
        item = self.tableWidget.item(line, 0)
        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosTarefas') or self.frm_DadosTarefas is None or not self.frm_DadosTarefas.isVisible():
                self.frm_DadosTarefas = QWidget()
                self.ui = Ui_frm_DadosTarefas()
                self.ui.setupUi(self.frm_DadosTarefas)

                self.frm_DadosTarefas.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosTarefas.destroyed.connect(lambda: setattr(self, 'frm_DadosTarefas', None))

                self.frm_DadosTarefas.show()

        else:
            self.frm_DadosTarefas.raise_()
            self.frm_DadosTarefas.activateWindow() 

    def excluirTarefas(self):

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('Por favor, selecione uma tarefa para excluir.')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 

        item = self.tableWidget.item(line, 0)

        if item:
            idTarefas = item.text()

            mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
            )

            mycursor = mydb.cursor()
            sql = "DELETE FROM tarefas WHERE idTarefas = %s"
            mycursor.execute(sql, (idTarefas,))
            mydb.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Tarefa excluída')
            msg.setText('Tarefa excluída com sucesso!')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

            mycursor.execute("SELECT * FROM tarefas")
            myresult = mycursor.fetchall()
            df = pd.DataFrame(myresult, columns=['idTarefas', 'Nome', 'Início', 'Fim', 'Observação', 'Situação'])
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
            msg.setText('Tarefa não selecionada!')
            caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
            msg.setWindowIcon(QIcon(caminho_icone))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def retranslateUi(self, frm_Tarefas):
        frm_Tarefas.setWindowTitle(QCoreApplication.translate("frm_Tarefas", u"Tarefas", None))
        self.btn_Add.setText("")
        self.btn_voltar.setText("")
        self.btn_consul.setText("")
        self.btn_alterar.setText("")
        self.btn_excluir.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_Tarefas.setText(QCoreApplication.translate("frm_Tarefas", u"Tarefas:", None))
        self.btn_filtro.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Tarefas", u"idTarefas", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Tarefas", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Tarefas", u"In\u00edcio", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Tarefas", u"Fim", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Tarefas", u"Observa\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_Tarefas", u"Situa\u00e7\u00e3o", None));
    # retranslateUi
        self.btn_filtro.clicked.connect(self.consultarGeral)
        self.btn_pesquisar.clicked.connect(self.pesquisarGeral)
        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_Add.clicked.connect(self.cadastrarTarefas)
        self.btn_alterar.clicked.connect(self.alterarTarefas)
        self.btn_consul.clicked.connect(self.consultarTarefas)
        self.btn_excluir.clicked.connect(self.excluirTarefas)

if __name__ == "__main__":
    app = QApplication([])
    frm_Tarefas = QWidget()
    ui = Ui_frm_Tarefas()
    ui.setupUi(frm_Tarefas)
    frm_Tarefas.show()
    app.exec()