import os
import time
import eyed3
import telepot
import datetime
from Brain import Chatbot

bot = Chatbot("Martha")# Nome do Bot
telegram = telepot.Bot(SEU_TOKEN_AQUI)# Token recebido quando você criou um bot no Telegram

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    frase = frase.lower()
    resp = bot.pensa(frase)
    bot.fala(resp)
    
    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    # Referencia a Yu-Gi-Oh
    if resp == 'Com esta carta virada para baixo eu encerro minha jogada':
    	telegram.sendChatAction(chatID, 'upload_photo')
    	telegram.sendPhoto(chatID, open('imagens/carta.png', 'rb'))
    # /Referencia a Yu-Gi-Oh

    # Stickers
    if frase == '/start':
    	telegram.sendChatAction(chatID, 'upload_photo')
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/15.png', 'rb'))

    if frase == 'o que você faz nos fins de semana?':
    	telegram.sendChatAction(chatID, 'upload_photo')
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/22.png', 'rb'))

    if ('Muito prazer' in resp) or ('Olá ' in resp):
    	telegram.sendChatAction(chatID, 'upload_photo')
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/14.png', 'rb'))

    if 'kkk' in resp:
    	telegram.sendChatAction(chatID, 'upload_photo')
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/13.png', 'rb'))
    if 'tocar ' in frase:
        telegram.sendChatAction(chatID, 'upload_photo')
        telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/27.png', 'rb'))
   	# /Stickers
    
    # Audio
    if frase == 'você gosta de carnaval?':
    	# send (message, voice, audio,documment, videos, localization)
    	telegram.sendChatAction(chatID, 'upload_audio')# atualiza os estatos do bot Ex.: enviando audio | (typing, record_audio, audio,documment, videos, localization)
    	time.sleep(5) # Espera 5 segundos para enviar a mensagem
    	telegram.sendVoice(chatID, voice=open('audios/carnaval.ogg', 'rb'))# Envia um audio como mensagem de voz
    # /Audio

    telegram.sendChatAction(chatID, 'typing')# Enquanto espera os 3 segundos o status do bot ficam como Typing(Digitando)
    time.sleep(3)# Espera 3 segundos para enviar a mensagem
    telegram.sendMessage(chatID, resp)# Responde a mensagem do ID do usuario que a envoiu, mensagem analizada pelo Brain.py

telegram.message_loop(recebendoMsg)

while True:
	pass