import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'


# case 4.1
def test_positive_order():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item and add it to cart:
    browser.find_element('xpath', '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(2)

    # go to cart:
    browser.find_element('xpath', '//a[@data-test="shopping-cart-link"]').click()
    time.sleep(2)

    # go to checkout:
    browser.find_element('xpath', '//button[@data-test="checkout"]').click()
    time.sleep(2)

    # fill a form:
    browser.find_element('xpath', '//input[@data-test="firstName"]').send_keys('Jane')
    browser.find_element('xpath', '//input[@data-test="lastName"]').send_keys('Smith')
    browser.find_element('xpath', '//input[@data-test="postalCode"]').send_keys('123456')

    # click 'continue' button:
    browser.find_element('xpath', '//input[@id="continue"]').click()
    time.sleep(2)

    # click 'finish' button:
    browser.find_element('xpath', '//button[@id="finish"]').click()
    time.sleep(2)

    # check url and success message:
    curr_url = browser.current_url
    success_msg = browser.find_element('xpath', '//h2[@data-test="complete-header"]').text

    assert curr_url == 'https://www.saucedemo.com/checkout-complete.html'
    assert success_msg == 'Thank you for your order!'
    time.sleep(2)
