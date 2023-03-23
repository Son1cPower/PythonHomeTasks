from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:

    wait = WebDriverWait(driver, 6)
    driver.get('https://www.epam.com/')

    # Check page Title
    expected_title = "EPAM | Software Engineering & Product Development Services"
    assert driver.title == expected_title, f"The page title does not match the expected one: {driver.title}"

    # Check page Logo
    logo_locator_CSS = (
        By.CSS_SELECTOR, "a[class='header__logo-container desktop-logo'] img[class='header__logo']")
    logo_element = wait.until(EC.presence_of_element_located(logo_locator_CSS))

    assert logo_element.is_displayed(), "The logo is not displayed on the page."

    # Check the existence of the text “AUTOMATION"”
    search_icon = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".header-search__button")))
    search_field = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@id='new_form_search']")))
    find_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".header-search__submit-text")))
    search_text = 'AUTOMATION'

    search_icon.click()
    time.sleep(1)
    search_field.send_keys(search_text)
    find_button.click()
    search_result = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".search-results__counter")))
    assert search_text in search_result.text, f"Sorry, but your search returned no results. Please try another query."
finally:
    driver.quit()
