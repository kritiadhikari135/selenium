from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(2)

#locate username web element 
# username = driver.find_element(By.ID, value="user-name")

#  using and condition
username = driver.find_element(By.XPATH, value="//input[@type='text' and @id = 'user-name' ]")


# enter user name 
username.send_keys("standard_user")

# by using xpath 

# ....... username = driver.find_element(By.XPATH, valure: "//input[@id = 'user_name']")


password = driver.find_element(By.ID,value= "password")
password.send_keys("secret_sauce")

time.sleep(5)

#locate login button 
loginBtn = driver.find_element(By.XPATH, value="//input[@id ='login-button' or id ='wrong-id']")
loginBtn.click()
time.sleep(2)

driver.quit()

