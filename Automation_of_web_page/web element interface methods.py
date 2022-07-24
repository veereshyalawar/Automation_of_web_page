import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.instagram.com/")
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH,"//input[@name ='username']")
print(element.get_attribute("name"))
print(element.send_keys("veeresh"))
print(element.clear())
print(element.is_displayed())
print(element.location)
