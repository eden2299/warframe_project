from time import sleep

import allure

from pages.base import Base


@allure.suite("item search")
def test_test1(set_up):
    driver = set_up
    basic = Base(driver)


    basic.get_homepage()
    basic.get_search_bar().send_keys("soma prime set")
    basic.get_search_button().click()
    sleep(0.5)

    assert "Soma Prime Set" in driver.title









