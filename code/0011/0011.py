# 敏感词文本文件 filtered_words.txt，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
# coding=utf-8

def getFormatList():
	file=open('filtered_words.txt')
	str=file.readlines()
	formatStr=[]
	for i in range(len(str)):
		formatStr.append(str[i].strip('\n'))
	return formatStr

def checkIsValid(input,filtered_words):
	for x in range(len(filtered_words)):
		if filtered_words[x] in input:
			return False;
	return True;

if __name__ == '__main__':
	input=str(input('随便输入点什么吧:'))
	if(checkIsValid(input,getFormatList())==True):
		print('Human Rights')
	else:
		print('Freedom')
