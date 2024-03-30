from browser_init import *
from auth import standard_auth


# case 6.1
def test_positive_logout(standard_auth):
    # find and click burger menu:
    browser.find_element('id', 'react-burger-menu-btn').click()
    time.sleep(3)

    # find and click 'logout' button:
    browser.find_element('css selector', '#logout_sidebar_link').click()

    # check if we are on login page:
    assert browser.current_url == url


# case 6.2
def test_positive_about_btn(standard_auth):
    # find and click burger menu:
    browser.find_element('id', 'react-burger-menu-btn').click()
    time.sleep(3)

    # find and click 'about' button:
    browser.find_element('css selector', '#about_sidebar_link').click()

    # check expected url and title:
    curr_title = browser.title
    exp_title = 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing'
    assert browser.current_url == about_url and curr_title == exp_title, 'Wrong page url or title'


# case 6.3
def test_reset_app_state_positive(standard_auth):
    # add two items to cart:
    browser.find_element('xpath', '//button[@name="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element('xpath', '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(2)

    # find and click burger menu:
    browser.find_element('id', 'react-burger-menu-btn').click()
    time.sleep(3)

    # find and click 'reset app state' button:
    browser.find_element('css selector', '#reset_sidebar_link').click()

    # check if cart is empty:
    cart_tag3 = browser.find_element('css selector', '#shopping_cart_container>a:empty')
    assert bool(cart_tag3) == True, 'Shopping cart is not empty'
    time.sleep(5)


# case 6.4  DEFECT FOUND
def test_reset_app_state_negative(standard_auth):
    # check 'add to cart' buttons quantity before:
    add_btns_before = browser.find_elements('xpath', '//button[@class="btn btn_primary btn_small btn_inventory "]')
    print(len(add_btns_before))

    # add two items to cart:
    browser.find_element('xpath', '//button[@name="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element('xpath', '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(2)

    # find and click burger menu:
    browser.find_element('id', 'react-burger-menu-btn').click()
    time.sleep(3)

    # find and click 'reset app state' button:
    browser.find_element('css selector', '#reset_sidebar_link').click()

    # check if cart is empty:
    cart_tag3 = browser.find_element('css selector', '#shopping_cart_container>a:empty')
    assert bool(cart_tag3), 'Shopping cart is not empty'
    time.sleep(5)

    # check all 'add to cart' buttons are unpressed by its quantity before and after:
    add_btns_after = browser.find_elements('xpath', '//button[@class="btn btn_primary btn_small btn_inventory "]')
    print(len(add_btns_after))
    assert len(add_btns_before) != len(add_btns_after), 'Buttons are not unpressed after reset the app'

