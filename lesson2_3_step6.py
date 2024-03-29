from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")

    button.click()
    time.sleep(30)
