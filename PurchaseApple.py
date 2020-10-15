# Version 1.0
priceStr = input("请输入单价 : ")
weightStr = input("请输入重量 :")
price = float(priceStr)
weight = float(weightStr)
print("价格为" + str(price * weight))

# Version 2.0
print("价格为" + str(float(input("请输入单价 : ")) * float(input("请输入重量"))))

# Version 1.1
price = input("请输入单价 : ")
weight = input("请输入重量 :")
price = float(price)
weight = float(price)
print("价格为" + str(price * weight))
