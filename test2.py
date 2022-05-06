from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://ispi.cdo.vlsu.ru/login/index.php')

username=browser.find_element(by=By.NAME, value='username')
username.send_keys('<ваш логин>')

password=browser.find_element(by=By.ID, value='password')
password.send_keys('<ваш пароль>')

button=browser.find_element(by=By.CSS_SELECTOR, value='#loginbtn')
button.click()

try:
    assert 'Учебный сайт кафедры ИСПИ' in browser.title
    assert '<ФИО пользователя>' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
browser.close()