import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'


# case 2.1
def test_add_to_cart():
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    pick_item = browser.find_element('xpath', '//div[contains(text(), "Sauce Labs Backpack")]').text

    add_to_cart_btn = browser.find_element('css selector', 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_btn.click()

    shoping_cart_link = browser.find_element('css selector', 'a[class ="shopping_cart_link"]')
    shoping_cart_link.click()

    check_item_picked = browser.find_element('xpath',
                                             '//a[@id="item_4_title_link"]/div[@class="inventory_item_name"]').text

    assert pick_item == check_item_picked

    browser.quit()


# case 2.2
def test_remove_from_cart():
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # выбор товара и добавление выбранного в корзину:
    browser.find_element('xpath', '//a[@id="item_3_title_link"]')
    browser.find_element('xpath', '//button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    time.sleep(2)

    # переход в корзину:
    browser.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
    time.sleep(3)

    # фиксация количества товаров в корзине до удаления:
    cart_tag_before = browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_tag_before == '1'
    time.sleep(3)

    # удаление товара из корзины:
    browser.find_element('xpath', '//button[@class="btn btn_secondary btn_small cart_button"]').click()
    time.sleep(3)

    # проверка отсутствия дочернего элемента в ссылке корзины:
    is_cart_link_empty = browser.find_element('css selector', 'a[class="shopping_cart_link"]:empty')
    assert bool(is_cart_link_empty) == True
    time.sleep(3)

    browser.quit()


def test_click_on_cart_btn():
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)
    browser.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
    time.sleep(3)
    assert browser.current_url == cart_url, 'Wrong url'

