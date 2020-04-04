from .base_page import BasePage
from .locators import ProductPageLocator
import math
import time
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocator.ADD_TO_BASKET_BTN), "Add to basket button is not presented"

    def click_add_good_to_basket_btn(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET_BTN)
        add_to_basket_button.click()

    def send_answer_and_accept_prompt(self):
        prompt = self.browser.switch_to.alert
        x = prompt.text.split(" ")[2]
        prompt.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
        prompt.accept()
        try:
            alert = self.browser.switch_to.alert
            code = alert.text.split(" ")[-1]
            print(f"Code: {code}")
            alert.accept()
            #time.sleep(600)
        except NoAlertPresentException:
            print("No second alert presented")

    def compare_book_titles(self):
        book_name = self.browser.find_element(*ProductPageLocator.BOOK_NAME)
        book_name_in_message = self.browser.find_element(*ProductPageLocator.ADDED_BOOK_NAME)
        assert book_name.text == book_name_in_message.text, "Book's name is not right"

    def compare_prices(self):
        book_price = self.browser.find_element(*ProductPageLocator.BOOK_PRICE)
        total_mes_in_basket = self.browser.find_element(*ProductPageLocator.TOTAL_BASKET)
        print(total_mes_in_basket.text)
        total_price_in_basket = total_mes_in_basket.text.split(" ")[-2]
        tpib = total_price_in_basket.split("\n")[0]
        assert book_price.text == tpib, f"Prices is difference '{book_price.text}' != '{tpib}'"

