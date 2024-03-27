from selenium import webdriver
import time

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'


# case 1.1
# standard auth:
def test_standart_login():
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()

    time.sleep(2)
    assert browser.current_url == inventory_url, 'Wrong url'


# case 1.2
def test_auth_positive_locked_out_user():
    browser.get(url)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('locked_out_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    time.sleep(2)

    err_msg1 = browser.find_element('xpath', '//*[@id="login_button_container"]//h3')
    assert err_msg1.text == 'Epic sadface: Sorry, this user has been locked out.'
    assert browser.current_url == url, 'Wrong url'
    time.sleep(2)


# case 1.3
def test_auth_positive_problem_user():
    browser.get(url)
    time.sleep(2)

    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('problem_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    time.sleep(5)

    assert browser.current_url == inventory_url, 'Wrong url'
    time.sleep(2)


# case 1.4
def test_auth_positive_performance_glitch_user():
    browser.get(url)
    time.sleep(2)

    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('performance_glitch_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    time.sleep(5)

    assert browser.current_url == inventory_url, 'Wrong url'
    time.sleep(5)


# case 1.5
def test_auth_negative_wrong_login():
    browser.get(url)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('user')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    time.sleep(2)

    err_msg2 = browser.find_element('xpath', '//*[@id="login_button_container"]//h3')
    assert err_msg2.text == 'Epic sadface: Username and password do not match any user in this service'
    assert browser.current_url == url, 'Wrong url'
    time.sleep(2)
