from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QMessageBox)

import icon_pagamentoTe
import icon_calcularTroco
import os

import mysql.connector
import time
import Controle
import pandas as pd


import icon_pagamentoTe

class Ui_frm_TelaPagamento(object):
    def setupUi(self, frm_TelaPagamento):
        self.frm_TelaPagamento = frm_TelaPagamento
        if not frm_TelaPagamento.objectName():
            frm_TelaPagamento.setObjectName(u"frm_TelaPagamento")
        frm_TelaPagamento.setFixedSize(524, 650)
        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
        frm_TelaPagamento.setWindowIcon(QIcon(caminho_icone))
        frm_TelaPagamento.setStyleSheet(u"QWidget{\n"
"	background-color: #2E8B57;\n"
"}")
        self.label = QLabel(frm_TelaPagamento)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 211, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Dinheiro = QLineEdit(frm_TelaPagamento)
        self.txt_Dinheiro.setObjectName(u"txt_Dinheiro")
        self.txt_Dinheiro.setGeometry(QRect(220, 80, 281, 41))
        self.txt_Dinheiro.setStyleSheet(u"QLineEdit {\n"
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
        self.label_2 = QLabel(frm_TelaPagamento)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 191, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Cheque = QLineEdit(frm_TelaPagamento)
        self.txt_Cheque.setObjectName(u"txt_Cheque")
        self.txt_Cheque.setGeometry(QRect(220, 320, 281, 41))
        self.txt_Cheque.setStyleSheet(u"QLineEdit {\n"
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
        self.label_3 = QLabel(frm_TelaPagamento)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 320, 151, 41))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.label_4 = QLabel(frm_TelaPagamento)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 151, 41))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Cartao = QLineEdit(frm_TelaPagamento)
        self.txt_Cartao.setObjectName(u"txt_Cartao")
        self.txt_Cartao.setGeometry(QRect(220, 160, 281, 41))
        self.txt_Cartao.setStyleSheet(u"QLineEdit {\n"
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
        self.label_5 = QLabel(frm_TelaPagamento)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 250, 71, 31))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Pix = QLineEdit(frm_TelaPagamento)
        self.txt_Pix.setObjectName(u"txt_Pix")
        self.txt_Pix.setGeometry(QRect(220, 240, 281, 41))
        self.txt_Pix.setStyleSheet(u"QLineEdit {\n"
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
        self.txt_Total = QLineEdit(frm_TelaPagamento)
        self.txt_Total.setObjectName(u"txt_Total")
        self.txt_Total.setEnabled(False)
        self.txt_Total.setGeometry(QRect(240, 410, 271, 41))
        self.txt_Total.setStyleSheet(u"QLineEdit {\n"
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
        self.label_6 = QLabel(frm_TelaPagamento)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 410, 241, 41))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.txt_Troco = QLineEdit(frm_TelaPagamento)
        self.txt_Troco.setObjectName(u"txt_Troco")
        self.txt_Troco.setEnabled(False)
        self.txt_Troco.setGeometry(QRect(240, 480, 271, 41))
        self.txt_Troco.setStyleSheet(u"QLineEdit {\n"
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
        self.label_7 = QLabel(frm_TelaPagamento)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 480, 131, 41))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}")
        self.btn_CalcularTroco = QPushButton(frm_TelaPagamento)
        self.btn_CalcularTroco.setObjectName(u"btn_CalcularTroco")
        self.btn_CalcularTroco.setGeometry(QRect(120, 560, 121, 81))
        self.btn_CalcularTroco.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_Troco/converter_resized.png);\n"
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
        self.btn_pagamento = QPushButton(frm_TelaPagamento)
        self.btn_pagamento.setObjectName(u"btn_pagamento")
        self.btn_pagamento.setGeometry(QRect(280, 560, 121, 81))
        self.btn_pagamento.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px; \n"
"    color: #5a5a5a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 10px 16px; \n"
"    background-image:url(:/icon_pagamento/forma-de-pagamento AA (2).png);\n"
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

        self.retranslateUi(frm_TelaPagamento)

        QMetaObject.connectSlotsByName(frm_TelaPagamento)
    # setupUi

    def adicionarValores(self):
        self.txt_Dinheiro.setText(str(0))
        self.txt_Cartao.setText(str(0))
        self.txt_Pix.setText(str(0))
        self.txt_Cheque.setText(str(0))
        self.txt_Troco.setText("R$" + str(0))

        totalVenda = self.txt_Total.setText("R$" + str(Controle.totalDaVenda))

    def calculandoTroco(self):
        totalvd = Controle.totalDaVenda

        dinheiro = float(self.txt_Dinheiro.text().replace(",", ".") or 0)
        cartao = float(self.txt_Cartao.text().replace(",", ".") or 0)
        pix = float(self.txt_Pix.text().replace(",", ".") or 0)
        cheque = float(self.txt_Cheque.text().replace(",", ".") or 0)

        totalPago = dinheiro + cartao + pix + cheque

        if totalPago < totalvd:
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText('Valores insuficientes para finalizar a compra!')
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.Critical) 
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

                self.txt_Troco.setText("Insira valores válidos!")

        else:
                troco = totalPago - totalvd
                self.txt_Troco.setText("R$ " + str(troco)) 

    def finalizarCompra(self):

        totalvd = Controle.totalDaVenda

        #captura os valores preenchidos nos campos de pagamento
        dinheiro = float(self.txt_Dinheiro.text().replace(",", ".") or 0)
        cartao = float(self.txt_Cartao.text().replace(",", ".") or 0)
        pix = float(self.txt_Pix.text().replace(",", ".") or 0)
        cheque = float(self.txt_Cheque.text().replace(",", ".") or 0)

        #soma os valores para verificar se o pagamento é suficiente
        totalPago = dinheiro + cartao + pix + cheque

        #verifica se o total pago é menor que o total da venda
        if totalPago < totalvd:
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText('Valores insuficientes para finalizar a compra!')
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.Critical) 
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

                self.txt_Troco.setText("Insira valores válidos!")

        else:
                troco = totalPago - totalvd
                self.txt_Troco.setText("R$ " + str(troco))


                msg = QMessageBox()
                msg.setWindowTitle("Finalizar venda")
                msg.setText("Deseja finalizar a venda e cadastrar ao banco de dados?")
                caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                msg.setWindowIcon(QIcon(caminho_icone))
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

                resposta = msg.exec()

                if resposta == QMessageBox.Yes:
                        from frm_Vendas import Ui_Frm_Vendas
                        valorTotal = Controle.totalDaVenda
                        totalDeItens = Controle.totalItens
                        print(valorTotal)
                        print(totalDeItens)

                        dinheiro = valorTotal
                        itens = totalDeItens

                        mydb = mysql.connector.connect(
                                host=Controle.host,
                                user=Controle.user,
                                password=Controle.password,
                                database=Controle.database
                        )
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT `Quantidade de Itens`, `Valor total` FROM total")
                        resultado = mycursor.fetchone() 

                        if resultado:
                                itens_existentes = int(float(resultado[0])) 
                                valor_existente = float(resultado[1])  
                        else:
                                itens_existentes, valor_existente = 0, 0

                        novos_itens = itens_existentes + int(totalDeItens)
                        novo_valor = valor_existente + float(valorTotal)

                        sql = "UPDATE total SET `Quantidade de Itens` = %s, `Valor total` = %s"
                        val = (novos_itens, novo_valor)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print("VENDA ATUALIZADA")

                        msgF = QMessageBox()
                        msgF.setWindowTitle("Venda Finalizada")
                        msgF.setText("Sua venda foi finalizada com sucesso!")
                        caminho_icone = os.path.join(os.path.dirname(__file__), "avsIcon.png")
                        msgF.setWindowIcon(QIcon(caminho_icone))
                        msgF.setIcon(QMessageBox.Information)
                        msgF.setStandardButtons(QMessageBox.Ok)
                        
                        vendaFinalizada = msgF.exec()

                        if vendaFinalizada == QMessageBox.Ok:

                                mydb = mysql.connector.connect(
                                        host=Controle.host,
                                        user=Controle.user,
                                        password=Controle.password,
                                        database=Controle.database
                                )
                                
                                cursor = mydb.cursor()
                                cursor.execute("SELECT Produto, Valor, Quantidade FROM vendas")
                                dados = cursor.fetchall()
                                print(dados)
                                
                                cursor.close()
                                mydb.close()

                                self.receberDadosCarrinho(dados)
                                self.cadastrarPontos()
                                self.pegarItensCarrinho(dados)
                                self.sairTela()

                else:
                        self.frm_TelaPagamento.close()
                
    def sairTela(self):
        self.frm_TelaPagamento.close()
        self.frm_TelaPagamento = None
    
    def receberDadosCarrinho(self, dados):
        obs = 'Vendas'

        mydb = mysql.connector.connect(
                host=Controle.host,      
                user=Controle.user,     
                password=Controle.password,
                database=Controle.database
        )
        mycursor = mydb.cursor()

        sql = """INSERT INTO `banco-lucros` 
                (`Nome`, `Valor`, `Observação`, `Quantidade`)
                VALUES (%s, %s, %s, %s)"""

        for registro in dados:
                nomeProduto = registro[0]
                valor = float(registro[1])
                quantidade = int(float(registro[2]))  

                valores = (nomeProduto, valor, obs, quantidade)
                mycursor.execute(sql, valores)

        mydb.commit()
        mycursor.close()
        mydb.close()

        print("Dados inseridos com sucesso no novo banco.")
        
    def cadastrarPontos(self):
        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )

        mycursor = mydb.cursor()

        consultaSQL = "SELECT IdCliente FROM vendas"
        mycursor.execute(consultaSQL)
        clientes_vendas = mycursor.fetchall()  

        clientes_unicos = set(cliente[0] for cliente in clientes_vendas)

        for cliente_id in clientes_unicos:
                sql_update = "UPDATE cliente SET Pontos = pontos + 10 WHERE idCliente = %s"
                mycursor.execute(sql_update, (cliente_id,))

        mydb.commit()

        print("Pontos adicionados com sucesso!")

        mycursor.close()
        mydb.close()

    def pegarItensCarrinho(self, dados):

        mydb = mysql.connector.connect(
                host=Controle.host,
                user=Controle.user,
                password=Controle.password,
                database=Controle.database
        )
                                
        cursor = mydb.cursor()
        cursor.execute("SELECT Produto, Data, Quantidade, Valor FROM vendas")
        dados = cursor.fetchall()
        print(dados)

        sql = """INSERT INTO `vendas-consulta` 
                (`Nome/Produto`, `Data`, `Valor`,`Quantidade`)
                VALUES (%s, %s, %s, %s)"""

        for registro in dados:
                nomeProduto = registro[0]
                data = registro[1]
                quantidade = int(float(registro[2]))  
                valor = float(registro[3])
                

                valores = (nomeProduto, data, valor, quantidade)
                cursor.execute(sql, valores)

        mydb.commit()

        cursor.close()
        mydb.close()
        
        print('Adicionado com sucesso em vendas-consulta')

    def retranslateUi(self, frm_TelaPagamento):
        frm_TelaPagamento.setWindowTitle(QCoreApplication.translate("frm_TelaPagamento", u"Tela Pagamento", None))
        self.label.setText(QCoreApplication.translate("frm_TelaPagamento", u"PAGAMENTO", None))
        self.label_2.setText(QCoreApplication.translate("frm_TelaPagamento", u"DINHEIRO:", None))
        self.label_3.setText(QCoreApplication.translate("frm_TelaPagamento", u"CHEQUE:", None))
        self.label_4.setText(QCoreApplication.translate("frm_TelaPagamento", u"CART\u00c3O:", None))
        self.label_5.setText(QCoreApplication.translate("frm_TelaPagamento", u"PIX:", None))
        self.label_6.setText(QCoreApplication.translate("frm_TelaPagamento", u"VALOR TOTAL:", None))
        self.txt_Troco.setText("")
        self.label_7.setText(QCoreApplication.translate("frm_TelaPagamento", u"TROCO:", None))
        self.btn_CalcularTroco.setText("")
        self.btn_pagamento.setText("")
    # retranslateUi
    
        self.btn_CalcularTroco.clicked.connect(self.calculandoTroco)
        self.btn_pagamento.clicked.connect(self.finalizarCompra)
        self.adicionarValores()

if __name__ == "__main__":
    app = QApplication([])
    frm_TelaPagamento = QWidget()
    ui = Ui_frm_TelaPagamento()
    ui.setupUi(frm_TelaPagamento)
    frm_TelaPagamento.show()
    app.exec()