from core.db import conectar
from datetime import datetime

def criarCarona():
    """
    Solicita os dados da viagem ao usuário e insere um novo registro no banco de dados.

    A função captura origem, destino, data/hora e descrição via terminal e persiste 
    as informações na tabela 'carona'.
    """
    
    print("Insira os seguintes dados abaixo para criar uma carona\n")
    
    # Loop para capturar origem, destino e descrição
    while True:
        origem = input("Origem: ")
        destino = input("Destino: ")
        descricao = input("Descricao(opcional): ")
        if origem != '' and destino != '':
            break
        else: 
            print("Insira as informações faltantes")
        
    # Novo loop para capturar e validar a data
    while True:
        data_input = input("Data e Hora da Carona (dd/mm/aaaa HH:MM): ")
        try:
            # Tenta converter o texto do usuário para um objeto datetime
            dt_objeto = datetime.strptime(data_input, "%d/%m/%Y %H:%M")
            
            # Converte para o formato padrão do banco (ISO 8601: AAAA-MM-DD HH:MM:SS)
            data = dt_objeto.strftime("%Y-%m-%d %H:%M:%S")
            break # Sai do loop se a conversão der certo
        except ValueError:
            print("Formato inválido! Por favor, use: dd/mm/aaaa HH:MM (ex: 10/03/2026 14:30)")
    
    con = conectar()
    cursor = con.cursor()
    
    cursor.execute(
        "INSERT INTO carona (origem, destino, data_carona, descricao) VALUES (?, ?, ?, ?)", 
        (origem, destino, data, descricao)
    )
    
    con.commit()
    con.close()
    print("Carona criada com sucesso!")