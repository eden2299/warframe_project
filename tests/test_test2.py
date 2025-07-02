from time import sleep
import allure
from pages.base import Base





@allure.suite("item search")
def test_test2(set_up):
    driver = set_up
    basic=Base(driver)

    basic.get_homepage()
    basic.get_search_bar().send_keys("a")
    basic.get_search_button().click()
    sleep(1)

    assert "Abating Link" in driver.title