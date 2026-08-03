#import webdriver module from selenium package
from selenium import webdriver

#installing webdriver and launch chrome browser
driver = webdriver.Chrome()

#open google.com web page
driver.get("https://www.google.com")

# close the browser window
driver.quit()