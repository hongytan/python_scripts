# python3
# Opens up a 2048 via link and plays moving only up, right, down, left
# NOTE: THE PATH is only for windows

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH_WIN = 'C:\\Users\\hongt\\Downloads\\chromedriver.exe'
browser = webdriver.Chrome(PATH_WIN)
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)