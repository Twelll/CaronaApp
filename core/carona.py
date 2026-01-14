from core.db import conectar
from datetime import datetime

def criarCarona():
    
    """
    Solicita os dados da viagem ao usuário e insere um novo registro no banco de dados.

    A função captura origem, destino e descrição via terminal, gera o timestamp 
    atual automaticamente e persiste as informações na tabela 'carona'.
    """
    
    print("Insira os seguintes dados abaixo para criar uma carona\n")
    while True:
        origem = input("Origem: ")
        destino = input("Destino: ")
        descricao = input("Descricao(opcional): ")
        if origem != '' and destino != '':
            break
        else: 
            print("Insira as informações faltantes")
        
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
    "INSERT INTO carona (origem, destino, data_carona, descricao) VALUES (?, ?, ?, ?)", (origem, destino, data, descricao)
    )
    con.commit()
    con.close()
    print("Carona criada com sucesso!")
