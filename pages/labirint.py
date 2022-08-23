import os
from pages.base import WebPage
from pages.elementes import WebElement
from pages.elementes import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)


    search = WebElement(id='search-field')

    #кнопка поиска
    search_run_button = WebElement(
        xpath='//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]')

    #название книги
    products_titles = ManyWebElements(
        xpath='//a[@class="product-title-link"]')

     #сообщение об ошибке поиска
    msg_search_er = WebElement(
        xpath='//*[@id="search"]/div[1]/h1')

    # кнопка ТИП ТОВАРА
    product_type = WebElement(
        xpath='//span[@class="navisort-item__content" and contains(text(),"ТИП ТОВАРА")]')

    # в выпадающем списке - Бумажные книги
    paper_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Бумажные")]')

    # в выпадающем списке -  Электронные книги
    electronic_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Электронные")]')

    # в выпадающем списке -  Другие товары
    other_goods = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Другие")]')

    # кнопка "Показать"
    show_button = WebElement(
        xpath='//input[@class="w100p show-goods__button" and @value="Показать"]')

    # тип товара в результатах поиска
    products_types = ManyWebElements(xpath='//span[@class="card-label__text card-label__text_inversed"]')

    # кнопка "Бумажные книги"
    without_paper_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Бумажные")]')

    # кнопка "Электронные книги"
    without_electronic_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Электронные")]')

    # кнопка "Прочие товары"
    without_others_products_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Прочие")]')

    # кнопка "В наличии"
    sort_products_by_type_in_stock_is = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"В наличии")]')

    # кнопка "Предзаказ"
    sort_products_by_type_order = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Предзаказ")]')

    # кнопка "Ожидаются"
    sort_products_by_type_waiting = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Ожидаются")]')

    # статус "Ожидается" в описании товара
    products_waiting = ManyWebElements(
        xpath='//a[@class="btn-not-avaliable"]')

    # часть описания товара
    products_in_stock = ManyWebElements(
        xpath='//div[@class="btn buy-link btn-primary"]')

    # кнопка "Нет в продаже"
    sort_products_by_type_out_of_stock = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Нет в продаже")]')

    # кнопка "Что почитать: выбор редакции"
    what_to_read_button = WebElement(
        xpath='//*[@id="right-inner"]/div[1]/div[1]/a')

    # названия книг на странице "Что почитать: выбор редакции"
    products_titles_large = ManyWebElements(
        xpath='//span[@class="product-title large-name"]')

    # заголовок страницы
    page_title = WebElement(xpath='//h1')

    # кнопка "Новинки"
    fair_button = WebElement(
        #xpath='//*[@id="bottom"]/div[1]/div[1]/a') Не работает
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]')


    # содержание раздела на открывшейся странице "Новинки"
    fair_content = WebElement(
        # xpath='//div[@class="t005__text t-text t-text_md"]')
        xpath='//div[@class="catalog-title"]')

    # кнопка "Акции"
    best_buy_button = WebElement(
        xpath='//*[@id="bottom"]/div[19]/div[1]/a[1]')

    #  на странице "Лучшая покупка дня"
    products_pubhouse = ManyWebElements(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[1]/h2[1]/a[1]')

    # кнопка "Больше книг со скидками"
    discounts_button = WebElement(
        xpath='//*[@id="bottom"]/div[17]/div[1]/a[1]')

    # карточки книг в результатах поиска
    products_books = ManyWebElements(
        xpath='//div[@class="product need-watch watched" and @data-dir="books"]')

    # описание скидки на книгу в результатах поиска
    discounts_books = ManyWebElements(
        xpath='//a[contains(@class, "card-label_profit")]')

    # кнопка "Читатели выбирают сегодня"
    today_button = WebElement(
        xpath='//*[@id="bottom"]/div[6]/div[1]/a[1]')

    # кнопка "Книги" в основном меню header на черном фоне
    button_books = WebElement(
        xpath='/html/body/div[1]/div[5]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')

    # кнопка "Молодежная литература" в выпадающем меню "Книги" основного меню в заголовке
    button_youth_literature = WebElement(
        xpath='/html/body/div[1]/div[5]/div[5]/div/div[4]/div/ul/li[7]/a')

    # кнопка "Лабиринт. Сейчас"
    now_button = WebElement(
        xpath='//*[@id="bottom"]/div[8]/div[1]/a[1]')

    # кнопка "Детский навигатор — что читать детям и с детьми"
    kids_button = WebElement(
        xpath='//*[@id="bottom"]/div[10]/div[1]/a[1]')

    # кнопка "Книги для школы"
    teenagers_button = WebElement(
        xpath='//*[@id="bottom"]/div[3]/div[1]/a[1]')

    # заголовок на странице "Книги для школы"
    heading_on_the_page = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[4]/h1[1]')

    # кнопка "Книжные лидеры продаж"
    leaders_button = WebElement(
        xpath='//*[@id="bottom"]/div[15]/div[1]/a[1]')

    # кнопка "Книги: новинки 2022"
    novelties_books_button = WebElement(
        xpath='//*[@id="bottom"]/div[17]/div[1]/a[1]')

    # заголовок на открывшейся странице "новинки 2022"
    novelties_title = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[1]/h1[1]')

    # кнопка "Книжные обзоры и рецензии"
    reviews_button = WebElement(
        xpath='//*[@id="bottom"]/div[20]/div[1]/a[1]')

    # заголовок на открывшейся странице "Книжные обзоры и рецензии"
    heading_reviews = WebElement(
        xpath='//*[@id="newslist"]/div[1]/div[1]/div[1]')


    # название раздела на странице "Доставка и оплата"
    section_title = WebElement(
        xpath='//*[@id="right-inner"]/div[1]/div[1]/div[1]/div[3]')

     # содержание раздела на открывшейся странице "Сертификаты"
    section_content = WebElement(
        xpath='//*[@id="newslist"]/div[1]/p[1]')

    # название раздела на странице "Поддержка"
    section_title_support = WebElement(
        xpath='//a[@class="support-all active"]')


    # название раздела на странице "N пункт самовывоза"
    section_title_export = WebElement(
        xpath='//*[@id="js-tab-1"]/div[1]/div[1]/span[1]')

         # список авторов в результатах поиска
    authors_names = ManyWebElements(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a/span[1]')

    # кнопка "Изд-ва" в горизонтальном меню
    publishing_offices_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul[1]/li[3]/a[1]/span[1]')

    # список издательств в результатах поиска
    publishing_offices = ManyWebElements(
        xpath='div[@class="b-search-rubric-items-content"]')

    # кнопка "Все книги"
    all_books_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')

    # кнопка "Серии" в горизонтальном меню
    product_series_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul/li[4]/a/span[1]')

    # список серий товаров в результатах поиска
    product_series = ManyWebElements(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a/span[1]')

        # кнопка "Видео" в горизонтальном меню
    video_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul[1]/li[9]/a[1]/span[1]')

    # список видео в результатах поиска
    video_products = ManyWebElements(
        xpath='//a[@class="rubric-list-item videobloc-carousel-item js-videoblock-video-show"]')


    # список тем в результатах поиска
    themes_products = ManyWebElements(
        xpath='//a[@class="rubric-list-item"]')


