from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert  self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"