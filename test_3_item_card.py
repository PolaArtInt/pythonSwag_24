from auth import *


# case 3.1
def test_click_on_item_img(standard_auth):
    # pick item description:
    item_desc1 = browser.find_element('xpath', '(//div[@class="inventory_item_desc"])[2]').text
    time.sleep(2)

    # pick item image and click:
    browser.find_element('xpath', '//a[@id="item_0_img_link"]/img').click()
    time.sleep(2)

    # check if url changed and we can get the same item:
    item_card_desc1 = browser.find_element('xpath', '//div[@data-test="inventory-item-desc"]').text
    assert browser.current_url != url and item_desc1 == item_card_desc1, 'Different item description or wrong url'
    time.sleep(2)


# case 3.2
def test_click_on_item_title(standard_auth):
    # pick item description:
    item_desc1 = browser.find_element('xpath', '(//div[@class="inventory_item_desc"])[3]').text
    time.sleep(2)

    # pick item title and click:
    browser.find_element('xpath', '//a[@id="item_1_title_link"]/div').click()
    time.sleep(2)

    # check if url changed and we can get the same item:
    item_card_desc1 = browser.find_element('xpath', '//div[@data-test="inventory-item-desc"]').text
    assert item_desc1 == item_card_desc1 and browser.current_url != url, 'Different item description or wrong url'
    time.sleep(2)
