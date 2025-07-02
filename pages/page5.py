from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Page5:
    def __init__(self, driver):
        self.driver = driver

    def get_sign_in(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Sign In']")