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
import mysql.connector
import pandas as pd
import os

#Import Imagens
import icon_adicionar
import icon_consultar
import icon_excluir
import icon_filtro
import icon_pesquisar
import icon_voltar
import icon_alterar
import Controle

from frm_DadosCliente import Ui_frm_DadosCliente

class Ui_frm_Cliente(object):
    
    def setupUi(self, frm_Cliente):
        if not frm_Cliente.objectName():
            frm_Cliente.setObjectName(u"frm_Cliente")
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_Cliente.setWindowIcon(QIcon(caminho_icone))
        frm_Cliente.setStyleSheet(u"QWidget {\n"
"    background-color: #e8f5e9;\n"
"}")
        self.btn_Add = QPushButton(frm_Cliente)
        self.btn_Add.setObjectName(u"btn_Add")
        self.btn_Add.setGeometry(QRect(0, 0, 91, 81))
        self.btn_Add.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a; \n"
"    font-size: 14px;\n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_add/adicionar.png);\n"
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
"    border-color: #b39b8d;\n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.btn_voltar = QPushButton(frm_Cliente)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(490, 510, 91, 81))
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
        self.btn_consul = QPushButton(frm_Cliente)
        self.btn_consul.setObjectName(u"btn_consul")
        self.btn_consul.setGeometry(QRect(180, 0, 91, 81))
        self.btn_consul.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_alt/consultar.png);\n"
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
        self.btn_alterar = QPushButton(frm_Cliente)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setGeometry(QRect(90, 0, 91, 81))
        self.btn_alterar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a; \n"
"    font-size: 14px;\n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_alt/alterar.png);\n"
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
"    border-color: #b39b8d;\n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.btn_excluir = QPushButton(frm_Cliente)
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
        self.btn_pesquisar = QPushButton(frm_Cliente)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setGeometry(QRect(530, 110, 21, 21))
        self.btn_pesquisar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px;\n"
"    color: #5a5a5a; \n"
"    font-size: 14px;\n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_pesq/pesquisar.png); \n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0; \n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf;\n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px; \n"
"    padding-top: 4px;\n"
"}")
        self.lbl_nomeCliente = QLabel(frm_Cliente)
        self.lbl_nomeCliente.setObjectName(u"lbl_nomeCliente")
        self.lbl_nomeCliente.setGeometry(QRect(0, 110, 151, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_nomeCliente.setFont(font)
        self.lbl_nomeCliente.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeCliente = QLineEdit(frm_Cliente)
        self.txt_nomeCliente.setObjectName(u"txt_nomeCliente")
        self.txt_nomeCliente.setGeometry(QRect(150, 100, 371, 41))
        font1 = QFont()
        self.txt_nomeCliente.setFont(font1)
        self.txt_nomeCliente.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"       color: #333333;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.btn_filtro = QPushButton(frm_Cliente)
        self.btn_filtro.setObjectName(u"btn_filtro")
        self.btn_filtro.setGeometry(QRect(530, 80, 21, 21))
        self.btn_filtro.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px;\n"
"    color: #5a5a5a; \n"
"    font-size: 14px; \n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_filt/filtro.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0; \n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf; \n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px;\n"
"    padding-top: 4px;\n"
"}")
        self.tableWidget = QTableWidget(frm_Cliente)
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

        self.retranslateUi(frm_Cliente)
        QMetaObject.connectSlotsByName(frm_Cliente)
    # setupUi



    
    ##Função dos botões##
    def consultarGeral(self):
        self.host = Controle.host
        self.user = Controle.user
        self.password = Controle.password
        self.database = Controle.database
        print('Conectando...')
        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
        print('Conexão bem-sucedida!')
        mycursor = mydb.cursor()
        nomeConsulta = self.txt_nomeCliente.text()
        consultaSQL = "SELECT * FROM cliente WHERE nome LIKE '" + nomeConsulta + "%'"
        mycursor.execute(consultaSQL)
        myresult = mycursor.fetchall()

        # Criando DataFrame
        df = pd.DataFrame(myresult, columns=["idCliente", "Nome", "Celular", "Cpf", "Cidade", "Rua", "Bairro", "Número", "Cep", "E-mail"])
        self.all_data = df

        # Configurando a tabela no Pyside
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        # Preenchendo a tabela
        for i in range(numRows):
                for j in range(numCols):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        # Ajustando o layout das colunas e linhas
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        mycursor.close()


    def sairTela(self, frm_Cliente):
         Controle.tiposTelaDadosCliente == ''
         frm_Cliente.close()
         self.frm_Cliente = None


    def pesquisarCliente(self):

        self.host = Controle.host
        self.user = Controle.user
        self.password = Controle.password
        self.database = Controle.database 
        print('Conectando...')
        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )
        print('Conexão bem-sucedida!')

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeCliente.text()  # Obtendo o texto da caixa de pesquisa
        consultaSQL = "SELECT * FROM cliente WHERE nome LIKE %s"
        mycursor.execute(consultaSQL, ('%' + nomeConsulta + '%',))  # Parametrizando a consulta SQL

        myresult = mycursor.fetchall()  # Obtendo os resultados

        # Criando DataFrame
        df = pd.DataFrame(myresult, columns=["idCliente", "Nome", "Celular", "Cpf", "Cidade", "Rua", "Bairro", "Número", "Cep", "E-mail"])
        self.all_data = df

        # Configurando a tabela no Pyside
        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        # Preenchendo a tabela
        for i in range(numRows):
                for j in range(numCols):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        # Ajustando o layout das colunas e linhas
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        mycursor.close()

    def cadastrarCliente(self):
        Controle.tiposTelaDadosCliente = "incluir"
        if not hasattr(self, 'frm_DadosCliente') or self.frm_DadosCliente is None or not self.frm_DadosCliente.isVisible():
              #Cria a tela se não tiver aberta
              self.frm_DadosCliente = QWidget()
              self.ui = Ui_frm_DadosCliente()
              self.ui.setupUi(self.frm_DadosCliente)

              #Config para garantir a remoção da referência ao fechar a janela
              self.frm_DadosCliente.setAttribute(Qt.WA_DeleteOnClose)
              self.frm_DadosCliente.destroyed.connect(lambda: setattr(self, 'frm_DadosCliente', None))

              self.frm_DadosCliente.show()
        
        else:
             #Traz a janela existente
             self.frm_DadosCliente.raise_()
             self.frm_DadosCliente.activateWindow() 

    def consultarCliente(self):

        # Tipo tela dados Cliente
        Controle.tiposTelaDadosCliente = "consultar"
        print('frmCliente: ', Controle.tiposTelaDadosCliente)
        
        # Verificar se há uma linha selecionada na tabela
        line = self.tableWidget.currentRow()
        
        if line == -1:  # Se não houver linha selecionada
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText("Por favor, selecione um cliente para consultar.")
                msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return  # Não prosseguir com a consulta
        
        item = self.tableWidget.item(line, 0)  # Obtém o item da primeira coluna (ID do cliente)
        
        if item:  # Verifica se o item não é None
                Controle.idConsulta = item.text()
                if not hasattr(self, 'frm_DadosCliente') or self.frm_DadosCliente is None or not self.frm_DadosCliente.isVisible():
                        #Cria a tela se não tiver aberta
                        self.frm_DadosCliente = QWidget()
                        self.ui = Ui_frm_DadosCliente()
                        self.ui.setupUi(self.frm_DadosCliente)

                        #Config para garantir a remoção da referência ao fechar a janela
                        self.frm_DadosCliente.setAttribute(Qt.WA_DeleteOnClose)
                        self.frm_DadosCliente.destroyed.connect(lambda: setattr(self, 'frm_DadosCliente', None))

                        self.frm_DadosCliente.show()
                        
                else:
                        #Traz a janela existente
                        self.frm_DadosCliente.raise_()
                        self.frm_DadosCliente.activateWindow() 

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro de Seleção")
                msg.setText("Não foi possível obter o ID do cliente selecionado.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

    def alterarCliente(self):
        # Tipo tela dados Cliente
        Controle.tiposTelaDadosCliente = "alterar"
        print('frmCliente: ', Controle.tiposTelaDadosCliente)
        
        # Verificar se há uma linha selecionada na tabela
        line = self.tableWidget.currentRow()
        
        if line == -1:  # Se não houver linha selecionada
                msg = QMessageBox()
                msg.setWindowTitle("Erro de Seleção")
                msg.setText("Por favor, selecione um cliente para alterar.")
                msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return  # Não prosseguir com a alteração
        
        item = self.tableWidget.item(line, 0)  # Obtém o item da primeira coluna (ID do cliente)
        
        if item:  # Verifica se o item não é None
                Controle.idConsulta = item.text()
                if not hasattr(self, 'frm_DadosCliente') or self.frm_DadosCliente is None or not self.frm_DadosCliente.isVisible():
                        #Cria a tela se não tiver aberta
                        self.frm_DadosCliente = QWidget()
                        self.ui = Ui_frm_DadosCliente()
                        self.ui.setupUi(self.frm_DadosCliente)

                        #Config para garantir a remoção da referência ao fechar a janela
                        self.frm_DadosCliente.setAttribute(Qt.WA_DeleteOnClose)
                        self.frm_DadosCliente.destroyed.connect(lambda: setattr(self, 'frm_DadosCliente', None))

                        self.frm_DadosCliente.show()
                
                else:
                        #Traz a janela existente
                        self.frm_DadosCliente.raise_()
                        self.frm_DadosCliente.activateWindow() 
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro de Seleção")
                msg.setText("Não foi possível obter o ID do cliente selecionado.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

    def excluirCliente(self):
        # Verificar se há uma linha selecionada na tabela
        line = self.tableWidget.currentRow()
        
        if line == -1:  # Se não houver linha selecionada
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText("Por favor, selecione um cliente para excluir.")
                msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return  # Não prosseguir com a exclusão
        
        item = self.tableWidget.item(line, 0)  # Obtém o item da primeira coluna (ID do cliente)
        
        if item:  # Verifica se o item não é None
                idCliente = item.text()
                
                # Conexão com o banco de dados
                mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
                )

                mycursor = mydb.cursor()
                sql = "DELETE FROM cliente WHERE idCliente = %s"
                mycursor.execute(sql, (idCliente,))
                mydb.commit()

                msg = QMessageBox()
                msg.setWindowTitle("Cliente excluído")
                msg.setText("Cliente excluído com sucesso.")
                msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

                # Atualiza a tabela após a exclusão
                mycursor.execute("SELECT * FROM cliente")
                myresult = mycursor.fetchall()
                df = pd.DataFrame(myresult, columns=['idCliente', 'Nome', 'Celular', 'Cpf', 'Cidade', 'Rua', 'Bairro', 'Número', 'Cep', 'E-mail'])
                self.all_data = df
                numRows = len(self.all_data.index)
                self.tableWidget.setColumnCount(len(self.all_data.columns))
                self.tableWidget.setRowCount(numRows)
                self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

                for i in range(numRows):
                        for j in range(len(self.all_data.columns)):
                                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()

                mycursor.close()
        
        else:  # Se o item não for encontrado
                msg = QMessageBox()
                msg.setWindowTitle("Erro de Seleção")
                msg.setText("Não foi possível obter o ID do cliente selecionado.")
                msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

    def retranslateUi(self, frm_Cliente):
        frm_Cliente.setWindowTitle(QCoreApplication.translate("frm_Cliente", u"Cliente", None))
        self.btn_Add.setText("")
        self.btn_voltar.setText("")
        self.btn_consul.setText("")
        self.btn_alterar.setText("")
        self.btn_excluir.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_nomeCliente.setText(QCoreApplication.translate("frm_Cliente", u"Nome do Cliente:", None))
        self.btn_filtro.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_Cliente", u"idCliente", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_Cliente", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_Cliente", u"Celular", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_Cliente", u"Cpf", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_Cliente", u"Cidade", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_Cliente", u"Rua", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_Cliente", u"Bairro", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_Cliente", u"Número", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_Cliente", u"Cep", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("frm_Cliente", u"E-mail", None));
    # retranslateUi

        ##Botões##
        self.btn_filtro.clicked.connect(self.consultarGeral)
        self.btn_voltar.clicked.connect(lambda: self.sairTela(frm_Cliente))
        self.btn_pesquisar.clicked.connect(self.pesquisarCliente)
        self.btn_Add.clicked.connect(self.cadastrarCliente)
        self.btn_consul.clicked.connect(self.consultarCliente)
        self.btn_alterar.clicked.connect(self.alterarCliente)
        self.btn_excluir.clicked.connect(self.excluirCliente)

if __name__ == "__main__":
    app = QApplication([])
    frm_Cliente = QWidget()
    ui = Ui_frm_Cliente()
    ui.setupUi(frm_Cliente)
    frm_Cliente.show()
    app.exec()