from base.base_driver import BaseDriver
from page.registration import Registration

class Login(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    USER_NAME_LOCATOR_FIELD = "//input[@name='username']"
    PASSWORD_LOCATOR_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//input[@value='Log In']"
    ERROR_MSG = "//p[@class='error']"
    REGISTRATION_LINK = "//a[text()='Register']"

    def loadLoginPage(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")

    def doLogin(self, username, password):
        self.enterTextField(username, self.USER_NAME_LOCATOR_FIELD)
        self.enterTextField(password, self.PASSWORD_LOCATOR_FIELD)
        self.click(self.LOGIN_BUTTON)
        if self.driver.title == "ParaBank | Error":
            return False
        else:
            return True

    def validateErrorMsg(self):
        assert self.getText(self.ERROR_MSG) == "An internal error has occurred and has been logged."

    def navigateToRegistrationPage(self):
        self.click(self.REGISTRATION_LINK)
        if self.driver.title == "ParaBank | Register for Free Online Account Access":
            return Registration(self.driver, self.wait)
        else:
            print("Failed to navigate to Registration page.")
