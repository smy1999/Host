# 001.格式化输出
name = "Lee"
print("我的名字叫 %s, 请多关照~" % name)

studentNumber = 14
print("我的学号是%06d" % studentNumber)
student2Number = 123112312
print("我的学号是%06d" % student2Number)

price = 1.4
weight = 2.3
money = price * weight
print("苹果单价%.2f元/斤，购买了%.2f斤，需支付%.2f元" % (price, weight, money))

scale = 10
print("数据比例为%.2f%%" % scale)

# 002.判断语句
age = int(input("请输入年龄 : "))
if age >= 18:
    print("可以进入网吧")
else:
    print("不可以进入网吧")

# 判断节日
holiday_name = "情人节"
if holiday_name == "情人节":
    print("买玫瑰, 看电影")
elif holiday_name == "平安夜":
    print("买苹果, 吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("每天都是节日")

# 火车站安检
has_ticket = True
knife_length = 25.0
if has_ticket:
    print("去安检")
    if knife_length > 20:
        print("刀长" + str(knife_length) + "厘米, 不允许上车")
    else:
        print("安检通过")
else:
    print("不能安检")

# 003.逻辑
# 判断年龄合法
age = 14
if 0 <= age <= 120:
    print("年龄正确")
else:
    print("年龄错误")

# 判断成绩合格
python_score = 99
c_score = 51
if python_score > 60 or c_score > 60:
    print("成绩合格")
else:
    print("成绩不合格")

# 判断是否是员工
is_employee = False
if not is_employee:
    print("请勿入内")
else:
    print("请进入")

# 004.循环
# 0-100求和
ans = 0
i = 0
while i <= 100:
    ans += i
    i += 1
print("ans = %d" % ans)

# 0-100偶数求和
ans = 0
i = 0
while i <= 100:
    ans += i
    i += 2
print("ans = %d" % ans)
