import random
import math

inside = 0 #inside為圓裡點的個數
center = (0.5, 0.5) #center為圓心座標
value = int(input("請輸入矩形裡點的個數:")) #value為矩形裡點的個數

for i in range(value):
    point = (random.random(), random.random()) #利用隨機亂數產生點的座標
    d = math.dist(center, point) #算出點和圓心的距離
    if d <= 0.5: #若距離大於半徑(0.5),則點在圓外
        inside += 1

rate = inside / value #計算出圓裡的點和圓外的點的比率
pi = rate / 0.5**2 #將圓面積除以半徑的平方即可推算出圓周率
print("pi:", pi)