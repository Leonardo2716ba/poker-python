import sys
import os

def imprimir_forcado(mensagem):
    print(mensagem, end="")
    sys.stdout.flush()

def is_valid_username(username):
    if not username:
        return False
    else:
        return True


def limpar_terminal():
    # Verifica o sistema operacional e executa o comando correspondente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Outros sistemas operacionais (Linux, macOS)
        os.system('clear')
def string_vazia():
    return ""
