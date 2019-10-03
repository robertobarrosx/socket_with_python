import socket

HOST ='localhost'
PORT = 12346
BUFSIZ = 4024
ADDR = (HOST, PORT)


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    server_socket.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR, 1 )
    while True:
        print('Server waiting for connection...')
        client_sock, addr = server_socket.accept()
        print('Client connected from: ', addr)
        while True:
            data = client_sock.recv(BUFSIZ)
            if not data or data.decode('utf-8') == 'END':
                break
            #print("Received from client: %s" % data.decode('utf-8'))
            print("Received from client {}: {}".format(addr,data.decode('utf-8')))
            try:
                data = data.decode('utf-8')
                comando = data.split(" ",1)

                if comando[0] == "CRIAR_ARQUIVO":
                    print("Estou criando um arquivo..")
                    nome_arquivo = comando[1]
                    if not ".txt" in nome_arquivo:
                        nome_arquivo = nome_arquivo + ".txt"
                    conteudo = ""
                    try:
                        arquivo = open('arquivos/lista.txt', 'r')
                        conteudo = arquivo.readlines()
                        if (nome_arquivo in conteudo) == False:
                            conteudo.append('\n' + nome_arquivo)
                    except:
                        pass
                    arquivo = open('arquivos/lista.txt', 'w')
                    arquivo.writelines(conteudo)
                    arquivo.close()
                    arquivo = open(f"arquivos/{nome_arquivo}", 'w')
                    arquivo.close()
                    msg = f"Arquivo \"{nome_arquivo}\" criado com sucesso!"
                    print(msg)
                elif comando[0] == "ESCREVER_ARQUIVO":
                    splitcomando = comando[1].split(" ",1)
                    nome_arquivo = splitcomando[0]
                    texto = splitcomando[1]
                    if not ".txt" in nome_arquivo:
                        nome_arquivo = nome_arquivo + ".txt"
                    conteudo = ""
                    try:
                        arquivo = open(f"arquivos/{nome_arquivo}", 'r')
                        conteudo = arquivo.readlines()
                        if (nome_arquivo in conteudo) == False:
                            conteudo.append(texto + '\n')
                        arquivo = open(f"arquivos/{nome_arquivo}", 'w')
                        arquivo.writelines(conteudo)
                        arquivo.close()
                        msg = f"Arquivo \"{nome_arquivo}\" escrito com sucesso!"
                    except:
                        msg = f"O arquivo \"{nome_arquivo}\" não existe!"

                    print(msg)
                elif comando[0] == "LISTAR":
                    try:
                        arquivo = open('arquivos/lista.txt', 'r')
                        conteudo = arquivo.readlines()
                        msg = "\nLista de Arquivos:\n"
                        for arq in conteudo:
                            msg += arq

                    except:
                        msg = f"Não existe arquivos criados!"
                    print(msg)
                elif comando[0] == "MOSTRAR_LINHA-NOME_ARQUIVO":
                    splitcomando = comando[1].split(" ", 1)
                    nome_arquivo = splitcomando[0]
                    linha = int(splitcomando[1])
                    if not ".txt" in nome_arquivo:
                        nome_arquivo = nome_arquivo + ".txt"
                    conteudo = ""
                    try:
                        arquivo = open(f"arquivos/{nome_arquivo}", 'r')
                        conteudo = arquivo.readlines()
                        if len(conteudo) >= linha:
                            msg = f"Arquivo \"{nome_arquivo}\" - Conteudo da linha \'{linha}\': \"{conteudo[linha-1]}\""
                        else:
                            msg = f"O arquivo \"{nome_arquivo}\" não tem essa linha!"
                    except:
                        msg = f"O arquivo \"{nome_arquivo}\" não existe!"

                    print(msg)
                elif comando[0] == "BUSCAR_PALAVRA-NOME_ARQUIVO":
                    splitcomando = comando[1].split(" ", 1)
                    nome_arquivo = splitcomando[0]
                    palavra = splitcomando[1]
                    if not ".txt" in nome_arquivo:
                        nome_arquivo = nome_arquivo + ".txt"
                    conteudo = ""
                    try:
                        arquivo = open(f"arquivos/{nome_arquivo}", 'r')
                        conteudo = arquivo.readlines()
                        linhas = []
                        naotem = True
                        for i,linha in enumerate(conteudo,1):
                            forma = ""
                            for x in range(0,len(linha)):
                                if linha[x] != ' ' and linha[x] != '\n' and linha[x] != ',' and linha[x] != '.' and linha[x] != ':' and linha[x] != ';':
                                    forma += linha[x]
                                else:
                                    if forma.lower() == palavra.lower():
                                        if not i in linhas:
                                            linhas.append(i)
                                        naotem = False
                                    forma = ""
                        if naotem:
                            msg = f"Arquivo \"{nome_arquivo}\" - Palavra não encontrada no arquivo."
                        else:
                            msg = f"A palavra \"{palavra}\" esta nas linhas {linhas} do arquivo \"{nome_arquivo}\"."
                    except Exception as e:
                        print(e)
                        msg = f"O arquivo \"{nome_arquivo}\" não existe!"

                    print(msg)
                elif comando[0] == "CONTAR_LINHAS":
                    nome_arquivo = comando[1]
                    if not ".txt" in nome_arquivo:
                        nome_arquivo = nome_arquivo + ".txt"
                    conteudo = ""
                    try:
                        arquivo = open(f"arquivos/{nome_arquivo}", 'r')
                        conteudo = arquivo.readlines()

                        msg = f"O arquivo \"{nome_arquivo}\" tem \'{len(conteudo)}\' linhas"
                    except:
                        msg = f"O arquivo \"{nome_arquivo}\" não existe!"
                    print(msg)

                elif comando[0] == "CONTAR_PALAVRAS":
                    nome_arquivo = comando[1]

                    if not ".txt" in nome_arquivo:
                        nome_arquivo = nome_arquivo + ".txt"
                    conteudo = ""
                    try:
                        arquivo = open(f"arquivos/{nome_arquivo}", 'r')
                        conteudo = arquivo.readlines()
                        palavras = 0
                        naotem = True
                        for i, linha in enumerate(conteudo, 1):
                            forma = ""
                            for x in range(0, len(linha)):
                                if linha[x] != ' ' and linha[x] != '\n' and linha[x] != ',' and linha[x] != '.' and \
                                        linha[x] != ':' and linha[x] != ';':
                                    forma += linha[x]
                                else:
                                    if forma.lower() != "":
                                        palavras += 1
                                        naotem = False
                                    forma = ""
                        if naotem:
                            msg = f"Arquivo \"{nome_arquivo}\" - não tem palavras."
                        else:
                            msg = f"O arquivo \"{nome_arquivo}\" tem \'{palavras}\' palavras."
                    except Exception as e:
                        print(e)
                        msg = f"O arquivo \"{nome_arquivo}\" não existe!"

                    print(msg)

                client_sock.send(msg.encode('utf-8'))
            except KeyboardInterrupt:
                print("Exited by user")
        client_sock.close()
    server_socket.close()