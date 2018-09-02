# -*- coding: utf-8 -*-
from firstScrapy import getPersoonInfoList
from firstScrapy import downloadWithCookies,getPersoonInfoList, getFensList
from lxml import etree , html
import urllib2
import csv
import time
import re
list=[]
with open(r'waterArmyOne.csv','r') as csvfile:
	reader=csv.reader(csvfile)
	for line in reader:
		list.append(line[0])
		# list 是一个一维列表，内面是一堆用户id
print list
the_list=[]
for id in list:
	time.sleep(3)
	vRootUrl='https://weibo.cn/u/%s' % id
	personPage=downloadWithCookies(vRootUrl)
	personInfo=getPersoonInfoList(personPage)
	the_list.append(personInfo)
with open(r'waterArmyInfo.csv','w+') as csvfile:
	writer=csv.writer(csvfile)
	writer.writerow(['url','name','sex','region','weiboCount','foucsCount','fensCount'])
	writer.writerows(the_list)
