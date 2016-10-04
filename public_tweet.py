#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import time, sys
from tweme import *
 
api = authen(*cred('credentials'))

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
