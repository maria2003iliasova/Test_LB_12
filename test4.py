from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://www.chitai-gorod.ru/catalog/book/2903552/')

button=browser.find_element(by=By.CLASS_NAME, value='js__card_button_text')
button.click()

browser.get('https://www.chitai-gorod.ru/personal/basket/')

try:
    assert 'Мертвая земля: роман' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
browser.close()