from db import consultarBanco
from pessoa import cadastrarPessoa
from carona import criarCarona
from pessoa_carona import pessoaCarona
from create import inicializar_banco  
from db import inputPersonalizado

def main(): 
    inicializar_banco()
    
    while True:

        print("\nMENU - Gerenciamento de Caronas")
        
        print("0 - sair")
        print("1 - Consultas")
        print("2 - Cadastros")
        print("3 - Input db")
        opcao_menu = input("Digite sua opção: ")
        
        if opcao_menu == "0":
            print("Saindo do programa...\n")
            break
        elif opcao_menu == "1":
    
            print("\n1 - Consultar todo banco de dados")
            print("2 - Consultar pessoas")
            print("3 - Consultar viagens")
            print("4 - Consultar Caronas")
            print("5 - Pendencias")
            print("6 - Pagos(Valor recibo)")
            opcao_sub = input("Digite sua opção: ")
            
            
            if opcao_sub == "1":
                consultarBanco()
            elif opcao_sub == "2":
                print("1")
            #    consultarPessoa()
            elif opcao_sub == "3":
                print("1")

             #   consultarViagens()
            elif opcao_sub == "4":
                print("1")

              #  consultarCaronas()
            elif opcao_sub == "5":
                print("1")

               # consultarPendencias()
            elif opcao_sub == "6": 
                print("1")

               # consultarPagos()
            else:
                print("Opção invalida 1, tente novamente...\n")
              
        elif opcao_menu == "2":
    
            print("1 - cadastras pessoa")
            print("2 - cadastras viagem")
            print("3 - Cadastrar carona")
            opcao_sub = input("Digite usa opção: ")
            
            if opcao_sub == "1": 
                cadastrarPessoa()
            elif opcao_sub == "2":
                criarCarona()
            elif opcao_sub == "3":
                pessoaCarona()
            else: 
                print("Opção invalida 2, tente novamente...\n")
        elif opcao_menu == "3":
            print("teste")
            input_personalizado = input("Digite seu input: ")
            inputPersonalizado(input_personalizado)
        else : 
            print("Nenhuma opção valida 3, tente novamente...\n")
            
# chama a função
if __name__ == "__main__":
    main()