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


def write_output(filename, returned_text):
    with open(filename, 'a+') as f:
        f.writelines(returned_text)

with webdriver.Firefox() as driver:    
    driver.get("https://worldscinema.org/")
    wait = WebDriverWait(driver, 15)
    # titles = driver.find_element(By.CLASS_NAME, 'container-wrapper').find_elements(By.CSS_SELECTOR, "h2[class='post-title']")
    description = driver.find_elements(By.TAG_NAME, 'p')

    if driver.find_element(By.CSS_SELECTOR, "src['@https://worldscinema.org']"):
        

 
    for item in description:
        description_list = []
        
        text = item.text
        description_list.append(text + '\n')
        write_output('quotes.txt', description_list)
        

# Enumerate the list
# And print out every item in the elements like this
# Slice the list until there is no readme at the end(easily with [:-7gibi]) and then zip these two lists
# And maybe create rss feed? something like pushbullet
# Get the imdb scores from imdb

# Understanding HTML context could be better and my lack of python proficency
# is starting to show itself, need to get better in python, doing quite good on
# both ends so far(udemy and selenium)