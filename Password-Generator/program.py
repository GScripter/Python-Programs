from random import choices
from time import sleep
from datetime import datetime, date
import os


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
  - [S/n] Caso nada seja digitado em continuar, o S será usado como padrão.
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



class PasswordGenerator:
    nums = '0123456789'
    letras_g = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_p = letras_g.lower()
    crt = '!@#$%^&*()?:.,;-=+\|/'
    tudo = nums + letras_p + letras_g + crt


    def __init__(self, tamanho=6, quantidade=1):
        self.tamanho = tamanho
        self.quantidade = quantidade


    # Gerar Senhas
    def gerar(self):
        senhas = []
        n=lg=lp=c=False
        for c in range(0, quantidade):
            while True:
                senha = choices(self.tudo,k=tamanho)
                for c in senha:
                    if c in self.nums:
                        n = True
                    elif c in self.letras_g:
                        lg = True
                    elif c in self.letras_p:
                        lp = True
                    elif c in self.crt:
                        c = True
                if n == True and lg == True and lp == True and c == True:
                    n=lg=lp=c=False
                    senhas.append(senha)
                    break
                else:
                    n=lg=lp=c=False
        return senhas


    # Salvar senha(s) em um arquivo de texto.
    def salvar(self,senhas):
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
                    obj = PasswordGenerator(tamanho,quantidade)
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
