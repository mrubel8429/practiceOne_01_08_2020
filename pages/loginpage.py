import utils.customlogger as cl
import logging


class LoginPage():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

        self.username_txt_id = "txtUsername"
        self.password_txt_id = "txtPassword"
        self.login_btn = "btnLogin"

    def enterUserName(self, username):
        self.driver.find_element_by_id(self.username_txt_id).send_keys(username)
        self.log.info("enter user name success fully ")
