import os
import wget
from pprint import pprint
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] = r"C:/SeleniumDrivers"


# with webdriver.Firefox() as driver:    
#     driver.get("https://worldscinema.org/")
#     wait = WebDriverWait(driver, 15)
#     contents = driver.find_element(By.CLASS_NAME, 'container-wrapper').find_elements(By.TAG_NAME, 'div')
    
#     # with open('output.txt', 'w+') as f:
#     #     text = contents.text
#     #     f.writelines(text + '\n')

#     # print('\n'.join(contents))
#     # pprint(contents.get_attribute('p'))

#     with open('output.txt', 'w+') as f:
#         for content in contents:
#             print(type(content))
#             text = content.text
#             f.writelines(text + '\n')

with webdriver.Firefox() as driver:    
    driver.get("https://worldscinema.org/")
    wait = WebDriverWait(driver, 15)
    contents = driver.find_element(By.CLASS_NAME, 'container-wrapper').find_elements(By.CSS_SELECTOR, "h2[class='post-title']")
    
    # print(contents.text) # For when you are looking for `a` element
    
    with open('output.txt', 'w+') as f:
        for content in contents:
            print(type(content))
            text = content.text
            f.writelines(text + '\n')


# .find_elements(By.TAG_NAME, 'br')

# Understanding HTML context could be better and my lack of python proficency
# is starting to show itself, need to get better in python, doing quite good on
# both ends so far(udemy and selenium)