import keyword

# 001.注释使用
print("hello world!")  # 井号前必须两个空格
# good
print()  # 默认带换行符
print("nice Python")
"""
This is multi line.
This is multi line.
"""

# 002.四则运算(直接除, 取整除, 字符串乘法)
# 10 / 20 = 0.5
# 9 // 2 = 4
print("?" * 19)  # 字符串可以用乘法

# 003.变量类型
price = 12.3
weight = 999
money = price * weight
print(weight)
print(price)
print(money)
# int float bool str 不指定类型
# Python3不区分long和int
print(type(money))  # type()显示变量类型

# 004.字符计算
str1 = "hello "
str2 = "world !"
str3 = str1 + str2
print(str3)
print((str1 + str2) * 10)
print(str(price) + str1)  # str()将int转换为string
print("10" + str1)

# 005.bool型视为0和1,大于0视为True
what = True
x1 = 10
print(what + x1)

# 006.input输入为string
inputData = input("Please Input : ")
print(inputData)

# 007.类型转换函数
str4 = "12"
str5 = "12.4"
int(str4)
float(str5)

# 008.格式化字符串%
print("%s" % str1)
print("%s%s%s" % (str1, str2, str3))  # 多个变量输出
print("%06d" % x1)  # 输出6位整数,缺位以0补齐
print("%4d" % x1)  # 输出4位整数,缺位以空格补齐
print("%.02f" % price)  # 小数点后输出2位
print("%f" % price)
print("%%%s" % str1)  # 输出百分号%

# 009.显示关键字
print(keyword.kwlist)

# 010.
# 011.
# 012.
