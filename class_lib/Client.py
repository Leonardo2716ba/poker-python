import socket
from Functions import *

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    limpar_terminal()
    try:
        while True:
            print("Aguardando resposta do servidor...")
            jogada = string_vazia()
            mensagem_servidor = string_vazia()
            
            mensagem_servidor = client_socket.recv(1024).decode('utf-8')

            if mensagem_servidor == "input":
                mensagem_servidor = string_vazia()
                mensagem_servidor = client_socket.recv(1024).decode('utf-8')
                jogada = input(mensagem_servidor)
                client_socket.send(jogada.encode('utf-8'))
            else:
                print(mensagem_servidor)
                
    except KeyboardInterrupt:
        client_socket.close()
    except BrokenPipeError:
        client_socket.close()

if __name__ == "__main__":  
    main()
