from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//*[@class='oxd-form']/div[3]/button")
    error_message = (By.XPATH, "//*[@class='orangehrm-login-error']/div[1]/div[1]/p")

    def execute_login(self, username: str, password: str):
        log = self.get_logger()
        log.info("Enter Username - " + username)
        self.find(self.username).send_keys(username)
        log.info("Enter Password - " + password)
        self.find(self.password).send_keys(password)
        self.find(self.submit_button).click()

    def actual_error(self):
        log = self.get_logger()
        actual_errormessage = self.find(self.error_message).text
        log.info("Actual Error Message - " + actual_errormessage)
        return actual_errormessage
