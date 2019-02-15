import json
import sys
import os
import subprocess as s
import datetime

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open('database/Martha.json','r')
            afirm = open('database/afirm.json','r')
        except FileNotFoundError:
            memoria = open('database/Martha.json','w')
            memoria.close()
            memoria = open('database/Martha.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        self.resp_afir = json.load(afirm)
        afirm.close()
        memoria.close()
        self.historico = [None]

    def escuta(self,frase=None):
        if frase == None:# Se não ouvef nada armazenado na variavel 'frase' ele irá exigir que algo seja digitado para que assim ela tenho um valor(str)
            frase = str(input('\033[36muser\033[35m@martha\033[0;0m:$ ')).lower()# Texto que será exibido ates do campo onde será incerido a frase do usuario, "\033[35m" e os outros são para modificar a cor do texto
            # str(frase)# Esta parte recebe o que foi digitado pelo usuario e converte em uma string
            # lower()# Isso faz com que a frase fique toda em menusculo para facilitar o reconhecimento da frase
            # strip() retira os espaços indesejados de uma string
        frase = frase.strip().replace('é','eh') # E isso troca todo 'é' por 'eh' para evitar problemas com carecteris especiais
        return frase# Em seguida ele retorna a frase depois destes processos

    def pensa(self,frase):
        if frase in self.frases:
            return self.frases[frase]
        if 'data' in frase: # Se a mensagem digitada pelo úsuario for data ele dira a data e hora do dia
            day = datetime.datetime.now().strftime("%d/%m/%Y") # Data atual
            hour = datetime.datetime.now().strftime("%H:%M") # Hora atual
            return ('Data: {} Hora: {}'.format(day,hour)) # E exibi as informações na tela em forma de texto

        if 'kk' in frase:
            return 'kklkkj'

        if 'obrigad' in frase:# Responde 'De nada' quando é digitado obrigado(a)
            return 'De nada'

        if frase == '/aprende':
            return 'Digite a frase: '

        # Responde frases que dependem do historico
        ultimaFrase = self.historico [-1]
        if self.historico:
            if ultimaFrase == 'Olá, qual o seu nome?':
                nome = self.pegaNome(frase)
                frase = self.respondeNome(nome)
                return frase
            if ultimaFrase == 'Digite a frase: ':
                self.chave = frase
                return 'Digite a resposta: '
            if ultimaFrase == 'Digite a resposta: ':
                resp = frase
                self.frases[self.chave] = resp
                self.gravaMemoria()
                return 'Aprendido'
        
            if ultimaFrase == 'Posso me defender?':                
                if frase in self.resp_afir:
                    return 'Com esta carta virada para baixo eu encerro minha jogada'
                if frase == 'não':
                    return 'Droga'

        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
            return 'Não entendi'
        
    def pegaNome(self,nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:]
        nome = nome.title().split() # title() deixa a 1ª letra de cada palavra maiuscula e split() divide a frase em palavras
        return nome[0]+' '+nome[len(nome)-1] # Ele retorna somente a 1ª palavra do nome

    def respondeNome(self,nome):
        if nome in self.conhecidos:
            frase = 'Olá '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome

    def gravaMemoria(self):# remover partes desnecessarias antes de enviar ao GitHub
        memoria = open('database/'+self.nome+'.json','w')
        afirm = open('database/afirm.json','w')
        json.dump([self.conhecidos,self.frases], memoria, indent=3, sort_keys=True)
        json.dump([self.resp_afir], afirm, indent=1, sort_keys=True)
        memoria.close()
        afirm.close()

    def fala(self,frase):
        if 'executar ' in frase:# Se o bot responder alguma frase que tenha a palavra 'executar'
            comando = frase.replace('executar ','')# Ele irá armazenar na variavel 'comando' a mesma frase só que sem a palavra 'executar'
            try:
                s.Popen(comando)# E então ira tentar executar o resto da frase como um comando do terminal do Linux
            except FileNotFoundError:
                s.Popen(['xdg-open',comando])       
        else:# Se não for o caso ele irá exibir uma frase como resposta
            print('\033[33mrbot\033[35m@martha\033[0;0m:$ '+frase)# Como já mencionado assima "\033[35m" e as demais sentensas semelhantes são para colorir o texto que será exibido
        self.historico.append(frase)
