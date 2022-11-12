# 4장 4~

# 04-4 CSV 파일 데이터 분석
print('# 04-4 CSV 파일 데이터 분석')

# Do it 외국인 비율이 3% 넘는 구 정보만 CSV 파일로 저장하기
print('# Do it 외국인 비율이 3% 넘는 구 정보만 CSV 파일로 저장하기')

import os, re
from Function import Learning, usercsv

# CSV 파일을 읽을 수 있도록 Directory 이동
path = Learning.MoveLearningDataDir()
# CSV 파일 open
fileName = 'popSeoul.csv'
total = usercsv.opencsv(fileName)

# File Data List화
newPop = usercsv.switch(total)
# 확인 print(newPop[:4])

# 첫 행 지정하기
new = [['구', '한국인', '외국인', '외국인 비율(%)']]

# 등록외국인 비율 계산하기
# 게산 : i[2]/(i[1] + i[2]) * 100
# i = newPop[1];  foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass

# CSV 파일 저장하기
usercsv.writecsv('newPop.csv', new)


