import time, math, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 

    browser = webdriver.Chrome()
    browser.get(link)


    btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text

    answer = calc(x)
    
    field = browser.find_element(By.ID, "answer")
    field.send_keys(answer)

    btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn.click()

finally:
    time.sleep(4)
    browser.quit()
