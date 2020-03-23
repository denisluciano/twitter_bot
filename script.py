import os
import tweepy

from dotenv import load_dotenv
load_dotenv()


texto = "Test2 usando crontab"

consumer_secret = os.getenv('CONSUMER_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
access_token = os.getenv('ACESS_TOKEN')
access_token_secret = os.getenv('ACESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 


try:
  res = api.update_status(status=texto)
except tweepy.TweepError as e:
  print (e)

