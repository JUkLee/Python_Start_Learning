import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import usercsv, Learning
import numpy as np 
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

# Selenuum 임포트
from selenium import webdriver as selen

driver = selen.Chrome()
#url = 'https://www.google.com'
#url = r'https://prod.danawa.com/list/?cate=112747'
url = r'https://news.daum.net/'
driver.get(url)
# 인터넷 창을 연다.

