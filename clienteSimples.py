import socket

if __name__ == '__main__':
    # HOST = input('Digite o endereco do servidor:')
    # PORT = input('Digite a porta do servidor:')
    HOST = "localhost"
    PORT = 12346
    BUFSIZ = 4096
    ADDR = (HOST,int(PORT))

    client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_sock.connect(ADDR)

    continua=True
    try:
        while continua:
            print("---------------MENU-----------------")
            print("1 - Criar Arquivo Texto")
            print("2 - Escrever arquivo Texto")
            print("3 - Listar Arquivos de Texto")
            print("4 - Ler linha do Aquivo")
            print("5 - Buscar Palavra no Arquivo")
            print("6 - Contar linhas em um Arquivo")
            print("7 - Contar Palavras em um Arquivo")
            opcao = int(input("Opção: "))
            if(opcao == 1):
                texto = input('Digite o nome do arquivo: ')
                dados = f"CRIAR_ARQUIVO {texto}"
            elif opcao == 2:
                texto = input('Digite o nome do arquivo e o texto\n Ex: NOME_ARQUIVO TEXTO: ')
                dados = f"ESCREVER_ARQUIVO {texto}"
            elif opcao == 3:
                dados = f"LISTAR"
            elif opcao == 4:
                texto = input('Digite o nome do arquivo e a linha \n Ex: NOME_ARQUIVO 1: ')
                dados = f"MOSTRAR_LINHA-NOME_ARQUIVO {texto}"
            elif opcao == 5:
                texto = input('Digite o nome do arquivo e a PALAVRA \n Ex: NOME_ARQUIVO PALAVRA: ')
                dados = f"BUSCAR_PALAVRA-NOME_ARQUIVO {texto}"
            elif opcao == 6:
                texto = input('Digite o nome do arquivo: ')
                dados = f"CONTAR_LINHAS {texto}"
            elif opcao == 7:
                texto = input('Digite o nome do arquivo: ')
                dados = f"CONTAR_PALAVRAS {texto}"

            client_sock.send(dados.encode('utf-8'))
            resposta = client_sock.recv(BUFSIZ)
            if not resposta:
                break
            print("Received from server:", resposta.decode('utf-8'))
            continuar = input("Continuar[s/n]?")
            if(continuar.lower()=="n"):
                client_sock.send(b"END")
                continua=False

    except KeyboardInterrupt:
        print("Ok, saindo!!")

    client_sock.close()    
    