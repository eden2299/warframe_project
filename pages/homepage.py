from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver):
        self.driver = driver
    def get_homepage(self):
        return self.driver.get("https://warframe.market/")

    def get_search_bar(self):
        return self.driver.find_element(By.XPATH, "//*[@id='panel']/section[1]/div[1]/section/section/div/section/span/input")

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, "html/body/section/section/div/section[1]/div[1]/section/section/button")

    def get_sign_in(self):
        return self.driver.find_element(By.XPATH, "/html/body/section/section/nav[1]/ul[2]/li[5]/a")













