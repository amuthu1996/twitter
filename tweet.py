#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import time, sys

argfile = str(sys.argv[1])
 

api = authen(*cred('credentials'))

filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(30)#Tweet every 30 seconds
