import json
from twitterbot import TwitterBot


with open('app/config/secret.json') as arq:
    credentials = json.load(arq)
    login = credentials['login']
    password = credentials['password']

bot = TwitterBot(login, password)

bot.reuitar('o jogo')

