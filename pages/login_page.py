from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") != -1, "Login url is not correct"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)
        pass1_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        pass1_input.send_keys(password)
        pass2_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_2)
        pass2_input.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        reg_btn.click()




