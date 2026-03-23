from config.config import BASE_URL
import time


def test_window_handling(driver):
    driver.get(BASE_URL)
    time.sleep(10)

    # open new tab
    driver.execute_script("window.open('https://www.google.com');")

    # get all windows
    windows = driver.window_handles
    time.sleep(10)
    # switch to new tab
    driver.switch_to.window(windows[1])

    # switch back to original tab
    driver.switch_to.window(windows[0])