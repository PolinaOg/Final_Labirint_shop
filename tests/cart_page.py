
from pages.labirint_locators import MainPage

#Добавление в корзину


def test_add_book_to_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    #page.btn_ok_close.click()

    assert page.successfuly_odered


#Увеличение количества книг в корзине


def test_make_more_books_in_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.btn_ok_close.click()
    page.plus_one_more.click()



    assert page.two_books_in_cart


#Удаление книг из корзины.


def test_remove_book_from_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    #page.btn_ok_close.click()
    page.remove_from_cart.click()

    assert page.empty_cart
