from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocator():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_BASKET = (By.CSS_SELECTOR, ".hidden-xs")
#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong