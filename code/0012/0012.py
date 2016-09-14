#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
#  例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
# coding=utf-8

def getFormatList():
	file=open('filtered_words.txt')
	str=file.readlines()
	formatStr=[]
	for i in range(len(str)):
		formatStr.append(str[i].strip('\n'))
	return formatStr

def checkIsValid(input1,filtered_words):
	for x in range(len(filtered_words)):
		if filtered_words[x] in input1:
			stars=generateStar(filtered_words[x])
			input1=input1.replace(filtered_words[x],stars)
	return input1;

def generateStar(filtered_word):
	star=""
	for x in range(len(filtered_word)):
		star+="*"
	return star


if __name__ == '__main__':
	input1=str(input('随便输入点什么吧:'))
	print(checkIsValid(input1,getFormatList()))
