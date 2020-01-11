import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(
        executable_path="/Users/mdrubel/Documents/Rubel_python_workSpace/OrangeHRM_v1/chromedriver")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
