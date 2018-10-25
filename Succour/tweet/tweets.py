#!/usr/bin/python
# -*- coding: utf-8 -*-

from twitter import *
import database as db

# Connecting to twitter app
api = Api(consumer_key='IIxGHjK9oQNh6WtD8Jl8iNIDz', 
          consumer_secret='z4T9k4QxaMafKUiQcnewC1xoKSJhMM0nki8ItkXUXgc5hsZfyJ',
          access_token_key='994419842726805504-m5W1ZA4hll108sKSnyEfA88axynRiWJ',
          access_token_secret='TFloRt0np39kiXa4lHz52B01nch3FQCQjePr4LI5Im3Zg')

f = open('mytweets-disaster.txt','a')
f1 = open('maxidkerala.txt','r')

q="q=%23KeralaFloodrelief%20and%20%23KeralaFloods&src=typd"

i=0
maxid=""

try:
    #Read the maxid from the file
    tid = f1.read()
    if len(tid)==0:
        res = api.GetSearch(raw_query=q, return_json=True)
    else:	
        res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)
    
    temp=res["statuses"]
    f1.close()

    while i<10:
        if not temp:
            break
        print ("Call no: {}".format(i))
        i+=1

        for t in temp:
            retweetcount = t['retweet_count']
            tweet = t['text']
            time = t['created_at']
            db.insertTweets(tweet, time, retweetcount)
            # f.write(t['text'].encode('utf-8')+',,,'+'\n')
            # f.flush()

        maxid = temp[0]["id"]
        print ("Maxid = {}".format(str(maxid)))
        tid=""
        with open('maxidkerala.txt', 'w') as f1:
            f1.write(str(maxid))
            f1.flush()
        with open('maxidkerala.txt', 'r') as f1:
            tid = f1.read()
            print('inside file')
            print(tid)
            res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)
            temp=res["statuses"]

except Exception as e:
    print (e)
finally:
    f.close()
    print ("Successfull")