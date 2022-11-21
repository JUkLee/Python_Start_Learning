#4장 1~3

import os, re, sys, csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname((__file__)))))      # 같은 Level의 폴더에서 import 하고 싶다면...

# CSV 데이터 알아보기
import os, csv
dataPath = r'\Learning_Data'
path = os.getcwd() + dataPath
os.chdir(path)
filepath = 'new_1.csv'

# 기존 파일 Open
print('# 기존 파일 Open')
fCSV = open(filepath, 'r')
fileData = fCSV.read()

# CSV 파일 Open
print('# CSV 파일 Open')
fCSV.seek(0)
fNew = csv.reader(fCSV)
print(fNew)
for i in fNew:
    print(i)

# csv형 List
print('# csv형 List')
fCSV.seek(0)
a_list = []
for i in fNew:
    print(i)
    a_list.append(i)
print(a_list)

fCSV.close()

# Function 만들어서 사용
def opencsv(fileName):
    f = open(fileName, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

# CSV 파일 만들기
print('# CSV 파일 만들기')
a = [['구', '전체', '내국인', '외국인'], 
['관악구', '519864', '502089', '177775'], 
['강남구', '547602', '542498', '5104'], 
['송파구', '686181', '679247', '6934'], 
['강동구', '428547', '424235', '4312']
]

f = open('abc.csv', 'w', newline = '')
csvobject = csv.writer(f, delimiter = ',')
csvobject.writerows(a)
f.close()

# CSV write function 만들기
def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        csvobject = csv.writer(f, delimiter = ',')
        csvobject.writerows(the_list)
    
# usercsv 모듈을 만들고
print('# usercsv 모듈을 만들고')
from Function import usercsv
a = [['국어', '영어', '수학'], ['99', '88', '77']]
usercsv.writecsv('test.csv', a)

# CSV 파일 안에 문자를 숫자로 전환하기
print('# CSV 파일 안에 문자를 숫자로 전환하기')
import os, re
from Function import usercsv, Learning

path = Learning.MoveLearningDataDir()
total = usercsv.opencsv('popSeoul.csv')
for i in total:
    print(i)

# 문자형 자료를 숫자형으로 바꾸기
print('# 문자형 자료를 숫자형으로 바꾸기')
i = '123'
print('float() 함수로 바꾸기 -> ' + str(float(i)))
print('int() 함수로 바꾸기 -> ' + str(int(i)))

# print(str(float('1,468,146'))) # 쉼표로 인하여 문제가 발행

j = '1,468,146'
subj = float(re.sub(',', '', j))
print('쉼표를 제거하고 float() 함수로 바꾸기 -> ' + str(subj))
print('그 type -> ' + str(type(subj)))

# 숫자 원소만 골라서 쉽표(,) 제거
print('# 숫자 원소만 골라서 쉽표(,) 제거')
import re
i = total[2]
k = []
for j in i:
    if re.search('\d', j):
        k.append(float(re.sub(',', '', j)))
    else:
        k.append(j)

print(k)

# 문자와 숫자가 섞인 원소 고르기
print('# 문자와 숫자가 섞인 원소 고르기')
p = ['123가나다', '123,456', '456,789', '27,123']
k = []
for j in p:
    if re.search(r'[a-z가-힣]', j):
        k.append(j)
    else:
        k.append(float(re.sub(',', '', j)))
print(k)

# 특수문자와 숫자가 섞인 원소 골라내기
print('# 특수문자와 숫자가 섞인 원소 골라내기')
i = ['123!!', '123,456', '456,789', '27,123']
k = []
for j in i:
    if re.search(r'[0-9가-힣!]', j):
        k.append(j)
    else:
        k.append(float(re.sub(',', '', j)))
print(k)

# 본래 list를 활용
print('# 본래 list를 활용')
i = ['123!!', '123,456', '456,789', '27,123']
for j in i:
    if re.search(r'[0-9가-힣!]', j):
        i[i.index(j)] = j
    else:
        i[i.index(j)] = float(re.sub(',', '', j))
print(i)

# 예외 처리로 오류 넘어가기
print('# 예외 처리로 오류 넘어가기')
i = ['123!!', '123,456', '456,789', '27,123', '', '!!!$%']  # i에 특수문자와 빈 문자열로 된 원소를 추가하여 에러가 나오도록 수정된 list
for j in i:
    try:
        i[i.index(j)] = j   # 모든 j를 실수행으로 변경
    except:                 # 오류가 발생했다면
        pass                # pass를 실행해 넘어가도록 
print(i)

# 예외 처리로 숫자만 골라서 숫자형으로 바꾸기
print('# 예외 처리로 숫자만 골라서 숫자형으로 바꾸기')
for i in total:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',', '', j))
        except:
            pass
print(total)

