import sqlite3

DB_NAME = "caronas.db"

def conectar():
    con = sqlite3.connect(DB_NAME)
    con. execute("PRAGMA foreign_keys = ON")
    return con

def consultarBanco():
    con = conectar()
    cur = con.cursor()
    
    # SQL com JOIN
    cur.execute("""
        SELECT p.nome, c.tipo, c.data_carona, r.status
        FROM pessoas p
        JOIN pessoa_carona r ON p.id_pessoa = r.id_pessoa
        JOIN carona c ON c.id_carona = r.id_carona
        ORDER BY c.data_carona
    """)
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Caronas cadastradas ===")
        for linha in resultados:
            nome, tipo, data_carona, status = linha
            print(f"Nome: {nome} | Tipo: {tipo} | Data/Hora: {data_carona} | Status: {status}")
    else:
        print("Nenhuma carona encontrada.")
    
    con.close()
    
def inputPersonalizado(input_personalizado):
    con = conectar()
    cur = con.cursor()
    
    # SQL com JOIN
    cur.execute(input_personalizado)
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Caronas cadastradas ===")
        for linha in resultados:
            nome, tipo, data_carona, status = linha
            print(f"Nome: {nome} | Tipo: {tipo} | Data/Hora: {data_carona} | Status: {status}")
    else:
        print("Nenhuma carona encontrada.")
    
    con.close()
    