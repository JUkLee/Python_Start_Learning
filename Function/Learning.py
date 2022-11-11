# Learning Function 
import os

def MoveDefaultDir():
    defulatPath = 'C:\\000_002_Python\\01_Start'
    os.chdir(defulatPath)
    return os.getcwd()

def MoveLearningDataDir():
    path = os.getcwd()
    comparePath = 'C:\\000_002_Python\\01_Start\\Learning_Data'
    if path != comparePath:
        os.chdir(comparePath)
    return os.getcwd()
