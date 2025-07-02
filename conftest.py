from time import sleep

import pytest
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def set_up():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    yield driver
    sleep(1.5)
    driver.quit()


