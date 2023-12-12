import random

realInt = random.randint(0, 9)
myInt = int(input("请输入猜一个0-9的数字："))
count = 0

while myInt != realInt:
    count += 1
    if myInt > realInt and count<10:
        myInt = int(input("太大了, 继续："))
    elif myInt < realInt and count<10:
        myInt = int(input("太小了, 继续："))
    
    if count >= 10:
        print("超过" + str(count) + "次了！")
        break

if myInt == realInt:
    print("猜对了！")
