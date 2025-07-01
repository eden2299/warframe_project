from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Itempage:
    def __init__(self, driver):
        self.driver = driver


    def maxprice(self):
        return self.driver.find_element(By.XPATH, "/html/body/section/section/div/section[2]/div[2]/div[2]/div/div[3]/div[1]/input")


    def scroll_down(self,times):
        body = self.driver.find_element(By.TAG_NAME, "body")
        for i in range(times):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(0.2)




    def listing_count(self):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section/section/div/section[2]/div[3]/div[2]/div[2]/div/div/div")))

        listings = self.driver.find_elements(By.XPATH, "/html/body/section/section/div/section[2]/div[3]/div[2]/div[2]/div/div/div")
        last_listing = listings[-1]
        count_str = last_listing.get_attribute("data-index")
        count = int (count_str)
        print(f"Number of listings: {count}")
        return count










#    def listing_count(self):
 #       listings = self.driver.find_elements(By.XPATH, "/html/body/section/section/div/section[2]/div[3]/div[2]/div[2]/div/div/div")
 #       count = len(listings)
  #      print(f"Number of listings: {count}")
 #       return count
#
