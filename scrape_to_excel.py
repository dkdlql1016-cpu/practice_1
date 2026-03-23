from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://mindbridge-ema.kpmg.com/idp/login"
MAX_WAIT_TIME = 10
LOGIN_SELECTOR = "a[href*='microsoft']"


driver = webdriver.Edge()
wait = WebDriverWait(driver, MAX_WAIT_TIME)

driver.get(LOGIN_URL)

links = wait.until(
    EC.element_to_be_clickable(
    find_element(
        By.CSS_SELECTOR, LOGIN_SELECTOR)
    )
)

print("찾은갯수", len(links))

login_link.click()

input("Press enter to continue...")
driver.quit()