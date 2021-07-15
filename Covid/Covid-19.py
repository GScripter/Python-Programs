from covid import Covid

print('—'*50)
print('\033[1;37m{:^50}\033[m'.format('Covid-19 INFORMAÇÕES'))
print('—'*50)

# Listar Países
continua = True
while continua:
    try:
        print('\033[1;33mFiltrando Lugares...\033[m')
        covid = Covid(source='worldometers')
        paises = covid.list_countries()
        paises.sort()
        for c in range(1, len(paises)):
            print(f'[ {c} ]> {paises[c]}',end=' ')
            if c % 3 == 0:
                print('\n')
    except:
        print('\033[1;31mError: Verifique seu acesso a Internet.\033[m',end='')
        continua = False
    else:
        break

while continua:
    try:
        num = int(input('\n\033[1;32mNúmero da Região:\033[m '))
    except KeyboardInterrupt:
        print('\033[1;33mO usuário decidiu parar o Programa.\033[m')
        break
    except:
        print('\033[1;31mPor favor digite algo valido.\033[m',end='')
    else:
        if num >= 1 and num <= len(paises):
            status = covid.get_status_by_country_name(paises[num])
            print('+'*34)
            print(f'{paises[num]:^34}'.upper())
            print('+'*34)
            listak = ['Região', 'Total_de_Casos', 'Confirmados', 'Novos_Casos', 'Mortes', 'Novas_Mortes', 'Recuperados', 'Ativos', 'Casos_Ativo', 'Crítico', 'Total_de_Testes', 'Testes_por_Milhão', 'Casos_por_Milhão', 'Mortes_por_Milhão', 'População']
            for c,v in enumerate(status.values()):
                if v == 0:
                    v = '?'
                print(f'{listak[c]:<24} {v}')
            # Perguntar se o usuário deseja continuar em seguida faz o tratamento e validação da respostas.
            while True:
                try:
                    print('-'*34)
                    res = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
                    print('-'*34,end='')
                except KeyboardInterrupt:
                    print('\033[1;33mO usuário decidiu parar o Programa.\033[m')
                    continua = False
                    break
                except:
                    print('\033[1;31mPor favor digite algo valido.\033[m')
                else:
                    if res in 'SN':
                        if res == 'N':
                            continua = False
                            break
                        else:
                            break
                    print('\033[1;31m\nEssa opção não existe. Digite Novamente.\033[m')
        else:
            print('\033[1;31mEssa opção de Região não existe. Digite Novamente.\033[m',end='')
print("""
    ##############################################
     # Tempos difíceis, exigem amor ao extremo, #
     #     "Finais doem, mas recomeços curam"   #
    ##############################################
                             #
                              #
                               ^  ^
                               (oo)\_______
                               (__)\       )/\/
                                   ||----W |
                                   ||     || 
""")

