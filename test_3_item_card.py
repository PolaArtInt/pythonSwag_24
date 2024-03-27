import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'


# case 3.1
def test_click_on_item_img():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item description:
    item_desc1 = browser.find_element('xpath', '(//div[@class="inventory_item_desc"])[2]').text
    time.sleep(2)

    # pick item image and click:
    browser.find_element('xpath', '//a[@id="item_0_img_link"]/img').click()
    time.sleep(2)

    # check if url changed and we can get the same item:
    assert browser.current_url != url
    item_card_desc1 = browser.find_element('xpath', '//div[@data-test="inventory-item-desc"]').text
    assert item_desc1 == item_card_desc1
    time.sleep(2)


# case 3.2
def test_click_on_item_title():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item description:
    item_desc1 = browser.find_element('xpath', '(//div[@class="inventory_item_desc"])[3]').text
    time.sleep(2)

    # pick item title and click:
    browser.find_element('xpath', '//a[@id="item_1_title_link"]/div').click()
    time.sleep(2)

    # check if url changed and we can get the same item:
    assert browser.current_url != url
    item_card_desc1 = browser.find_element('xpath', '//div[@data-test="inventory-item-desc"]').text
    assert item_desc1 == item_card_desc1
    time.sleep(2)
