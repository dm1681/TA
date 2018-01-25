# made by Diego McDonald for the usage of Thoroughbred Analytics
# this script will post tweet_string to the twitter account
# whose credientials are stord in credentials.py

# first lets initialize the credentials
import tweepy
import pandas as pd
import sqlite3
from credentials import *

# and authenticate

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_string = 'this is a test'

#print(tweet_string)

api.update_status(tweet_string)
