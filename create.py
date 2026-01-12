import sqlite3
import os

# Nome do banco definido no seu projeto
DB_NAME = "caronas.db"
SQL_FILE = "data.sql"

def inicializar_banco():
    if not os.path.exists(SQL_FILE):
        print(f"Erro: Arquivo '{SQL_FILE}' não encontrado.")
        return

    # Conecta ao banco (ele cria o arquivo se não existir)
    con = sqlite3.connect(DB_NAME)
    
    # Lê o arquivo .sql
    with open(SQL_FILE, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    # Executa todas as instruções do arquivo
    try:
        con.executescript(sql_script)
        print("SISTEMA: Banco de dados atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao executar SQL: {e}")
    finally:
        con.close()

if __name__ == "__main__":
    inicializar_banco()
    