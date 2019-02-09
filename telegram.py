import os
import time
import telepot
import datetime
from Brain import Chatbot

bot = Chatbot("Martha")# Nome do Bot
SEU_TOKEN_AQUI = "Token"
telegram = telepot.Bot(SEU_TOKEN_AQUI)# Token recebido quando você criou um bot no Telegram

def recebendoMsg(msg):
	# Funções importadas do arquivo Brain.py 
    frase = bot.escuta(frase=msg['text'])# A frase do usuario é igual ao que ele digitar, isso irá passar pela função escuta do bot
    frase = frase.lower()# A frase será colocada completamente em menusculo para evitar erros e para diminuir o codigo
    resp = bot.pensa(frase)# A frase do usuario irá passar pela função pensa e o bot irá responder de acordo com o database
    bot.fala(resp)# E enviará a resposta com a função fala 
    
    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    # Referencia a Yu-Gi-Oh
    if resp == 'Com esta carta virada para baixo eu encerro minha jogada':# Se isto for digitado...
    	telegram.sendChatAction(chatID, 'upload_photo')# O bot fica com o status de Enviando Imagem
    	telegram.sendPhoto(chatID, open('imagens/carta.png', 'rb'))# Envia esta imagem para o usuario
    # /Referencia a Yu-Gi-Oh



    # Stickers
    ## Para quando começar a conversa
    if frase == '/start':# Se isto for digitado...
    	telegram.sendChatAction(chatID, 'upload_photo')# O bot fica com o status de Enviando Imagem
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/15.png', 'rb'))# Envia esta imagem para o usuario

    ## Para perguntas especiais
    if frase == 'o que você faz nos fins de semana?':# Se isto for digitado...
    	telegram.sendChatAction(chatID, 'upload_photo')# O bot fica com o status de Enviando Imagem
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/22.png', 'rb'))# Envia esta imagem para o usuario

    ## Para comprimentar o usuario
    if ('Muito prazer' in resp) or ('Olá ' in resp):# Se isto for digitado...
    	telegram.sendChatAction(chatID, 'upload_photo')# O bot fica com o status de Enviando Imagem
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/14.png', 'rb'))# Envia esta imagem para o usuario

    ## Para simular uma risada durante a conversa
    if 'kk' in resp:# Se isto for digitado...
    	telegram.sendChatAction(chatID, 'upload_photo')# O bot fica com o status de Enviando Imagem
    	telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/13.png', 'rb'))# Envia esta imagem para o usuario
    
    ## Para o caso do usuario pedir para o bot tocar algúma musica 
    if 'tocar ' in frase:# Se isto for digitado...
        telegram.sendChatAction(chatID, 'upload_photo')# O bot fica com o status de Enviando Imagem
        telegram.sendSticker(chatID, open('imagens/Stickers/Alice Fox/27.png', 'rb'))# Envia esta imagem para o usuario
   	# /Stickers
    


    # Audio
    ## Referencia a Ciri do IOS
    if frase == 'você gosta de carnaval?':# Se isto for digitado...
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