from time import sleep

import allure

from pages.base import Base
from pages.page4 import Page4




@allure.suite("listing count confirmation")
def test_test4(set_up):
    driver = set_up
    page = Page4(driver)
    basic = Base(driver)

    basic.get_homepage()
    basic.get_search_bar().send_keys("arcane energize")
    basic.get_search_button().click()
    sleep(0.5)
    basic.maxprice().send_keys("8")
    page.align_bottom_of_page()


    sleep(0.5)
    basic.scroll_to_bottom()
    count_assert = page.listing_count()
    assert count_assert >= 2000
