# # wait until we see a skill
# login_button = wait.until(
#     EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'I ALREADY HAVE AN ACCOUNT')]"))
# )

# # click the login button (it says "I ALREADY HAVE AN ACCOUNT")
# login_button.click()

from Screenshot import Screenshot
from selenium import webdriver

with webdriver.Firefox() as driver:    
    driver.get("https://www.skyscanner.com/transport/flights-from/ista/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=2307&iym=2307&qp_prevScreen=HOMEPAGE")
    driver.maximize_window()
    driver.implicitly_wait(15)
    ob = Screenshot.Screenshot()

    img_url = ob.full_screenshot(driver, save_path=r'.', image_name='myimage.png', is_load_at_runtime=True,
                                          load_wait_time=3)
    print(img_url)
