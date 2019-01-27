from Brain import Chatbot

Bot = Chatbot('Martha')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'Tchau': # Se a resposto for Tchau o programa é encerrado
        break # Encerra o programa