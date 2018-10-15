from types import MethodType

str1 = 'ABC'
str2 = 'DEF'

result = 'true' if type(str1)==type(str2) else 'false'
print(result)

var1 = 123
var2 = '123'
result = 'true' if type(var1)==type(var2) else 'false'
print(result)

type1 = 123

result = 'true' if type(type1)==int else 'false'
print(result)


print(type(dir(str1)))
print(dir(str1))

print(str1.__len__())
print(len(str1))

class Dog(object):
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

    def set_color(self,color):
        self.color = color


d = Dog('藏獒','黑色')
result = 'Dog 里存在 breed ' if hasattr(d,'breed') else 'Dog 里不存在 breed '
print(result)

result = 'Dog 里存在 name ' if hasattr(d,'name') else 'Dog 里不存在 name '
print(result)

if not hasattr(d,'name'):
    setattr(d,'name','小黑')

result = 'Dog 里存在 name ' if hasattr(d,'name') else 'Dog 里不存在 name '
print(result)
print(d.name)
print(getattr(d,'name'))

#del d.breed

# print(d.breed)

to_address = ['李腾<litengit@163.com>']
address = ';'.join(to_address)
print(address)









    

