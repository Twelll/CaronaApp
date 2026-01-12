import sqlite3
import os

# 1. Pega a pasta onde este ficheiro está: .../ProjetoCarona/core
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Sobe um nível para chegar à raiz: .../ProjetoCarona
ROOT_DIR = os.path.dirname(BASE_DIR)

# 3. Define a pasta de dados: .../ProjetoCarona/data
DATA_DIR = os.path.join(ROOT_DIR, "data")

# 4. Define os caminhos dentro da pasta data
# ISTO É O QUE ESTAVA A FALHAR:
DB_NAME = os.path.join(DATA_DIR, "caronas.db")
SQL_FILE = os.path.join(DATA_DIR, "data.sql")

def inicializar_banco():
    """
    Inicializa a estrutura do banco de dados a partir de um arquivo SQL externo.
    """
    
    # Verifica se a pasta 'data' existe, se não, cria (segurança extra)
    if not os.path.exists(DATA_DIR):
        try:
            os.makedirs(DATA_DIR)
            print(f"SISTEMA: Pasta '{DATA_DIR}' criada.")
        except OSError as e:
            print(f"Erro ao criar pasta de dados: {e}")
            return

    # Verifica se o arquivo .sql existe
    if not os.path.exists(SQL_FILE):
        print(f"Erro Crítico: Arquivo '{SQL_FILE}' não encontrado.")
        print("Verifique se moveu o arquivo data.sql para dentro da pasta 'data'.")
        return

    # Conecta ao banco (ele cria o arquivo se não existir)
    con = sqlite3.connect(DB_NAME)
    
    # Lê o arquivo .sql
    try:
        with open(SQL_FILE, 'r', encoding='utf-8') as f:
            sql_script = f.read()
    
        # Executa todas as instruções do arquivo
        con.executescript(sql_script)
        print("SISTEMA: Banco de dados verificado/atualizado com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro ao executar SQL: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        con.close()

if __name__ == "__main__":
    inicializar_banco()