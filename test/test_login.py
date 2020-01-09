from utils import utils as utils
import pytest
from pages.loginpage import LoinPage


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_loginPage(self):
        driver = self.driver

        driver.get(utils.URL)
        lp = LoinPage(driver)
        lp.enterUserName(utils.USERNAME)

    def test_logout(self):
        driver = self.driver
        driver.close()
        driver.quit()

