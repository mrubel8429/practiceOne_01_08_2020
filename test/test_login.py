from utils import utils as utils
import pytest
from pages.loginpage import LoginPage


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_loginpage(self):
        driver = self.driver

        driver.get(utils.URL)
        lp = LoginPage(driver)
        lp.enterUserName(utils.USERNAME)

    def test_logout(self):
        driver = self.driver
        driver.close()
        driver.quit()

