# 번역한 예문을 표로 저장하기

# 시작하기 앞서 PIP를 이용해서 구글 번역 설치하기
# 1. cmd 에서 C:\users\pc>pip install googletrans
# 2. 설치

# 프로그램 작동 순서
# 1. 영어 원문을 번역
# 2. 각각 korean과 English 라는 객체를 만들어 저장
# 3. re.split()함수를 사용해 '마침표(.)'로 문장을 구분해 리스트로 저장
# 4. CSV 형 리스트를 저장할 빈 리스트 객체를 만듬
# 5. 영어 문장 하나, 한국어 문장 하나를 각각 리스트로 만들어서 빈 리스트에 추가
# 6. usercsv 모듈의 writecsv()함수를 활용해 CSV 파일로 저장

import re, os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import usercsv, Learning

English = 'She is a vegetarian. She does not est meat. She thinks that animals should not be killed. It is hard for her to hang out with people. Many people like to est meat. She told his parents nt to have meat. They laughed at her. She realized they couldn\'t give up meat.'

Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물들을 죽이지 말아야 한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃습니다. 그녀는 그들이 포기할 수 없다는 것을 깨달았습니다.'

path = Learning.MoveLearningDataDir()

# split 함수를 사용하여 문장을 나눠서 list화
Korean_List = re.split('\.', Korean)
English_list = re.split('\.', English)

# 확인
print(Korean_List)

total = []
for i in range(len(English_list)):
    # list 객체에 들어 있는 수량 만큼 loop
    total.append([English_list[i], Korean_List[i]])

usercsv.writecsv('Korean_English.csv', total)

from googletrans import Translator 

translator = Translator()
print(translator)

Kroean_tr = translator.translate(English, 'ko').text
print(Kroean_tr)
