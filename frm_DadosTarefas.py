from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget, QMessageBox)

import Controle
import pandas as pd
import mysql.connector
import os

import icon_cadastrar
import icon_cancelar


class Ui_frm_DadosTarefas(object):
    def setupUi(self, frm_DadosTarefas):
        if not frm_DadosTarefas.objectName():
            frm_DadosTarefas.setObjectName(u"frm_DadosTarefas")
        frm_DadosTarefas.setFixedSize(558, 560)
        self.frm_DadosTarefas = frm_DadosTarefas
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_DadosTarefas.setWindowIcon(QIcon(caminho_icone))
        frm_DadosTarefas.setStyleSheet(u"QWidget{\n"
"	background-color: #001F3F;\n"
"\n"
"}")
        self.lbl_nome = QLabel(frm_DadosTarefas)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(70, 50, 61, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosTarefas)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(130, 40, 361, 41))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_inicio = QLabel(frm_DadosTarefas)
        self.lbl_inicio.setObjectName(u"lbl_inicio")
        self.lbl_inicio.setGeometry(QRect(70, 110, 51, 20))
        self.lbl_inicio.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_fim = QLabel(frm_DadosTarefas)
        self.lbl_fim.setObjectName(u"lbl_fim")
        self.lbl_fim.setGeometry(QRect(80, 170, 41, 20))
        self.lbl_fim.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosTarefas)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(180, 460, 101, 91))
        self.btn_cancelar.setAutoFillBackground(False)
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffebee; \n"
"    border: 2px solid #ffcdd2;\n"
"    border-radius: 10px;\n"
"    color: #b71c1c; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_cancelar/cancelar.png);\n"
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
        self.txt_inicio = QLineEdit(frm_DadosTarefas)
        self.txt_inicio.setObjectName(u"txt_inicio")
        self.txt_inicio.setGeometry(QRect(130, 100, 361, 41))
        self.txt_inicio.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_fim = QLineEdit(frm_DadosTarefas)
        self.txt_fim.setObjectName(u"txt_fim")
        self.txt_fim.setGeometry(QRect(130, 160, 361, 41))
        self.txt_fim.setStyleSheet(u"QLineEdit {\n"
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
        self.lbl_obs = QLabel(frm_DadosTarefas)
        self.lbl_obs.setObjectName(u"lbl_obs")
        self.lbl_obs.setGeometry(QRect(20, 270, 101, 20))
        self.lbl_obs.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar = QPushButton(frm_DadosTarefas)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(310, 460, 101, 91))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d1c4b2;\n"
"    border-radius: 12px;\n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px;\n"
"    background-image:url(:/icon_cadastrar/cadastrar.png); \n"
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
        self.textEdit = QTextEdit(frm_DadosTarefas)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 220, 371, 121))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 16px; /* Fonte maior */\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"    text-align: left; /* Alinha o texto \u00e0 esquerda */\n"
"    vertical-align: top; /* Escreve do topo */\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}")
        self.lbl_Situacao = QLabel(frm_DadosTarefas)
        self.lbl_Situacao.setObjectName(u"lbl_Situacao")
        self.lbl_Situacao.setGeometry(QRect(40, 360, 81, 20))
        self.lbl_Situacao.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.comboSituacao = QComboBox(frm_DadosTarefas)
        self.comboSituacao.addItem("")
        self.comboSituacao.addItem("")
        self.comboSituacao.setObjectName(u"comboSituacao")
        self.comboSituacao.setGeometry(QRect(130, 360, 361, 31))
        self.comboSituacao.setStyleSheet(u"QComboBox {\n"
"    background-color: #2c3e50;\n"
"    color: #ecf0f1;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #34495e;\n"
"    background-color: #34495e;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border-left: 6px solid transparent;\n"
"    border-right: 6px solid transparent;\n"
"    border-top: 8px solid #ecf0f1;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #34495e;\n"
"    color: #ecf0f1;\n"
"    selection-background-color: #1abc9c;\n"
"    selection-color: #ffffff;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    outline: none;\n"
"    min-width: 100px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #1abc9c;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #16a085;\n"
"}\n"
"\n"
"/* Barra de rolagem vertical personalizada */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2c3e50;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #1abc9c;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"/* Barra de rolagem horizontal personalizada */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"   "
                        " background: #2c3e50;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #1abc9c;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"")

        self.retranslateUi(frm_DadosTarefas)

        QMetaObject.connectSlotsByName(frm_DadosTarefas)
    # setupUi

    def sairTela(self):
        self.frm_DadosTarefas.close()
        self.frm_DadosTarefas = None

    def adicionarTarefas(self):
        campos_comuns = {
            "Nome": self.txt_nome.text().strip(),
            "Observacao": self.textEdit.toPlainText().strip(),
        }
        campos_mask = {
            "Inicio": self.txt_inicio.text().strip(),
            "Fim": self.txt_fim.text().strip(),
        }

        for campo, valor in campos_comuns.items():
             if not valor:
                 msg = QMessageBox()
                 msg.setWindowTitle("Erro!")
                 msg.setText(f"O campo {campo} é obrigatório e não pode ficar vazio!")
                 msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
                 msg.setIcon(QMessageBox.Warning)
                 msg.setStandardButtons(QMessageBox.Ok)
                 msg.exec()
                 return
        
        obs = self.textEdit.toPlainText()
        if len(obs) > 500:
                msg = QMessageBox()
                msg.setWindowTitle("Erro!")
                msg.setText("Preencha o campo de observação com 500 caracteres ou menos!")
                msg.setWindowIcon(QIcon((r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png")))
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        
        nome = self.txt_nome.text()
        inicio = self.txt_inicio.text()
        fim = self.txt_fim.text()
        obs = self.textEdit.toPlainText()
        situacao = self.comboSituacao.currentText()

        mydb = mysql.connector.connect(
            host = Controle.host,
            user = Controle.user,
            password = Controle.password,
            database = Controle.database,
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO tarefas(`Nome`, `Início`, `Fim`, `Observação`, `Situação`) values (%s, %s, %s, %s, %s)"
        val = (nome, inicio, fim, obs, situacao)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'Registros inseridos')

        mycursor.close()
        mydb.close()

        self.txt_nome.setText("")
        self.txt_inicio.setText("")
        self.txt_fim.setText("")
        self.textEdit.setText("")
        self.comboSituacao.setCurrentIndex(0)

        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Tarefa adicionada com sucesso!")
        icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
        msg.setWindowIcon(QIcon(icon_path))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def alterarTarefas(self): 
        print(Controle.idConsulta)
        nome = self.txt_nome.text()
        inicio = self.txt_inicio.text()
        fim = self.txt_fim.text()
        obs = self.textEdit.toPlainText()
        situacao = self.comboSituacao.currentText()



        mydb = mysql.connector.connect(
                host = Controle.host,
                user = Controle.user,
                password = Controle.password,
                database = Controle.database
        )

        mycursor = mydb.cursor()
        sql = """
        UPDATE tarefas
        SET Nome = %s, Início = %s, Fim = %s, Observação = %s, Situação = %s WHERE idTarefas = %s
        """

        val = (nome, inicio, fim, obs, situacao, Controle.idConsulta)
        mycursor.execute(sql, val)
        mydb.commit()

        msg = QMessageBox()
        msg.setWindowTitle('Sucesso!')
        msg.setText('Dívida alterada com sucesso!')
        msg.setWindowIcon(QIcon(r'C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png'))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosTarefas.close()


    def retranslateUi(self, frm_DadosTarefas):
        frm_DadosTarefas.setWindowTitle(QCoreApplication.translate("frm_DadosTarefas", u"Dados Tarefas", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosTarefas", u"Nome:", None))
        self.lbl_inicio.setText(QCoreApplication.translate("frm_DadosTarefas", u"In\u00edcio:", None))
        self.lbl_fim.setText(QCoreApplication.translate("frm_DadosTarefas", u"Fim:", None))
        self.btn_cancelar.setText("")
        self.txt_inicio.setInputMask(QCoreApplication.translate("frm_DadosTarefas", u"00/00/0000", None))
        self.txt_inicio.setText(QCoreApplication.translate("frm_DadosTarefas", u"//", None))
        self.txt_fim.setInputMask(QCoreApplication.translate("frm_DadosTarefas", u"00/00/0000", None))
        self.lbl_obs.setText(QCoreApplication.translate("frm_DadosTarefas", u"Observa\u00e7\u00e3o:", None))
        self.btn_cadastrar.setText("")
        self.lbl_Situacao.setText(QCoreApplication.translate("frm_DadosTarefas", u"Situa\u00e7\u00e3o:", None))
        self.comboSituacao.setItemText(0, QCoreApplication.translate("frm_DadosTarefas", u"PENDENTE", None))
        self.comboSituacao.setItemText(1, QCoreApplication.translate("frm_DadosTarefas", u"FINALIZADO", None))
        #Condições do botão
        if Controle.tiposTelaDadosCliente == 'incluir':
            self.btn_cadastrar.clicked.connect(self.adicionarTarefas)
        if Controle.tiposTelaDadosCliente == 'alterar':
            self.btn_cadastrar.clicked.connect(self.alterarTarefas)
        
        self.btn_cancelar.clicked.connect(self.sairTela)
        ##Condições da tela
        if Controle.tiposTelaDadosCliente == 'incluir':
            print('incluindo')
            self.txt_nome.setEnabled(True)
            self.txt_inicio.setEnabled(True)
            self.txt_fim.setEnabled(True)
            self.textEdit.setEnabled(True)
            self.comboSituacao.setEnabled(True)
            self.btn_cadastrar.setEnabled(True)
        elif Controle.tiposTelaDadosCliente == 'alterar':
            print('alterando')
            self.txt_nome.setEnabled(True)
            self.txt_inicio.setEnabled(True)
            self.txt_fim.setEnabled(True)
            self.textEdit.setEnabled(True)
            self.comboSituacao.setEnabled(True)
            self.btn_cadastrar.setEnabled(True)

            print('conectando')

            mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )

            mycursor = mydb.cursor()

            consultarSQL = "SELECT * FROM tarefas WHERE idTarefas = %s"

            mycursor.execute(consultarSQL, (Controle.idConsulta,))
            myresult = mycursor.fetchone()

            nome = myresult[1]
            inicio = myresult[2]
            fim = myresult[3]
            obs = myresult[4]
            situacao = myresult[5]

            self.txt_nome.setText(nome)
            self.txt_inicio.setText(inicio)
            self.txt_fim.setText(fim)
            self.textEdit.setText(obs)
            self.comboSituacao.setCurrentText(situacao)

            # Fechar o cursor e a conexão
            mycursor.close()
            mydb.close()
        elif Controle.tiposTelaDadosCliente == 'consultar':
            print('DadosTarefas', Controle.tiposTelaDadosCliente)

            self.txt_nome.setEnabled(False)
            self.txt_inicio.setEnabled(False)
            self.txt_fim.setEnabled(False)
            self.textEdit.setEnabled(False)
            self.comboSituacao.setEnabled(False)
            self.btn_cadastrar.setEnabled(False)

            mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
            mycursor = mydb.cursor()    
            consultaSQL = """
            SELECT Nome, Início, Fim, Observação, Situação FROM tarefas WHERE idTarefas = %s
            """
            mycursor.execute(consultaSQL, (Controle.idConsulta,))
            myresult = mycursor.fetchall()

            df = pd.DataFrame(myresult, columns=["Nome", "Início", "Fim", "Observação", "Situação"])
            
            self.txt_nome.setText(str(df['Nome'][0]))
            self.txt_inicio.setText(str(df['Início'][0]))
            self.txt_fim.setText(str(df['Fim'][0]))
            self.textEdit.setText(str(df['Observação'][0]))
            comboSituacao = str(df['Situação'][0]) if not df.empty else ""
            self.comboSituacao.setCurrentText(comboSituacao)

    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_DadosTarefas = QWidget()
    ui = Ui_frm_DadosTarefas()
    ui.setupUi(frm_DadosTarefas)
    frm_DadosTarefas.show()
    app.exec()