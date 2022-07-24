import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")

driver.save_screenshot('facebook.png')
screenshot = Image.open('facebook.png')
screenshot.show()
time.sleep(2)
driver.close()