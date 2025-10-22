from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, link):
        assert self.browser.current_url != LoginPageLocators.LOGIN_URL, "Login page url doesn't match"

    def should_be_login_form(self):
        assert (
            self.is_element_present(*LoginPageLocators.LOGIN_SIGN_IN_FORM) and
            self.is_element_present(*LoginPageLocators.LOGIN_SIGN_IN_PASSWORD_FORM)
            ), "Login form is not presented"

    def should_be_register_form(self):
        assert (
                self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FORM) and
                self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FORM) and
                self.is_element_present(*LoginPageLocators.REGISTER_SECOND_PASSWORD_FORM)
                ), "Register form is not presented"