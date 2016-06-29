#做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
#使用 Python 如何生成 200 个激活码（或者优惠券）

#coding:utf-8
import random	
import string

text="abcdefghiklmnopqrstuvwxyzABCDEFGHIJKHMNOPQRSTUVWXYZ0123456789"

#生成一组激活码
#count:一组激活码的四位随机数个数
def generateKey(count):
	key=""
	for i in range(count):
		if(i==0):
			key+="".join(random.sample(text,4))
		else:
			key+="-"+"".join(random.sample(text,4))
	return key

#group 生成激活码组数
def generateKeyByGroup(group):
	for x in range(group):
		print(generateKey(4))

#generateKeyByGroup(200)

