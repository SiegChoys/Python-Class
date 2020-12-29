f = open('새파일.txt', 'w')

for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)

f.close()

f = open('새파일.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open('새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('새파일.txt', 'r')
data = f.read()
print(data)
f.close()

f = open('새파일.txt', 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

with open('foo.txt', 'w') as f:
    f.write('Life is too short, you need python')

def is_odd(number):
    if number % 2 == 1:
        print('홀수입니다')
    else:
        print('짝수입니다')
    
number=int(input('자연수를 입력하세요'))

print(is_odd(number))

def ave(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

print(ave(1,2,3,4,5))

try:
    number_input_a = int(input('정수 입력>'))
except:
    print('정수를 입력하지 않았습니다')
else:
    print('원의 반지름:', number_input_a)
    print('원의 둘레:', 2 * 3.14 * number_input_a)
    print('원의 넓이:', 3.14 * number_input_a * number_input_a)
    

try:
    number_input_a = int(input('정수 입력>'))
except:
    print('정수를 입력하지 않았습니다')
else:
    print('예외가 발생하지 않았습니다')
finally:
    print('어떻게든 끝났습니다')

try:
    file = open('info.txt', 'w')
    file. close()
except Exception as e:
    print(e)

print('# 파일이 제대로 닫혔는지 확인하기')
print('file.closed:', file.closed)

def test():
    print('test() 함수의 첫 줄입니다.')
    try:
        print('try 구문이 실행되었습니다.')
        return
        print('try 구문 뒤의 return 키워드 뒤입니다.')
    except:
        print('except 구문이 실행되었습니다.')
    else:
        print('else 구문이 실행되었습니다.')
    finally:
        print('finally 구문이 실행되었습니다.')
    print('test() 함수의 마지막 줄입니다.')
    
test()

print('프로그램이 시작되었습니다.')

while True:
    try:
        print('try 구문이 실행되었습니다.')
        break
        print('try 구문 뒤의 break 키워드 뒤입니다.')
    except:
        print('except 구문이 실행되었습니다.')
    finally:
        print('finally 구문이 실행되었습니다.')
    print('while 반복문의 마지막 줄입니다.')
print('프로그램이 종료되었습니다.')

try:
    
    number_input_a = int(input('정수 입력>'))

    print('원의 반지름:', number_input_a)

except Exception as exception:
    print('type(exception):', type(exception))
    print('exception:', exception)

list_number = [52, 273, 32, 72, 100]

try:
    
    number_input = int(input('정수 입력>'))

    print('{}번째 요소: {}'.format(number_input, list_number[number_input]))
except Exception as exception:
    print('type(exception):', type(exception))
    print('exception:', exception)

try:
    
    number_input = int(input('정수 입력>'))

    print('{}번째 요소: {}'.format(number_input, list_number[number_input]))

except ValueError:
    print('정수를 입력해주세요')

except IndexError:
    print('리스트의 인덱스를 벗어났습니다')