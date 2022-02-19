from time import sleep
from covid import Covid

print('—'*50)
print(f'\033[1;34m{"Covid-19 INFORMAÇÕES":^50}\033[m')
print('—'*50)
# Listar Países
continua = True
while continua:
    print('\033[1;33mFiltrando Lugares...\033[m')
    try:
        covid = Covid(source='worldometers')
        paises = covid.list_countries()
        paises.sort()
        for c in range(1, len(paises)):
            print(f'[ {c} ]> {paises[c]}', end=' ')
            if c % 3 == 0:
                print('\n')
    except:
        sleep(4)
        print('\033[1;31mError: Verifique seu acesso a Internet.\033[m', end='')
        continua = False
    else:
        break

while continua:
    try:
        num = int(input('\n\033[1;32mNúmero da Região:\033[m '))
    except KeyboardInterrupt:
        print('\033[1;33mPrograma Interrompido.\033[m')
        break
    except:
        print('\033[1;31mPor favor digite algo válido.\033[m', end='')
    else:
        if num >= 1 and num <= len(paises):
            dados = covid.get_status_by_country_name(paises[num])
            print('+'*34)
            print(f'{paises[num]:^34}'.upper())
            print('+'*34)
            titulos = ['Região', 'Total_de_Casos', 'Confirmados',
                       'Novos_Casos', 'Mortes', 'Novas_Mortes',
                       'Recuperados', 'Ativos', 'Casos_Ativo',
                       'Crítico', 'Total_de_Testes', 'Testes_por_Milhão',
                       'Casos_por_Milhão', 'Mortes_por_Milhão', 'População']
            for contador, dado in enumerate(dados.values()):
                if dado == 0:
                    dado = '?'
                print(f'{titulos[contador]:<24} {dado}')

            # Pergunta se o usuário deseja continuar e faz a validação da respostas.
            while True:
                try:
                    print('-'*34)
                    res = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
                    print('-'*34, end='')
                except KeyboardInterrupt:
                    print('\033[1;33mPrograma Interrompido.\033[m')
                    continua = False
                    break
                except:
                    print('\033[1;31mPor favor digite algo valido.\033[m')
                else:
                    if res in 'SN':
                        if res == 'N':
                            continua = False
                        break
                    print('\033[1;31m\nOpção não existe. Digite Novamente.\033[m')
        else:
            print('\033[1;31mOpção de região não existe. Digite Novamente.\033[m', end='')

print(r"""
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

