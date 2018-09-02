#coding=utf-8
# -*- coding: utf-8 -*-
import urllib2
import re
import csv
import time
import random
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
# download 函数开始
def download(url,num_retrues=2):
	# download函数定义了两个参数，且第二个有默认值2
	print 'downloading ',url
	# 打印一下，没什么用~~
	headers={'User-agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'}
	cookies={'SCF':'Avh0_aszm03EDhbPBhLKLzMm-lEmZcTWNpQrHxmq3ASgzFmvp5r-9UXkpkFL1ZAoLDhTr11GTiUa6J2lYwOFbPY.', '_T_WM':'ad5f1cb12be4f9fbd5f59720cf33cc91', 'SUB':'_2A252XNPUDeRhGeNH4lcR9CrFzj2IHXVVvv2crDV6PUJbkdANLUOhkW1NSkv7AwT9XvnJGWCzqcGcQruOaaiMh5EC', 'SUHB':'0tKqolLINoTzAu', 'SSOLoginState':'1532535684'}
	# header里面放置了伪装浏览器代理
	try:
		request=urllib2.Request(url,headers=headers)
		# headers=headers因为传递参数有顺序，这里没有按照顺序，所以特指headers 是headers
		html=urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		html=None
		if num_retrues>0:
			if hasattr(e,'code') and 500<=e.code<600:
				# hasattr方法表示e对象有没有’code'属性
				return download(url,num_retrues-1)
				# download函数自己调用自己，递归
	return html
# download函数结束

def link_crawler(seed_url,link_regex):
	# 两个参数，一个是种子最开始的页面，一个是连接的正则
	crawl_queue=[seed_url]
	# 设置待爬列表
	while crawl_queue:
		url=crawl_queue.pop()
		# pop用于抠出列表里的url来爬，默认最后一个
		html=downloadWithCookies(url)
		weibo=etree.HTML(html)
		# 调用函数下载url网页，返回一个str对象html
		# 把字符串html转换成html文档weibo用lxml解析
		link_fens=weibo.xpath("//table//td[2]/a[1]/@href")
		# 用xpath解析得到粉丝链接，返回一个列表link_fens
		for link in link_fens:
			crawl_queue.append(link)

# downloadWithCookies   BEGIN
def downloadWithCookies(url,num_retrues=2):
	# download函数定义了两个参数，且第二个有默认值2
	print 'downloading ',url
	# 打印一下，没什么用~~
	headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
   		'Connection':'keep-alive',
   		'Cookie':'_T_WM=c74a5726c7897a5acdd1785671c7346d; SCF=Alo6LMRJDBYbtB5ME4xUQCVGWhdRsu2n9W4Ke8vJTN5HaJ0vtATznQdoIhm0oAr1YHPAFgdxG1iB03sB9Ov_U7g.; SUB=_2A252Zg6sDeRhGeNH4lcR9CrFzj2IHXVVqJLkrDV6PUJbkdAKLVmikW1NSkv7A4i1v14QGBNZ7_ibl8cxkZwX_YPI; SUHB=079jP0ZM89loBG; SSOLoginState=1533181692'}
	
	# header里面放置了伪装浏览器代理,放了cookie
	# cookie 需要在浏览器里按f12打开调试模式，在https://weibo.cn/这个wap版本微博登录账号，比如在Chrome里，打开f12后，可以点击network，在Headers里找到cookies，把cookies那串东西黏贴到上面那个’cookie‘：’这里面‘
	try:
		request=urllib2.Request(url,headers=headers)
		# headers=headers因为传递参数有顺序，这里没有按照顺序，所以特指headers 是headers
		html=urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		html=None
		if num_retrues>0:
			if hasattr(e,'code') and 500<=e.code<600:
				# hasattr方法表示e对象有没有’code'属性
				return download(url,num_retrues-1)
				# download函数自己调用自己，递归
	print type(html)
	return html
# downloadWithCookies函数结束

def getFensList(html):
	# 接受downloadWith Cookies的html字符串
	weibo=etree.HTML(html)
 	# 把下载的html字符串文件转换成html文档
 	link_fens_list=weibo.xpath("//table//td[2]/a[1]/@href")
 	return link_fens_list

def getPersoonInfoList(html):
	# 传入一个参数str对象html，这也是downloadWithCookie返回的type
	personInfo=[]
	personPage=etree.HTML(html)
	# 返回粉丝的信息大表
	urlInfo=personPage.xpath('//div[@class="u"]//td[@valign="top"]/a/@href')[0].encode('utf-8')
	url='https://weibo.cn/u/'+re.search(r'(?<=\/)\d*(?=\/)',urlInfo).group()
	print "************** url get *******************"

	nameInfo=personPage.xpath('//div[@class="u"]//span[@class="ctt"]/text()')
	nameInfo=" ".join(nameInfo)
	# 将列表转为字符串
	print nameInfo
	if re.search(ur'^\S+(?= *)?',nameInfo) is not None:
		name=re.search(ur'^\S+(?= *)?',nameInfo).group()
	else :
		name=''
	if re.search(ur'.(?=\/)',nameInfo) is not None:
		sex=re.search(ur'.(?=\/)',nameInfo).group()
	else : 
		sex=''
	if re.search(ur'(?<=\/).+',nameInfo) is not None:
		region=re.search(ur'(?<=\/)\S*',nameInfo).group()
	else :
		region=''
	print "*************** name info get *****************"

	weiboCount=personPage.xpath('//span[@class="tc"]/text()')[0].encode('utf-8')
	print weiboCount
	weibo=re.search(ur'\d+(?=\])',weiboCount).group()
	print '************ weiboCount get *****************'

	focusCount=personPage.xpath('//div[@class="u"][1]/div/a[1]/text()')[0].encode('utf-8')
	print focusCount
	focus=re.search(ur'\d+(?=\])',focusCount).group()
	print '************ focusCount get ******************'

	fensCount=personPage.xpath('//div[@class="u"][1]/div/a[2]/text()')[0].encode('utf-8')
	print fensCount
	fens=re.search(ur'\d+(?=\])',fensCount).group()
	print '************* fensCount get *******************'
	# 上面这些代码有点冗长，先用lxml支持的xpath选取内容，然后用正则取出资料
	personInfo.append(url)
	personInfo.append(name)
	personInfo.append(sex)
	personInfo.append(region)
	personInfo.append(weibo)
	personInfo.append(focus)
	personInfo.append(fens)
	return personInfo
	# 本函数返回一个列表

def get(vRootUrl):
	fens_list=[]
	i=1
	while i<=20:
		# 以下代码循环二十次
		time.sleep(random.randint(1,6))
		indexUrl=vRootUrl+str(i)
		# i是几，indexUrl就是第几个粉丝页的url
		html=downloadWithCookies(indexUrl)
		# 获得索引页，下载成html
		link_fens_list=getFensList(html)
		# 得到索引页中的粉丝列表
		for url in link_fens_list:
			personPage=downloadWithCookies(url)
			# 对于每个粉丝，获取personPage页面HTML
			fens_list.append(getPersoonInfoList(personPage))
			# 将获得的信息（一个列表）加入到这个大二维表中
 		i=i+1
		 # 迭代列表，下载粉丝的个人主页personPage，然后用getPersonInfoList方法来得到一个包含粉丝信息的列表，然后加入列表fens_list
	return fens_list
	# 完成二十次迭代后返回二维列表

