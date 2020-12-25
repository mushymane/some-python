from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')


assert 'Selenium Easy Demo' in chrome_browser.title
button_text = chrome_browser.find_element_by_class_name('btn-default')
print(button_text.get_attribute('innerHTML'))
