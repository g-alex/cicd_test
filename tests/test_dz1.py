from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_title(browser):
    browser.get('https://www.saucedemo.com')
    browser_title = browser.title
    print(browser_title)
    assert("Swag Labs" in browser_title)