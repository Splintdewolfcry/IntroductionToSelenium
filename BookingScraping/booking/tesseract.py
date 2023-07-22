from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Firefox()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url = ob.full_screenshot(driver, save_path=r'.', image_name='myimage.png', is_load_at_runtime=True,
                                          load_wait_time=3)
print(img_url)
driver.close()

driver.quit()

# REMOVED CODE
   # def select_currency_button(self, currency=None):
    #     currency_element = self.find_element(By.CSS_SELECTOR,
    #     'button[data-testid="header-currency-picker-trigger"]'
    #     )
    #     currency_element.click()
        
        
    # def select_currency(self, currency=None):
    #     currency_element = self.find_element(By.CLASS_NAME, "e9768bbaf2")\
    #         .find_element(By.XPATH, "//*[contains(text(),'USD')]").click()
    #     print(currency_element.text)  

    #     selected_currency_element = self.find_element(By.CSS_SELECTOR, '')