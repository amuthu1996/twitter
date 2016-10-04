#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy,sys

'''
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1234abcd...'        #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'     #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'          #keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'       #keep the quotes, replace this with your access token secret
'''

__all__ = ['cred','authen']

def cred(filename, split='\n'):
    key = open(filename).read().split(split)
    #credentials
    CONSUMER_KEY    = key[0]    #keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = key[1]    #keep the quotes, replace this with your consumer secret key
    ACCESS_KEY      = key[2]    #keep the quotes, replace this with your access token
    ACCESS_SECRET   = key[3]    #keep the quotes, replace this with your access token secret
    return CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY


def authen(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_SECRET,ACCESS_KEY):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    pass
