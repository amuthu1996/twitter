#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import  time, sys
from tweme import *
 
api = authen(*cred('credentials'))
user = api.get_user('iamsrk')
print 'Name\t\t: ',user.screen_name
print 'Followers Count\t: ',user.followers_count
for friend in user.friends():
   print friend.screen_name

