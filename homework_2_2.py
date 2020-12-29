S = [1,3,4,8,13,17,20]

difference = 2
i = 0
result = int(S[i+1])-int(S[i])

def distance(*i):
    for i in range(1,len(S)):
        if result > difference:
            continue
        
        else:
            difference = result
        finally: i+1
    
        return difference

distance(S)

print(S[i], S[i+1])

# 초기값 설정 - 3-1 = 2

# 위치 기본 설정 = 0

# for 원소의 개수 만큼 range(1,len(S))

# 판단 n ~ n-1 작은지 확인

# 초기값보다 작으면, 초기값을 이 값으로 변경

# 인덱스도 같이 변경

# 아니면 무시

#인쇄 (인덱스-1, 인덱스)