from random import randint
from time import sleep

pos = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def velha():
    print(f"""

          {pos[0][0]} |  {pos[0][1]}  | {pos[0][2]}
         -------------
          {pos[1][0]} |  {pos[1][1]}  | {pos[1][2]}
         -------------
          {pos[2][0]} |  {pos[2][1]}  | {pos[2][2]}

    """)


print('\033[34m=\033[m'*28)
print(f'{"JOGO DA VELHA":^28}')
print('\033[34m=\033[m'*28)
fim = False
while fim == False:
    velha()
    para = False
    while True:
        if para == True:
            break
        try:
            simb = str(input('Você quer X ou O? ')).strip().upper()[0]
        except KeyboardInterrupt:
            print('\033[1;33mO usuário decidiu Interromper o Jogo\033[m')
            fim = True
            break
        except:
            print('\033[1;31mOpção Invalidá. Digite Novamente\033[m')
        else:
            if simb in 'XO':
                while True:
                    if para == True:
                        break
                    # Usuário Joga
                    while True:
                        try:
                            linha = int(input('Linha: '))
                            coluna = int(input('Coluna: '))
                        except KeyboardInterrupt:
                            print('\033[1;33mO usuário decidiu Interromper o Jogo\033[m')
                            fim = True
                            para = True
                            break
                        except:
                            print('\033[1;31mOpção Invalidá. Digite Novamente\033[m')
                        else:
                            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
                                if pos[linha][coluna] == ' ':
                                    pos[linha][coluna] = simb
                                    velha()
                                    # Circunstâncias onde o Jogador Ganhara
                                    if pos[0][0] == simb and pos[0][1] == simb and pos[0][2] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[1][0] == simb and pos[1][1] == simb and pos[1][2] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[2][0] == simb and pos[2][1] == simb and pos[2][2] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[2][0] == simb and pos[2][1] == simb and pos[2][2] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[0][0] == simb and pos[1][0] == simb and pos[2][0] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[0][1] == simb and pos[1][1] == simb and pos[2][1] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[0][2] == simb and pos[1][2] == simb and pos[2][2] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[0][0] == simb and pos[1][1] == simb and pos[2][2] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[0][2] == simb and pos[1][1] == simb and pos[2][0] == simb:
                                        print('\033[1;32mParabéns você VENCEU!\033[m')
                                        para = True
                                        break
                                    elif pos[0][0] != ' ' and pos[0][1] != ' ' and pos[0][2] != ' ' and  pos[1][0] != ' ' and pos[1][1] != ' ' and pos[1][2] != ' ' and pos[2][0] != ' ' and pos[2][1] != ' ' and pos[2][2] != ' ':
                                        print('\033[1;34mOuvi um Empate!\033[m')
                                        para = True
                                        break
                                    break
                                else:
                                    print('\033[1;31mEssa casa já esta ocupada. Jogue em outra\033[m')
                            else:
                                print('\033[1;31mPosição Invalidá. Digite Novamente\033[m')
                    # Maquina Joga
                    while para == False:
                        maq_simb = ' '
                        if simb == 'X':
                            maq_simb = 'O'
                        else:
                            maq_simb = 'X'
                        maquina_l = randint(0,2)
                        maquina_c = randint(0,2)
                        if pos[maquina_l][maquina_c] == ' ':
                            print('\033[1;33mMaquina Jogando...\033[m')
                            sleep(3)
                            pos[maquina_l][maquina_c] = maq_simb
                            velha()
                            # Circunstâncias onde a maquina Ganhara
                            if pos[0][0] == maq_simb and pos[0][1] == maq_simb and pos[0][2] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[1][0] == maq_simb and pos[1][1] == maq_simb and pos[1][2] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[2][0] == maq_simb and pos[2][1] == maq_simb and pos[2][2] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[2][0] == maq_simb and pos[2][1] == maq_simb and pos[2][2] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[0][0] == maq_simb and pos[1][0] == maq_simb and pos[2][0] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[0][1] == maq_simb and pos[1][1] == maq_simb and pos[2][1] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[0][2] == maq_simb and pos[1][2] == maq_simb and pos[2][2] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[0][0] == maq_simb and pos[1][1] == maq_simb and pos[2][2] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[0][2] == maq_simb and pos[1][1] == maq_simb and pos[2][0] == maq_simb:
                                print('\033[1;35mVocê Perdeu!\033[m')
                                para = True
                                break
                            elif pos[0][0] != ' ' and pos[0][1] != ' ' and pos[0][2] != ' ' and  pos[1][0] != ' ' and pos[1][1] != ' ' and pos[1][2] != ' ' and pos[2][0] != ' ' and pos[2][1] != ' ' and pos[2][2] != ' ':
                                print('\033[1;34mOuvi um Empate!\033[m')
                                para = True
                                break
                            break
            else:
                print('\033[1;31mOpção Inválida. Digite Novamente\033[m')
    if fim == False:
        while True:
            try:
                continua = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
            except KeyboardInterrupt:
                print('\033[1;33mO usuário decidiu Interromper o Jogo\033[m')
                fim = True
                break
            except:
                print('\033[1;31mOpção Invalidá. Digite Novamente\033[m')
            else:
                if continua in 'SN':
                    break
                print('\033[1;31mOpção Invalidá. Digite Novamente\033[m')
        if continua == 'N':
            fim = True
        elif continua == 'S':
            print('\033[34m=\033[m'*28)
            print(f'{"NOVO JOGO":^28}')
            print('\033[34m=\033[m'*28)
            for c in range(0,len(pos)):
                for i in range(0,len(pos)):
                    pos[c][i] = ' '
            para = False
print('\033[1;33;44m<<< Fim de Jogo >>>\033[m')

