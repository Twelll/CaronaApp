from  db import conectar 

def cadastrarPessoa():
    print("Insira os seguintes dados abaixo para cadastrar uma pessoa\n")
    nome = input("Nome: ")
    contato = input("Contato: ")
    descricao = input("Descrição(opcional): ")
    
    con = conectar()
        
    con.execute(
    "INSERT INTO pessoas (nome, contato, descricao) VALUES (?, ?, ?)", 
    (nome, contato, descricao)
    )
        
    con.commit()
    con.close()
    print("Pessoa cadastrada com sucesso!")