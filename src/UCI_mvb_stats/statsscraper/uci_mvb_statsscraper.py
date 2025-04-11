from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

cService = webdriver.ChromeService(executable_path='C:/Users/ashle/OneDrive/Documents/chromedriver-v35.1.4-win32-arm64/chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get('https://ucirvinesports.com/sports/mens-volleyball/roster/shane-aitken/7170/')

# switching to stats tab
tab = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/div[4]/ul/li[3]')
ActionChains(driver).click(tab).perform()

# buffer for page to laad
driver.implicitly_wait(1)

off_stats_raw = driver.find_elements(By.XPATH, '//*[@id="career-stats"]/div/section[1]/div/table')
def_stats_raw = driver.find_elements(By.XPATH, '//*[@id="career-stats"]/div/section[2]/div/table')

off_stats_raw_list = []
for i in range(len(off_stats_raw)):
    off_stats_raw_list.append(off_stats_raw[i].text)

def_stats_raw_list = []
for i in range(len(def_stats_raw)):
    def_stats_raw_list.append(def_stats_raw[i].text)

print(off_stats_raw_list)
print(def_stats_raw_list)