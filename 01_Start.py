print("Hello world")
for i in range(1, 11):
    print(str(i) + '번째 인사')

### 기본 문법
# 더하기            : +
# 뺴기              : -
# 곱하기            : *
# 제곰              : **
# 나누기            : /
# 나눗셈의 몫       : //
# 누눗셈의 나머지   : %
5 + 2   # 7
5 - 2   # 3
5 * 2   # 10
2 ** 4  # 16
10 / 2  # 5
11 // 2 # 5
8 % 5   # 3

for i in range(100):    # 100 미만 정수를 차례대로 i에 입력
    if i % 7 == 0:      # i를 7로 나눴을 때 나머지가 0이면
        print(i)        # i를 출력

# 평균
(50 + 45 + 33 + 39 + 29 + 30) / 6
# round(숫자, 표시할 소수점 자릿수)
round((50 + 45 + 33 + 39 + 29 + 30)/6, 1)   # 37.7

# lambda() 와 def 문
Three = lambda x : x * 3
print(Three(12))

def FuncThree(x):
    return x * 3
print(FuncThree(13))
# 개발자들은 lambda보다 def를 주로 사용, 가독성이 떯어지기 떄문

def FuncCaculator(a, b):
    return a + b, a - b, a * b, a / b
print(FuncCaculator(12, 3))     # (15, 9, 36, 4.0) 
print(type(FuncCaculator(12, 3)))   # 반환값은 튜플로 반환됨

# input('사용자에게 입력받을 값을 설명하는 내용')
a = input('In put some number. : ')
print('Nunber : ', a)

# type() 함수는 자료형의 유형을 알수있음
a = int(a)
print(type(a))

a = float(a)
print(type(a))

#if-else 문
def DefSeperate():
    a = int(input('자연수 중 하나를 입력하세요 : '))
    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')

DefSeperate()
DefSeperate()
DefSeperate()

# 비교 연산자
#   X < Y     : X 가 Y 보다 작다.
#   X > Y     : X 가 Y 보다 크다.
#   X == Y    : X 와 Y 같다.
#   X != Y    : X 와 Y 다르다.
#   X <= Y    : X 가 Y 보다 작거나 같다.
#   X >= Y    : X 가 Y 보다 크가나 같다.
#   if a is not b : a 가 b 아니라면

# 서비스 가격 출력 프로그램을 완성하기
price = [23, 40, 67]        # 리스트를 사용
for i in price:             # price의 리스트를 하나씩 얻어
    i * 1.1                 # i에 1.1을 곱함

def DefService_price():
    service = input('서비스 종류를 입력하세요, a/b/c : ')
    valueAdded = input('부가세를 포함합니까? (y/n) : ')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 * 1.1
        if service == 'b':
            result = 40 * 1.1
        if service == 'c':
            result = 67 * 1.1
    else:
        if service == 'a':
            result = 23
        if service == 'b':
            result = 40
        if service == 'c':
            result = 67
    print(round(result, 1), '만 원입니다.')

DefService_price()
DefService_price()


