#numlist = [str(i) for i in range(1, 10000+1, 1)]

# count(8)
#198쪽, 204쪽 참조

#print(numlist)

count_8 = 0
for i in range(1, 10000+1):
    count_8 += str(i).count('8')
print(count_8)