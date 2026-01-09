from  db import conectar 

def cadastrarPessoa():
    print("Insira os seguintes dados abaixo para cadastrar uma pessoa\n")
    nome = input("Nome: ")
    contato = input("\nContato: ")
    
    con = conectar()
        
    con.execute(
    "INSERT INTO pessoas (nome, contato) VALUES (?, ?)", 
    (nome, contato)
    )
        
    con.commit()
    con.close()
    print("Pessoa cadastrada com sucesso!")