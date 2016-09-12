#使用 Python 生成类似于下图中的字母验证码图片
# coding=utf-8

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import string,random

#获取随机字母
def getRandomChar(count):
	return [random.choice(string.ascii_letters) for _ in range(count)]

#获取随机颜色
def getRandomColor():
	return (random.randint(30,100),random.randint(30,100),random.randint(30,100))

#获取验证码图片
def getCodePic(count):
	width=240
	height=60
	#创建画布
	image=Image.new('RGB',(width,height),(180,180,180))
	font=ImageFont.truetype(r'C:\Windows\Fonts\Arial.TTF',30);
	draw=ImageDraw.Draw(image)

	code=getRandomChar(count)

	for t in range(count):
		draw.text((240/count*t+30,20),code[t],font=font,fill=getRandomColor())

	for x in range(random.randint(1500,3000)):
		draw.point((random.randint(0,width), random.randint(0,height)), fill=getRandomColor())

	image=image.filter(ImageFilter.BLUR)

	image.save("".join(code)+'.jpg','jpeg')
	image.show()

if __name__ == '__main__':
	getCodePic(4)