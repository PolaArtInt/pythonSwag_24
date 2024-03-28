## Бургер меню: test_6_menu.py  
case 6.1  
test_positive_logout  
Авторизация:  
1.Открыть url: https://www.saucedemo.com/  
2.Ввести 'standard_user' в 'Username'  
3.Ввести 'secret_sauce' в 'Password'  
4.Кликнуть 'Login'  
На странице каталога товаров:  
5.Кликнуть по бургер-меню  
6.Кликнуть по кнопке 'Logout'  
7.Проверить, что мы перешли на страницу авторизации  
https://www.saucedemo.com/  
  
case 6.2  
test_positive_about_btn  
Авторизация:  
1.Открыть url: https://www.saucedemo.com/  
2.Ввести 'standard_user' в 'Username'  
3.Ввести 'secret_sauce' в 'Password'  
4.Кликнуть 'Login'  
На странице каталога товаров:  
5.Кликнуть по бургер-меню  
6.Кликнуть по кнопке 'About'  
7.Проверить, что мы перешли на страницу 'About'  
https://saucelabs.com/  
  
case 6.3  
test_positive_logout  
Авторизация:  
1.Открыть url: https://www.saucedemo.com/  
2.Ввести 'standard_user' в 'Username'  
3.Ввести 'secret_sauce' в 'Password'  
4.Кликнуть 'Login'  
На странице каталога товаров:  
5.Кликнуть по бургер-меню  
7.Добавить два товара в корзину  
6.Кликнуть по кнопке 'Reset App State'  
7.Убедиться, что кнопка работает   
8.Убедиться, что корзина пуста   
  
case 6.4  DEFECT FOUND  
test_reset_app_state_negative  
Авторизация:  
1.Открыть url: https://www.saucedemo.com/  
2.Ввести 'standard_user' в 'Username'  
3.Ввести 'secret_sauce' в 'Password'  
4.Кликнуть 'Login'  
На странице каталога товаров:  
5.Кликнуть по бургер-меню  
6.Зафиксировать количество кнопок 'Add to cart'  
7.Добавить два товара в корзину  
8.Кликнуть по кнопке 'Reset App State'  
9.Зафиксировать количество кнопок 'Add to cart' после ресета  
10.Убедиться, что количество кнопок 'Add to cart' не совпадает  
  
