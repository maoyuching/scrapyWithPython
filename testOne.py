#coding=utf-8
# -*- coding: utf-8 -*-
from firstScrapy import downloadWithCookies
from firstScrapy import getFensList , getPersoonInfoList
from firstScrapy import get
import urllib2
import random
import csv
import time
from bs4 import BeautifulSoup
from lxml import etree,html
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

vRootUrl='https://weibo.cn/1676317545/fans?page='
# vRootUrl不是完整的网址，把他黏贴到浏览器地址栏，然后在后面加上小于二十的数字，比如加上4变成https://weibo.cn/6551258245/fans?page=4 就是某个微博用户（微博id就是那一长串数字）的某个粉丝列表，一页有十个，访问该网页的前提是你已经登录微博wap版，也就是https://weibo.cn/
fens_list=get(vRootUrl)
print 'fens_lists is ok ','*************************'
with open(r'./csv/tthFens.csv','w') as csvfile:
		# testTwo.csv就是要保存的csv文件的名字，因为wap版本微博的限制，一次仅可以浏览某微博用户的200个粉丝，所以抓取一次后，应另外写一个xxx.csv 来保存另外的200个微博用户，当本程序运行时其他打开这个csv文件的程序应当关闭
		writer=csv.writer(csvfile)
		writer.writerow(['url','name','sex','region','weiboCount','foucsCount','fensCount'])
		writer.writerows(fens_list)

print 'Congratulations! ****************************'