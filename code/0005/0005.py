# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#-*- coding:utf-8 -*-

import os
from PIL import Image,ImageDraw,ImageFont
import imghdr

#判断该文件是否为图片
def isPic(file):
	if(i.endswith('.jpg') or i.endswith('.png') or i.endswith('.gif')):
		return True;
	else:
		return False;

#iphone5分辨率1136×640
def changeSize(oldsize):
	if oldsize[0]<640  and oldsize[1]<1136:
		return oldsize
	else:
		w=oldsize[0]/640
		h=oldsize[1]/1136
		scale=w if w>h else h
		return ((int)(oldsize[0]/scale),(int)(oldsize[1]/scale))


images=os.listdir('images')
print(images)
for i in images:
	if(isPic(i)==True):
		image=Image.open('images/'+i,'r')
		#print(image.size)
		targetSize=changeSize(image.size)
		print(targetSize)
		if(targetSize!=image.size):
			image.thumbnail(targetSize,Image.ANTIALIAS)
			image.save("images/new_"+i,"jpeg")
