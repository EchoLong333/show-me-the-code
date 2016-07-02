#你有一个目录，放了你一个月的日记，都是 txt，
#为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# coding:utf-8

import re
import os
from collections import Counter

def find_import_word(file,diary):
	#re.sub 字符串替换
	tmp_str=re.sub('[,|.]',' ',all_the_text)
	dict={}
	list=tmp_str.split()
	for word in list:
		if word in dict:
			dict[word]+=1
		else:
			dict[word]=1
	count=Counter(dict)
	print("the import word in %s is %s:"%(file,count.most_common()[:1]))

files=os.listdir("files")
print(files)
for x in files:
	file_object = open(r"files/"+x)
	try:
	     all_the_text = file_object.read( )
	     find_import_word(x,all_the_text)
	finally:
	     file_object.close( )
	     

