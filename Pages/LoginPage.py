from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class LoginPage(BasePage):

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Log in')]")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """PAGE ACTIONS"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    #def is_signup_link_exist(self):
       #return self.is_visible(self,)

    def do_login(self, username, password):
        # self.do_send_keys(self.EMAIL, "")
        self.do_send_keys(self.EMAIL,username)
        # self.do_send_keys(self.PASSWORD, "")
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
