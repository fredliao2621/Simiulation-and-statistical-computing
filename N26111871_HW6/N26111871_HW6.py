import random
import math
import matplotlib.pyplot as plt

lam = int(input("請輸入lambda:")) #Arrival Rate
mu = int(input("請輸入mu:")) #Service Time
t = int(input("請輸入t:")) #營業時間的長度

arrival = [0] * lam #每位顧客的抵達時間
service = [0] * lam #每位顧客的服務時間
start_service = [0] * lam #每位顧客的開始服務時間
end_service = [0] * lam #每位顧客的結束服務時間

for i in range(lam): #利用lambda和mu算出每位顧客的抵達時間和服務時間
    if i == 0:
        arrival[i] = (-1 / lam) * math.log(random.random())
    else:
        arrival[i] = arrival[i - 1] + (-1 / lam) * math.log(random.random())

    service[i] = (-1 / mu) * math.log(random.random())

#第一位顧客的開始服務時間和結束服務時間
start_service[0] = arrival[0]
end_service[0] = arrival[0] + service[0]
total_service = 1 #總共服務多少位顧客

for i in range(1, lam):
    #若前一位顧客已經離開且商店還沒打烊
    if end_service[i - 1] <= arrival[i] and arrival[i] <= 1:
        start_service[i] = arrival[i] #則顧客抵達後可直接被服務
        total_service += 1
    #若前一位顧客還沒離開且商店還沒打烊
    elif end_service[i - 1] > arrival[i] and arrival[i] <= 1:
        start_service[i] = end_service[i - 1] #則顧客排隊等待前一位顧客離開
        total_service += 1
    #商店打烊
    else: 
        total_service = i
        break

    end_service[i] = start_service[i] + service[i]


for i in range(lam): #將時間單位調整程適當大小
    arrival[i] *= t
    service[i] *= t
    start_service[i] *= t
    end_service[i] *= t

#利用數學公式計算出utilization
math_utilization = lam / mu
print("Server utilization(math):", math_utilization)

#利用模擬的數據計算出utilization
busy = 0
for i in range(total_service):
    busy += end_service[i] - start_service[i]
simulation_utilization = busy / t
print("Server utilization(simulation):", simulation_utilization)

waiting = [0] * total_service
for i in range(total_service): #計算出每位顧客的等待時間
    waiting[i] = start_service[i] - arrival[i]
avg_waiting = sum(waiting) / total_service #計算出平均的等待時間
print("Average waiting time:",avg_waiting)

#畫出等待時間的分布圖
plt.plot(waiting)
plt.title("waiting time distribution")
plt.xlabel("customer") 
plt.ylabel("waiting time") 
plt.show()