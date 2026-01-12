from db import conectar
from datetime import datetime

#Funcao responsavel por criar e inserir as viagens no banco de dados, utilizando origem, destino, descrição e data/hora
def criarCarona():
    # Requisitando as informações necessesarias para a criação da viagem
    print("Insira os seguintes dados abaixo para criar uma carona\n")
    origem = input("Origem: ")
    destino = input("Destino: ")
    descricao = input("Descricao(opcional): ")
    
    # Pega data e hora atual
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Passos 
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
    "INSERT INTO carona (origem, destino, data_carona, descricao) VALUES (?, ?, ?, ?)", (origem, destino, data, descricao)
    )
    con.commit()
    con.close()
    print("Carona criada com sucesso!")
