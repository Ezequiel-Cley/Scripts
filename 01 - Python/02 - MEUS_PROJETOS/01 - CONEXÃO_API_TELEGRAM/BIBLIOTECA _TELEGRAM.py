import os
import asyncio
#python-telegram-bot
from telegram import Bot
from telegram import InputFile

# define o token do seu bot do Telegram
TOKEN = 'TOKEN_DO_SEU_BOT_DO_TELEGRAM'

# define o Grupo que deseja realizar o Envio
GRUPO = 'ID_DO_GRUPO_OU_USUARIO'

# inicializa o objeto bot
bot = Bot(token=TOKEN)

# caminho para o arquivo da imagem
caminho_imagem = r'\\DISCO\LOCAL\ONDE\ESTA\IMAGEM\PARA\ENVIO\FOTO.png'

# verifica se o arquivo da imagem existe
if not os.path.exists(caminho_imagem):
    print(f'O arquivo {caminho_imagem} não existe')
    exit()

# define uma função assíncrona para enviar a foto
async def enviar_foto0():
    with open(caminho_imagem, 'rb') as imagem:
        await bot.send_photo(chat_id=GRUPO, photo=InputFile(imagem))

# chama a função assíncrona usando asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(enviar_foto0())
