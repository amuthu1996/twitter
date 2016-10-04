#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
 
 
'''
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1234abcd...'        #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'     #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'          #keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'       #keep the quotes, replace this with your access token secret
'''

def cred(filename, split='\n'):
    key = open(filename).read().split(split)
    CONSUMER_KEY = key[0]       #keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = key[1]    #keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = key[2]         #keep the quotes, replace this with your access token
    ACCESS_SECRET = key[3]      #keep the quotes, replace this with your access token secret
    #return CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY
    return key


def authen(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

#CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY = cred('credentials')
#api = authen(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY)
api = authen(cred('credentials'))
user = api.get_user('iamsrk')
print 'name\t\t: ',user.screen_name
print 'followers_count\t:',user.followers_count
for friend in user.friends():
   print friend.screen_name

