import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC3

os.environ['PATH'] = r"C:/SeleniumDrivers"

with webdriver.Firefox() as driver:    
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'password')

    username.send_keys('tomsmith')
    password.send_keys('SuperSecretPassword')

    driver.find_elements(By.CSS_SELECTOR, 'li.post-item:nth-child(2) > div:nth-child(4) > figure:nth-child(1)')