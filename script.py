# import libraries
import tweepy

texto = "Essa mensagem foi postada porde sum bots s"

consumer_secret = "5kCk5tC6OMZfxTHILeZ517FzhzEB1bHT4hxWfEphl6clMVCUEd"
consumer_key = "J0E5BDn1Tb14m41dBBgBqHa9S"           #Credencias do twitter dev
access_token = "1179805875701272581-E3bHjsiNuCcT3yUk6SIakyDjYastMq"
access_token_secret = "jbwXdhehHFtF0yG7hbPYtgNZOEFwB6tSbZcLe2JYqHDo3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 


try:
  res = api.update_status(status=texto)
except tweepy.TweepError as e:
  print (e)

