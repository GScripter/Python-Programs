from time import sleep

value = True
while value:
    try:
        arquivo = str(input('[Nome/Caminho] do Arquivo: '))
        abrir = open(arquivo,'r')
    except KeyboardInterrupt:
        print('\033[1;33mO usuário prefiril interromper o Programa.\033[m')
        break
    except:
        print('\033[1;31mO caminho especificado foi invalido. Tente Novamente.\033[m')
    else:
        while value:
            print('='*50)
            print(f'{"Busca de Palavras":^50}')
            print('='*50)

            try:
                palavra = str(input('Buscar Palavra: '))
            except KeyboardInterrupt:
                print('\033[1;33mO usuário prefiril interromper o Programa.\033[m')
                value = False
                break
            except:
                print('\033[1;31mErro: Por favor digite algo valido\033[m')
            else:
                print('\033[1;35mBuscando...\033[m')
                sleep(2)
                lista = []
                for a,c in enumerate(abrir):
                    if palavra in c:
                        lista.append(a+1)
                abrir.seek(0)
                if len(lista) != 0:
                    print(f'A palavra {palavra} foi encontrada na(s) linha(s): ',end='')
                    print(lista)
                else:
                    print('Não teve nem uma ocorrência dessa palavra no arquivo')
                lista.clear()
            while True:
                try:
                    res = str(input('Continua? [S/N] ')).strip().upper()[0]
                except KeyboardInterrupt:
                    print('\033[1;33mO usuário prefiril interromper o Programa.\033[m')
                    value = False
                    break
                except:
                    print('\033[1;31mErro: Por favor digite algo valido\033[m')
                else:
                    if res in 'SN':
                        if res == 'N':
                            value = False
                            break
                        elif res == 'S':
                            value = True
                            break
                    print('\033[1;31mPor favor digite uma opção valida.\033[m')
print('<<< Fim do Programa >>>')
