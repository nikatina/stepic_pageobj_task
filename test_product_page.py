from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.click_add_good_to_basket_btn()  # выполняем метод страницы -
    page.send_answer_and_accept_prompt()
    page.compare_book_titles()
    page.compare_prices()

    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()