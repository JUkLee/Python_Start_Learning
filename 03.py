# os 모듈을 임포트(import)
import os
print('os.getcwd() = ', os.getcwd())     # 현재 위치한 경로가 표시

# 폴더 이동
os.chdir('C:\\000_002_Python\\01_Start\\Test')
print('os.getcwd() = ', os.getcwd())