from auth import *


# case 5.1
def test_a_to_z_filter(standard_auth):
    # sort items a-z before clicking on a-z filter:
    items_before1 = browser.find_elements('xpath', '//div[@data-test="inventory-item-name"]')
    before1 = []
    for item in items_before1:
        before1.append(item.text)

    before1.sort(reverse=False)
    print(f'\n{before1}')

    # click a-z filter:
    browser.find_element('xpath', '//option[@value="az"]').click()

    # check if filter works properly:
    items_after1 = browser.find_elements('xpath', '//div[@data-test="inventory-item-name"]')
    after1 = []
    for item in items_after1:
        after1.append(item.text)
    print(f'\n{after1}')

    assert before1 == after1, 'Filter A to Z doesn\'t work properly'


# case 5.2
def test_z_to_a_filter(standard_auth):
    # sort items z-a before clicking on a-z filter:
    items_before2 = browser.find_elements('xpath', '//div[@data-test="inventory-item-name"]')
    before2 = []
    for item in items_before2:
        before2.append(item.text)

    before2.sort(reverse=True)
    print(f'\n{before2}')

    # click z-a filter:
    browser.find_element('xpath', '//option[@value="za"]').click()

    # check if filter works properly:
    items_after2 = browser.find_elements('xpath', '//div[@data-test="inventory-item-name"]')
    after2 = []
    for item in items_after2:
        after2.append(item.text)
    print(f'\n{after2}')

    assert before2 == after2, 'Filter Z to A doesn\'t work properly'


# case 5.3
def test_high_to_low_filter(standard_auth):
    # sort items low-high before clicking on low-high filter:
    prices_before3 = browser.find_elements('xpath', '//div[@class="inventory_item_price"]')
    before3 = []
    for item in prices_before3:
        before3.append(float(item.text.lstrip('$')))

    before3.sort(reverse=False)
    print(f'\n{before3}')

    # click low-high filter:
    browser.find_element('xpath', '//option[@value="lohi"]').click()

    # check if filter works properly:
    prices_after3 = browser.find_elements('xpath', '//div[@class="inventory_item_price"]')
    after3 = []
    for item in prices_after3:
        after3.append(float(item.text.lstrip('$')))
    print(f'\n{after3}')

    assert before3 == after3, 'Filter Low to High doesn\'t work properly'


# case 5.4
def test_low_to_high_filter(standard_auth):
    # sort items low-high before clicking on low-high filter:
    prices_before4 = browser.find_elements('xpath', '//div[@class="inventory_item_price"]')
    before4 = []
    for item in prices_before4:
        before4.append(float(item.text.lstrip('$')))

    before4.sort(reverse=True)
    print(f'\n{before4}')

    # click low-high filter:
    browser.find_element('xpath', '//option[@value="hilo"]').click()

    # check if filter works properly:
    prices_after4 = browser.find_elements('xpath', '//div[@class="inventory_item_price"]')
    after4 = []
    for item in prices_after4:
        after4.append(float(item.text.lstrip('$')))
    print(f'\n{after4}')

    assert before4 == after4, 'Filter Low to High doesn\'t work properly'
