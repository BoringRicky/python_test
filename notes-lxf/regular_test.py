
# * 表示任意个字符（包含0个）； 
# + 表示至少一个字符；
# ？ 表示0或1个字符 
# {n} 表示 n 个字符
# {n，m} 表示 n-m 个字符

# \d 表示匹配一个数字 ，比如 00\d 可以匹配 007
# \w 表示匹配一个字母或者数字， 
# . 表示匹配任何字符
# \s 表示匹配一个 空格
# \d{3} 表示匹配3个数字
# \d{3，8} 表示匹配3-8个数字
# \- 表示匹配一个 - 字符
# \_ 表示匹配一个下划线 _ 字符


#[]表示范围
#[0-9a-zA-Z\_] 表示匹配一个数字、字母或者下划线
#[0-9a-zA-Z\_]+ 表示至少匹配一个数字、字母或者下划线；比如：a100,0_z,py200
#[a-zA-Z\_][0-9a-zA-Z\_]* 表示匹配由任意字母或者下划线开头，后接任意一个数字、字母或下划线 的字符串
#[a-zA-Z\_][0-9a-zA-Z\_]{0,19} 表示 前面一个字符+后面最多19个字符


#A|B 表示匹配 A或B 例如： (P|Python) 可以匹配 P 或者 Python
#^表示行的开头，^\d表示必须以数字开头
#$表示行的结束， $\d表示必须以数字结束  ^py$ 只能匹配 py 字符
#\表示转义，如果本身就有意义的字符，就需要通过\来转义，例如 \\ 表示 \
#在Python里可以在字符串的开头添加r ,表示忽略转义的问题。 'ABC\\-001'和 r'ABC\-001'：都可以表示 ABC\-001

#分组 使用（）
#正则有提取子串的功能，用（）表示要提取的分组（group）
#例如：^(\d{3})-(\d{3,8})$ ；分别定义了两个分组 ^(\d{3}) 和 (\d{3,8})$

#贪婪匹配
#  re.match(r'^(\d+)(0*)$', '102300') ，其中的 \d+ 会采取贪婪匹配，直接把后面所有的数字都匹配进去
#  需要在加个问好 ？让 \d+ 采用非贪婪匹配 re.match(r'^(\d+?)(0*)$', '102300')

#正则的编译 在使用正则时会干两件事情
# 1.编译正则表达式，如果正则表达式不合法，报错
# 2.用编译后的正则表达式去匹配字符串

#如果某一个正则会用到很多次，最好先预编译好，然后，再去匹配
# compiled_regular = re.compile(r'^(\d+)(0*)$')
# compiled_regular.match('12300').groups()

from datetime import datetime
import time
import re

string = 'a b,n c,m   d'

splits = 'a b c'.split(' ')
print(splits)

splits = re.split(r'\s+',string)
print(splits)

splits = re.split(r'[\s\,]+',string)
print(splits)

regular_expr = r'(\d{3})-(\d{3,5})'
result = re.match(regular_expr,'010-12345')
print(result[0])
print(result[1])
print(result[2])


str_group = '010abcd'
groups = re.match(r'(\d{3})([a-zA-Z]{0,4})',str_group)
print(groups[0])
print(groups[1])
print(groups[2])

email = 'rickylee@163.com'
email_groups = re.match(r'([a-zA-Z]*)@([\d]+)',email).groups()
print(email_groups)


emails = ['rickylee@163.com']
emails.append('liteng@haima.me')
emails.append('liteng@gmail.com')
emails.append('liteng@sina.com')
emails.append('liteng@*sina.com')


regular_email_expr = r'^[a-zA-Z][a-zA-Z0-9_-]*@[a-zA-Z0-9_]+.[a-zA-Z0-9]+'
is_email = re.match(regular_email_expr,email)
print(is_email)

print('----------------未预编译-----------------------')
begin_time = time.time()
for email in emails:
	is_email = re.match(regular_email_expr,email)
	if(is_email):
		print(email+' is a rightful email address')
	else:
		print(email+' is a illgal email address')
end_time = time.time()

print("耗时：",(end_time - begin_time))

print('----------------预编译-----------------------')
print('begin 当前时间 = ',datetime.now())
compiled_email_regular = re.compile(regular_email_expr)
for email in emails:
	if(compiled_email_regular.match(email)):
		print(email+' is a rightful email address')
	else:
		print(email+' is a illgal email address')
print('end 当前时间 = ',datetime.now())


d = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(d)




















