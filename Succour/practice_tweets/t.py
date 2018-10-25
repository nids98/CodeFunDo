#!/usr/bin/python
# -*- coding: utf-8 -*-

from twitter import *

api = Api(consumer_key='IIxGHjK9oQNh6WtD8Jl8iNIDz',
                      consumer_secret='z4T9k4QxaMafKUiQcnewC1xoKSJhMM0nki8ItkXUXgc5hsZfyJ',
                      access_token_key='994419842726805504-m5W1ZA4hll108sKSnyEfA88axynRiWJ',
                      access_token_secret='TFloRt0np39kiXa4lHz52B01nch3FQCQjePr4LI5Im3Zg')

f1 = open('max.txt','r+')

maxid=""

q="q=%23KeralaFloodrelief&src=typd&lang=en&result_type=recent&since=2018-01-01&count=100"

try:
	#Read the maxid from the file
	tid = f1.read()
	if len(tid)==0:
		res = api.GetSearch(raw_query=q, return_json=True)
	else:
		res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)

	temp=res["statuses"]

	maxid = temp[0]["id"]
	f1.write(str(maxid))
	print "Maxid = {}".format(maxid)

except Exception as e:
	print e


