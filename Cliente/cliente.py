import socket
import sys
import os

def cliente(ip_servidor, caminho_arquivo):
    porta = 5001

    if not os.path.exists(caminho_arquivo):
        print("Arquivo não foi encontrado.")
        return

    nome_arquivo = os.path.basename(caminho_arquivo)

    with open(caminho_arquivo, 'rb') as f:
        conteudo = f.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_servidor, porta))

        # manda o arquivo
        s.sendall(nome_arquivo.encode())

        # espera o servidor confirmar 
        ack = s.recv(1024)
        if ack != b'ACK':
            print("Erro com o servidor.")
            return

        # Envia o arquivo 
        s.sendall(conteudo)

        print(f"Arquivo '{nome_arquivo}' enviado com sucesso para {ip_servidor}:{porta}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        #testei como python cliente.py localhost arquivo.txt
        print("Uso: python cliente.py <ip-do-servidor> <arquivo>")
        sys.exit(1)

    ip = sys.argv[1]
    arquivo = sys.argv[2]

    cliente(ip, arquivo)