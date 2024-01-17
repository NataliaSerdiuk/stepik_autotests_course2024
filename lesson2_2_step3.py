from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/selects2.html")
    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    z = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)


# не забываем оставить пустую строку в конце файла