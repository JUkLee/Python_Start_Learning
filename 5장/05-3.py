import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import usercsv, Learning
import numpy as np  # 먼저 넘파이를 임포트합니다.

discount = .05      # 할인율은 5%입니다.
cashflow = 100      # 현금 흐름은 100(억 원)입니다.

def presentvalue(n):
    return (cashflow / (1 + discount) ** n)
# 자본의 현재 가치를 구하는 공식을 함수로 만듭니다.

print(presentvalue(1))
# 95.23809523809524
print(presentvalue(2))
# 90.70294784580499
