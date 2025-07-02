from time import sleep

import allure

from pages.homepage import Homepage
from pages.itempage import Itempage




@allure.suite("listing count confirmation")
def test_test4(set_up):
    driver = set_up
    page = Itempage(driver)
    home = Homepage(driver)

    home.get_homepage()
    home.get_search_bar().send_keys("arcane energize")
    home.get_search_button().click()
    sleep(0.5)
    page.maxprice().send_keys("8")
    page.align_bottom_of_page()


    sleep(0.5)
    page.scroll_to_bottom()
    count_assert = page.listing_count()
    assert count_assert >= 2000
