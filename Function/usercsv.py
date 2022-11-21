import csv, os, re
# 새롭게 시작할 때 CSV 모듈을 먼저 임포트

# CSV Read Function
# @Func : opencsv() 함수에서는 f를 파일 객체로 해 직접 open 하는 방식을 사용
# @Retrun : File 객체
# @Parameter
#   - filenaem : (In) 파일 이름
def opencsv(fileName):
    f = open(fileName, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

# CSV Read Function Jump Line
# @Func : opencsv() 함수에서는 f를 파일 객체로 해 직접 open 하는 방식을 사용
# @Retrun : File 객체
# @Parameter
#   - filenaem : (In) 파일 이름
def opencsv(fileName, jumpLine):
    f = open(fileName, 'r')
    reader = csv.reader(f)
    output = []
    count = 0
    for i in reader:
        count += 1
        if count <= jumpLine:
            continue
        output.append(i)
    f.close()
    return output

# CSV write Function
# @Func : writecsv() 함수에서는 with 문을 사용해 코드 길이가 조금 더 짧아짐
# @Retrun : NULL
# @Parameter
#   - filenaem : (In) 파일 이름
#   - the_list : (In) List 객체
def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        csvobject = csv.writer(f, delimiter = ',')
        csvobject.writerows(the_list)

# list에서 숫자에서만 쉽표(,)를 제거
# @Func : 숫자의 쉼표(,)를 제거 하는 Function
# @Retrun : list에서 숫자에서만 쉽표(,)를 제거하고 반환
# @Parameter
#   - list : (in) 2중 list
def switch(list):
    for i in list:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return list

    
