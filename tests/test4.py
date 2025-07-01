from itertools import count
from time import sleep

import allure

from pages.homepage import Homepage
from pages.itempage import Itempage




@allure.suite("item search")
def test_test4(set_up):
    driver = set_up
    page = Itempage(driver)

    Homepage(driver).get_homepage()
    Homepage(driver).get_search_bar().send_keys("arcane energize")
    Homepage(driver).get_search_button().click()
    sleep(0.5)
    page.maxprice().send_keys("40")


    sleep(1)
    page.scroll_down(50)
    sleep(2)
    page.listing_count()

    count_assert = page.listing_count()

    assert count_assert >= 20
