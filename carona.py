from db import conectar
from datetime import datetime

def criarCarona():
    print("Insira os seguintes dados abaixo para criar uma carona\n")
    tipo = input("Tipo(ida/volta): ")

    # Pega data e hora atual
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
    "INSERT INTO carona (tipo, data_carona) VALUES (?, ?)", (tipo, data)
    )
    con.commit()
    con.close()
    print("Carona criada com sucesso!")
