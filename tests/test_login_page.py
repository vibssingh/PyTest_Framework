import pytest

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_login_negative(driver, get_data):

    login_page = LoginPage(driver)

    login_page.execute_login(get_data["username"], get_data["password"])
    assert login_page.actual_error() == "Invalid credentials", "Error message does not match expected value"


def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.execute_login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.actual_heading() == "Dashboard", "Heading is different"


#@pytest.fixture(params=[("admin", "admin$$"),("Admin123", "123")])
#def get_data(request):
#    return request.param

@pytest.fixture(params=[{"username":"admin", "password":"admin$$"},
                        {"username":"Admin123", "password":"123"}])
def get_data(request):
    return request.param