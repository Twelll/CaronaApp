from core.db import conectar, consultarViagens, consultarPessoa

def pessoaCarona():    
    """
    Registra a associação entre uma pessoa e uma carona no banco de dados.
    
    A função interage com o usuário solicitando os IDs necessários (mostrando
    as tabelas disponíveis para consulta) e o status do pagamento.
    """
    print("Insira os seguintes dados abaixo para criar uma carona\n")

    consultarViagens() 
    while True:
        id_carona = input("ID Carona: ")
        
        consultarPessoa() 
        id_pessoa = input("ID Pessoa: ")
        status = input("Status(pago/pendente): ")

        if id_carona != '' and id_pessoa != '':
            if status == 'pago' or status == 'pendente':
                break
            else:
                print("Status deve ser pago ou pendente apenas")
        else:
            print("Insira as informações faltantes")
    
    con = conectar()
    con.execute(
        "INSERT INTO pessoa_carona (id_carona, id_pessoa, status) VALUES (?, ?, ?)",
        (id_carona, id_pessoa, status)
    )
    con.commit()
    con.close()
    print("Carona criada com sucesso!")
    