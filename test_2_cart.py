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
    pick_item1 = browser.find_element('xpath', '//div[contains(text(), "Sauce Labs Backpack")]').text

    # add item to cart:
    browser.find_element('css selector', 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # go to cart:
    browser.find_element('css selector', 'a[class ="shopping_cart_link"]').click()

    # check if item picked is the same item in cart:
    check_item_picked1 = browser.find_element('xpath',
                                             '//a[@id="item_4_title_link"]/div[@class="inventory_item_name"]').text

    assert pick_item1 == check_item_picked1, 'Different item picked'

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

    # pick two items and add it to cart:
    browser.find_element('xpath', '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    browser.find_element('xpath', '//button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    time.sleep(2)

    # items quantity in cart before:
    cart_tag_before2 = browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a/span').text
    time.sleep(3)

    # go to cart:
    browser.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
    time.sleep(2)

    # remove one item from cart:
    browser.find_element('xpath', '//button[@id="remove-sauce-labs-bolt-t-shirt"]').click()

    # items quantity in cart after:
    cart_tag_after2 = browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_tag_before2 != cart_tag_after2, 'Items are not removed from cart'
    time.sleep(3)

    # remove item from cart:
    browser.find_element('xpath', '//button[@class="btn btn_secondary btn_small cart_button"]').click()
    time.sleep(3)

    # check if cart icon has child element (quantity tag): ???
    # is_cart_link_empty2 = browser.find_element('css selector', 'a[class="shopping_cart_link"]:empty')
    # assert bool(is_cart_link_empty2) == True
    # time.sleep(3)


# case 2.3
def test_add_item_from_item_card():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item title:
    item_title3 = browser.find_element('xpath', '(//div[@data-test="inventory-item-name"])[1]').text

    # find item link and click it:
    browser.find_element('xpath', '//a[@id="item_4_title_link"]').click()
    time.sleep(2)

    # check if item title is the same item title:
    card_item_title3 = browser.find_element('xpath', '//div[@data-test="inventory-item-name"]').text
    assert item_title3 == card_item_title3, 'Wrong item'

    # add to cart:
    browser.find_element('xpath', '//button[@id="add-to-cart"]').click()

    # go to cart:
    browser.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
    time.sleep(2)

    # check if item title is the same item title and url is cart url:
    cart_item_title3 = browser.find_element('xpath', '//div[@data-test="inventory-item-name"]').text
    assert cart_item_title3 == card_item_title3 and browser.current_url == cart_url, 'Wrong url or different item'

    # remove item from cart:
    browser.find_element('xpath', '//button[@id="remove-sauce-labs-backpack"]').click()


# case 2.4
def test_remove_item_from_item_card():
    # standard auth:
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)

    # pick item text:
    item_title4 = browser.find_element('xpath', '//div[contains(text(), "Sauce Labs Backpack")]').text

    # add item to cart:
    browser.find_element('css selector', 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # items quantity in cart:
    cart_tag_before4 = browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_tag_before4 == '1', 'Wrong quantity of items'
    time.sleep(3)

    # go to item card:
    browser.find_element('xpath', '//div[contains(text(), "Sauce Labs Backpack")]').click()
    time.sleep(2)
    assert item_title4 == 'Sauce Labs Backpack', 'Wrong item title'

    # click remove button:
    browser.find_element('xpath', '//button[@id="remove"]').click()
    time.sleep(2)

    # check the button changed:
    btn_txt4 = browser.find_element('xpath', '//button[@id="add-to-cart"]').text
    assert btn_txt4 == 'Add to cart', 'Button didn\'t change'
