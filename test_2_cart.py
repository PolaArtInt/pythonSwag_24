import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'


# case 2.1
def test_add_to_cart():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item text:
    pick_item = browser.find_element('xpath', '//div[contains(text(), "Sauce Labs Backpack")]').text

    # add item to cart:
    browser.find_element('css selector', 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # go to cart:
    browser.find_element('css selector', 'a[class ="shopping_cart_link"]').click()

    # check if item picked is the same item in cart:
    check_item_picked = browser.find_element('xpath',
                                             '//a[@id="item_4_title_link"]/div[@class="inventory_item_name"]').text

    assert pick_item == check_item_picked

    # remove item from cart:
    browser.find_element('xpath', '//button[@id="remove-sauce-labs-backpack"]').click()


# case 2.2
def test_remove_from_cart():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item and add it to cart:
    browser.find_element('xpath', '//a[@id="item_3_title_link"]')
    browser.find_element('xpath', '//button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    time.sleep(2)

    # go to cart:
    browser.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
    time.sleep(3)

    # items quantity in cart:
    cart_tag_before = browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_tag_before == '1'
    time.sleep(3)

    # remove item from cart:
    browser.find_element('xpath', '//button[@class="btn btn_secondary btn_small cart_button"]').click()
    time.sleep(3)

    # check if cart icon has child element (quantity tag):
    is_cart_link_empty = browser.find_element('css selector', 'a[class="shopping_cart_link"]:empty')
    assert bool(is_cart_link_empty) == True
    time.sleep(3)


def test_click_on_cart_btn():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # go to cart:
    browser.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
    time.sleep(3)

    # check if current url is cart url:
    assert browser.current_url == cart_url, 'Wrong url'

