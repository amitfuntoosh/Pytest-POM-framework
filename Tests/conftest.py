import pytest
from selenium import webdriver
from Config.config import TestData
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"],scope='class')

def init_driver(request):
    print("################ ", request.param)
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()