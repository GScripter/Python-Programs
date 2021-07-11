from pytube import YouTube, Playlist, Channel
import os
from time import sleep

# Função pra tratar as exceções de escolha
def opcao(i,f):
    while True:
        try:
            var_op = int(input('Opção: '))
        except KeyboardInterrupt:
            print('\033[1;33mO usuário decidiu parar o Programa\033[m')
            global continua
            continua = False
            break
        except ValueError:
            print('\033[1;31mValor digitado não é um Inteiro. Digite Novamente\033[m')
        except:
            print('\033[1;31mNão sei o que você digitou. Por favor digite algo válido\033[m')
        else:
            if var_op >= i and var_op <= f:
                return var_op
            print('\033[1;31mOpção inexistente. Digite Novamente.\033[m')
            


# Função pra tratar as exceções do link
def val_link():
    global continua
    while True:
        try:
            link = str(input('Digite o link: ')).strip()
        except KeyboardInterrupt:
            print('\033[1;33mO usuário decidiu parar o Programa\033[m')
            continua = False
            break
        except:
            print('\033[1;31mValor digitado não é Valido. Digite Novamente\033[m')
        else:
            return link


# Bloco Principal
continua = True
while continua:
    print('\033[34m{}\033[m'.format('='*38))
    print('\033[1;37m{:^38}\033[m'.format('Baixar Videos YouTube'))
    print('\033[34m{}\033[m'.format('='*38), end='')
    print("""
\033[1;33m[ 1 ] - \033[34mBaixar Video\033[m
\033[1;33m[ 2 ] - \033[34mBaixar PlayList\033[m
\033[1;33m[ 3 ] - \033[34mBaixar Tudo de um Canal\033[m
\033[1;33m[ 4 ] - \033[34mSair\033[m""")
    print('\033[34m{}\033[m'.format('='*38))
    var_op = opcao(1,4)
    if continua:
        if var_op == 1:
            while True:
                link = val_link()
                if continua:
                    try:
                        yt = YouTube(link)
                        print('\033[1;35mAguarde...\033[m')
                        stream = yt.streams.filter(file_extension='mp4').order_by('resolution')
                        print('\033[1;33mEscolha uma das resoluções disponíveis.\033[m')
                        cont = -1
                        for e,c in enumerate(stream,start=0):
                            print(f'[ {e} ]{c.resolution:>8}')
                            print('—'*14)
                            cont += 1
                    except:
                        print('\033[1;31mError: Veja se há o acesso a Internet ou se o link esta defasado. Então digite Novamente\033[m')
                    else:
                        var_op1 = opcao(0,cont)
                        if continua:
                            print('\033[1;35mAguarde...\033[m')
                            sleep(2)
                            print('\033[1;35mIsso pode demorar um pouco. Depende de sua Internet ou do Tamanho do video\033[m')
                            stream[var_op1].download(output_path='YouTube-Videos')
                            print('\033[1;32mDownload Concluído. O arquivo de video se encontra na pasta: \033[m')
                            caminho = os.getcwd()
                            print(f'{caminho}/YouTube-Videos')
                            break
                        else:
                            break
                else:
                    break
        elif var_op == 2:
            con = True
            while con:
                link = val_link()
                if continua:
                    try:
                        pl = Playlist(link)
                        print('\033[1;35mAguarde enquanto Filtramos...\033[m')
                        print('\033[34m{}\033[m'.format('='*38))
                        for video in pl.video_urls:
                            print(video)
                        print('\033[34m{}\033[m'.format('='*38))
                    except:
                        print('\033[1;31mError: Veja se há o acesso a Internet ou se o link esta defasado. Então digite Novamente\033[m')
                    else:
                        while True:
                            try:
                                res = str(input('Deseja baixar todos os videos dessa PlayList? [S/N] ')).strip().upper()[0]
                            except KeyboardInterrupt:
                                print('\033[1;33mO usuário decidiu parar o Programa\033[m')
                                continua = False
                                con = False
                                break
                            except:
                                print('\033[1;31mValor digitado não é Valido. Digite Novamente\033[m')
                            else:
                                if res in 'SN':
                                    if res == 'N':
                                        continua = False
                                        con = False
                                        break
                                    else:
                                        print('\033[1;35mAguarde...\033[m')
                                        sleep(2)
                                        print('\033[1;35mIsso pode demorar um pouco. Depende de sua Internet ou da quantidade de videos\033[m')
                                        for video in pl.videos:
                                            video.streams.get_highest_resolution().download(output_path='YouTube-Videos')
                                        print('\033[1;32mDownload Concluído. A PlayList esta na Pasta: \033[m')
                                        caminho = os.getcwd()
                                        print(f'{caminho}/YouTube-Videos')
                                        con =False
                                        break
                                print('\033[1;31mOpção inexistente. Digite Novamente.\033[m')
                else:
                    break
        elif var_op == 3:
            con = True
            while con:
                link = val_link()
                if continua:
                    try:
                        cn = Channel(link)
                        print('\033[1;35mAguarde enquanto Filtramos...\033[m')
                        lc = []
                        for video in cn.video_urls:
                            lc.append(video)
                    except:
                        print('\033[1;31mError: Veja se há o acesso a Internet ou se o link esta defasado. Então digite Novamente\033[m')
                    else:
                        while True:
                            try:
                                res = str(input(f'Há {len(lc)} videos nesse canal. Tem certeza que Deseja baixar todos, isso pode demorar? [S/N] ')).strip().upper()[0]
                            except KeyboardInterrupt:
                                print('\033[1;33mO usuário decidiu parar o Programa\033[m')
                                continua = False
                                con = False
                                break
                            except:
                                print('\033[1;31mValor digitado não é Valido. Digite Novamente\033[m')
                            else:
                                if res in 'SN':
                                    if res == 'N':
                                        continua = False
                                        con = False
                                        break
                                    else:
                                        print('\033[1;35mAguarde...\033[m')
                                        sleep(2)
                                        print('\033[1;35mIsso pode demorar. Depende de sua Internet ou da quantidade de videos existentes no canal.\033[m')
                                        for video in cn.videos:
                                            video.streams.get_highest_resolution().download(output_path='YouTube-Videos')
                                        print('\033[1;32mDownload Concluído. Todos os videos estão na Pasta: \033[m')
                                        caminho = os.getcwd()
                                        print(f'{caminho}/YouTube-Videos')
                                        con =False
                                        break
                                print('\033[1;31mOpção inexistente. Digite Novamente.\033[m')
                else:
                    break
        elif var_op == 4:
            break
        if continua:
            while True:
                try:
                    res = str(input('Deseja Continua? [S/N] ')).strip().upper()[0]
                except KeyboardInterrupt:
                    print('\033[1;33mO usuário decidiu parar o Programa\033[m')
                    continua = False
                    break
                except:
                    print('\033[1;31mValor digitado não é Valido. Digite Novamente\033[m')
                else:
                    if res in 'SN':
                        if res == 'N':
                            continua = False
                        break
                    print('\033[1;31mOpção inexistente. Digite Novamente.\033[m')

print('\033[1;30m<<< Fim do Programa >>>\033[m')
