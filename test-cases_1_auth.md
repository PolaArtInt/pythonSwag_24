## Авторизация: test_auth.py
case 1.1
test_standart_login
Авторизация стандартного пользователя:
1.Открыть url: https://www.saucedemo.com/
2.Ввести 'standard_user' в 'Username'
3.Ввести 'secret_sauce' в 'Password'
4.Кликнуть 'Login'
5.Проверить, что мы перешли на новый url:
https://www.saucedemo.com/inventory.html

case 1.2
test_auth_positive_locked_out_user
1.Открыть url: https://www.saucedemo.com/
2.Ввести 'locked_out_user' в 'Username'
3.Ввести 'secret_sauce' в 'Password'
4.Кликнуть 'Login'
5.1.Убедиться, что появилось сообщение об ошибке:
'Epic sadface: Sorry, this user has been locked out.'
5.2.Проверить, что мы никуда не перешли, а находимся на том же url:
https://www.saucedemo.com/

case 1.3
test_auth_positive_problem_user
test_auth_positive_locked_out_user
1.Открыть url: https://www.saucedemo.com/
2.Ввести 'problem_user' в 'Username'
3.Ввести 'secret_sauce' в 'Password'
4.Кликнуть 'Login'
5.Проверить, что мы перешли на новый url:
https://www.saucedemo.com/inventory.html

case 1.4
test_auth_positive_performance_glitch_user
1.Открыть url: https://www.saucedemo.com/
2.Ввести 'performance_glitch_user' в 'Username'
3.Ввести 'secret_sauce' в 'Password'
4.Кликнуть 'Login'
5.Проверить, что мы перешли на новый url:
https://www.saucedemo.com/inventory.html

case 1.5
test_auth_negative_wrong_login
1.Открыть url: https://www.saucedemo.com/
2.Ввести 'user' в 'Username'
3.Ввести 'user' в 'Password'
4.Кликнуть 'Login'
5.1.Убедиться, что появилось сообщение об ошибке:
'Epic sadface: Username and password do not match any user in this service'
5.2.Проверить, что мы никуда не перешли, а находимся на том же url:
https://www.saucedemo.com/