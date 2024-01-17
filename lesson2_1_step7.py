from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
    robot_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)


# не забываем оставить пустую строку в конце файла