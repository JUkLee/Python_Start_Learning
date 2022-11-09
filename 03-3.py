# 03-3 드라마 대본 텍스트 파일 가공하기
import os, re

strFileName = 'friends101.txt'

# friends101.txt 파일이 있는 폴더로 이동
path = os.getcwd() + r'\Learning_Data'
os.chdir(path)
# 폴더 위치 확인
print(os.getcwd())

# File open
fScript = open(strFileName, 'r', encoding = 'utf8')

# File read
strScript = fScript.read()
print(strScript[:100])
# >>> Written by: Marta Kauffman & 

# File Close
fScript.close()

# 특정 등장인물의 대사만 모으기
# 'Monica: ' 의 대사만 모으기
print('\'Monica\' 의 대사만 모으기')
strLine = re.findall(r'Monica:.+', strScript)   # '.+' 다음 아무 문자나 반복되는 패턴
print(strLine[:3])
# >>> ["Monica: There's nothing to tell! He's just some guy I work with!", 
# "Monica: Okay, everybody relax. This is not even a date. It's just two people going out to dinner and- not having sex.", 
# "Monica: And they weren't looking at you before?!"]
for item in strLine[:3]:
    print(item)

monica = ''
fMonica = open('monica.txt', 'w', encoding = 'utf8')
for line in strLine:
    monica += (line + '\n')
result = fMonica.write(monica)
fMonica.close()

# 등장인물 리스트 만들기
print('등장인물 리스트 만들기')
char = re.compile(r'[A-Z][a-z]+:')
AlllistCharScript = re.findall(char, strScript)
#print(AlllistCharScript)
listCharScript = set(AlllistCharScript)   # 중복된 이름 하나만 나오도록 수정
#print(listCharScript)
listChar = []
for strChar in listCharScript:
    #re.sub(':', '', charter)
    listChar += [strChar[:-1]]
print(listChar)

# 한줄로 작성하기
print('한줄로 작성하기')
listChar = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', strScript)))]
print(listChar)

# 지문만 출력하기
print('지문만 출력하기')
pattern = r'\([A-Za-z].+?[a-z|\.]\)'
directive = re.findall(pattern, strScript)
print(directive[:6])

# 파일에서 줄단위로 읽어 list로 만들기
print('파일에서 줄단위로 읽어 list로 만들기')
fFile = open(strFileName, 'r')
sentences = fFile.readlines()   # 파일 객체 안에 모든 문장을 원소로 하는 리스트를 만듬
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)
# 한줄로 표현
print('한줄로 표현')
line = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
print(line[:10])

# 특정 단어의 예문만 모아 파일로 저장하기
print('특정 단어의 예문만 모아 파일로 저장하기')
# would 가 들어간 예문
print('would 가 들어간 예문')
world = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(world)

# take 가 들어간 예문 파일로 저장하기
print('take 가 들어간 예문 파일로 저장하기')
take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
fTake = open('take.txt', 'w')
fTake.writelines(take)
fTake.close()


