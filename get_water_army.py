# -*- coding: utf-8 -*-
#coding=utf-8
import csv
import sys 
import re
import codecs
reload(sys) 
sys.setdefaultencoding('utf8')

userList=[]
waterArmy=[]


with open(r'./csv/testNine.csv','r') as csvfile:
	spamreader = csv.reader(csvfile,delimiter=',')
	for row in spamreader:
		userList.append(row)
userList.pop(0)
for user in userList:
	if 0<int(user[6])<=2:
		if int(user[4])==0:
			print '这名用户没有发过微博\n'
			with open(r'zeroWeiboWaterarmy.csv','a+') as csvfile:
				writer=csv.writer(csvfile)
				writer.writerow([re.search(r'\d+',user[0]).group(),user[1]])
		else:
			print '这名用户微博不为0\n'
			with open(r'WeiboWaterarmy.csv','a+') as csvfile:
				writer=csv.writer(csvfile)
				writer.writerow([re.search(r'\d+',user[0]).group(),user[1]])
	else:
		print 'not this guy\n'


