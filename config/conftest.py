import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="class")
def setup(request):
    driver_path = ChromeDriverManager().install()
    print(f"ChromeDriver path: {driver_path}")
    driver = webdriver.Chrome(service=ChromeService(driver_path))
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()
    driver.quit()