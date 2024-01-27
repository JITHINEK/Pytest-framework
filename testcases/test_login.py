import pytest
from config.conftest import setup
from page.login import Login


@pytest.mark.usefixtures("setup")
class TestLoginFunctionality():

    def test_login_with_invalid_credentials(self):
        loginPage = Login(self.driver, self.wait);
        loginPage.loadLoginPage()
        loginStatus = loginPage.doLogin("test", "test")
        assert loginStatus is False
        loginPage.validateErrorMsg()














