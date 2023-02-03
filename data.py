import requests


class Dados:
    def __init__(self, qt_quest, cat):
        parametros = {
            'amount': qt_quest,
            'category': cat,
            'type': 'boolean'

        }
        resposta = requests.get('https://opentdb.com/api.php', params=parametros)
        self.dados_questao = resposta.json()['results']


