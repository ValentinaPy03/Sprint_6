from curl import *
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions

@pytest.fixture(scope='function')
def driver():
    options = FireFoxOptions()
    options.add_argument("--windows-size=1200, 600")
    driver = webdriver.Firefox(options=options)
    driver.get(main_page)
    yield driver
    driver.quit()
