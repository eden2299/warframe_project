from time import sleep

import allure

from pages.base import Base
from pages.page5 import Page5



@allure.suite("sign in")
def test_sign_in(set_up):
    driver = set_up
    basic = Base(driver)
    page = Page5(driver)
    basic.get_homepage()
    page.get_sign_in().click()

    assert "Sign In" in driver.title