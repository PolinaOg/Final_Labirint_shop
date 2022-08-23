
def test_check_main_search(web_browser):
#Проверка работы поиска
    page = MainPage(web_browser)

    page.search = 'пирог'
    page.search_run_button.click()

    assert page.products_titles.count() >= 1

    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'пирог' in title.lower(), msg

def test_check_main_exact_search(web_browser):
#Отображение списка книг
    page = MainPage(web_browser)

    page.search = 'яблочный пирог'
    page.search_run_button.click()


    assert page.products_titles.count() >= 1


    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'яблочный пирог' in title.lower(), msg

def test_check_wrong_input_in_search(web_browser):
#Проверка ввода с латиницы

    page = MainPage(web_browser)

    page.search = 'gbhju'
    page.search_run_button.click()

    assert page.products_titles.count() >= 1

    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'пирог' in title.lower(), msg

def test_check_wrong_input(web_browser):
#Проверка ввода с опечатками
    page = MainPage(web_browser)

    page.search = 'яплако'
    page.search_run_button.click()

    assert page.products_titles.count() >= 1

    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert title == 'Все, что мы нашли в Лабиринте по запросу «яблоко»', msg

def test_check_search_electronic_books(web_browser):
#Проверка поиска электронной книги

    page = MainPage(web_browser)

    page.search = 'пирог'
    page.search_run_button.click()

    page.without_others_products_button.click()

    page.without_paper_books_button.click()
    time.sleep(5)

    assert page.products_titles.count() >= 1

    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' in title.lower(), msg


def test_check_search_paper_books(web_browser):
#Проверка поиска бумажных книг

    page = MainPage(web_browser)

    page.search = 'зима'
    page.search_run_button.click()

    page.without_electronic_books_button.click()

    page.without_others_products_button.click()

    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' not in title.lower(), msg


def test_check_search_expected(web_browser):
#Проверка фильтра товаров со статусом "Ожидается"

    page = MainPage(web_browser)

    page.search = 'золото'
    page.search_run_button.click()

    page.sort_products_by_type_order.click()

    page.sort_products_by_type_in_stock_is.click()

    for title in page.products_waiting.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'ожидается' in title.lower(), msg


def test_check_search_in_stock(web_browser):
#Проверка фильтра товаров со статусом "В наличии"

    page = MainPage(web_browser)

    page.search = 'тушь'
    page.search_run_button.click()

    page.sort_products_by_type_out_of_stock.click()

    page.sort_products_by_type_waiting.click()

    page.sort_products_by_type_order.click()

    assert page.products_titles.count() >= 1

     for title in page.products_in_stock.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'корзину' in title.lower(), msg


def test_check_search_electronic_books_another_way(web_browser):
#Проверка работы фильтра по электронным книгам

    page = MainPage(web_browser)

    page.search = 'пудра'
    page.search_run_button.click()

    page.product_type.click()

    page.paper_books.click()

    page.other_goods.click()

    page.show_button.click()

    time.sleep(5)

     for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' in title.lower(), msg


def test_check_search_paper_books_another_way(web_browser):
#Проверка работы фильтра по бумажным книгам

    page = MainPage(web_browser)

    page.search = 'пирог'
    page.search_run_button.click()

    page.product_type.click()

    page.electronic_books.click()

    page.show_button.click()

    page.product_type.click()

    page.other_goods.click()

    page.show_button.click()

    for title in page.products_types.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'электронная' not in title.lower(), msg

def test_check_search_other_goods(web_browser):
#Проверка работы фильтра по другим товарам.

    page = MainPage(web_browser)

    page.search = 'карандаш'
    page.search_run_button.click()

    page.product_type.click()

    page.paper_books.click()

    page.show_button.scroll_to_element()

    page.show_button.click()

    assert page.products_titles.count() >= 1

def test_check_search_authors(web_browser):

    page = MainPage(web_browser)

    page.search = 'Алмазов'
    page.search_run_button.click()

    assert page.products_titles.count() >= 1

    page.authors_button.click()

    for title in page.authors_names.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Алмазов' in title.lower(), msg

def test_check_search_product_series(web_browser):
#Проверка фильтра по сериям книг с ключевым словом

    page = MainPage(web_browser)

    page.search = 'дворец'
    page.search_run_button.click()

    assert page.products_titles.count() >= 1

    page.product_series_button.click()

    for title in page.product_series.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'дворец' in title.lower() or 'дворц' in title.lower(), msg


def test_check_search_what_to_read(web_browser):
#Проверка работы кнопки "Что почитать. Выбор редакции"

    page = MainPage(web_browser)

    page.what_to_read_button.click()

    assert page.products_titles_large.count() >= 1


def test_check_button_what_to_read(web_browser):

    page = MainPage(web_browser)

    page.what_to_read_button.click()

    assert page.page_title.get_text() == "Что почитать: выбор редакции"


def test_check_button_fair(web_browser):
#Проверка работы кнопки "Новинки"

    page = MainPage(web_browser)

    page.fair_button.click()

    title = page.fair_content.get_text()
    msg = 'Неправильный товар в поиске "{}"'.format(title)
    assert 'новые книги' in title.lower(), msg


def test_check_search_best_buy(web_browser):
#Проверка работы кнопки "Лучшая покупка дня"

    page = MainPage(web_browser)

    page.best_buy_button.click()

    assert page.products_pubhouse.count() >= 1


def test_check_button_best_buy(web_browser):

    page = MainPage(web_browser)

    page.best_buy_button.click()


    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'акции' in title.lower(), msg


def test_check_search_discounts_books(web_browser):
#Проверка работы кнопки "Акции"

    page = MainPage(web_browser)

    page.discounts_button.click()

    for title in page.discounts_books.get_text():
        msg = 'Неправильный товар в поиске "{}"'.format(title)
        assert '%' in title, msg


def test_check_button_discounts_books(web_browser):

    page = MainPage(web_browser)

    page.best_buy_button.click()

    title = page.page_title.get_text()

    msg = 'Wrong product in search "{}"'.format(title)
    assert 'акции августа' in title.lower(), msg


def test_check_search_today(web_browser):
#Проверка работы кнопки "Читатели выбирают сегодня"

    page = MainPage(web_browser)

    page.today_button.click()

    assert page.products_books.count() >= 1


def test_check_button_today(web_browser):

    page = MainPage(web_browser)

    page.today_button.click()

    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'главные книги' in title.lower(), msg


def test_check_button_now(web_browser):
# Проверка работы кнопки "Лабиринт. Сейчас"

    page = MainPage(web_browser)

    page.now_button.click()

    title = page.active_menu_item.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'лабиринт. сейчас' in title.lower(), msg


def test_check_button_kids(web_browser):
#Проверка кнопки "Детский навигатор"

    page = MainPage(web_browser)

    page.kids_button.click()

    title = page.active_menu_item.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'детский навигатор' in title.lower(), msg


def test_check_button_teenagers(web_browser):
#Проверка работы кнопки "Книги для школы"

    page = MainPage(web_browser)

    page.teenagers_button.click()

    title = page.heading_on_the_page.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'пять четвертей' in title.lower(), msg


def test_check_button_leaders(web_browser):
#Проверка кнопки "Книжные лидеры продаж"

    page = MainPage(web_browser)

    page.leaders_button.click()

    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'рейтинг продаж' in title.lower(), msg


def test_check_button_delivery(web_browser):
#Проверка перехода по кнопке "Доставка и оплата"

    page = MainPage(web_browser)

    page.delivery_button.click()

    title = page.section_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'доставка' in title.lower(), msg

def test_check_button_certificates(web_browser):
#Проверка перехода по кнопке "Сертификаты"

    page = MainPage(web_browser)

    page.certificates_button.click()

    title = page.section_content.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'сертификаты' in title.lower(), msg


def test_check_button_novelties(web_browser):
#Проверка работы кнопки "Новинки"

    page = MainPage(web_browser)

    page.novelties_button.click()

    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'новые книги' in title.lower(), msg


def test_check_button_discounts(web_browser):
# Проверка работы кнопки "Скидки"

    page = MainPage(web_browser)

    page.discounts_books_button.click()

    for title in page.discounts_books.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert '%' in title, msg


def test_check_button_contacts(web_browser):
# Проверка работы кнопки "Контакты"

    page = MainPage(web_browser)

    page.contacts_button.click()

    title = page.page_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'контакты' in title.lower(), msg


def test_check_button_novelties_books(web_browser):
# Проверка работы кнопки "Книги: новинки 2022"

    page = MainPage(web_browser)

    page.novelties_books_button.click()

    title = page.novelties_title.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'новые книги' in title.lower(), msg


def test_check_button_reviews(web_browser):
#Проверка перехода по кнопке "Книжные обзоры и рецензии"

    page = MainPage(web_browser)

    page.reviews_button.click()

    title = page.heading_reviews.get_text()
    msg = 'Wrong product in search "{}"'.format(title)
    assert 'обзоры и рецензии' in title.lower(), msg

