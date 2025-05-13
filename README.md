

## 📄 Descrição Geral
Este projeto implementa um cliente e servidor TCP em Python para realizar a **transferência de arquivos entre máquinas** conectadas via rede local ou simuladas. Ele permite que o cliente envie um arquivo ao servidor, que o recebe e o salva localmente.

## 🧩 Componentes do Sistema

### 1. Servidor (`servidor.py`)
- Escuta conexões na porta 5001.
- Aguarda o nome do arquivo enviado pelo cliente.
- Responde com um `ACK` para confirmar o recebimento do nome.
- Recebe o conteúdo do arquivo em blocos de 4096 bytes.
- Salva o arquivo com o nome original.

### 2. Cliente (`cliente.py`)
- Verifica a existência do arquivo localmente.
- Conecta ao servidor por IP e porta.
- Envia o nome do arquivo.
- Aguarda confirmação (`ACK`) do servidor.
- Envia o conteúdo binário do arquivo.
- Exibe confirmação de envio bem-sucedido.

### 3. Arquivo de Teste (`arquivo.txt`)
- Conteúdo: `teste teste testando`.
- Usado para validar o envio e recebimento.


## Video explicando 
- Vídeo explicativo: [YouTube](https://youtu.be/nCOOmlSuZ58)

## 🎯 Objetivo
Demonstrar conhecimentos em:
- Redes TCP/IP
- Comunicação com sockets
- Manipulação de arquivos binários
- Estrutura cliente-servidor em Python
- Execução e testes locais de sistemas distribuídos simples

