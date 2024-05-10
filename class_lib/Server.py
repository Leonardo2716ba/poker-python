import socket
import threading
from Functions import *
import time
from Player import Player

def definir_vencedor():
    return int(input("Quem foi o vencedor ?"))

def receive_players_username(clientes):
    players = []
    for cliente in clientes:
        player = Player()
        mensagem_jogador = string_vazia()
        cliente[0].send('input'.encode('utf-8'))
        time.sleep(1)
        cliente[0].send("Digite seu nome de usuário: ".encode('utf-8'))
        mensagem_jogador = cliente[0].recv(1024).decode('utf-8')
        
        if is_valid_username(mensagem_jogador):
            player.set_username(mensagem_jogador)
            player.set_addr(cliente[0].getpeername())
            players.append(player)
            print(f"Jogador digitou username: {mensagem_jogador}")
            
        else:
            cliente[0].send("input".encode('utf-8'))
            time.sleep(3)
            cliente[0].send("Nome de usuário não pode ser vazio".encode('utf-8'))
            pass
    return players

def enviar_resultado(clientes, resultado):
    for cliente in clientes:
        cliente[0].send(resultado.encode('utf-8'))

def jogar_jokenpo(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif (jogada1 == "pedra" and jogada2 == "tesoura") or \
         (jogada1 == "tesoura" and jogada2 == "papel") or \
         (jogada1 == "papel" and jogada2 == "pedra"):
        return "Jogador 1 venceu!"
    else:
        return "Jogador 2 venceu!"

def handle_client(clientes):
    try:
        jogadas = []
        for cliente in clientes:
            print(f"Jogador conectado: {cliente[0].getpeername()}")
        
        players = receive_players_username(clientes)
        
        for p in players:
            print(p.display_info())

        while True:
            try:
                jogadas.clear()
                for cliente in clientes:
                    print(cliente[0])
                    cliente[0].send("input".encode('utf-8'))
                    time.sleep(1)
                    cliente[0].send("Sua vez de jogar! Escolha pedra, papel ou tesoura: ".encode('utf-8'))
                    mensagem_jogador = cliente[0].recv(1024).decode('utf-8')
                                        
                    print(f"Jogador{encontrar_player(players, cliente.get_addr())} escolheu: {mensagem_jogador}")
                    jogadas.append(mensagem_jogador)

                resultado = jogar_jokenpo(jogadas[0], jogadas[1])
                print(f"Resultados: {resultado}")
                time.sleep(3)
                
                thread_envio = threading.Thread(target=enviar_resultado, args=(clientes, resultado))
                thread_envio.start()
                thread_envio.join()

            except KeyboardInterrupt:
                print("\nEncerrando conexões")
                break
            
            #finally:
            #    limpar_terminal()
    except KeyboardInterrupt:
        print("\nEncerrando conexões")
    finally:
        for cliente in clientes:
            cliente[0].close()


def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print(f"Servidor aguardando conexões na porta {port}...")

    clientes = []
    try:
        for _ in range(2):
            cliente = server_socket.accept()
            clientes.append(cliente)

        game_thread = threading.Thread(target=handle_client, args=(clientes,))
        game_thread.start()
        game_thread.join()

    except KeyboardInterrupt:
        print("\nEncerrando servidor")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
