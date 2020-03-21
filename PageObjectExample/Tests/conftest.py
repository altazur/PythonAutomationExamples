import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def get_driver():
    driver = webdriver.Firefox(executable_path="./driver/geckodriver")
    yield driver
    driver.quit()
