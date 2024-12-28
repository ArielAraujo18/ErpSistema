import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QVBoxLayout, QWidget, QMessageBox
import mysql.connector

class TesteComboBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teste ComboBox com Banco de Dados")
        self.setGeometry(100, 100, 400, 200)

        # ComboBox
        self.comboBox = QComboBox(self)
        self.comboBox.setEnabled(False)  # Inicialmente desabilitada

        # Botão para carregar dados
        self.btnCarregar = QPushButton("Carregar Fornecedores", self)
        self.btnCarregar.clicked.connect(self.carregarFornecedores)

        # Botão para habilitar a ComboBox
        self.btnEnable = QPushButton("Habilitar ComboBox", self)
        self.btnEnable.clicked.connect(self.enableComboBox)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.btnCarregar)
        layout.addWidget(self.btnEnable)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def carregarFornecedores(self):
        try:
            # Conexão com o banco de dados
            mydb = mysql.connector.connect(
                host="localhost",
                user="Ariel",
                password="IRani18@#",
                database="sistema"
            )

            # Consulta SQL
            mycursor = mydb.cursor()
            mycursor.execute("SELECT `Razão Social` FROM fornecedor")

            # Limpa a ComboBox antes de carregar
            self.comboBox.clear()

            # Adiciona os fornecedores na ComboBox
            for (nome,) in mycursor.fetchall():
                self.comboBox.addItem(nome)

            mycursor.close()
            mydb.close()

            # Mensagem de sucesso
            QMessageBox.information(self, "Sucesso", "Fornecedores carregados com sucesso!")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro ao Conectar", f"Erro ao carregar fornecedores: {e}")

    def enableComboBox(self):
        self.comboBox.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TesteComboBox()
    window.show()
    sys.exit(app.exec())