from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class Page4:
    def __init__(self, driver):
        self.driver = driver

    def listing_count(self):
        listings = self.driver.find_elements(By.XPATH, "//div[@data-test-id='virtuoso-item-list']/div")
        last_listing = listings[-1]
        count_str = last_listing.get_attribute("data-index")
        count = int(count_str)
        print(f"Number of listings: {count}")
        return count


    def align_bottom_of_page(self):

        statistics_button = self.driver.find_element(By.XPATH, "//span[text()='Statistics']")
        orders_button = self.driver.find_element(By.XPATH, "//span[text()='Orders']")

        statistics_button.click()
        orders_button.click()


