names = ['이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌']
i = 0

i = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')

print(i)

# 1번 문제
print('1번 문제')
def count_kim():
    count = 0
    for item in i:
        count_kim = item[0]
        if count_kim.startswith('김'):
            count +=1
    return count

def count_lee():
    count = 0
    for item in i:
        count_lee = item[0]
        if count_lee.startswith('이'):
            count +=1
    return count

print('김씨는', count_kim(), '명입니다.')
print('이씨는', count_lee(), '명입니다.')

#2번 문제
print('2번 문제')
print(i.count('이재영'))

#3번 문제
print('3번 문제')
print(list(set(i)))

#4번 문제
print('4번 문제')
print(sorted(list(set(i))))