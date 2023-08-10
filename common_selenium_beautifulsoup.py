# pip install --upgrade pip
# pip install selenium
# pip install beautifulsoup4 
# pip install requests


import pandas as pd
from bs4 import BeautifulSoup     
import json, requests , shutil, os
import urllib.request
 

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time




def first_bs4(url, headers):
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')        

    else : 
        print(response.status_code)

    return soup
