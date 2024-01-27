from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class BaseDriver:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def getElement(self, locator, locatorType=By.XPATH):
        try:
            return self.wait.until(EC.presence_of_element_located((locatorType, locator)))
        except:
            print("Failed to Locate: ", locator)
            return False


    def getElements(self, locator, locatorType=By.XPATH):
        return self.wait.until(EC.presence_of_all_elements_located((locatorType, locator)))

    def visibilityOfElementLocated(self, locator, locatorType=By.XPATH):
        return self.wait.until(EC.visibility_of_element_located((locatorType, locator)))
    def enterTextField(self, text, locator, locatorType=By.XPATH):
        self.getElement(locator, locatorType).send_keys(text)

    def click(self, locator, locatorType=By.XPATH):
        print(locator, locatorType)
        try:
            element = self.wait.until(EC.element_to_be_clickable((locatorType, locator)))
            element.click();
        except:
            print("Failed to click on :", locator)
        else:
            print("Element sucessfully clicked: ", locator)

    def getText(self, locator, locatorType=By.XPATH):
        element = self.visibilityOfElementLocated(locator, locatorType)
        if element:
            return element.text
        else:
            print("element not visible :: Locator- ", locator)
            return element
