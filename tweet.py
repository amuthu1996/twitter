#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'rnL2vUB2I7mOwhvGDmpOa6u0F'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'A8RUv7nLSPEDApykU8cBHdf1Uglj0pLsPiJdb4RfTeY1ZUAbFN'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '463728688-ZWf4u7McXqRDaEfBoQeSgmNvULUHwRvc64yd5kIB'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'e78Y0FhdQls8ZbPqRLSTh087qZ4CWjirqkVeBkCEWJjYt'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
'''

filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
