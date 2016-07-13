#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# coding:utf-8
import os
file=open('Activity.java')
code_count=0
null_count=0
annotation_count=0
lines=file.readlines()
print(len(lines))
for line in lines:
	line_strip=line.strip()
	if(line=='\n'):
		null_count=null_count+1
	elif(line_strip.startswith(r'/**') or line_strip.startswith(r'*') or line_strip.startswith(r'*/') or line_strip.startswith(r'//')):
		annotation_count=annotation_count+1
	else:
		code_count=code_count+1
print('空行: %d'%null_count)
print('注释: %d'%annotation_count)
print('代码: %d'%code_count)
