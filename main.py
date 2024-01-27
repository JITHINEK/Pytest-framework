from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Install ChromeDriver and get its path
driver_path = ChromeDriverManager().install()
print(f"ChromeDriver path: {driver_path}")
driver = webdriver.Chrome(service=ChromeService(driver_path))
wait = WebDriverWait(driver, 10)
print(driver.title)

wait.until(EC.element_to_be_clickable()).click()

driver.quit()