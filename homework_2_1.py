i = [3, 4, 5, 6, 7]
j = [12, 16, 22, 24, 29]
k = [41, 43, 45, 47, 49]

numbers = i + j + k

count_2x = 0
count_not_2x = 0

for item in numbers:
    if item % 2 == 0:
        count_2x +=1
    else:
        count_not_2x +=1

print('홀수', count_not_2x, '개,', '짝수', count_2x,'개')

### --- ###

def func():
    count_2x = 0
    count_not_2x = 0

    for item in range:
        if item % 2 == 0:
            count_2x +=1
        else:
            count_not_2x +=1

print('홀수', count_not_2x, '개,', '짝수', count_2x,'개')

func([3, 4, 5, 6, 7])
func([12, 16, 22, 24, 29])
func([41, 43, 45, 47, 49])