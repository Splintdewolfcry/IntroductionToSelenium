# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC3
import os
from selenium import webdriver


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"C:/SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] = self.driver_path
        super(Booking, self).__init__()
        
    # def const_url(self, BASE_URL="https://www.booking.com/"):
    #     BASE_URL = self.BASE_URL

    def land_first_page(self):
        BASE_URL="https://www.booking.com/"
        self.get(BASE_URL)

# booking = Booking()
# with booking as bot:
    # bot.land_first_page()
    

