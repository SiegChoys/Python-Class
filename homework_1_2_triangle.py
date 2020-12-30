def search (x, y, z):
    if x+y+z!=180 or x == 0 or y == 0 or z == 0:
        print('삼각형이 아닙니다')
    else:
        if x > 90 or y > 90 or z > 90:
            print('둔각 삼각형')
        elif x == 90 or y == 90 or z == 90:
            print('직각 삼각형')
        else:
            print('예각 삼각형')
    return ''

x=int(input('제1각을 입력하세요'))
y=int(input('제2각을 입력하세요'))
z=int(input('제3각을 입력하세요'))

print(search(x,y,z))