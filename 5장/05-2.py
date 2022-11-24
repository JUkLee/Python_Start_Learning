import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import usercsv, Learning
import numpy as np

fileName = 'quest.csv'
Learning.MoveLearningDataDir()                  # quest.csv를 저장한 경로로 이동
quest = np.array(usercsv.switch(usercsv.opencsv(fileName, 0)))
# quest.csv 파일을 열어 숫자 원소를 실수형으로 바꾼 다음 배열 형태로 quest 객체에 저장합니다.
quest
# array([[1., 2., 1., 2., 2.],                  # quest.csv 파일의 값이 배열로 잘 저장되었네요.
#       [1., 3., 2., 3., 2.],
#       [1., 4., 3., 3., 3.],
#       [2., 5., 4., 4., 4.],
#       [2., 5., 6., 2., 5.],
#       [3., 6., 4., 2., 5.],
#       [3., 5., 4., 1., 6.],
#       [3., 5., 5., 1., 3.]])
quest > 5                                       # 간단한 조건문을 입력해 볼까요?
# array([[False, False, False, False, False],   # 5보다 큰면 True, 작거나 같으면 False입니다.
#        [False, False, False, False, False],
#        [False, False, False, False, False],
#        [False, False, False, False, False],
#        [False, False,  True, False, False],
#        [False,  True, False, False, False],
#        [False, False, False, False,  True],
#        [False, False, False, False, False]])
quest[quest > 5]                                # 인덱싱을 활용해 5보다 큰 수만 가져옵니다.
# array([6., 6., 6.])
quest[quest > 5] = 5                            # 5보다 큰 숫자가 전부 5로 바꿉니다.
quest
# array([[1., 2., 1., 2., 2.],                  # 5보다 큰 숫자가 전부 5로 바뀌었네요
#        [1., 3., 2., 3., 2.],
#        [1., 4., 3., 3., 3.],
#        [2., 5., 4., 4., 4.],
#        [2., 5., 5., 2., 5.],
#        [3., 5., 4., 2., 5.],
#        [3., 5., 4., 1., 5.],
#        [3., 5., 5., 1., 3.]])
usercsv.writecsv('resultcsv.csv', list(quest))
# 결과물을 다시 'resultcsv.csv'라는 이름으로 저장