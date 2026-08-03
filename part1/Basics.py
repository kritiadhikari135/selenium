# navigaating urls:

#steps: 
# import webdriver module from selenium package 

from selenium import webdriver

# importing time package
import time

# instantiate webdriver and launch chrome browser 
driver = webdriver.Chrome()


#open url
# navigate to google

driver.get("https://www.google.com")

# sleep for 2 sec
time.sleep(2)

# navigate to youtube
driver.get("https://www.youtube.com")
time.sleep(2)

#go back to google
driver.back()
time.sleep(2)

#go forward
driver.forward()
time.sleep(2)

#refresh current pagr
driver.refresh()
time.sleep(2)

#closing the browser
driver.quit()