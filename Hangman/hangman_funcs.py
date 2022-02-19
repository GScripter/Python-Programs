from constants import CORES, ALIMENTOS, ANIMAIS

def cercar_mensagem(msg):
    print('-'*22)
    print(f'{CORES["AZUL"]} {msg:^22} {CORES["FIM"]}')
    print('-'*22)


def escolher_categoria():
    cercar_mensagem('GÊNERO')
    print(f'''{CORES['AMARELO']}1- Animais
2- Alimentos\033[m''')
    print('-'*22)
    while True:
        try:
            opcao = int(input('Escolha uma categoria: '))
        except:
            print('\033[31mErro: digite 1 ou 2 \033[m')
        else:
            if opcao == 1 or opcao == 2:
                return opcao
            print('\033[31mErro: digite 1 ou 2 \033[m')
