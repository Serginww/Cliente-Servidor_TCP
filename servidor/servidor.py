import socket

HOST = '0.0.0.0'  
PORTA = 5001      

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'wb') as f:
        f.write(dados)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORTA))
        s.listen(1)
        print(f"Servidor esperando a conexão na porta {PORTA}...")

        conexao, endereco = s.accept()
        with conexao:
            print(f"Conectado por {endereco}")

            # Primeiro recebe o nome do arquivo
            nome_arquivo = conexao.recv(1024).decode()
            print(f"Nome do arquivo: {nome_arquivo}")

            # Confirma recebimento do nome
            conexao.sendall(b'ACK')

            # Agora recebe o conteúdo do arquivo
            dados = b''
            while True:
                parte = conexao.recv(4096)
                if not parte:
                    break
                dados += parte

            salvar_arquivo(nome_arquivo, dados)

if __name__ == "__main__":
    servidor()
