from db import consultarBanco
from pessoa import cadastrarPessoa
from carona import criarCarona
from pessoa_carona import pessoaCarona
from create import inicializar_banco  
from db import inputPersonalizado

def main(): 
    inicializar_banco()
    
    while True:

        print("\nMENU - Gerenciamento de Caronas\n")
        
        print("Consultas\n")
        print("0 - sair")
        print("1 - Consultas\n")
        print("2 - Cadastros\n")
        print("3 - Comando personalizado no banco de dados\n")
        opcao_menu = ("Digite sua opção: ")
        
        if opcao_menu == 0:
            print("Saindo do programa...\n")
            break
        elif opcao_menu == 1:
    
            print("1 - Consultar todo banco de dados\n")
            print("2 - Consultar pessoas\n")
            print("3 - Consultar viagens\n")
            print("4 - Consultar Caronas\n")
            print("5 - Pendencias\n")
            print("6 - Pagos(Valor recibo)\n")
            opcao_sub = ("Digite sua opção: ")
            
            
            if opcao_sub == 1:
                consultarBanco()
            elif opcao_sub == 2:
                print("1")
            #    consultarPessoa()
            elif opcao_sub == 3:
                print("1")

             #   consultarViagens()
            elif opcao_sub == 4:
                print("1")

              #  consultarCaronas()
            elif opcao_sub == 5:
                print("1")

               # consultarPendencias()
            elif opcao_sub == 6: 
                print("1")

               # consultarPagos()
            else:
                print("Opção invalidam, tente novamente...\n")
              
        elif opcao_menu == 2:
    
            print("1 - cadastras pessoa\n")
            print("2 - cadastras viagem\n")
            print("3 - Cadastrar carona\n")
            
            if opcao_sub == "2": 
                cadastrarPessoa()
            elif opcao_sub == 2:
                criarCarona()
            elif opcao_sub == 3:
                pessoaCarona()
            else: 
                print("Opção invalida, tente novamente...\n")
        elif opcao_menu == 3:
            input_personalizado = ("Digite seu input personalizado e entao click 'enter': \n")
            inputPersonalizado(input_personalizado)
        else : 
            print("Nenhuma opção valida, tente novamente...\n")
            
# chama a função
if __name__ == "__main__":
    main()