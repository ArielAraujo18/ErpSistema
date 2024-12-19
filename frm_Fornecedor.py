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

from frm_DadosFornecedor import Ui_frm_DadosFornecedor

import mysql.connector
import Controle
import pandas as pd

import icon_adicionar
import icon_consultar
import icon_excluir
import icon_filtro
import icon_pesquisar
import icon_voltar
import icon_alterar

class Ui_frm_Fornecedor(object):
    def setupUi(self, frm_Fornecedor):
        if not frm_Fornecedor.objectName():
            frm_Fornecedor.setObjectName(u"frm_Fornecedor")
        #frm_Fornecedor.resize(581, 592)
        frm_Fornecedor.setFixedSize(581, 592)
        frm_Fornecedor.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        frm_Fornecedor.setStyleSheet(u"QWidget{\n"
"	background-color: #264653;\n"
"\n"
"}")
        self.btn_Add = QPushButton(frm_Fornecedor)
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
"    background-color: #83C5BE;\n"
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
        self.btn_voltar = QPushButton(frm_Fornecedor)
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
"QPushButton:pressed {\n"
"    background-color: #7C3AED; \n"
"    color: #FFFFFF; \n"
"    padding-top: 2px; \n"
"    padding-left: 2px;\n"
"}")
        self.btn_consul = QPushButton(frm_Fornecedor)
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
"    background-color: #83C5BE;\n"
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
        self.btn_alterar = QPushButton(frm_Fornecedor)
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
"    background-color: #83C5BE;\n"
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
        self.btn_excluir = QPushButton(frm_Fornecedor)
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
        self.btn_pesquisar = QPushButton(frm_Fornecedor)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setGeometry(QRect(520, 70, 21, 21))
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
        self.lbl_nomeFornecedor = QLabel(frm_Fornecedor)
        self.lbl_nomeFornecedor.setObjectName(u"lbl_nomeFornecedor")
        self.lbl_nomeFornecedor.setGeometry(QRect(0, 110, 181, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_nomeFornecedor.setFont(font)
        self.lbl_nomeFornecedor.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeFornecedor = QLineEdit(frm_Fornecedor)
        self.txt_nomeFornecedor.setObjectName(u"txt_nomeFornecedor")
        self.txt_nomeFornecedor.setGeometry(QRect(180, 100, 371, 41))
        font1 = QFont()
        self.txt_nomeFornecedor.setFont(font1)
        self.txt_nomeFornecedor.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;"
"    transition: all 0.3s ease;\n"

"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"")
        self.btn_filtro = QPushButton(frm_Fornecedor)
        self.btn_filtro.setObjectName(u"btn_filtro")
        self.btn_filtro.setGeometry(QRect(520, 40, 21, 21))
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
        self.tableWidget = QTableWidget(frm_Fornecedor)
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

        self.retranslateUi(frm_Fornecedor)

        QMetaObject.connectSlotsByName(frm_Fornecedor)
    # setupUi
    ##Funções##
    def sairTela(self, frm_Fornecedor):
        frm_Fornecedor.close()
        self.frm_Fornecedor = None

    def consultarGeral(self):
        self.host = Controle.host
        self.user = Controle.user
        self.password = Controle.user
        self.database = Controle.database
        print('Conectando...')
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = 'Ariel',
                password = 'IRani18@#',
                database = 'sistema' 
        )
        print('Conexão bem sucedida!')
        mycursor = mydb.cursor()
        nomeConsulta = self.txt_nomeFornecedor.text()
        consultaSQL = "SELECT * FROM fornecedor WHERE `Razão Social` LIKE'" + nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        #Crianda DataFrame
        df = pd.DataFrame(myresult, columns=["idFornecedor", "Razão Social", "Contato", "Cnpj", "Cidade", "Rua", "Bairro", "Cep", "E-mail"])
        self.all_data = df

        #Configurando a tabela 
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        #Preenchendo a tabela
        for i in range(numRows):
                for j in range(numCols):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
        
        #Layout das colunas e linhas                
        self.tableWidget.resizeColumnsToContents()

        #Ajusta todas as linhas
        for row in range(self.tableWidget.rowCount()):
                self.tableWidget.resizeRowToContents(row)
                mydb.close()

    def pesquisarFornecedor(self):
         
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = 'Ariel',
                password = 'IRani18@#',
                database = 'sistema'
        )
        
        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeFornecedor.text().strip() #texto da caixa de pesquisa
        consultaSQL = 'SELECT * FROM fornecedor WHERE `Razão Social` LIKE %s'
        mycursor.execute(consultaSQL, ('%' + nomeConsulta + '%',)) #Parametro da consulta sql

        myresult = mycursor.fetchall() #resultados

        #Criando df
        df = pd.DataFrame(myresult, columns=['idFornecedor', 'Razão Social', 'Contato', 'Cnpj', 'Cidade', 'Rua', 'Bairro', 'Cep', 'E-mail'])
        self.all_data = df

        #Configurando a tbl no pyside
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        #tabela
        for i in range(numRows):
             for j in range(numCols):
                  self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
        
        #Layout das colunas e lines
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        mycursor.close()
    
    def cadastrarCliente(self):
        Controle.tiposTelaDadosCliente = 'incluir'
        if not hasattr(self, 'frm_DadosFornecedor') or self.frm_DadosFornecedor is None or not self.frm_DadosFornecedor.isVisible():
                #Criando a tela
                self.frm_DadosFornecedor= QWidget()
                self.ui = Ui_frm_DadosFornecedor()
                self.ui.setupUi(self.frm_DadosFornecedor)

                #remoção da ref para fechar janela
                self.frm_DadosFornecedor.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosFornecedor.destroyed.connect(lambda: setattr(self, 'frm_DadosFornecedor', None))

                self.frm_DadosFornecedor.show()
        else:
             #Traz a janela aberta
             self.frm_DadosFornecedor.raise__()
             self.frm_DadosFornecedor.activateWindow()



    def consultarFornecedor(self):
         
        Controle.tiposTelaDadosCliente = 'consultar'
        print('frmFornecedor', Controle.tiposTelaDadosCliente)

        #Verifica se há linha selecionada na tabela
        line = self.tableWidget.currentRow()

        #Se não houver linha selecionada na tabela
        if line == -1:
             msg = QMessageBox()
             msg.setWindowTitle('ERRO!')
             msg.setText('Por favor, selecione um Fornecedor para consultar.')
             msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
             msg.setIcon(QMessageBox.Warning)
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec()
             return
        
        item = self.tableWidget.item(line, 0) #primeiro item 
        
        if item: #Verifica se não é none
             Controle.idConsulta = item.text()
             if not hasattr(self, 'frm_DadosFornecedor') or self.frm_DadosFornecedor is None or not self.frm_DadosFornecedor.isVisible():
                #Cria a tela se não tiver aberta
                self.frm_DadosFornecedor = QWidget()
                self.ui = Ui_frm_DadosFornecedor()
                self.ui.setupUi(self.frm_DadosFornecedor)

                #Configuração para garantir a remoção da referência ao fechar a janela
                self.frm_DadosFornecedor.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosFornecedor.destroyed.connect(lambda: setattr(self, 'frm_DadosFornecedor', None))

                self.frm_DadosFornecedor.show()
             else:
                self.frm_DadosFornecedor.raise_()
                self.frm_DadosFornecedor.activateWindow()

        else:
             msg = QMessageBox()
             msg.setWindowTitle("Erro de Seleção")
             msg.setText("Não foi possível obter o ID do cliente selecionado.")
             msg.setIcon(QMessageBox.Warning)
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec()

    def alterarFornecedor(self):
        #Tipo da tela
        Controle.tiposTelaDadosCliente = 'alterar'
        print('frm_Fornecedor', Controle.tiposTelaDadosCliente)
        
        line = self.tableWidget.currentRow() 

        if line == -1: #Se não houver linha selecionada
             msg = QMessageBox()
             msg.setWindowTitle('Erro de Seleção')
             msg.setText('Por favor, selecione algum fornecedor para alterar')
             msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
             msg.setIcon(QMessageBox.Warning)
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec()
             return #Retorna e não prossegue
        
        item = self.tableWidget.item(line, 0) #primeiro cliente

        if item:
                Controle.idConsulta = item.text()
                if not hasattr(self, 'frm_DadosFornecedor') or self.frm_DadosFornecedor is None or not self.frm_DadosFornecedor.isVisible():
                        #Cria a tela se não tiver aberta
                        self.frm_DadosFornecedor = QWidget()
                        self.ui = Ui_frm_DadosFornecedor()
                        self.ui.setupUi(self.frm_DadosFornecedor)

                        #Configuração para garantir a remoção da referência ao fechar a janela
                        self.frm_DadosFornecedor.setAttribute(Qt.WA_DeleteOnClose)
                        self.frm_DadosFornecedor.destroyed.connect(lambda: setattr(self, 'frm_DadosFornecedor', None))

                        #Abre a tela
                        self.frm_DadosFornecedor.show()
                else:
                        self.frm_DadosFornecedor.raise_()
                        self.frm_DadosFornecedor.activateWindow()
        
    def excluirFornecedor(self):
        
        line = self.tableWidget.currentRow()

        if line == -1: #Sem linha selecionada
             msg = QMessageBox()
             msg.setWindowTitle('Erro!')
             msg.setText('Por favor, selecione um forncedor para excluir.')
             msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
             msg.setIcon(QMessageBox.Warning)
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec()
             return #Retorna se a codição for falsa
        
        item = self.tableWidget.item(line, 0) #Obtém o item da primeira coluna

        if item:
             idFornecedor = item.text()

             #Conexão com bd
             mydb = mysql.connector.connect(
                        host = 'localhost',
                        user = 'Ariel',
                        password = 'IRani18@#',
                        database = 'sistema' 
                )
             
             mycursor = mydb.cursor()
             sql = 'DELETE FROM fornecedor WHERE idFornecedor = %s'
             mycursor.execute(sql, (idFornecedor,))
             mydb.commit()

             msg = QMessageBox()
             msg.setWindowTitle('Fornecedor excluído')
             msg.setText('Fornecedor excluído com sucesso!')
             msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
             msg.setIcon(QMessageBox.Information)
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec()

             mycursor.execute('SELECT * FROM fornecedor')
             myresult = mycursor.fetchall()
             df = pd.DataFrame(myresult, columns=['idFornecedor', 'Razão Social', 'Contato', 'Cnpj', 'Cidade', 'Rua', 'Bairro', 'Cep', 'E-mail'])
             self.all_data = df

             numRows = len(self.all_data.index)
             self.tableWidget.setColumnCount(len(self.all_data.columns))
             self.tableWidget.setRowCount(numRows)
             self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

             for i in range(numRows):
                  for j in range(len(self.all_data.columns)):
                       self.tableWidget.setItem(i, j, QTableWidget(str(self.all_data.iat[i, j])))
        
             self.tableWidget.resizeColumnsToContents()
             self.tableWidget.resizeRowsToContents()

             mydb.close()
        
        else: 
             msg = QMessageBox()
             msg.setWindowTitle('Erro seleção')
             msg.setText('Fornecedor não selecionado!')
             msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
             msg.setIcon(QMessageBox.Warning)
             msg.setStandardButtons(QMessageBox.Ok)
             msg.exec()

    def retranslateUi(self, frm_Fornecedor):
        frm_Fornecedor.setWindowTitle(QCoreApplication.translate("frm_Fornecedor", u"Fornecedor", None))
        self.btn_Add.setText("")
        self.btn_voltar.setText("")
        self.btn_consul.setText("")
        self.btn_alterar.setText("")
        self.btn_excluir.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_nomeFornecedor.setText(QCoreApplication.translate("frm_Fornecedor", u"Nome do Fornecedor: ", None))
        self.btn_filtro.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Fornecedor", u"idFornecedor", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Fornecedor", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Fornecedor", u"Contato", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Fornecedor", u"Cnpj", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Fornecedor", u"Cidade", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_Fornecedor", u"Rua", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_Fornecedor", u"Bairro", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_Fornecedor", u"Cep", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_Fornecedor", u"E-mail", None));
    # retranslateUi

    #Botões
        self.btn_voltar.clicked.connect(lambda: self.sairTela(frm_Fornecedor))
        self.btn_filtro.clicked.connect(self.consultarGeral)
        self.btn_pesquisar.clicked.connect(self.pesquisarFornecedor)
        self.btn_Add.clicked.connect(self.cadastrarCliente)
        self.btn_consul.clicked.connect(self.consultarFornecedor)
        self.btn_alterar.clicked.connect(self.alterarFornecedor)
        self.btn_excluir.clicked.connect(self.excluirFornecedor)

if __name__ == "__main__":
    app = QApplication([])
    frm_Fornecedor= QWidget()
    ui = Ui_frm_Fornecedor()
    ui.setupUi(frm_Fornecedor)
    frm_Fornecedor.show()
    app.exec()