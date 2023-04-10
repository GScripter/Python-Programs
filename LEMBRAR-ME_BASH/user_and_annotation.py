import requests
import endpoints


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signIn(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = requests.post(endpoints.TOKEN_OBTAIN, json=data)
        if response.ok == True:
            return [response.access, response.refresh]
        raise 'Username ou senha inválida'
