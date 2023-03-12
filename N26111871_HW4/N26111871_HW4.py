import random
import math

mean = 10 #設定mean,可改為1、4等數值
interval_num = 35 #設定區間數

#1
interval = [0] * (interval_num) #初始各區間的頭尾為0
sum = 0 #用來計算當前累計的區間
for i in range(interval_num): #計算各個區間
    p = math.exp(-1 * mean) * math.pow(mean, i) / math.factorial(i) #帶入公式求出p
    interval[i] = p + sum
    sum += p

count_1 = [0] * interval_num #統計各個區間的數量
for i in range(10000000): #利用隨機亂數產生一千萬筆資料
    u = random.random()
    for j in range(interval_num): #將隨機亂數和區間做比對
        if  u < interval[j]: #若符合條件則代表找到該區間
            count_1[j] += 1
            break
for i in range(interval_num):
    print("p",i,"：",count_1[i])

print("---------------------------------")

#2
count_2 = [0] * interval_num #統計各個區間的數量
for i in range(10000000): #產生一千萬筆資料
    prod = random.random() 
    j = 1 #計算目前乘了多少次prod
    while prod >= math.exp(-1 * mean): #帶入公式來求出j
        prod *= random.random()
        j += 1
    count_2[j - 1] += 1

for i in range(interval_num):
    print("p",i,"：",count_2[i])
