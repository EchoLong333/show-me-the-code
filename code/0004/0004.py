#任一个英文的纯文本文件，统计其中的单词出现的个数。
#-*- coding:utf-8 -*-

file_text=open('words.txt','r')
words_text=file_text.read()
Dict={}
for i in words_text:
	j=i.lower()
	try:
		Dict[j]+=1
	except KeyError:
		Dict[j]=1
	except:
		raise e
#首字母排序打印
sort_Dict=sorted(Dict.items(),key=lambda asd:asd[0])

for i in sort_Dict:
	print("%s:%s"%i)