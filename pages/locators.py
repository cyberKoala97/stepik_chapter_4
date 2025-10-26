from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_SIGN_IN_FORM = (By.ID, "id_login-username")
    LOGIN_SIGN_IN_PASSWORD_FORM = (By.ID, "id_login-password")

    REGISTER_EMAIL_FORM = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FORM = (By.ID, "id_registration-password1")
    REGISTER_SECOND_PASSWORD_FORM = (By.ID, "id_registration-password2")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages div:first-child")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")