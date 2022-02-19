import random

from hangman_funcs import escolher_categoria
from drawing import desenho
from constants import CORES, ALIMENTOS, ANIMAIS

print('#'*30)
print(f'# {"JOGO DA FORCA":^26} #')
print('#'*30)
print()

continua = True
while continua:
    categoria = escolher_categoria()
    if categoria == 1:
        palavra_sorteada = random.choice(ANIMAIS)
    else:
        palavra_sorteada = random.choice(ALIMENTOS)
    letras_palavra_sorteada = []
    letras_faladas = []
    casas = []
    for letra in palavra_sorteada:
        letras_palavra_sorteada.append(letra)
        casas.append('_')
    desenho(0)
    for c in range(0, len(casas)):
        if c == 0:
            print(f'{casas[c]:>17}', end='')
        else:
            print(f'{casas[c]}', end='')
    print()
    # Perguntar letra.
    erros = 0
    while True:
        try:
            letra_escolhida = str(input('\nDigite uma letra: ')).strip().upper()[0]
        except:
            print(f'{CORES["VERMELHO"]}Erro: Digite uma letra.{CORES["FIM"]}')
        else:
            if letra_escolhida.isalpha():
                print()
                # Verifica a existência da letra na palavra sorteada.
                for contagem in range(0, len(letras_palavra_sorteada)):
                    if letra_escolhida in letras_palavra_sorteada[contagem]:
                        casas[contagem] = letra_escolhida
                if letra_escolhida not in letras_faladas:
                    letras_faladas.append(letra_escolhida)
                # Desenhos da forca, listar as letras já faladas.
                print(f'{CORES["AMARELO"]}LETRAS FALADAS.{CORES["FIM"]}')
                for letra in letras_faladas:
                    print(f'  {letra}', end='')
                if letra_escolhida not in letras_palavra_sorteada:
                    erros += 1
                if erros == 0:
                    desenho(0)
                elif erros == 1:
                    desenho(1)
                elif erros == 2:
                    desenho(2)
                elif erros == 3:
                    desenho(3)
                if erros != 4:
                    for c in range(0, len(casas)):
                        if c == 0:
                            print(f'{casas[c]:>17}', end='')
                        else:
                            print(f'{casas[c]}', end='')
                    print()
                # Verifica se perdeu ou venceu a partida.
                if '_' not in casas:
                    print()
                    print()
                    print(f'{CORES["VERDE"]}Parabéns! Você, venceu.{CORES["FIM"]}')
                    break
                if erros == 4 and '_' in casas:
                    desenho(4)
                    print()
                    print(f'\033[35mA palavra era{CORES["LILAS"]}"{palavra_sorteada}"{CORES["FIM"]}')
                    print()
                    break
            else:
                print(f'{CORES["VERMELHO"]}Erro: Digite uma letra.{CORES["FIM"]}')
    # Perguntar ao jogador se quer jogar novamente.
    while True:
        print()
        try:
            continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        except:
            print(f'{CORES["VERMELHO"]}ERRO: Digite [S/N] {CORES["FIM"]}')
        else:
            if continuar in 'SN':
                if continuar == 'N':
                    continua = False
                break
            print(f'{CORES["VERMELHO"]}Opção inválida.{CORES["FIM"]}')

