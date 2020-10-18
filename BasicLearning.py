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
# step over 越过函数
# step into 进入函数
# 函数前后量空行, 注释在函数内部第一行

# 016.列表List可存储不同类型数据 有序
name_list = ["lg", "smy", "lzy", "my", "zzp"]
print(name_list[2])
print(name_list.index("smy"))  # 目标值所在索引位置index, 不在则报错
name_list[3] = "mbd"  # 修改
name_list.append("wow")  # 增加到末尾
name_list.insert(3, "hey")  # 在指定位置增加, 其后向后推移
name_list.extend(["zzz", "tzp"])  # 列表末加入新列表
name_list.remove("smy")  # 删除第一个出现的指定数据
name_list.pop()  # 删除末尾数据/指定位置数据
del name_list[3]  # 删除指定位置(将变量从内存中删除, debug中删除这个变量)
name_list.clear()  # 清空列表
name_list_len = len(name_list)  # 统计列表中元素个数
name_list.count("lg")  # 统计指定数据出现的次数
name_list.sort()  # 升序
name_list.sort(reverse=True)  # 降序
name_list.reverse()  # 翻转
name_list.copy()
for name in name_list:  # for循环遍历List
    print(name)

# 017.元组Tuple表示多个元素的序列,不可修改
info_tuple = ("smy", 22, 178)
empty_tuple = ()  # 空元组
one_element_tuple = ("smy", )  # 只有一个元素的元组,若无","则视为括号内类型
info_tuple.count(22)  # 计算指定元素出现次数
len(info_tuple)  # 计算元素个数
var = info_tuple[1]  # 访问指定位置
info_tuple.index(22)  # 目标值所在索引位置index
for info_element in info_tuple:  # 应当注意数据类型不同, 循环内部可能出现不同
    print(info_element)
print("%s %d %f" % ("smy", 10, 10.4))  # 后面括号本质就是元组
print("%s %d %f" % info_tuple)
info_str = "%s %d %f" % info_tuple
list(info_str)  # 转换格式
tuple(name_list)

# 018.字典Dictionary 无序
# 键唯一, 只能为字符串、数字、元组
smy = {"name": "shaomingyue",
       "age": 21,
       "gender": True,
       "height": 1.78}
var1 = smy["name"]  # 取值
smy["language"] = "java"  # 增加, 存在则修改
smy.pop("language")  # 删除指定键值对
len(smy)  # 统计键值对数量
smy2 = {"language": "Java"}
smy.update(smy2)  # 合并字典, 若有重复则覆盖
smy.clear()  # 清空
