import os
import tweepy
from datetime import datetime
from pytz import timezone

from dotenv import load_dotenv
load_dotenv()

consumer_secret = os.getenv('CONSUMER_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
access_token = os.getenv('ACESS_TOKEN')
access_token_secret = os.getenv('ACESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y')
hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%H:%M')

user_twitter = '@lBlack_11'

text = "Bot do bom dia! Hoje é dia " + data_sao_paulo_em_texto + ", " + hora_sao_paulo_em_texto + ". Bom dia para todos menos para " + user_twitter


try:
  res = api.update_status(status=text)
except tweepy.TweepError as e:
  print (e)

