import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.forward()
driver.get("https://www.amazon.in/")
driver.save_screenshot('facebook.png')
time.sleep(4)
driver.close()