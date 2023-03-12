import random
color = red = orange = yellow = green = blue = purple = 0

sample = int(input("請輸入取球次數 : "))
Expected_Value = int(sample)/6
for i in range(sample):
    color = random.randrange(6)
    if color == 0:
        red += 1
    elif color == 1:
        orange += 1
    elif color == 2:
        yellow += 1
    elif color == 3:
        green += 1
    elif color == 4:
        blue += 1
    elif color == 5:
        purple += 1

print("期望值 :", Expected_Value)
print("紅色 :", red)
print("橙色 :", orange)
print("黃色 :", yellow)
print("綠色 :", green)
print("藍色 :", blue)
print("紫色 :", purple)