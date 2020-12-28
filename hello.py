print("Hello Coding Python")
#하나만 출력합니다.
print('#하나만 출력합니다.')
print('Hello Python Programming...!')
print()

#여러개를 출력합니다.
print('#여러 개를 출력합니다.')
print(10, 20, 30, 40, 50)
print('안녕하세요', '저의 이름은', '조용식입니다')
print()

#아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print('#아무것도 출력하지 않습니다')
print("--확인 전용선---")

def add_many(*args):
        result = 0
        for i in args:
            result = result + i
        return result

result = add_many(1, 2, 3)
print(result)

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3)
print(result)

def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d입니다.' % old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('조용식', 34, 'man')

a = 1
def vartest(a):
    a = a +1
    return a
a = vartest(a)
print(a)

add = lambda a, b: a+b
result = add(3, 4)
print(result)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
print('1!', factorial(1))
print('2!', factorial(2))
print('3!', factorial(3))

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print('fibonacci(1):', fibonacci(1))
print('fibonacci(2):', fibonacci(2))
print('fibonacci(3):', fibonacci(3))
print('fibonacci(4):', fibonacci(4))
print('fibonacci(5):', fibonacci(5))

#print('fibonacci(6):', fibonacci(6))
#print('fibonacci(7):', fibonacci(7))
#print('fibonacci(8):', fibonacci(8))
#print('fibonacci(9):', fibonacci(9))
#print('fibonacci(10):', fibonacci(10))

#print('fibonacci(35):', fibonacci(35))

        
def power(item):
    return itm * item
def under_3(item):
    return item <3

lists_input_a = (1, 2, 3, 4, 5)

output A = map_power(list_input_a)
print ('# map 함수()의 실행결과')
print ('map() 함수의 실행결과')
print ('map(power, list_input_a):', output_a)
print ('map(power, list_input_a):', list(output_a))
print()

###

power = lambda x: x * x

under_3 = lamda x: x < 3
    
lists_input_a = [1, 2, 3, 4, 5]

output A = map_power(list_input_a)
print ('# map 함수()의 실행결과')
print ('map() 함수의 실행결과')
print ('map(power, list_input_a):', output_a)
print ('map(power, list_input_a):', list(output_a))
print()

###

###

