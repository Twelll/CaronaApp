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
        print("SISTEMA: Nenhuma carona encontrada.")
    
    con.close()
    
def inputPersonalizado(sql):
    try:
        con = conectar()
        cur = con.cursor()

        cur.execute(sql)

        # Se for SELECT
        if sql.strip().lower().startswith("select"):
            colunas = [desc[0] for desc in cur.description]
            resultados = cur.fetchall()

            if resultados:
                print("\n=== Resultado ===")
                print(" | ".join(colunas))
                print("-" * 50)

                for linha in resultados:
                    print(" | ".join(str(valor) for valor in linha))
            else:
                print("SISTEMA: Nenhum resultado encontrado.")

        else:
            # INSERT, UPDATE, DELETE, CREATE, etc
            con.commit()
            print("SISTEMA: Comando executado com sucesso.")

        con.close()

    except Exception as e:
        print("ERRO:", e)