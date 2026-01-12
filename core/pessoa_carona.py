from core.db import conectar, consultarViagens, consultarPessoa

def pessoaCarona():    
    """
    Registra a associação entre uma pessoa e uma carona no banco de dados.
    
    A função interage com o usuário solicitando os IDs necessários (mostrando
    as tabelas disponíveis para consulta) e o status do pagamento.
    """
    print("Insira os seguintes dados abaixo para criar uma carona\n")

    consultarViagens() 
    id_carona = input("ID Carona: ")
    
    consultarPessoa() 
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
    