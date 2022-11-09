# os 모듈을 임포트(import)
import os
OriginPath = os.getcwd()
print('os.getcwd() = ', os.getcwd())     # 현재 위치한 경로가 표시

# 폴더 이동
os.chdir('C:\\000_002_Python\\01_Start\\Test')
print('os.getcwd() = ', os.getcwd())

os.chdir(OriginPath)
# 폴더 안의 파일 확인하기
print('os.listdir() Type >>> ', type(os.listdir()))
print('os.listdir() Data >>> ', os.listdir())

# 파일 열기 open()
# 파일 객체 = open('파일 이름', 파일 열기 모드)
#   # 파일 열기 모드
#   # 'w' 파일에 내용을 새로 쓸 때 사용
#   # 'r' 파일 내용을 읽을 때 사용
#   # 'a' 파일에 내용을 추가할 떄 사용
f = open('a.txt', 'w')
print('f.write(''abc'') >>> ', f.write('abc'))
# 파일 닫기
f.close()

f = open('a.txt', 'w')
print('f.write(''abc'') >>> ', f.write('나는 오늘 파이썬을 배우고있다.'))
f.close()

f = open('a.txt', 'r')
print('f.read() >>> ', f.read())
print('f.read() >>> ', f.read())    # 커서 위치가 파일 가장 끝에 있어 더 읽을 수 없다.
f.seek(0)                           # 커서 위치를 파일 가장 처음으로 이동하라는 의미
print('f.read() >>> ', f.read())
f.close()

f = open('a.txt', 'r')
strDirary = f.read()
print('strDirary >>> ', strDirary)
print('strDirary[:5] >>> ', strDirary[:5])
f.close()


f = open('a.txt', 'a')
print('f.write(''abc'') >>> ', f.write('파이썬의 모든 것을 깨우칠때가 올까?'))
f.close()
f = open('a.txt', 'r')
print('f.read() >>> ', f.read())
f.close()

# with 를 사용하여 close를 생략하기
with open('test.txt', 'w') as f:        # 먼저 with 문을 사용해 test.txt를 쓰기 모드로 열기
    f.write('오늘 나는 학교에 갔습니다.')

# 한글 파일 오류
f = open('한글파일.txt', 'r', encoding='utf8')
f.close()

# codecs 모듈을 임포트하여 파일 형식 utf-8로 지정해 파일을 open
import codecs
f = codecs.open('한글파일.txt', 'r', 'utf-8')
f.read()[:18]
f.close()

# 03-2 정규표현식으로 문자열 다루기
# 정규표현식이란?
# 정규표형식 모듈 re를 호출
import re
example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018).'
result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
print('result = ', result)

# match 매서드 - 문자열 도입에서 패턴 찾기
# re.match(패턴, 문자열)
import re
pattern = r'life'                           # 패턴을 객체에 저장, 패턴 앞에는 r을 붙여줍니다.
script = 'life'                             # 패턴과 같은 스크립트를 다른 객체에 저장
print(re.match(pattern, script))            # script 에서 pattern을 찾으세요
print(re.match(pattern, script).group())    # group() 매서드를 사용해 매치된 내용을 반환

def DefRefinder(pattern, script):           # DefRefinder라는 함수를 정의
    if re.match(pattern, script):           # 원고(Script)에서 패턴을 찾을 수 있는지 확인
        print('Match!')                     # 패턴을 찾았다면, Match 출력
    else:
        print('Not a Match!')               # 패턴을 찾지 못했다면, Not a Match를 추력

pattern = r'Life'
script ='Life is so cool'
DefRefinder(pattern, script)

pattern = r'life'
script ='Life is so cool'
DefRefinder(pattern, script)

# findall 매서드
# re.findall(패턴, 찾으려는 문자열)
number = 'My Number is 511223-1****** and yours is 521012-2******'
result = re.findall('\d{6}', number)        # \d{6} 패턴은 숫자를 6번 반복한 값을 의미
print('Number >>> ', result)

# 정규표현식의 탐욕 제어하기: 마침표(.)와 물음표(?)
example = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년입니다.'
result = re.findall(r'\d.+년', example)
print(result)

result = re.findall(r'\d.+?년', example)
print(result)

result = re.findall(r'\d+년', example)
print(result)


example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018).'
result = re.findall(r'\(.+\)', example)
print('result = ', result)

result = re.findall(r'\(.+?\)', example)
print('result = ', result)

# split 매서드 - 문장 나누는 패턴 만들기
# Split는 특정한 패턴이 등장할 떼 문자열을 나눕며 사용. 
# re.split(패턴, 문자열)

strSentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
print(re.split(r'[.?!]', strSentence))
# >>> ['I have a lovely dog, really', ' I am not telling a lie', ' What a pretty dog', ' I love this dog', '']

strData = 'a:3; b:4; c:5'
for i in re.split(r';', strData):
    print(re.split(r':', i))
# >>> ['a', '3']
# >>> [' b', '4']
# >>> [' c', '5']


