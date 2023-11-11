# Importando Bibliotecas

# Biblioteca para Conexão com SFTP
import paramiko
# Biblioteca para controlar comandos do CMD de sua MAQUINA
import os
# Bibliotecas de controle Datas e Tempo
from datetime import date, datetime, timedelta
from time import sleep
# Biblioteca para Mondelagem e Criação de Dados
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
#Bibliotecas para envio de MSG no telegram
import asyncio
# Instalar o pacote (python-telegram-bot)
from telegram import Bot
from telegram import InputFile

# Definindo sua conexão com API para realizar conexão:
ip = 'Inserir_Seu_IP' # Exemplo "00.00.00.000"
Usuario = 'Inserir_Usuario_do_SFTP'
Senha =  'Inserir_Senha_do_SFTP'

# Configurado Report para Envio de Informações em caso de erro por Telegram!!!
# define o token do seu bot do Telegram
TOKEN = 'TOKEN_DO_SEU_BOT_TELEGRAM'

# inicializa o objeto bot
bot = Bot(token=TOKEN)

# Incluir código do grupo
GRUPO = 'ID_DE_GRUPO_OU_USUARIO'

# Cria variáveis para o caminho dos arquivos
pasta_remota  = '/Caminho/do/SFTP/para/Colocar/Arquivo'
pasta_local  = '//Disco/Local/Onde/Esta/Arquivo/Para/Enviar'

# Cria uma variável de data para identificar o arquivo
formatted_date = date.today().strftime('%d/%m/%Y').replace("/", "")

# Cria variáveis para o caminho dos arquivos
# Definindo Varivael com o Caminho completo do local onde deve enviar o arquivo 01 :
file_path_s = fr'\Caminho\do\SFTP\para\Colocar\Arquivo\Nome_do_Arquivo_01_{str(formatted_date)}.TXT'
# Definindo o Local onde se encontra o arquivo que deve ser encaminhado arquivo 01:
file_path_r = fr'Disco\Local\Onde\Esta\Arquivo\Para\Enviar\Nome_do_Arquivo__01_.{str(formatted_date)}.TXT'
# Definindo Varivael com o Caminho completo do local onde deve enviar o arquivo 01 :
file_path_s_2 = fr'\Caminho\do\SFTP\para\Colocar\Arquivo\Nome_do_Arquivo_02_{str(formatted_date)}.TXT'
# Definindo o Local onde se encontra o arquivo que deve ser encaminhado arquivo 01:
file_path_r_2 = fr'Disco\Local\Onde\Esta\Arquivo\Para\Enviar\Nome_do_Arquivo__02_.{str(formatted_date)}.TXT'

fulls_path = {file_path_s,file_path_r,file_path_r_2, file_path_s_2}

for i in fulls_path:
    # Verifica se o arquivo 01 existe
    if not os.path.exists(i):
        raise FileNotFoundError("O arquivo não foi encontrado")


# Conectando-se ao SFTP
# Armazendo IP para Conexão com SFTP
transport = paramiko.Transport((ip, 22))
# Armazenando Usuario e Senha para Conexão com SFTP
transport.connect(username= Usuario, password= Senha)
# Realizado Tentativa de Conexão com SFTP
sftp = transport.open_sftp_client()
print("Conexão estabelecida... ")
# Realizar o envio via SFTP 
sleep(3)

try:
    # Realiza o envio do arquivo via SFTP do primeiro arquivo
    sftp.put(file_path_r, file_path_s)
    print("Upload realizado com sucesso do Arquivo 01")

except Exception as e:
    print("Erro ao realizar o upload:", e)

sleep(3)

try:
    # Realiza o envio do arquivo via SFTP do segundo arquivo
    sftp.put(file_path_r_2, file_path_s_2)
    print("Upload realizado com sucesso do Arquivo 02")

except Exception as e:
    print("Erro ao realizar o upload:", e)

finally:
    # Fecha a conexão
    sftp.close()
    transport.close()
    
# Fecha a conexão SFTP e SSH
sftp.close()
transport.close()
print("Arquivos Enviados com sucesso!")


# Realizado Nova_Conexão ao SFTP
# Armazendo IP para Conexão com SFTP
transport = paramiko.Transport((ip, 22))
# Armazenando Usuario e Senha para Conexão com SFTP
transport.connect(username= Usuario, password= Senha)
# Realizado Tentativa de Conexão com SFTP
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


# Cria variáveis para o caminho dos arquivos > Aramzenados no Drive > Extraidos do SFTP
file_path_l = F'{pasta_local}/Nome_do_Arquivo__01_.'+ str(formatted_date) + '.TXT'
file_path_l2 = F'{pasta_local}/Nome_do_Arquivo__02_.' + str(formatted_date) + '.TXT'

print('Realizado Leitura dos arquivos para Comparações')

# Ler os arquivos do dia no Saturno (convencional)
# Lendo e criando colunas validadoras arquivo Servidor Arquivo 01 
convencional_r = pd.read_table(f'{file_path_r}', delimiter='\t', encoding='ISO-8859-1')
convencional_r['Arquivo'] = "Arquivo 01 Local"
convencional_r['ID'] = "1"
convencional_r['Qtd_Sat'] = (f'{convencional_r.shape[0]}')
convencional_r['Tam_Sat'] = (f'{os.path.getsize(file_path_r)}')

# Lendo e criando colunas validadoras arquivo SFTP Arquivo 01 
convencional_l = pd.read_table(f'{file_path_l}', delimiter='\t', encoding='ISO-8859-1')
convencional_l['Arquivo'] = "Arquivo 01 SFTP"
convencional_l['ID'] = "1"
convencional_l['Qtd_SFTP'] = (f'{convencional_l.shape[0]}')
convencional_l['Tam_SFTP'] = (f'{os.path.getsize(file_path_l)}')

# Ler os arquivos do dia no Saturno (digital)
# Lendo e criando colunas validadoras arquivo Servidor Arquivo 02 
digital_r2 = pd.read_table(f'{file_path_r_2}', delimiter='\t', encoding='ISO-8859-1')
digital_r2['Arquivo'] = "Arquivo 02 Local"
digital_r2['ID'] = "2"
digital_r2['Qtd_Sat'] = (f'{digital_r2.shape[0]}')
digital_r2['Tam_Sat'] = (f'{os.path.getsize(file_path_r_2)}')

# Lendo e criando colunas validadoras arquivo SFTP Arquivo 02 
digital_l2 = pd.read_table(f'{file_path_l2}', delimiter='\t', encoding='ISO-8859-1')
digital_l2['Arquivo'] = "Arquivo 02 SFTP"
digital_l2['ID'] = "2"
digital_l2['Qtd_SFTP'] = (f'{digital_l2.shape[0]}')
digital_l2['Tam_SFTP'] = (f'{os.path.getsize(file_path_l2)}')


print('Realizado Tratamento dos Dados')
# Agrupado para Obter Dados necessarios
convencional_r = convencional_r.groupby(by=['ID','Arquivo','Qtd_Sat','Tam_Sat']).agg(TESTE = ('ID','count')).reset_index().drop(columns='TESTE')
convencional_l = convencional_l.groupby(by=['ID','Arquivo','Qtd_SFTP','Tam_SFTP']).agg(TESTE = ('ID','count')).reset_index().drop(columns='TESTE')
digital_r2 = digital_r2.groupby(by=['ID','Arquivo','Qtd_Sat','Tam_Sat']).agg(TESTE = ('ID','count')).reset_index().drop(columns='TESTE')
digital_l2 = digital_l2.groupby(by=['ID','Arquivo','Qtd_SFTP','Tam_SFTP']).agg(TESTE = ('ID','count')).reset_index().drop(columns='TESTE')

# Realizado a Cruzamento para obter uma unica tabela!!!
convencional = pd.merge(left=convencional_r, right=convencional_l, on='ID').reset_index().drop(columns='ID')
digital = pd.merge(left=digital_r2, right=digital_l2, on='ID').reset_index().drop(columns='ID')
frames = [convencional, digital]
retorno = pd.concat(frames)

# Tornando os campos números em tipo float para realizar calculos com eles
retorno['Qtd_Sat'] = pd.to_numeric(retorno['Qtd_Sat'])
retorno['Qtd_SFTP'] = pd.to_numeric(retorno['Qtd_SFTP'])
retorno['Tam_Sat'] = pd.to_numeric(retorno['Tam_Sat'])
retorno['Tam_SFTP'] = pd.to_numeric(retorno['Tam_SFTP'])

# Criando novas colunas com Diferença dos tamanhos e quantidade para comparação
retorno['Dif_Qtd'] = retorno['Qtd_Sat'] - retorno['Qtd_SFTP']
retorno['Dif_Tam'] = retorno['Tam_Sat'] - retorno['Tam_SFTP']
retorno = retorno.drop(columns='index')

# Alterando o Formato das Colunas Valores, para Numero
retorno['Qtd_Sat'] = retorno['Qtd_Sat'].apply(lambda valor: f'{valor:,.2f}')
retorno['Qtd_SFTP'] = retorno['Qtd_SFTP'].apply(lambda valor: f'{valor:,.2f}')
retorno['Tam_Sat'] = retorno['Tam_Sat'].apply(lambda valor: f'{valor:,.2f} KB')
retorno['Tam_SFTP'] = retorno['Tam_SFTP'].apply(lambda valor: f'{valor:,.2f} KB')

# Retirando o Index de Forma Dinamica
b = [retorno]
for i in range(len(b)):
    # Initialize an empty dictionary
    dicionario = {}
    # Fill the dictionary with numerical keys
    for n in range(len(b[i])):
        dicionario[n] = ''
    # Remove the index from the DataFrame
    b[i].rename(index=dicionario, inplace= True)
    
# Armazenando a data e hora atual!!!
data_form = str(format(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'))


print('Realizado Criação de Foto para Disparo')
# Criando Imagem da Primeira Tabela
# Criando uma figura e eixo vazios
fig, ax = plt.subplots(figsize=(10, 6))

# Tamanhos personalizados das colunas (em proporção)
col_widths = [0.12, 0.1, 0.1, 0.12, 0.1, 0.1, 0.1, 0.1]

# Removendo eixos
ax.axis('off')

# Adicionando um título à tabela
titulo = f"Acompanhamento de Envio de Retorno SP  - Atualizado: {data_form}"
ax.set_title(titulo, fontsize=25, fontweight='bold', loc='center', pad=10)

# Criando uma tabela com os dados do DataFrame
tab = table(ax, retorno, loc='center', cellLoc='center', colWidths=col_widths)

# Personalizando o estilo da tabela
tab.auto_set_font_size(False)
tab.set_fontsize(12)
tab.scale(2.2, 2.2)  # Ajuste o tamanho da tabela conforme necessário

# Personalizando células específicas
for i in range(len(retorno.columns)):
    tab.get_celld()[0, i].set_facecolor("#435AC2")  # Fundo Verde para a primeira linha (cabeçalho)
    tab.get_celld()[0, i].set_fontsize(14)  # Tamanho de fonte maior para o cabeçalho
    tab.get_celld()[0, i].set_text_props(weight='bold')  # Texto em negrito para o cabeçalho
    # ... Continue personalizando outras células, como bordas, cores de fundo, cores de texto, etc.

for i, row in enumerate(retorno.iterrows()):
    color = "white" if i % 2 == 0 else "#E8E8E8"  # Alterne entre branco e cinza claro
    for j, cell in enumerate(row[1]):
        cell_obj = tab.get_celld()[i + 1, j]
        cell_obj.set_facecolor(color)  # Define a cor de fundo da célula
        cell_obj.set_edgecolor("gray")  # Cor das bordas
        cell_obj.set_linewidth(1.0)   # Define a cor de fundo da célula

img = '//DISCO/CAMINHO/IMAGEM/FOTO.jpeg'

# Salvando a figura como uma imagem
plt.savefig(rf'{img}', bbox_inches='tight', pad_inches=0.5)
#plt.show()

print('Realizado Disparo de Foto para Telegram')
# Enviar a mensagens desejada
# Cria uma função assicronica para Enviar_mensagens():
async def enviar_foto():
    with open(img, 'rb') as imagem:
        await bot.send_photo(chat_id=GRUPO, photo=InputFile(imagem))
# chama a função assíncrona usando asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(enviar_foto())

print('Envio e validações finalizadas')