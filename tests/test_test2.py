from time import sleep

import allure

from pages.homepage import Homepage
from pages.itempage import Itempage




@allure.suite("item search")
def test_test2(set_up):
    driver = set_up

    Homepage(driver).get_homepage()
    Homepage(driver).get_search_bar().send_keys("a")
    Homepage(driver).get_search_button().click()
    sleep(0.5)