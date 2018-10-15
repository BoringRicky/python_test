import os
from io import StringIO
from io import BytesIO

f = StringIO()
f.write('Hello')
f.write(' , ')
f.write('world')

print(f.tell())
print(f.getvalue())

f.seek(3, 0)
f.write("Lit")

print(f.tell())
print(f.getvalue())

# b = BytesIO("Ricky is 李腾".encode('utf-8'))
# print(b.read())
# print(b.getvalue())
#
# b1 = BytesIO()
# b1.write("李腾".encode('utf-8'))
# print(b1.getvalue())
#
#
# with open('./tmp', 'w') as f:
#     f.write("this is a temp file\n")
#
# with open('./tmp', 'a') as f:
#     f.write("this is a temp file")
#
# with open('./enum_test.py', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())
#
# with open('./img.jpg', 'rb') as f:
#     print(f.read())

# print(os.name)
# print(os.uname())
#
# print(os.environ)
# print('------------------------------------')
# print(os.environ.get('PATH'))

nums = (x * x for x in range(1, 11))
print(next(nums))
print(next(nums))

with open('./tmp', 'w') as f:
    f.write("temp file")

# 重命名
try:
    os.rename("tmp", "temp")
    os.remove('temp')
except FileNotFoundError as e:
    print(e.strerror)

name = (x for x in os.listdir('./') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py')
for i in name:
    s = "文件名：" + i if isinstance(i, str) else "非文件"
    print(s)
