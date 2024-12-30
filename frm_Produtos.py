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
 
import Controle
from frm_DadosProdutos import Ui_frm_DadosProdutos

import mysql.connector
import pandas as pd

import icon_adicionar
import icon_consultar
import icon_excluir
import icon_filtro
import icon_pesquisar
import icon_voltar
import icon_alterar

class Ui_frm_Produtos(object):
    def setupUi(self, frm_Produtos):
        if not frm_Produtos.objectName():
            frm_Produtos.setObjectName(u"frm_Produtos")
        frm_Produtos.setFixedSize(581, 592)
        self.frm_Produtos = frm_Produtos
        frm_Produtos.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        frm_Produtos.setStyleSheet(u"QWidget{\n"
"	background-color: #FAF3E0;\n"
"\n"
"}")
        self.btn_Add = QPushButton(frm_Produtos)
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
        self.btn_voltar = QPushButton(frm_Produtos)
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
        self.btn_consul = QPushButton(frm_Produtos)
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
        self.btn_alterar = QPushButton(frm_Produtos)
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
        self.btn_excluir = QPushButton(frm_Produtos)
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
        self.btn_pesquisar = QPushButton(frm_Produtos)
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
        self.lbl_Produtos = QLabel(frm_Produtos)
        self.lbl_Produtos.setObjectName(u"lbl_Produtos")
        self.lbl_Produtos.setGeometry(QRect(0, 110, 151, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_Produtos.setFont(font)
        self.lbl_Produtos.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeFornecedor = QLineEdit(frm_Produtos)
        self.txt_nomeFornecedor.setObjectName(u"txt_nomeFornecedor")
        self.txt_nomeFornecedor.setGeometry(QRect(160, 100, 371, 41))
        font1 = QFont()
        self.txt_nomeFornecedor.setFont(font1)
        self.txt_nomeFornecedor.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"	color: #000000;\n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.btn_filtro = QPushButton(frm_Produtos)
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
        self.tableWidget = QTableWidget(frm_Produtos)
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

        self.retranslateUi(frm_Produtos)

        QMetaObject.connectSlotsByName(frm_Produtos)
    # setupUi
##Funções##
    def sairTela(self, frm_Produtos):
        self.frm_Produtos.close()
        self.frm_Produtos = None
 
    def consultarGeral(self):
        print('conectando')
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'Ariel',
            password = 'IRani18@#',
            database = 'sistema'
        )
        print('Conexão bem sucedida')
        mycursor = mydb.cursor()
        #Esqueci de mudar o nome do txt fornecedor para txtProdutos
        nomeConsulta = self.txt_nomeFornecedor.text()
        consultaSQL = "SELECT * FROM produtos WHERE Nome LIKE '" +  nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        #Criando Dataframe
        df = pd.DataFrame(myresult, columns=["idProdutos", "Nome", "Quantidade", "Valor", "Fornecedor", "Observação"])
        self.all_data = df

        #Criando a tabela
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        #Preenchendo a tabela
        for i in range(numRows):
            for j in range(numCols):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        #Layout das colunas e linhas
        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.resizeRowsToContents()

        mydb.close()

    def pesquisarProdutos(self):
        print('Conectando')
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'Ariel',
            password = 'IRani18@#',
            database = 'sistema'
        )

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeFornecedor.text()
        consultaSQL = "SELECT * FROM produtos WHERE nome LIKE %s"
        mycursor.execute(consultaSQL, ('%' + nomeConsulta + '%',))

        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["idProdutos", "Nome", "Quantidade", "Valor", "Fornecedor", "Observação"])
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
    def cadastrarProdutos(self):
        Controle.tiposTelaDadosCliente = "incluir"
        if not hasattr(self, 'frmDadosProdutos') or self.frm_DadosProdutos is None or not self.frm_DadosProdutos.isVisible():
            self.frm_DadosProdutos = QWidget()
            self.ui = Ui_frm_DadosProdutos()
            self.ui.setupUi(self.frm_DadosProdutos)

            self.frm_DadosProdutos.setAttribute(Qt.WA_DeleteOnClose)
            self.frm_DadosProdutos.destroyed.connect(lambda: setattr(self, 'frm_DadosProdutos', None))

            self.frm_DadosProdutos.show()

        else:
            self.frm_DadosProdutos.raise_()
            self.frm_DadosProdutos.activateWindow()

    def consultarProdutos(self):

        Controle.tiposTelaDadosCliente = 'consultar'
        print('frmFornecedor: ', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()
        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('ERRO!')
            msg.setText('Por favor, selecione um Fornecedor para consultar.')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        item = self.tableWidget.item(line, 0)
        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosProdutos') or self.frm_DadosProdutos is None or not self.frm_DadosProdutos.isVisible():
                #Cria a tabela se não tiver aberta
                self.frm_DadosProdutos = QWidget()
                self.ui = Ui_frm_DadosProdutos()
                self.ui.setupUi(self.frm_DadosProdutos)

                self.frm_DadosProdutos.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosProdutos.destroyed.connect(lambda: setattr(self, 'frm_DadosProdutos', None))

                self.frm_DadosProdutos.show()
            else:
                self.frm_DadosProdutos.raise_()
                self.frm_DadosProdutos.activateWindow()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Erro de Seleção")
            msg.setText("Não foi possível obter o ID do produto selecionado.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def alterarProdutos(self):
        Controle.tiposTelaDadosCliente = 'alterar'
        print('frm_Produtos ', Controle.tiposTelaDadosCliente)

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro de Seleção')
            msg.setText('Por favor, selecione algum produto para alterar')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return #Retorna e não prossegue

        item = self.tableWidget.item(line, 0)

        if item:
            Controle.idConsulta = item.text()
            if not hasattr(self, 'frm_DadosProdutos') or self.frm_DadosProdutos is None or not self.frm_DadosProdutos.isVisible():
                #Cria a tela
                self.frm_DadosProdutos = QWidget()
                self.ui = Ui_frm_DadosProdutos()
                self.ui.setupUi(self.frm_DadosProdutos)

                #Config para garantir a remoção da referência ao fechar a janela
                self.frm_DadosProdutos.setAttribute(Qt.WA_DeleteOnClose)
                self.frm_DadosProdutos.destroyed.connect(lambda: setattr(self, 'frm_DadosProdutos', None))

                self.frm_DadosProdutos.show()

            else: 
                self.frm_DadosProdutos.raise_()
                self.frm_DadosProdutos.activateWindow()
    def excluirProdutos(self):

        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle('Erro!')
            msg.setText('Por favor, selecione um produto para excluir.')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return #Retorna se a codição for falsa

        item = self.tableWidget.item(line, 0)

        if item:
            idProduto = item.text()
            mydb = mysql.connector.connect(
                        host = 'localhost',
                        user = 'Ariel',
                        password = 'IRani18@#',
                        database = 'sistema' 
                )
            
            mycursor = mydb.cursor()
            sql = "DELETE FROM produtos WHERE idProdutos = %s"
            mycursor.execute(sql, (idProduto,))
            mydb.commit()

            msg = QMessageBox()
            msg.setWindowTitle('Produto excluído')
            msg.setText('Produto excluído com sucesso!')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

            mycursor.execute("SELECT * FROM produtos")
            myresult = mycursor.fetchall()
            df = pd.DataFrame(myresult, columns=['idProdutos', 'Nome', 'Quantidade', 'Valor', 'Fornecedor', '`Observação`'])
            self.all_data = df

            numRows = len(self.all_data.index)
            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(numRows)
            self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(numRows):
                for j in range(len(self.all_data.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tableWidget.resizeColumnsToContents()

            # Redimensiona todas as linhas
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.resizeRowToContents(row)

            mydb.close()
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Erro seleção')
            msg.setText('Produto não selecionado!')
            msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


    def retranslateUi(self, frm_Produtos):
        frm_Produtos.setWindowTitle(QCoreApplication.translate("frm_Produtos", u"Produtos", None))
        self.btn_Add.setText("")
        self.btn_voltar.setText("")
        self.btn_consul.setText("")
        self.btn_alterar.setText("")
        self.btn_excluir.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_Produtos.setText(QCoreApplication.translate("frm_Produtos", u"Nome do Produto:", None))
        self.btn_filtro.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Produtos", u"idProduto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Produtos", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Produtos", u"Quantidade", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Produtos", u"Valor", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Produtos", u"Forncedor", None));
    # retranslateUi

        #Botões
        self.btn_voltar.clicked.connect(self.sairTela)
        self.btn_filtro.clicked.connect(self.consultarGeral)
        self.btn_pesquisar.clicked.connect(self.pesquisarProdutos)
        self.btn_Add.clicked.connect(self.cadastrarProdutos)
        self.btn_consul.clicked.connect(self.consultarProdutos)
        self.btn_alterar.clicked.connect(self.alterarProdutos)
        self.btn_excluir.clicked.connect(self.excluirProdutos)

if __name__ == "__main__":
    app = QApplication([])
    frm_Produtos = QWidget()
    ui = Ui_frm_Produtos()
    ui.setupUi(frm_Produtos)
    frm_Produtos.show()
    app.exec()