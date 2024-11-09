

# Realizado Nova_Conexão ao SFTP
# Armazendo IP para Conexão com SFTP
transport = paramiko.Transport((ip, 22))
# Armazenando Usuario e Senha para Conexão com SFTP
transport.connect(username= Usuario, password= Senha)
# Realizado Tentativa de Conexão com SFTP
# Importando Bibliotecas

# Biblioteca para Conexão com SFTP
import paramiko
# Biblioteca para controlar comandos do CMD de sua MAQUINA
import os
# Bibliotecas de controle Datas e Tempo
from datetime import date, datetime, timedelta
from time import sleep

sftp = transport.open_sftp_client()
print("Conexão Restabelecida Para extração dos arquivos...")
sleep(2)

# Definindo o Local onde se encontra o arquivo que deve ser encaminhado arquivo 01:
pasta_local = '//Disco/Local/Onde/Esta/Arquivo/Para/Enviar/drive'
# Definindo Varivael com o Caminho completo do local onde deve enviar o arquivo 01 :
pasta_remota = '/Caminho/SFTP/para/Colocar/Arquivo'

# Lista todos os arquivos na pasta remota
arquivos_remotos = sftp.listdir(pasta_remota)

# Cria uma variavel em vetor para obter o caminho do local remoto e o arquivo
caminho_remoto = []
# Criar um loop para armazenar no loop todos os locais e nomes dos arquivos
for arquivo in arquivos_remotos:
    caminho_remoto.append(f"{pasta_remota}/{arquivo}")

# Cria uma variavel em vetor para obter o caminho do local do Saturno e o arquivo
caminho_local = []
# Criar um loop para armazenar no loop todos os locais e nomes dos arquivos
for arquivo in arquivos_remotos:
    caminho_local.append(f"{pasta_local}/{arquivo}")
    
for i in range(len(caminho_remoto)):
    caminho_remoto_atual = caminho_remoto[i]
    caminho_local_atual = caminho_local[i]    
    #print(f'Do remoto {caminho_remoto_atual} para o local {caminho_local_atual}')
    try:
        # Seu código para conexão SFTP e transferência de arquivos
        sftp.get(caminho_remoto_atual, caminho_local_atual)
        print(f"Arquivo {arquivo} extraído com sucesso!")
    except IOError as e:
        # Ignorar a validação do tamanho do arquivo
        if "size mismatch in get!" in str(e):
            print(f"Arquivo {arquivo} extraído, mas com tamanho não correspondente ao remoto.")
        else:
            print(f"Ocorreu um erro: {str(e)}")
            
# Fecha a conexão SFTP e SSH
sftp.close()
transport.close()
print("Arquivos extraídos com sucesso!")