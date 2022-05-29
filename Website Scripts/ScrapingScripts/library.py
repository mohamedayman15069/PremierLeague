import time
from click import option
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import numpy as np




# #Add the not working Links
# playerLinkSet.add('https://www.premierleague.com/players/114256/Shaqai-Forde/overview')
# playerLinkSet.add('https://www.premierleague.com/players/35741/Tony-Springett/overview')
# playerLinkSet.add('https://www.premierleague.com/players/49193/Bojan-Radulovi&#263;/overview')
# playerLinkSet.add('https://www.premierleague.com/players/88771/Wanya-Madavidua/overview')
# playerLinkSet.add('https://www.premierleague.com/players/64074/Jan-Zamb&#367;rek/overview')
# playerLinkSet.add('https://www.premierleague.com/players/66108/Nathaniel-Shio-Hong-Wan/overview')
# playerLinkSet.add('https://www.premierleague.com/players/66590/Abu-Kamara/overview')

# playerLinkSet.add('https://www.premierleague.com/players/35733/Matej-Kov%C3%A1&#345;/overview')

def load_csvFile(path):
    DF = pd.read_csv(path, index_col=0)
    return DF

def openBrowser(url, path):
    # open the browser
    Path = '/usr/bin/chromedriver' 
    driver = webdriver.Chrome(Path)
    driver.get(url)
    time.sleep(5)
    accept_cookies = driver.find_element(By.XPATH,path)
    accept_cookies.click()
    return driver

Season = {0: "2021/22",
          1: "2020/21",
          2: "2019/20",
          3: "2018/19" 
        }
