from random import choices
from time import sleep
from datetime import datetime, date
import os, string, secrets


print('''\033[34m
  ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
  ║╔═╗║║╔══╝║╔═╗║║╔═╗║╚╗╔╗║║╔═╗║║╔═╗║
  ║║─╚╝║╚══╗║╚═╝║║║─║║─║║║║║║─║║║╚═╝║
  ║║╔═╗║╔══╝║╔╗╔╝║╚═╝║─║║║║║║─║║║╔╗╔╝
  ║╚╩═║║╚══╗║║║╚╗║╔═╗║╔╝╚╝║║╚═╝║║║║╚╗
  ╚═══╝╚═══╝╚╝╚═╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝
              ╔═══╗╔═══╗
              ╚╗╔╗║║╔══╝
              ─║║║║║╚══╗
              ─║║║║║╔══╝
              ╔╝╚╝║║╚══╗
              ╚═══╝╚═══╝
    ╔═══╗╔═══╗╔═╗─╔╗╔╗─╔╗╔═══╗╔═══╗
    ║╔═╗║║╔══╝║║╚╗║║║║─║║║╔═╗║║╔═╗║
    ║╚══╗║╚══╗║╔╗╚╝║║╚═╝║║║─║║║╚══╗
    ╚══╗║║╔══╝║║╚╗║║║╔═╗║║╚═╝║╚══╗║
    ║╚═╝║║╚══╗║║─║║║║║─║║║╔═╗║║╚═╝║
  
  
  - O tamanho mínimo possível de senha é 6.
  - A quantidade de senhas que podem ser geradas é ilimitada.
  - Ctrl + c Interrompe o programa em qualquer parte do código.
  - [S/n] Isso significa que caso nada seja digitado o S será usado como padrão.
  - As senhas são salvas na pasta MinhasSenhas
  - Github: https://github.com/GabrielSantos198/\033[m
''')

cores = {'amarelo':'\033[1;33m',
        'vermelho':'\033[1;31m'}


# A vaca que aparece nas Mensagens
def vaca(msg,cor,q):
    print(f'''
{cor}{msg}\033[m
{"="*q}
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\

                ||----w |
                ||     ||
''')



class GeradordeSenhas:
    tudo = string.ascii_letters + string.digits + string.punctuation


    def __init__(self, tamanho, quantidade):
        self.tamanho = tamanho
        self.quantidade = quantidade


    # Gerar Senhas
    def gerar(self):
        """
        Método que gera senha ou grupos de senhas e as retorna em forma de lista.
        """
        senhas = []
        for total in range(0, self.quantidade):
            instancia = secrets.SystemRandom()
            senha = instancia.choices(GeradordeSenhas.tudo,k=self.tamanho-4)
            # Presença aleatória obrigatória nas senhas
            p = instancia.choice(string.ascii_lowercase)
            g = instancia.choice(string.ascii_uppercase)
            crt = instancia.choice(string.punctuation) 
            n = instancia.choice(string.digits)
            senhas.append(instancia.sample(g+p+crt+n,k=4)+senha)
        return senhas


    # Salvar senha(s) em um arquivo de texto ou não.
    def salvar(self,senhas):
        """
        Esse Método irá receber a lista de senha(s) retornadas pelo método gerar. E trabalhará para tornar possível salvá-la em arquivo de texto de forma organizada.
        """
        while True:
            try:
                res = str(input('Deseja Salvar em um Arquivo? [S/n] '))
                if res == '':
                    res = 'S'
            except KeyboardInterrupt:
                global continua
                continua = False
                break
            except:
                vaca(' Por favor digite uma opção válida.',cores['vermelho'],37)
            else:
                if res.strip().upper()[0] in 'SN':
                    if res.strip().upper()[0] == 'S':
                        if not os.path.isdir('MinhasSenhas'):
                            os.makedirs('MinhasSenhas')
                        arquivo = str(f'{date.today()}|{datetime.now().microsecond}')
                        abrir = open(f'MinhasSenhas/Senha-Gerada-Em-{arquivo}','w+')
                        for c in senhas:
                            for i in c:
                                abrir.write(i)
                            abrir.write('\n')
                        abrir.close()
                        print(f'\033[1;32mArquivo \033[1;33mSenha-Gerada-Em-{arquivo} \033[1;32msalvo com sucesso no caminho \033[1;33m{os.getcwd()}/MinhasSenhas/\033[m')
                        break
                    else:
                        break
                vaca(' Por favor digite uma opção válida.',cores['vermelho'],37)



continua = True
while continua:
    # Validar Tamanho da Senha
    while True:
        try:
            tamanho = int(input('Tamanho de Senha: '))
        except KeyboardInterrupt:
            continua = False
            break
        except:
            vaca(' Por favor digite um tamanho válido.',cores['vermelho'],37)
        else:
            if tamanho >= 6:
                break
            vaca(' Para a sua própria segurança crie senhas \n          com 6 ou mais caracteres.',cores['amarelo'],42)
    # Validar Quantidade de Senhas Geradas
    if continua:
        while True:
            try:
                quantidade = int(input('Quantas senhas você deseja? '))
            except KeyboardInterrupt:
                continua = False
                break
            except:
                vaca(' Por favor digite uma quantidade válida.',cores['vermelho'],37)
            else:
                if quantidade >= 1:
                    # Instancia da classe
                    obj = GeradordeSenhas(tamanho,quantidade)
                    gerar_senhas = obj.gerar()
                    if tamanho <= 20:
                        print('—'*20)
                        print('\033[1;32m{:^20}\033[m'.format('Senhas Geradas'))
                        print('—'*20)
                    else:
                        print('—'*tamanho)
                        print(f'\033[1;32m{"Senha(s) Gerada(s)"}\033[m'.center(tamanho+10))
                        print('—'*tamanho)
                    sleep(.5)
                    for c in gerar_senhas:
                        sleep(.5)
                        for i in c:
                            print(i,end='')
                        print()
                    if tamanho <= 20:
                        print('—'*20)
                    else:
                        print('—'*tamanho)
                    # Salvar senha(s) em um arquivo de texto.
                    obj.salvar(gerar_senhas)
                    break
                else:
                    vaca(' Não tem como gerar 0 senhas. \n  Por Favor Digite Novamente. ',cores['vermelho'],30)
    # Perguntar e validar escolha de parar ou rodar novamente o programa.
    if continua:
        while True:
            try:
                res = str(input('Deseja rodar novamente o programa? [S/n] '))
                if res == '':
                    res = 'S'
            except KeyboardInterrupt:
                continua = False
                break
            except:
                vaca(' Por favor digite uma opção válida.',cores['vermelho'],37)
            else:
                if res.strip().upper()[0] in 'SN':
                    if res.strip().upper()[0] == 'N':
                        continua = False
                        break
                    else:
                        break
                vaca(' Por favor digite uma opção válida.',cores['vermelho'],37)


print('''\033[34m
─██████████████─██████████─██████──────────██████
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒██─██▒▒██████████████▒▒██
─██▒▒██████████─████▒▒████─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
─██▒▒██───────────██▒▒██───██▒▒██████▒▒██████▒▒██
─██▒▒██████████───██▒▒██───██▒▒██──██▒▒██──██▒▒██
─██▒▒▒▒▒▒▒▒▒▒██───██▒▒██───██▒▒██──██▒▒██──██▒▒██
─██▒▒██████████───██▒▒██───██▒▒██──██████──██▒▒██
─██▒▒██───────────██▒▒██───██▒▒██──────────██▒▒██
─██▒▒██─────────████▒▒████─██▒▒██──────────██▒▒██
─██▒▒██─────────██▒▒▒▒▒▒██─██▒▒██──────────██▒▒██
─██████─────────██████████─██████──────────██████\033[m
''')
