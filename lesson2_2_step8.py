from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Petrov@stepic.ru")

    text_file_send = browser.find_element(By.ID, 'file')
    text_file_send.send_keys("C:\\Users\\b1ska\\Desktop\\Pyth.txt")

    button = browser.find_element(By.CLASS_NAME, "btn-primary")

    button.click()
    time.sleep(30)
