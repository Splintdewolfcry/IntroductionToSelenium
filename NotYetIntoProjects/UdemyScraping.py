import os
import wget
from pprint import pprint
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Screenshot import Screenshot

os.environ['PATH'] = r"C:/SeleniumDrivers"

link = "https://www.udemy.com/course/the-python-mega-course/"


with webdriver.Firefox() as driver:    
    driver.get(link)
    
    to_be_clicked_xpath = "//button[@data-purpose='expand-toggle']"
    toggling_expand = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, to_be_clicked_xpath)))
    toggling_expand.click()

    # section = driver.find_element(By.CLASS_NAME, 'section--row')
    # print(section)
    
    driver.maximize_window()
    driver.implicitly_wait(15)
    ob = Screenshot.Screenshot()

    img_url = ob.full_screenshot(driver, save_path=r'.', image_name='myimage.png', is_load_at_runtime=True,
                                          load_wait_time=3)
    print(img_url)


    