from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.dashboard_heading)
        ).is_displayed()