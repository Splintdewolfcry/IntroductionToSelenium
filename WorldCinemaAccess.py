import os
import wget
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] = r"C:/SeleniumDrivers"

with webdriver.Firefox() as driver:
    driver.get("https://worldscinema.org/")
    wait = WebDriverWait(driver, 15)
    content = driver.find_elements(By.ID, 'posts-container')
    titles = content.find_elements(By.TAG_NAME, 'a')
    for title in titles:
        href = title.get_attribute('href')
        if href is not None:
            print(href)
