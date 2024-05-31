from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("https://facebook.com/")
email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
email_element.send_keys("aneka6345@gmail.com")

password_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
password_element.send_keys("Chimezie98")

elem = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
elem.click()


post_element = driver.find_element(
    By.CSS_SELECTOR, "span[class='x1lliihq x6ikm8r x10wlt62 x1n2onr6']")
post_element.send_keys("hello")

buttons = driver.find_elements("button")
time.sleep(10)

for button in buttons:
    if button.text == "Post":
        button.click()
