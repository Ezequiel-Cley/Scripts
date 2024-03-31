import requests

# Função conecta a API do Telegram para envio de Mensagens automáticamente
def sender_photo(token,chat,caminho):
    """
    Envia uma foto para um chat no Telegram usando o bot e o token fornecidos.

    Parameters:
        token (str): O token do bot do Telegram.
        chat (str): O ID do chat para o qual a foto será enviada.
        caminho (str): O caminho do arquivo da foto a ser enviada.

    Returns:
        None

    Exemplo de uso:
    sender_photo('seu_token', 'id_do_chat', 'caminho_da_foto.jpg')
    """
    # URL da API do Telegram para enviar a foto
    url = f'https://api.telegram.org/bot{token}/sendPhoto'

    # Parâmetros da requisição
    params = {
        'chat_id': chat,
    }

    # Abrir o arquivo da foto em modo binário
    with open(caminho, 'rb') as foto:
        # Enviar a foto como um arquivo
        response = requests.post(url, params=params, files={'photo': foto})

    #---------------------------- DADOS INSERIDOS----------------------
    # Verifique a resposta
    if response.status_code == 200:
        print("Foto enviada com sucesso!")
    else:
        print("Erro ao enviar a foto:", response.text)


# Criando Variaveis para disparar a mensagem

# Define o token do seu bot do Telegram
tk = 'TOKEN_DO_SEU_BOT_DO_TELEGRAM'

# Define o Grupo que deseja realizar o Envio
gp = 'ID_DO_GRUPO_OU_USUARIO'

# Define Caminho da foto que deseja enviar Automáticamente
ft = r'\\C\aminho\completo\da\foto\imagem.png'

# Chama a função para envio da Mensagem
sender_photo(tk,gp,ft)