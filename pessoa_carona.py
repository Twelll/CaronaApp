from db import conectar

def pessoaCarona():
    print("Insira os seguintes dados abaixo para criar uma carona\n")
    id_carona = input("ID Carona: ")
    id_pessoa = input("ID Pessoa: ")
    status = input("Status(pago/pendente): ")
    
    con = conectar()
    con.execute(
        "INSERT INTO pessoa_carona (id_carona, id_pessoa, status) VALUES (?, ?, ?)",
        (id_carona, id_pessoa, status)
    )
    con.commit()
    con.close()
    print("Carona criada com sucesso!")
    