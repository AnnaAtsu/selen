from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    sum = int(x) + int(y)
    list = Select(browser.find_element(By.TAG_NAME, "select"))
    list.select_by_value(str(sum)).click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    
    # 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
  #  пустая строка в конце файла
