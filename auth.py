from selenium import webdriver
import pytest
import time

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
success_url = 'https://www.saucedemo.com/checkout-complete.html'
cart_url = 'https://www.saucedemo.com/cart.html'
about_url = 'https://saucelabs.com/'


@pytest.fixture(scope='session')
def standard_auth():
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(3)
    yield standard_auth
