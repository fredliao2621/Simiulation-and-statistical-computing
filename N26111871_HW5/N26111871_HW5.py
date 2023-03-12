import random
import math
import matplotlib.pyplot as plt

distribution = [0] * 101 # 分數為0~100
interval = [0] * 3 # 用來表示一、二及三個標準差內的分布情形
mu = 70 # 平均數
sigma = 5 # 標準差
num = 1000000 # 模擬資料數(學生數)

for i in range(num):
    y = -1 * math.log(random.random()) # 產生rate為1的隨機變數y
    u = random.random() # 產生隨機變數x
    while u > math.exp(-1 * (y - 1) **2 / 2): # 當u<=此公式時x=y，否則重新產生y及u
        y = -1 * math.log(random.random())
        u = random.random()
    x = y

    sign = random.random() #由於以上產生的x皆為正數，因此以50%的機率將x變為負號
    if sign < 0.5:
        x = -1 * x

    score = round(mu + x * sigma) #將x帶入公式後四捨五入為整數可以求出分數
    if score < 0: # 為了將分數合理化，將分數的最小值設為0，最大值設為100
        score = 0
    elif score > 100:
        score = 100

    distribution[score] += 1  # 統計出每一筆分數的分布
    for j in range(1,4): # 統計在一、二及三個標準差內的分布
        if score >= mu - j * sigma and score < mu + j * sigma:
            interval[j - 1] += 1

print("一個標準差 :", interval[0] / num * 100, "%")
print("兩個標準差 :", interval[1] / num * 100, "%")
print("三個標準差 :", interval[2] / num * 100, "%")

plt.plot(distribution)
plt.title("distribution")
plt.xlabel("score") 
plt.ylabel("number of people") 
plt.show()