import keyword
import MultiplicationTable

# 001.注释使用
print("hello world!")  # 井号前必须两个空格
# good
print()  # 默认带换行符
print(end='')  # 不换行
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

# 010.判断
if x1 == 10:  # 条件后不跟空格直接:/折叠/最下方显示条件
    print("isTrue")
elif x1 == 9:
    print("isMid")
else:
    print("isFalse")

# 011.逻辑运算and/or/not
a = 4
b = 5
if a > 4 and b < 5:
    print("1")
elif a > 4 or b < 4:
    print("2")
elif not a == 4:
    print("3")

# 012.判断过长缩进格式
if ((a == 1 and b == 1)
        or (a == 2 and b == 2)
        or (a == 2 and b == 3)):
    print("格式")

# 013.循环
i = 1
while i <= 5:
    print("round %d " % i, end='')
    i += 1
# break退出循环, continue不执行之后代码块而进入下一循环

# 014.转义字符
# \t制表符 \n换行 \\反斜杠 \'单引号 \"双引号 \r回车
print("1 2 3")
print("10 20 30")
print("1\t2\t3")  # 制表符\t
print("10\t20\t30")

# 015.函数调用:先import文件,再调用/文件中直接调用
MultiplicationTable.multiplication_table()
# 函数结束有两行空再运行
