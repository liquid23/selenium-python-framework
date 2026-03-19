from selenium.webdriver.common.by import By
from config.config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(BASE_URL)


    #locators
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    login_btn = (By.XPATH, "//button[normalize-space()='Login']")
    dashboard_heading = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    #actions
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_pass(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located(self.login_btn)).click()

    def is_dashboard_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_heading)).is_displayed()

    