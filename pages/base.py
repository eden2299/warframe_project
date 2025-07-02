from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver):
        self.driver = driver
    def get_homepage(self):
        return self.driver.get("https://warframe.market/")

    def get_search_bar(self):
        return self.driver.find_element(By.XPATH, "//input[@type='text']")

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, "//button[@class='btn btn__primary--L8HyD bfs--PcQ_p']")

    def maxprice(self):
        return self.driver.find_element(By.XPATH, "//h5[text()='Min Price']/following::input[@type='number']")






    def scroll_to_bottom(self):
        bottom = self.driver.find_element(By.XPATH, "//h3[text()='Total Online']")
        actions = ActionChains(self.driver)
        actions.move_to_element(bottom).perform()














