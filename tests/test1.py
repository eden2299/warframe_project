from time import sleep

from openpyxl.styles.builtins import title

from pages.homepage import Homepage


def test1(set_up):
    driver = set_up

    home = Homepage(driver)
    home.get_homepage()
    home.get_search_bar().send_keys("soma prime set")
    home.get_search_button().click()
    sleep(0.5)

    assert "Soma Prime Set" in driver.title








