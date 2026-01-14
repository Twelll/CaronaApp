import sys
from core.db import *
from core.pessoa import cadastrarPessoa
from core.carona import criarCarona
from core.pessoa_carona import pessoaCarona
from core.create import inicializar_banco 

def sair_programa():
    print("Saindo do programa...\n")
    sys.exit()

def wrapper_query():
    """Função para encapsular o input da query avançada"""
    query = input("Digite sua Query SQL: ")
    inputPersonalizado(query)

# --- Definição dos Menus ---
def navegar_menu(titulo, opcoes):
    """
    Função genérica para exibir e processar menus.
    Retorna False apenas se o usuário escolher '0' (Voltar/Sair).
    """
    while True:
        print(f"\n--- {titulo} ---")
        for key, (descricao, _) in opcoes.items():
            print(f"{key} - {descricao}")
        
        escolha = input("Digite sua opção: ")

        if escolha in opcoes:
            _, funcao = opcoes[escolha]
            if funcao() is False:
                break 
        else:
            print("Opção inválida, tente novamente...\n")

def menu_consultas():
    opcoes = {
        "1": ("Consultar todo banco de dados", consultarBanco),
        "2": ("Consultar pessoas", consultarPessoa),
        "3": ("Consultar viagens", consultarViagens),
        "4": ("Consultar Caronas", consultarCaronas),
        "5": ("Pendencias", consultarPendencias),
        "6": ("Pagos (Valor recibo)", consultarPagos),
        "0": ("Voltar", lambda: False) 
    }
    navegar_menu("MENU - Consultas", opcoes)

def menu_alteracoes():
    opcoes = {
        "1": ("Cadastrar pessoa", cadastrarPessoa),
        "2": ("Cadastrar viagem", criarCarona),
        "3": ("Cadastrar carona (vincular)", pessoaCarona),
        "4": ("Alterar Status", lambda: print("Função alterarStatus não importada/definida neste contexto")), # Ajuste aqui com a função real
        "0": ("Voltar", lambda: False)
    }
    navegar_menu("MENU - Alterações", opcoes)

# --- Main ---
def main(): 
    inicializar_banco()
    
    # Menu Principal
    opcoes_principais = {
        "1": ("Consultas", menu_consultas),
        "2": ("Alterações", menu_alteracoes),
        "3": ("Query (Avançado)", wrapper_query),
        "0": ("Sair", sair_programa)
    }

    navegar_menu("MENU - Gerenciamento de Caronas", opcoes_principais)

if __name__ == "__main__":
    main()