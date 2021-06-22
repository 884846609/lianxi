#1、使用while循环和for循环,求1～100之间所有偶数之和(至少一种方法)

# sum=0
# for a in range(0,101,2):
#     sum+=a
# print(sum)





#  2、 使用while循环和for循环输出1 2 3 4 5 6     8 9 10(至少一种方法)
# for i in range(1,11):
#     if i==7:
#         continue
#
#     print(i)

# 3、使用for循环,求1-100的所有数的和
# i=0
# i=0
# sum=0
# for i in range(101):
#     sum+=i
#
# print(sum)

# 4输出1到100之间的偶数与奇数

# a=2;b=1
# for a in range(2,100,2):
#     print(a)
# for b in range(1,100,2):
#     print(b)

# 5、用户登陆（三次机会重试），用户名为:abc；密码为123

# #
# i=1
# for i in range(1,4):
#     name = str(input('请输入用户名'))
#     key = str(input('请输入密码'))
#     if (name == "abc"and key =='qq')or (name=="ss"and key=="123") or (name=="ab"and key=="22"):
#         print('登录成功')
#         break
#     else:
#         print('用户名密码错误')
#         i+=1
#     if i >3:
#         print('游戏结束')

#### 6、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 外循环一次，内循环一周
# c=0
# for i in range(1,5):
#     for j in range(1,5):
#         for h in range(1, 5):
#             if i != j and j != h and i != h:
#                 print(i,j,h)
#                 c+=1
#
# print(c)


#### 7、输入三个整数x,y,z，请把这三个数由小到大输出。要求：(结合sort函数去做)
# a=int(input("请输入一个整数"))
# b=int(input("请输入一个整数"))
# c=int(input("请输入一个整数"))
# d=[a,b,c]
# d.sort()
# for i in d:
#     print(i)

#### 8、将一个列表的数据复制到另一个列表中。使用两种方法

##### 列表如下所示list1 = [11,22,33,44]
# a=[]
# list1 = [11,22,33,44]
# a.insert(0,list1)
# print(a)
# print(a+list1)
#
# a.extend(list1)
# print(a)

# 9、按相反的顺序输出列表的值a = ['one', 'two', 'three']
# a = ['one', 'two', 'three']
# print(a[2],a[1],a[0] )
# for i in a:
#     print(a[2],a[1],a[0])
# print(a[::-1])
# a.reverse()     #反向输出函数
# print(a)


# 10、有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，
# 将小于66值保存至第二个key的值中。
# a=[11,22,33,44,55,66,77,88,99,90]
# b=[]
# c=[]
# d={}
# for i in a:
#     if i >= 66:
#         b.append(i)
#
#     else:
#         c.append(i)
# # print(b)
# # print(c)
# d['key1']=b
# d['key2']=c
# print(d)


#### 11、列表去重,不用set()
#
# list1 = [12,45,12,34,12,0,33,45,0]
# new = []
# for i in list1:
#     # if i not in new:
#     #     new.append(i)
#     if list1.count(i)>1:
#         list1.remove(i)
# print(list1)
#




# 12、输入一个人名，如果字典中有这个人输出人名对应的城市。**

# 字典如下：places={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
#
# 执行结果如下：
#
# > 请输入名字:李四
# > ['九寨沟', '张家界', '张++']
# dict={'张三':['上海','广州','深圳'],'李四':['九寨沟','张家界','张++']}
# i=input('请输入')
#
# for a in dict:
#     if i==a:
#         print(dict[a])
#
# # 13、用户输一个数字，求那个数的阶乘  5=1*2*3*4*5
# a=int(input("shuru"))
# sum=1
# i=1
# for i in range(1,a+1):
#     sum*=i
#     i+=1
# print(sum)

# 14、输入一个字符，统计输出的字母、数字、空格个数

# s = input("请输入一个字符串")
# n=0 # 个数
# m=0
# o=0
# for i in s:
#
#     if i.isdigit():
#         n+=1
#     elif i.isalpha():
#         m+=1
#     elif i.count():
#         o+=1
#
# print("数字的个数为：",n)
# print("字母的个数为：",m)
# print("空格的个数为：",o)



# 15、猜数字游戏===用for和while两个循环实现
#
# 要求：
#     1.允许用户最多尝试3次，3次都没猜对的话，就直接退出并提示"三次机会已用完"，如果猜对了，打印恭喜信息并退出
#
# # 2.猜的数字给定要求：1----18之间的随机整数
# import random
# guess=random.randint(1,18)
# b=1

# while b <= 3:
#     a = int(input("输入"))
#     if a==guess:
#         print('猜对了')
#         break
#     else:
#         print('猜错了')
#     b+=1


# for i in range(3):
#     a=int(input())
#     if a==guess:
#         print('猜对了')
#         break
#     else:
#         print('猜错了')
# else:
#     print('三次机会用完')











# 求1000以内的水仙花数
#
# 如： 153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方



# 17、用户输入一个数，判断是否是一个回文数
# a = input("suru")
# s = a[::-1]
#
#
# if a == s:
#     print("你输入的是回文数")
# else:
#     print('错了')

# 18、data='<content>aaaaahss839a</content>
#
# 将标签里的内容打印出来，不用切片。
# data='<content>aaaaahss839a</content>'
# print('<content>aaaaahss839a</content>'.strip('<content>'))
# a="aaaaahss839a</"
# print(a.strip("</"))




