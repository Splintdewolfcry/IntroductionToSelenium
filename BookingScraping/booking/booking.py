from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC3
import os
from seleniumwire import webdriver


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"C:/SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] = self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.install_addon(r"C:\SeleniumDrivers\ublock_origin-1.50.0.xpi")
        
    def land_first_page(self):
        BASE_URL="https://www.booking.com/"
        self.get(BASE_URL)

    def wait_until_popup(self):
        self.implicitly_wait(15)
        try:
            self.find_element(By.CSS_SELECTOR, \
                "button[class='fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 ae1678b153']")\
                    .click()
        except Exception:
            pass
        except:
            self.find_element(By.XPATH, '//div[@aria-label="Kapat"]').click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':Ra9:')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR, 'li[class="a80e7dc237"]')
        first_result.click()

    def select_acomm_dates(self, check_in, check_out):
        check_in = self.find_element(By.CSS_SELECTOR, 
        f'td[data-date="{check_in}"]').click()
        checkout_out = self.find_element(By.CSS_SELECTOR, 
        f'td[data-date="{check_out}"]').click()
    

