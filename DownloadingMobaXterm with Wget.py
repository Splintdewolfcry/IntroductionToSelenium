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

    driver.get("https://mobaxterm.mobatek.net/download-home-edition.html")
    wait = WebDriverWait(driver, 10)
    downbutton = driver.find_element(By.CLASS_NAME, "btn_vert")
    # print(downbutton)
    download_link = downbutton.get_attribute('href')
    file_download = wget.download(f'{download_link}')


    # eg_link = "https://github.com/tqdm/tqdm/releases/download/v4.46.0/tqdm-4.46.0-py2.py3-none-any.whl"
    # eg_file = eg_link.split('/')[-1]

    # downbutton.send_keys(Keys.CONTROL, 'j')


