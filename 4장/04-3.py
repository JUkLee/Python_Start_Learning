import sys, os, re
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import usercsv, Learning

# 부동산 실거래가 살펴보기
fileName = 'apt_202211.csv'
path = Learning.MoveLearningDataDir()               # 실거래가 정보 파일을 저장한 폴더로 이동
apt = usercsv.switch(usercsv.opencsv(fileName, 15)) # 앞에서 만들어둔 usercsv 기능을 사용
# 먼저 opencsv() 함수로 CSV형 리스트를 불러오고 switch()함수를 사용

# print(apt[:3])    #확인
#print(len(apt))    # 아파트 거래가 15,230 건이 있음 + 1 항목

# 자료 구조 확인
print('# 자료 구조 확인')
print(apt[0])

# 시군구에 해당하는 값(6항목에서 확인)
print('# 시군구에 해당하는 값(6항목에서 확인)')
for i in apt[:6]:
    print(i[0])

# 시군구, 아파트 단지명, 거래 금액(만원)을 표기
print('# 시군구, 아파트 단지명, 거래 금액(만원)을 표기')
for i in apt[:6]:
    print(i[0], i[4], i[-7])

# 강원도에 120㎥ 이상 3억 원 이하 아파트 검색하기
print('# 강원도에 120㎥ 이상 3억 원 이하 아파트 검색하기')
for i in apt:
    try:
        # 오류가 날 경우를 대비해 예외 처리를 사용
        # 전용면적 i[6] 120 이상, 가격 i[-7] 3억 이하, 시군구 i[0]에서 '강원'을 포함하는 조건
        if i[6] >= 120 and i[-7] <= 30000 and re.match('강원', i[0]):
            # 시군구, 아파트 단지명, 가격 출력
            print(i[0], i[4], i[-7])
    except: pass

# 분석 결과를 CSV 파일로 저장
print('# 분석 결과를 CSV 파일로 저장')
# 빈 리스트를 만드는 것이 CSV 형 리스트를 만드는 첫걸음이라고 함...
new_list = [['시군구','단지명','가격(만)']]

for i in apt:
    try:
        if i[6] >= 120 and i[-7] <= 30000 and re.match('강원', i[0]):
            new_list.append([i[0], i[4], i[-7]])
    except: pass

usercsv.writecsv('over120_lower30000.csv', new_list)












