import pandas as pd
# 넘파이를 임포트 할 때와 마찬가지로 pd라는 줄임말을 판다스를 임포트 합니다.
data = {	'name' : ['Mark', 'Jane', 'Chris', 'Ryan'],
				'age' : [33, 32, 44, 42],
				'score' : [91.3, 83.4, 77.5, 87.7]}
# 임의의 딕셔너리형 자료를 data 객체에 저장합니다.
df = pd.DataFrame(data)
# DataFrame() 함수로 data 객체를 데이터프레임으로 만들어 df 객체에 저장합니다.

print(df)
#     name  age  score
# 0   Mark   33   91.3
# 1   Jane   32   83.4
# 2  Chris   44   77.5
# 3   Ryan   42   87.7


