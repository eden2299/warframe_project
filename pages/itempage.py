from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Itempage:
    def __init__(self, driver):
        self.driver = driver


    def maxprice(self):
        return self.driver.find_element(By.XPATH, "/html/body/section/section/div/section[2]/div[2]/div[2]/div/div[3]/div[1]/input")






    def scroll_to_bottom(self):
        bottom = self.driver.find_element(By.XPATH, "/html/body/section/section/div/footer/div[2]/div[2]/div[1]/div[1]/h3")
        actions = ActionChains(self.driver)
        actions.move_to_element(bottom).perform()




    def wait_for_element(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "listing-item")))





    def listing_count(self):

        listings = self.driver.find_elements(By.XPATH, "/html/body/section/section/div/section[2]/div[3]/div[2]/div[2]/div/div/div")
        last_listing = listings[-1]
        count_str = last_listing.get_attribute("data-index")
        count = int (count_str)
        print(f"Number of listings: {count}")
        return count


    def align_bottom_of_page(self):

        statistics_button = self.driver.find_element(By.XPATH, "/html/body/section/section/div/section[2]/div[1]/div[2]/div[2]/ul/li[2]/a")
        orders_button = self.driver.find_element(By.XPATH, "/html/body/section/section/div/section[2]/div[1]/div[2]/div[2]/ul/li[1]/a")

        statistics_button.click()
        orders_button.click()







