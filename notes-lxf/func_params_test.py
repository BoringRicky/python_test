def calc(*numbers):
    sum = 0
    for i in numbers:
        sum+=i

    return sum

#将 list或者tuple 当做 可变参数，需要在前面添加一个 * 
print(calc(*[1,2,3,4,5]))

extra={'gender':'F','city':'Beijing'}

#如果传入一个dict,只会传入dict的拷贝，不会影响原dict的内容
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('Ricky',28)
person('Ricky',28,gender='F',city='Beijing')
#将 dict 当做 可变参数，需要在前面添加两个 **
person('Ricky',28,**extra)

#限定关键字参数，必须使用city和job
def person1(name,age,*,city,job):
	print('name:',name,'age:',age,'city:',city,'job:',job)

person1('Ricky',28,city='Beijing',job='Android Programmer')

#如果已有可变参数，则关键字参数不要特殊分割符 * 了
def person2(name,age,*args,city="LiangShan",job):
	print('name:',name,'age:',age,'city:',city,'job:',job)

person2('Ricky',28,city='Beijing',job='Android Programmer')
person2('Ricky',28,job='Android Programmer')

def parameter1(p1,p2,p3=0,*args,**kw):
	print(p1,p2,p3,args,kw)

parameter1('p1','p2',111,111,city='Beijing',name='Ricky')


def parameter2(p1,p2,p3=101,*,d,**kw):
	print('p1 = ' ,p1)
	print('p2 = ' ,p2)
	print('p3 = ' ,p3)
	print('d = ' ,d)
	print('kw = ' ,kw)

parameter2('p1','p2',111,d='Beijing',city="Beijing")


d1={'name':'Ricky',1:'age'}
print(d1[1])

d2=dict(a=1,b=2)
print(d2['a'])

print('----------------------------------------分割线-------------------------------------------------')

def args_kw(p1,p2,p3=0,*args,**kw):
	print(p1,p2,p3,args,kw)
	for arg in args:
		print(arg)

	for k,w in kw.items():
		print(k,'=',w)

args_kw('p1','p2','p3',111,111,city='Beijing',name='Ricky')