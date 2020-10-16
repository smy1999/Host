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
