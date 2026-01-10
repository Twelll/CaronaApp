from db import conectar
from datetime import datetime


def criarCarona():
    print("Insira os seguintes dados abaixo para criar uma carona\n")
    origem = input("Origem: ")
    destino = input("Destino: ")
    descricao = input("Descricao(opcional): ")
    
    # Pega data e hora atual
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
    "INSERT INTO carona (origem, destino, data_carona, descricao) VALUES (?, ?, ?, ?)", (origem, destino, data, descricao)
    )
    con.commit()
    con.close()
    print("Carona criada com sucesso!")
