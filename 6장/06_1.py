import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Function import usercsv, Learning
import numpy as np 
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com'
html = ur.urlopen(url)
