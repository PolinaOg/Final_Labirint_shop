"""Тестируем возможность входа  в личный кабинет с корректным и некорректным логином (код скидки). 4 теста."""

from pages.labirint_locators import MainPage

#Вход с правильным кодом
def test_valid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("6195-441D-9EDF")
    page.enter.click()
    page.automatic_closing.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


#Вход по неправильному коду


def test_invalid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("6199-443D-E9DF")
    page.enter.click()

    assert page.auth_error


#Вход по символу


def test_blanc_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("   -   ")

    assert page.auth_error_2


#Вход по адресу электронной почты


def test_email_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("polinamelkova@gmail.com")
    page.enter.click()

    assert page.login_field
