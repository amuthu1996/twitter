#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
 
argfile = str(sys.argv[1])
 
'''
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1234abcd...'        #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'     #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'          #keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'       #keep the quotes, replace this with your access token secret
'''

def cred():
    key = open('credentials').read().split('\n')
    CONSUMER_KEY = key[0]       #keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = key[1]    #keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = key[2]         #keep the quotes, replace this with your access token
    ACCESS_SECRET = key[3]      #keep the quotes, replace this with your access token secret
    return CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY


def authen(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY = cred()
api = authen(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
