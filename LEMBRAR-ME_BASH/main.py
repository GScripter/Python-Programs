import os
import requests
import getpass

from user_and_annotation import User

def showAvailableActions(option):
    os.system('clear')
    if option == 0:
        print(
        """
        =========================================================
           __   ______  ______  ___  ___   ___      __  _______
          / /  / __/  |/  / _ )/ _ \/ _ | / _ \____/  |/  / __/
         / /__/ _// /|_/ / _  / , _/ __ |/ , _/___/ /|_/ / _/  
        /____/___/_/  /_/____/_/|_/_/ |_/_/|_|   /_/  /_/___/

        =========================================================
        [ 0 ] Sign In
        [ 1 ] Sign Up
        [ 2 ] Inscreva-se
        [ 3 ] Contatar
        [ 4 ] Políticas
        [ 5 ] Ajuda
        [ 6 ] Sair
        """)

showAvailableActions(0)
while True:
    option = int(input('Qual sua opção? '))
    if option == 0:
        username = str(input('Nome de usuário: '))
        password = getpass.getpass('Senha: ')
        try:
            user = User(username, password).signIn()
        except TypeError as error:
            print(error)
    elif option == 6:
        break
print('Programa encerrado')

