# a=[]
# for i in range(1,11):
#
#     a.append(pow(i,2))
# print(a)
# exmple = [[1,2,3],[4,5,6],[7,8,9],[10]]
# a = [pow(a,2) for i in exmple for a in i if a%2==0 ]
# print(a)
import random

print(''.join([str(random.randint(0,9)) for i in range(8)]))

a=[1,5,47]
b=tuple(a)
print(b)
# 1.匹配出163的邮箱地址，且@符号之前有4到20位，例如xxxx@163.com，@前面不能有.
# import re
# a=['xiaowang@163.com','xiaowang@163.comheihei','.com.xiaowang@qq.com']
# for i in a:
#     b=re.match(r"[a-z]{4,20}@\d{3}\.[a-z]{2}m$",i)
#     if b:
#         print(f"邮箱地址是{b.group()}")
#     else:
#         print(f"错误地址是{i}")


# 2.匹配出以下变量中163、126、qq邮箱
# 要求：
# (1).@前面不能有特殊字符
# (2).@之前有8到20位
# 变量内容如下:
# a = ["1762909851@163.com","hwwkn889#$%^@163.com","2972298996@qq.com",".haiaj@126.com","wsy127679@126.com"]
# for i in a:
#     r=re.match(r"[a-zA-Z0-9]{8,20}@(163|126|qq)\.com",i)
#     while r:
#         if r.group(1)=='163':
#             print(f"163邮箱有{r.group()}")
#             break
#         elif r.group(1)=='126':
#             print(f"126邮箱有{r.group()}")
#             break
#         elif r.group(1) == 'qq':
#             print(f"qq邮箱有{r.group()}")
#             break
#     else:
#         print(f"错误邮箱是{i}")




# 3.data='<content>aaaaahss839a</content>'
# 要求：使用正则将上面的标签里的内容"aaaaahss839a"解析出来，并打印。
# data=re.match(r"<([a-z]*)>(.*)</\1>","<content>aaaaahss839a</content>")
# print(data.group(2))



# 4.匹配出下面变量中的字符串，哪个是符合前端标签的。
labels = ["<html><h1>baidu</h1></html>", "<html><h1>baidu</h2></html>"]
for i in labels:
    a=re.match(r"<([a-z]{4})><([a-z].*)>.*</\2></\1>",i)
    if a:
        print(f'{a.group()}符号前端标签')
    else:
        print(f'{i}不符号前端标签')


# 5.不是以4、7结尾的手机号码(11位)
# r=input('请输入手机号')
# a=re.match("\d{10}[0-35-68-9]",r)
# if a:
#     print(f"你的手机号{a.group()}不是4、7结尾的")
# else:
#     print(f"你的手机号{r}是4、7结尾的")

