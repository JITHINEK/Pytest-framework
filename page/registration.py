from base.base_driver import BaseDriver

class Registration(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    FIRST_NAME_LOCATOR_FIELD = "//input[@id='customer.firstName']"
    LAST_NAME_LOCATOR_FIELD = "//input[@id='customer.lastName']"
    ADDRESS_LOCATOR_FIELD = "//input[@id='customer.address.street']"
    CITY_LOCATOR_FIELD = "//input[@id='customer.address.city']"
    STATE_LOCATOR_FIELD = "//input[@id='customer.address.state']"
    ZIP_CODE_LOCATOR_FIELD = "//input[@id='customer.address.zipCode']"
    PHONE_LOCATOR_FIELD = "//input[@id='customer.phoneNumber']"
    SSN_LOCATOR_FIELD = "//input[@id='customer.ssn']"

    USER_NAME_LOCATOR_FIELD = "//input[@id='customer.username']"
    PASSWORD_LOCATOR_FIELD = "//input[@id='customer.password']"
    CONFIRM_PASSWORD_LOCATOR_FIELD = "//input[@id='repeatedPassword']"
    ERROR_MSGS = "//span[@class='error']"
    REGISTRATION_BUTTON = "//input[@type='submit' and @value='Register']"

    def doRegistration(self, firstName="", lastName="", address="", city="",
                       state="", zip="", phone="", ssn="", username="", password="", confirmPasswd=""):
        self.enterTextField(firstName, self.FIRST_NAME_LOCATOR_FIELD)
        self.enterTextField(lastName, self.LAST_NAME_LOCATOR_FIELD)
        self.enterTextField(address, self.ADDRESS_LOCATOR_FIELD)
        self.enterTextField(city, self.CITY_LOCATOR_FIELD)
        self.enterTextField(state, self.STATE_LOCATOR_FIELD)
        self.enterTextField(zip, self.ZIP_CODE_LOCATOR_FIELD)
        self.enterTextField(phone, self.PHONE_LOCATOR_FIELD)
        self.enterTextField(ssn, self.SSN_LOCATOR_FIELD)
        self.enterTextField(username, self.USER_NAME_LOCATOR_FIELD)
        self.enterTextField(password, self.PASSWORD_LOCATOR_FIELD)
        self.enterTextField(confirmPasswd, self.CONFIRM_PASSWORD_LOCATOR_FIELD)
        self.click(self.REGISTRATION_BUTTON)
        if self.driver.title == "ParaBank | Error":
            return False
        else:
            return True

    def fieldsErrorMsgValidate(self, expectedErrors):
        errors = self.getElements(self.ERROR_MSGS);
        for error in errors:
            assert any(expected_error in error.text for expected_error in expectedErrors), \
                f"Expected one of {expectedErrors} in error text, but found: {error.text}"

