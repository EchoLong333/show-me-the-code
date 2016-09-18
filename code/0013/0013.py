# 用 Python 写一个爬图片的程序，爬 http://tieba.baidu.com/p/2166231880
# encoding=utf-8

from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import io  
import sys 

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码  

def getWebsiteContent(url):
	imgID = 0 
	content=urlopen(url).read()
	soup=BeautifulSoup(content,"html.parser")
	imgs=soup.find_all('img',class_="BDE_Image")
	for img in imgs:
		url=img.get('src')
		print(url)
		urlretrieve(url,"imgs/%d.jpg"%imgID)
		imgID=imgID+1
		
		

if __name__ == '__main__':
	getWebsiteContent('http://tieba.baidu.com/p/2166231880')
