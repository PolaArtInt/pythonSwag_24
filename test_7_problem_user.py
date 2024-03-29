from selenium import webdriver
import time

browser = webdriver.Chrome()

url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'


# case 7.1 DEFECT FOUND
def test_problem_user_negatiev_inventory_imgs():
    browser.get(url)
    time.sleep(2)

    # problem_user auth:
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('problem_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    time.sleep(5)
    assert browser.current_url == inventory_url, 'Wrong url'

    # get all inventory images:
    images = browser.find_elements('xpath', '//img[@class="inventory_item_img"]')

    # make list of images and list of its src-attributes:
    check_images = []
    list_images = []
    for img in images:
        if img.get_dom_attribute('src') == '/static/media/sl-404.168b1cce.jpg':
            check_images.append(img.get_dom_attribute('src'))
            list_images.append(img.get_dom_attribute('alt'))

    # make dict of images and its src-attributes:
    imgs_dict = dict(zip(list_images, check_images))
    # print(f'\n{imgs_dict}')

    # check if all items have only one image:
    for key, val in imgs_dict.items():
        if val != '/static/media/sl-404.168b1cce.jpg':
            assert val != '/static/media/sl-404.168b1cce.jpg', 'Image is correct'
            print(f'\nItem:{key} has its own image')
        else:
            assert val == '/static/media/sl-404.168b1cce.jpg', 'Wrong image url'
            print(f'\nError! Item:{key} has the same image URL:{val} with other items')



