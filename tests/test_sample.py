from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import USERNAME, PASSWORD, BASE_URL
import time

def test_open_page(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)


    login.open()
    login.enter_username(USERNAME)
    login.enter_pass(PASSWORD)
    login.click_login()
    time.sleep(5)

    assert login.is_dashboard_visible()
