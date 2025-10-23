from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_SIGN_IN_FORM = (By.ID, "id_login-username")
    LOGIN_SIGN_IN_PASSWORD_FORM = (By.ID, "id_login-password")

    REGISTER_EMAIL_FORM = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FORM = (By.ID, "id_registration-password1")
    REGISTER_SECOND_PASSWORD_FORM = (By.ID, "id_registration-password2")
    #DSFDSF
