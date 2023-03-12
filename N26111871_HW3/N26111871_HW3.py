import random
import math
import time

#1
p = 0.2 #成功的機率
first_start_time = time.time()
n_count = [0] * 100 #統計每一次的模擬中需要嘗試幾次才能成功
for i in range(10000000): #做一千萬次模擬
    n = 1 #記錄每一次模擬中嘗試的次數，從第一次開始
    while random.random() > p: #利用隨機亂數模擬結果，若失敗則再試一次
        n += 1
    n_count[n - 1] += 1 #將嘗試次數統計在列表中
first_end_time = time.time()
print("First time：", first_end_time - first_start_time)


#2
second_start_time = time.time()
interval = [] #紀錄每個區間的頭尾
head = 0 #代表每個區間的起始，初始為0
for i in range(1, 101): #將區間劃分為100份
    pr = (1 - p) ** (i - 1) * p #計算出在第i次成功的機率
    interval.append((head,head + pr)) #求出每個區間的頭跟尾
    head = head + pr

inverse_count = [0] * 100 #統計每一次的模擬中需要嘗試幾次才能成功
for i in range(10000000): #做一千萬次試驗
    u = random.random() #利用隨機亂數模擬結果
    for j in range(100): #將隨機亂數和區間做比對
        if u < interval[j][1]: #若符合條件則代表找到該區間
            inverse_count[j] += 1
            break
second_end_time = time.time()
print("Second time：", second_end_time - second_start_time)


#3
third_start_time = time.time()
x_count = [0] * 100 #統計每一次的模擬中需要嘗試幾次才能成功
for i in range(10000000): #做一千萬次模擬
    u = random.random() #利用隨機亂數模擬結果
    x = int(math.log(1 -u) / math.log(1 - p)) + 1 #帶入公式得出在第x次成功
    x_count[x - 1] += 1
third_end_time = time.time()
print("Third time：", third_end_time - third_start_time)
