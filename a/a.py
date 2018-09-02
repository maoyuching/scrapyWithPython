# -*- coding: utf-8 -*-
#coding=utf-8
import csv
'''以下代码吧weiboWaterarmy。csv文件去重，存到waterArmyOne。csv文件
list=[]
with open(r'WeiboWaterarmy.csv','r') as csvfile:
	reader=csv.reader(csvfile)
	for line in reader:
		list.append(line)
# reader is a list[][] and list is [][]
d=[]

c=[]
for line in list:
	if line[0] not in d:
		d.append(line[0])
		c.append(line)
	else:
		pass

with open(r'waterArmyOne.csv','w+') as csvfile:
	writer=csv.writer(csvfile) 
	writer.writerows(c)
print 'ok'
'''
'''
the_list=[]
with open(r'waterArmy.csv','r') as csvfile:
	reader=csv.reader(csvfile)
	for line in reader:
		the_list.append(line)
for line in the_list:
	line.pop(-1)
with open(r'waterArmyTwo.csv','w+') as csvfile:
	writer=csv.writer(csvfile)
	writer.writerows(the_list)
'''
the_list=[]
with open(r'waterArmyTwo.csv','r') as csvfile:
	reader=csv.reader(csvfile)
	for line in reader:
		the_list.append(line)
with open(r'waterArmyOne.csv','a+') as csvfile:
	writer=csv.writer(csvfile)
	writer.writerows(the_list)