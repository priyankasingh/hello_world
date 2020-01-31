from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

import pyautogui as pg 

print(pg.size()) 


usernameStr = '***'
passwordStr = '***'

driver = webdriver.Firefox()
#driver = webdriver.Chrome('./chromedriver')
driver.get('https://my.tomorrowland.com/')

wait = WebDriverWait(driver, 10)

elem = wait.until(
    EC.presence_of_element_located((By.NAME, "username"))
    )
elem.clear()
elem.send_keys(usernameStr)

sleep(3)
pg.click(740,590, duration=1)

sleep(3)
pg.typewrite(passwordStr)

sleep(3)
pg.click(900,680, duration=1)

sleep(10)
pg.scroll(-5)

pg.position()

sleep(2)
pg.click(900,680, duration=1)

# password = wait.until(
#     EC.visibility_of_element_located((By.NAME, 'password')))
# password.clear()   
# password.send_keys(passwordStr)

 
# signInButton = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))
# signInButton.click()

# driver.close()

#https://cdn.flxml.eu/lt-2166510556-e631fc3c7166e95fb079e53e8e0a721fd0f86338ffa4d17c
#https://cdn.flxml.eu/lt-2166510556-0da8e3f123900d319cbfb65d42f3e0ccd0f86338ffa4d17c 
