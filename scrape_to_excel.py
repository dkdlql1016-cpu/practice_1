from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://mindbridge-ema.kpmg.com/idp/login"
MAX_WAIT_TIME = 10
LOGIN_SELECTOR = "a[href='idp/oauth2/authorize/microsoft']"

driver = webdriver.Edge()
wait = WebDriverWait(driver, MAX_WAIT_TIME)

driver.get(LOGIN_URL)

login_link = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, LOGIN_SELECTOR)
    )
)

login_link.click()

input("Press enter to continue...")
driver.quit()