from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_BASKET = (By.CSS_SELECTOR, ".hidden-xs")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div.alertinner")
#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong