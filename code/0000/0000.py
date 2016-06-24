#-*- coding:utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
img=Image.open("avatar.jpg")
size=img.size
font=ImageFont.truetype(r'C:\Windows\Fonts\Arial.TTF',100);
print(r'size= %d,%d'%(size[0],size[1]))
draw=ImageDraw.Draw(img)
draw.text((size[0]-100,30), "2", font=font, fill=(222,84,72))
img.save("avatar1.jpg")
img.show()

