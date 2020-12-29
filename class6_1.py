# pip install math
#import math
#math.sin(1)


# pip install math
#import math
#from math import sin, cos, tan
#from math import *
# 쓰지 않을 것도 다 읽어오므로 메모리 관리 차원에서는 권장하지 않음

#sin(1)

import random

print(random.random())
print('- random():', random.random())

print('- uniform(10, 20):', random.uniform(10, 20))

print('- randrange(10):', random.randrange(10))

print('- choice([1, 2, 3, 4, 5]):', random.choice([1, 2, 3, 4,5]))

import os
print(os.name)
print(os.getcwd())
print(os.listdir())
#os.mkdir('hello')
#os.rmdir('hello')

import datetime

print('# 현재 시작 출력하기')
now = datetime.datetime.now()

print(now.year, '년')
print(now.month, '월')
print(now.day, '일')
print(now.hour, '시')
print(now.minute, '분')
print(now.second, '초')
print()

print('# 시간을 포맷에 맞춰 출력하기')
output_a = now.strftime('%Y.%m.%d %H:%M:%S')
output_b = '{}년 {}월 {}일 {}시 {}분 {}초'.format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초')

print(output_a)
print(output_b)
print(output_c)
print()

import time
print('지금부터 5초 동안 정지합니다!')
time.sleep(5)
print('프로그램을 종료합니다.')

print('지금부터 CCTV를 15분 동안 정지합니다!')
time.sleep(5)
print('CCTV 영상을 더미로 대체합니다.')

from urllib import request

target = request.urlopen('https://google.com')
output = target.read()

print(output)