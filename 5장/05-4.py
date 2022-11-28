import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import Learning, usercsv
import numpy as np

loss = [-750, -250]
# 1, 2년 차에 발생한 비용입니다.
profit = [100] * 18
print(profit)
# [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
cf = loss + profit
print(cf)
# [-750, -250, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
# 총 20년 동안 현금 흐름을 리스트로 만들어 cf에 저장했습니다.
len(cf)
# 20
# 총 20개의 정보가 있음을 확인했습니다.
cashflow = np.array(cf)
# 이제 cf를 배열로 만들어 cashflow에 저장합니다.

npv = np.npv(0.045, cashflow)

