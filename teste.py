import mysql.connector
import pandas as pd

class Controle:
    tiposTelaDadosCliente = 'alterar'
    idFornecedor = 1  # Defina o ID para teste

# Simulando uma função para testar o DataFrame
def testar_dataframe():
    if Controle.tiposTelaDadosCliente == 'alterar':
        print('DadosFornecedor: ', Controle.tiposTelaDadosCliente)

        try:
            # Conexão com o banco de dados
            mydb = mysql.connector.connect(
                host='localhost',
                user='Ariel',
                password='IRani18@#',
                database='sistema'
            )
            mycursor = mydb.cursor()

            # Consulta parametrizada
            sql = "SELECT * FROM fornecedor WHERE idFornecedor = %s"
            val = (Controle.idFornecedor,)
            mycursor.execute(sql, val)

            # Obter todos os resultados
            results = mycursor.fetchall()

            if results:
                # Criar um DataFrame a partir dos resultados
                columns = ["idFornecedor", "Razão Social", "Contato", "Cnpj", 
                           "Cidade", "Rua", "Bairro", "Cep", "E-mail"]
                df = pd.DataFrame(results, columns=columns)

                print("DataFrame criado com sucesso:")
                print(df)

                # Acessar os dados do DataFrame
                razaoSocial = df['Razão Social'].iloc[0]
                print("Razão Social:", razaoSocial)

            else:
                print("Fornecedor não encontrado.")

        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

        finally:
            # Fechar a conexão com o banco de dados
            if mydb.is_connected():
                mydb.close()

# Executar o teste
testar_dataframe()
