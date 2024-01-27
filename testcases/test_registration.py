import pytest
from base.base_driver import BaseDriver
from page.login import Login
from config.conftest import setup


@pytest.mark.usefixtures("setup")
class TestRegistrationFunctionality():
    def test_registration(self):
        expectedError = [
            "First name is required.",
            "Last name is required.",
            "Address is required.",
            "City is required.",
            "State is required.",
            "Zip Code is required.",
            "Social Security Number is required.",
            "Username is required.",
            "Password is required.",
            "Password confirmation is required."
        ]
        loginPage = Login(self.driver, self.wait);
        loginPage.loadLoginPage();
        registrationPage = loginPage.navigateToRegistrationPage();
        registrationPage.doRegistration();
        registrationPage.fieldsErrorMsgValidate(expectedError)




