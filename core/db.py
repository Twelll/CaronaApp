import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(ROOT_DIR, "data")

SQL_FILE = os.path.join(DATA_DIR, "data.sql") 

DB_NAME = os.path.join(DATA_DIR, "caronas.db")

def conectar():
    """
    Estabelece a conexão com o banco de dados SQLite e ativa a verificação de chaves estrangeiras.
    """
    con = sqlite3.connect(DB_NAME)
    con.execute("PRAGMA foreign_keys = ON")
    return con

def consultarBanco():
    """
    Lista todas as caronas associadas a pessoas, ordenadas por data.
    Exibe apenas nomes e detalhes básicos da viagem.
    """
    con = conectar()
    cur = con.cursor()
    
    cur.execute("""
        SELECT p.nome, c.origem, c.destino, c.data_carona, r.status
        FROM pessoas p
        JOIN pessoa_carona r ON p.id_pessoa = r.id_pessoa
        JOIN carona c ON c.id_carona = r.id_carona
        ORDER BY c.data_carona
    """)
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Caronas cadastradas ===")
        for linha in resultados:
            nome, origem, destino, data_carona, status = linha
            print(f"Nome: {nome} | Origem: {origem} | Destino: {destino} | Data/Hora: {data_carona} | Status: {status}")
    else:
        print("SISTEMA: Nenhuma carona encontrada.")
    
    con.close()

#Temporario
def inputPersonalizado(sql):
    """
    Executa uma instrução SQL arbitrária fornecida pelo usuário.
    Identifica automaticamente se é uma consulta (SELECT) para exibir resultados
    ou um comando de ação (INSERT, UPDATE, DELETE) para fazer commit.
    """
    con = None
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute(sql)

        if sql.strip().lower().startswith("select"):
            colunas = [desc[0] for desc in cur.description]
            resultados = cur.fetchall()

            print("\n=== Resultado ===")
            print(" | ".join(colunas))
            print("-" * 50)

            if resultados:
                for linha in resultados:
                    print(" | ".join(str(valor) for valor in linha))
            else:
                print("SISTEMA: Nenhum resultado encontrado.")
        else:
            con.commit()
            print("SISTEMA: Comando executado com sucesso.")

    except Exception as e:
        print("ERRO:", e)
    finally:
        if con:
            con.close()

def consultarPessoa():
    """
    Exibe todos os registros da tabela 'pessoas'.
    """
    con = conectar()
    cur = con.cursor()
    
    cur.execute("SELECT * FROM pessoas")
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Pessoas cadastradas ===")
        for linha in resultados:
            id_pessoa, nome, contato, descricao = linha
            print(f"ID: {id_pessoa} | Nome: {nome} | Contato: {contato} | Descrição: {descricao} |")
    else:
        print("SISTEMA: Nenhuma pessoa cadastrada.")
    
    con.close()
    
def consultarViagens():
    """
    Exibe todos os registros da tabela 'carona' (apenas dados da viagem, sem passageiros).
    """
    con = conectar()
    cur = con.cursor()
    
    
    cur.execute("SELECT * FROM carona")
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Viagens cadastradas ===")
        for linha in resultados:
            id_carona, origem, destino, data_carona, descricao = linha
            print(f"ID: {id_carona} | Origem: {origem} | Destino: {destino} | Data/Hora: {data_carona} | Descrição: {descricao}")
    else:
        print("SISTEMA: Nenhuma Viagem encontrada.")
    
    con.close()
    
def consultarCaronas():
    """
    Lista detalhada de caronas com passageiros, incluindo os IDs de pessoa e carona.
    Útil para identificar registros antes de realizar atualizações ou deleções.
    """
    con = conectar()
    cur = con.cursor()
    
    cur.execute("""
        SELECT p.id_pessoa, p.nome, c.id_carona, c.origem, c.destino, c.data_carona, r.status
        FROM pessoas p
        JOIN pessoa_carona r ON p.id_pessoa = r.id_pessoa
        JOIN carona c ON c.id_carona = r.id_carona
        ORDER BY c.data_carona
    """)
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Caronas cadastradas ===")
        for linha in resultados:
            id_pessoa, nome, id_carona,origem, destino, data_carona, status = linha
            print(f"ID_Pessoa: {id_pessoa} | Nome: {nome} | ID_Carona: {id_carona} | Origem: {origem} | Destino: {destino} | Data/Hora: {data_carona} | Status: {status}")
    else:
        print("SISTEMA: Nenhuma carona encontrada.")
    
    con.close()
    

def consultarPendencias():
    """
    Filtra e exibe apenas as relações passageiro-carona onde o status é 'pendente'.
    """
    con = conectar()
    cur = con.cursor()
    
    cur.execute("""
        SELECT p.nome, c.origem, c.destino, c.data_carona, r.status
        FROM pessoas p
        JOIN pessoa_carona r ON p.id_pessoa = r.id_pessoa
        JOIN carona c ON c.id_carona = r.id_carona
        WHERE r.status = 'pendente'
        ORDER BY c.data_carona;
    """)
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Pendências cadastradas ===")
        for linha in resultados:
            nome, origem, destino, data_carona, status = linha
            print(
                f"Nome: {nome} | Origem: {origem} | Destino: {destino} | "
                f"Data/Hora: {data_carona} | Status: {status}"
            )
    else:
        print("SISTEMA: Nenhuma pendência encontrada.")
    
    con.close()


def consultarPagos():
    """
    Filtra e exibe apenas as relações passageiro-carona onde o status é 'pago'.
    """
    con = conectar()
    cur = con.cursor()
    
    cur.execute("""
        SELECT p.nome, c.origem, c.destino, c.data_carona, r.status
        FROM pessoas p
        JOIN pessoa_carona r ON p.id_pessoa = r.id_pessoa
        JOIN carona c ON c.id_carona = r.id_carona
        WHERE r.status = 'pago'
        ORDER BY c.data_carona;
    """)
    
    resultados = cur.fetchall()
    
    if resultados:
        print("\n=== Pagos cadastradas ===")
        for linha in resultados:
            nome, origem, destino, data_carona, status = linha
            print(
                f"Nome: {nome} | Origem: {origem} | Destino: {destino} | "
                f"Data/Hora: {data_carona} | Status: {status}"
            )
    else:
        print("SISTEMA: Nenhum pagamento encontrado.")
    
    con.close()
    
def alterarStatus():
    """
    Solicita ao usuário os IDs de pessoa e carona para atualizar o status financeiro para 'pago'.
    Exibe a lista de caronas antes para facilitar a identificação dos IDs.
    """
    con = conectar()
    cur = con.cursor()

    consultarCaronas() 

    v_pessoa = int(input("Digite o ID_Pessoa: "))
    v_carona = int(input("Digite o ID da Carona: "))
    
    sql = """
        UPDATE pessoa_carona
        SET status = 'pago'
        WHERE id_pessoa = ? AND id_carona = ?
    """
    try:
        cur.execute(sql, (v_pessoa, v_carona))
        
        if cur.rowcount > 0:
            con.commit() 
            print(f"\nSISTEMA: Sucesso! {cur.rowcount} registo(s) atualizado(s) para 'pago'.")
        else:
            print("\nSISTEMA: Nenhuma carona encontrada com esses IDs.")
            
    except Exception as e:
        print(f"ERRO: Não foi possível atualizar. Detalhes: {e}")
    finally:
        con.close()