numlist = [i for i in range(1, 1000)] # 범위 지정하기
output_1 = [i for i in numlist if i % 3 == 0] # 3의 배수 구하기
output_2 = [i for i in numlist if i % 5 == 0] # 5의 배수 구하기
#output_3 = [i for i in numlist if i % 15 == 0] # 15의 배수 구하기

result = set(output_1 + output_2) # 합집합 구하기
#result = set(output_)
# - output_3 # 교집합 빼기

resolution = sum(list(result)) # 목록과 그 합으로 변화

#print(result)
print(resolution)