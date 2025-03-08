from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QMessageBox)

import mysql.connector
import pandas as pd

import Controle
import os
import icon_cadastrar
import icon_cancelar

class Ui_frm_DadosCliente(object):
    def setupUi(self, frm_DadosCliente):
        if not frm_DadosCliente.objectName():
            frm_DadosCliente.setObjectName(u"frm_DadosCliente")
        frm_DadosCliente.setFixedSize(526, 647)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_DadosCliente.setWindowIcon(QIcon(caminho_icone))
        self.frm_DadosCliente = frm_DadosCliente
        frm_DadosCliente.setStyleSheet(u"QWidget {\n"
"    background-color: #eaf2f8;\n"
"    border-radius: 8px;\n"
"}")
        self.lbl_nome = QLabel(frm_DadosCliente)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(50, 50, 51, 21))
        self.lbl_nome.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(frm_DadosCliente)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(120, 40, 371, 41))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_celular = QLabel(frm_DadosCliente)
        self.lbl_celular.setObjectName(u"lbl_celular")
        self.lbl_celular.setGeometry(QRect(40, 100, 61, 16))
        self.lbl_celular.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.lbl_cpf = QLabel(frm_DadosCliente)
        self.lbl_cpf.setObjectName(u"lbl_cpf")
        self.lbl_cpf.setGeometry(QRect(60, 150, 41, 20))
        self.lbl_cpf.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cancelar = QPushButton(frm_DadosCliente)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(150, 550, 101, 91))
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
        self.txt_celular = QLineEdit(frm_DadosCliente)
        self.txt_celular.setObjectName(u"txt_celular")
        self.txt_celular.setGeometry(QRect(120, 90, 371, 41))
        self.txt_celular.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_cpf = QLineEdit(frm_DadosCliente)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(120, 140, 371, 41))
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Rua = QLabel(frm_DadosCliente)
        self.lbl_Rua.setObjectName(u"lbl_Rua")
        self.lbl_Rua.setGeometry(QRect(60, 250, 41, 20))
        self.lbl_Rua.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Rua = QLineEdit(frm_DadosCliente)
        self.txt_Rua.setObjectName(u"txt_Rua")
        self.txt_Rua.setGeometry(QRect(120, 240, 371, 41))
        self.txt_Rua.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_cidade = QLabel(frm_DadosCliente)
        self.lbl_cidade.setObjectName(u"lbl_cidade")
        self.lbl_cidade.setGeometry(QRect(40, 200, 61, 20))
        self.lbl_cidade.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.btn_cadastrar_3 = QPushButton(frm_DadosCliente)
        self.btn_cadastrar_3.setObjectName(u"btn_cadastrar_3")
        self.btn_cadastrar_3.setGeometry(QRect(290, 550, 101, 91))
        self.btn_cadastrar_3.setStyleSheet(u"QPushButton {\n"
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
        self.txt_cidade = QLineEdit(frm_DadosCliente)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setGeometry(QRect(120, 190, 371, 41))
        self.txt_cidade.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_bairro = QLabel(frm_DadosCliente)
        self.lbl_bairro.setObjectName(u"lbl_bairro")
        self.lbl_bairro.setGeometry(QRect(40, 300, 61, 21))
        self.lbl_bairro.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_bairro = QLineEdit(frm_DadosCliente)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(120, 290, 371, 41))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_cep = QLabel(frm_DadosCliente)
        self.lbl_cep.setObjectName(u"lbl_cep")
        self.lbl_cep.setGeometry(QRect(60, 400, 41, 21))
        self.lbl_cep.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_cep = QLineEdit(frm_DadosCliente)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(120, 390, 371, 41))
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Numero = QLineEdit(frm_DadosCliente)
        self.txt_Numero.setObjectName(u"txt_Numero")
        self.txt_Numero.setGeometry(QRect(120, 340, 371, 41))
        self.txt_Numero.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_Numero = QLabel(frm_DadosCliente)
        self.lbl_Numero.setObjectName(u"lbl_Numero")
        self.lbl_Numero.setGeometry(QRect(30, 350, 71, 21))
        self.lbl_Numero.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_cidade_6 = QLineEdit(frm_DadosCliente)
        self.txt_cidade_6.setObjectName(u"txt_cidade_6")
        self.txt_cidade_6.setGeometry(QRect(120, 440, 371, 41))
        self.txt_cidade_6.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_email = QLabel(frm_DadosCliente)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(40, 450, 61, 21))
        self.lbl_email.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_cidade_7 = QLineEdit(frm_DadosCliente)
        self.txt_cidade_7.setObjectName(u"txt_cidade_7")
        self.txt_cidade_7.setEnabled(False)
        self.txt_cidade_7.setGeometry(QRect(120, 490, 371, 41))
        self.txt_cidade_7.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_email_2 = QLabel(frm_DadosCliente)
        self.lbl_email_2.setObjectName(u"lbl_email_2")
        self.lbl_email_2.setGeometry(QRect(10, 500, 91, 21))
        self.lbl_email_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")

        self.retranslateUi(frm_DadosCliente)

        QMetaObject.connectSlotsByName(frm_DadosCliente)
    # setupUi

    # setupUi
    
    def adicionarCliente(self):
        Controle.pontos = 0
        
        campos_comuns = {
              "Nome": self.txt_nome.text().strip(),
              "Cidade": self.txt_cidade.text().strip(),
              "Rua": self.txt_Rua.text().strip(),
              "Bairro": self.txt_bairro.text().strip(),
              "Número": self.txt_Numero.text().strip(),
              "E-mail": self.txt_cidade_6.text().strip(),
        }
        campos_mask = {
              "Celular": self.txt_celular.text().strip(),
              "Cpf": self.txt_cpf.text().strip(),
               "Cep": self.txt_cep.text().strip(),
        }

        for campos_comuns, valor in campos_comuns.items():
              if not valor.strip():
                    msg = QMessageBox()
                    msg.setWindowTitle("ERRO!")
                    msg.setText(f"O campo '{campos_comuns} é obrigatório, e não pode ficar vazio!' ")
                    icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                    msg.setWindowIcon(QIcon(icon_path)) 
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec()
                    return

        email = self.txt_cidade_6.text().strip()
        if "@" not in email or "." not in email.split("@")[-1]:
                msg = QMessageBox()
                msg.setWindowTitle("Erro!")
                msg.setText("O campo E-mail deve conter um endereço válido (ex: exemplo@email.com)")
                msg.setWindowIcon(QIcon((r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png")))
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return

        for campos_mask, valor in campos_mask.items():
                if len(valor.replace("_", "").replace(".", "").strip()) < 6:  # Remove "_" (máscaras) e verifica o comprimento
                        msg = QMessageBox()
                        msg.setWindowTitle("ERRO!")
                        msg.setText(f"O campo '{campos_mask}' deve ser preenchido!")
                        icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                        msg.setWindowIcon(QIcon(icon_path))
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec()
                        return
        
        numeroCliente = self.txt_Numero.text().strip()
        if not numeroCliente.isdigit():
                msg = QMessageBox()
                msg.setWindowTitle("Erro de Validação")
                msg.setText("O campo 'Número' deve conter apenas números!")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return  # Não prosseguir com a adição do cliente


        nomeCliente = self.txt_nome.text()
        celularCliente = self.txt_celular.text()
        cpfCliente = self.txt_cpf.text()
        cidadeCliente = self.txt_cidade.text()
        ruaCliente = self.txt_Rua.text()
        bairroCliente = self.txt_bairro.text()
        numeroCliente = self.txt_Numero.text()
        cepCliente = self.txt_cep.text()
        emailCliente = self.txt_cidade_6.text()

                # Conexão com o banco de dados
        mydb = mysql.connector.connect( 
              
                host= Controle.host,
                user= Controle.user,
                password= Controle.password,
                database= Controle.database
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO cliente(`Nome`, `Celular`, `Cpf`, `Cidade`, `Rua`, `Bairro`, `Número`, `Cep`, `E-mail`, `Pontos`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nomeCliente, celularCliente, cpfCliente, cidadeCliente, ruaCliente, bairroCliente, numeroCliente, cepCliente, emailCliente, Controle.pontos)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, 'Record(s) inserted')
        mycursor.close()

        # Limpa os campos após a inserção
        self.txt_nome.setText("")
        self.txt_celular.setText("")
        self.txt_cpf.setText("")
        self.txt_cidade.setText("")
        self.txt_Rua.setText("")
        self.txt_bairro.setText("")
        self.txt_Numero.setText("")
        self.txt_cep.setText("")
        self.txt_cidade_6.setText("")
        
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Adicionado com Sucesso!")
        msg.setWindowIcon(QIcon((r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png")))
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

        self.frm_DadosCliente.close()
                        
    def sairTela(self, frm_DadosCliente):
        frm_DadosCliente.close()


    def alterarCliente(self): 


       # Pegando os valores dos campos da interface
        nomeCliente = self.txt_nome.text()
        celularCliente = self.txt_celular.text()
        cpfCliente = self.txt_cpf.text()
        cidadeCliente = self.txt_cidade.text()
        ruaCliente = self.txt_Rua.text()
        bairroCliente = self.txt_bairro.text()
        numeroCliente = self.txt_Numero.text()
        cepCliente = self.txt_cep.text()
        emailCliente = self.txt_cidade_6.text() #email
        pontuacao = self.txt_cidade_7.text() #Data

        # Conectando ao banco de dados
        mydb = mysql.connector.connect(
        host=Controle.host,
        user=Controle.user,
        password=Controle.password,
        database=Controle.database
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT Pontos FROM cliente WHERE IdCliente = %s", (Controle.idConsulta,))
        pontos_atual = mycursor.fetchone()

        pontos = pontos_atual[0]  

        sql = """
        UPDATE cliente
        SET Nome = %s, Celular = %s, Cpf = %s, Cidade = %s, Rua = %s,
        Bairro = %s, Número = %s, Cep = %s, `E-mail` = %s, Pontos = %s
        WHERE IdCliente = %s
        """

        # Lista de valores sem incluir Pontos
        val = (
                nomeCliente, celularCliente, cpfCliente, cidadeCliente,
                ruaCliente, bairroCliente, numeroCliente, cepCliente,
                emailCliente, pontuacao, Controle.idConsulta
        )

        # Executando a query
        mycursor.execute(sql, val)
        mydb.commit()

        print(f"{mycursor.rowcount} registro(s) alterado(s).")

        # Exibindo mensagem de sucesso
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Alterado com Sucesso!")
        msg.setWindowIcon(QIcon(r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"))
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        self.frm_DadosCliente.close()

    def retranslateUi(self, frm_DadosCliente):
        frm_DadosCliente.setWindowTitle(QCoreApplication.translate("frm_DadosCliente", u"Dados Cliente", None))
        self.lbl_nome.setText(QCoreApplication.translate("frm_DadosCliente", u"Nome:", None))
        self.lbl_celular.setText(QCoreApplication.translate("frm_DadosCliente", u"Celular: ", None))
        self.lbl_cpf.setText(QCoreApplication.translate("frm_DadosCliente", u"CPF:", None))
        self.btn_cancelar.setText("")
        self.txt_celular.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"(00) 0 0000-0000", None))
        self.txt_cpf.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"000.000.000-00", None))
        self.lbl_Rua.setText(QCoreApplication.translate("frm_DadosCliente", u"Rua:", None))
        self.lbl_cidade.setText(QCoreApplication.translate("frm_DadosCliente", u"Cidade:", None))
        self.btn_cadastrar_3.setText("")
        self.lbl_bairro.setText(QCoreApplication.translate("frm_DadosCliente", u"Bairro:", None))
        self.lbl_cep.setText(QCoreApplication.translate("frm_DadosCliente", u"CEP:", None))
        self.txt_cep.setInputMask(QCoreApplication.translate("frm_DadosCliente", u"00000-000", None))
        self.lbl_Numero.setText(QCoreApplication.translate("frm_DadosCliente", u"N\u00famero:", None))
        self.txt_cidade_6.setText("")
        self.lbl_email.setText(QCoreApplication.translate("frm_DadosCliente", u"E-mail:", None))
        self.txt_cidade_7.setText("")
        self.lbl_email_2.setText(QCoreApplication.translate("frm_DadosCliente", u"Pontua\u00e7\u00e3o:", None))
    # retranslateUi
        
        if Controle.tiposTelaDadosCliente == 'incluir':
                self.btn_cadastrar_3.clicked.connect(self.adicionarCliente)
        if Controle.tiposTelaDadosCliente == 'alterar':
                self.btn_cadastrar_3.clicked.connect(self.alterarCliente)
                print('Dados Cliente: ', Controle.tiposTelaDadosCliente)
        self.btn_cancelar.clicked.connect(lambda: self.sairTela(frm_DadosCliente))
   ##Condições da tela
        if Controle.tiposTelaDadosCliente == 'incluir':
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(True)
                self.txt_celular.setEnabled(True)
                self.txt_cpf.setEnabled(True)
                self.txt_cidade.setEnabled(True)
                self.txt_Rua.setEnabled(True)
                self.txt_bairro.setEnabled(True)
                self.txt_Numero.setEnabled(True)
                self.txt_cep.setEnabled(True)
                self.txt_cidade_6.setEnabled(True)
                self.txt_cidade_7.setEnabled(False)
                self.btn_cadastrar_3.setEnabled(True)
        elif Controle.tiposTelaDadosCliente == 'consultar':            
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(False)
                self.txt_celular.setEnabled(False)
                self.txt_cpf.setEnabled(False)
                self.txt_cidade.setEnabled(False)
                self.txt_Rua.setEnabled(False)
                self.txt_bairro.setEnabled(False)
                self.txt_Numero.setEnabled(False)
                self.txt_cep.setEnabled(False)
                self.txt_cidade_6.setEnabled(False)
                self.txt_cidade_7.setEnabled(False)
                self.btn_cadastrar_3.setEnabled(False)
                #Conexão com bd
                print('Conectando...')
                mydb = mysql.connector.connect(
                        host = Controle.host,
                        user = Controle.user,
                        password = Controle.password,
                        database = Controle.database
                )
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM cliente WHERE idCliente = '" + Controle.idConsulta + "'"
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                mycursor.close()
                #Converte resultados bd para dataframe#
                df = pd.DataFrame(myresult, columns=["idCliente", "Nome", "Celular", "Cpf", "Cidade", "Rua", "Bairro", "Número", "Cep", "E-mail", "Pontos"])
                nomeCliente = df['Nome'][0]
                celularCliente = df['Celular'][0]
                cpfCliente = df['Cpf'][0]
                cidadeCliente = df['Cidade'][0]
                ruaCliente = df['Rua'][0]
                bairroCliente = df['Bairro'][0]
                NumeroCliente = df['Número'][0]
                cepCliente = df['Cep'][0]
                emailCliente = df['E-mail'][0]
                pontos = df['Pontos'][0]
                #Setar na tela do sitema
                self.txt_nome.setText(nomeCliente)
                self.txt_celular.setText(celularCliente)
                self.txt_cpf.setText(cpfCliente)
                self.txt_Rua.setText(ruaCliente)
                self.txt_cidade.setText(cidadeCliente)
                self.txt_bairro.setText(bairroCliente)
                self.txt_Numero.setText(str(NumeroCliente))
                self.txt_cep.setText(cepCliente)
                self.txt_cidade_6.setText(emailCliente)
                self.txt_cidade_7.setText(str(pontos))
        elif Controle.tiposTelaDadosCliente == 'alterar':
                print('DadosCliente: ', Controle.tiposTelaDadosCliente)
                self.txt_nome.setEnabled(True)
                self.txt_celular.setEnabled(True)
                self.txt_cpf.setEnabled(True)
                self.txt_cidade.setEnabled(True)
                self.txt_Rua.setEnabled(True)
                self.txt_bairro.setEnabled(True)
                self.txt_Numero.setEnabled(True)
                self.txt_cep.setEnabled(True)
                self.txt_cidade_6.setEnabled(True)
                self.txt_cidade_7.setEnabled(False)
                self.btn_cadastrar_3.setEnabled(True)
                #Conexão com bd
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
                mycursor = mydb.cursor()
                consultaSQL = "SELECT * FROM cliente WHERE idCliente = '" + Controle.idConsulta + "'"
                mycursor.execute(consultaSQL)
                myresult = mycursor.fetchall()
                mycursor.close()
                #Converte resultados bd para dataframe#
                df = pd.DataFrame(myresult, columns=["idCliente", "Nome", "Celular", "Cpf", "Cidade", "Rua", "Bairro", "Número", "Cep", "E-mail", "Pontos"])
                nomeCliente = df['Nome'][0]
                celularCliente = df['Celular'][0]
                cpfCliente = df['Cpf'][0]
                cidadeCliente = df['Cidade'][0]
                ruaCliente = df['Rua'][0]
                bairroCliente = df['Bairro'][0]
                NumeroCliente = df['Número'][0]
                cepCliente = df['Cep'][0]
                emailCliente = df['E-mail'][0]
                pontos = df['Pontos'][0]
                #Setar na tela do sitema
                self.txt_nome.setText(nomeCliente)
                self.txt_celular.setText(celularCliente)
                self.txt_cpf.setText(cpfCliente)
                self.txt_Rua.setText(ruaCliente)
                self.txt_cidade.setText(cidadeCliente)
                self.txt_bairro.setText(bairroCliente)
                self.txt_Numero.setText(str(NumeroCliente))
                self.txt_cep.setText(cepCliente)
                self.txt_cidade_6.setText(emailCliente)
                self.txt_cidade_7.setText(str(pontos))


if __name__ == "__main__":
    app = QApplication([])
    frm_DadosCliente = QWidget()
    ui = Ui_frm_DadosCliente()
    ui.setupUi(frm_DadosCliente)
    frm_DadosCliente.show()
    app.exec()