import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browers:
    def __init__(self):
        pass

    def browers():
        serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.facebook.com/")
        driver.forward()
        driver.get("https://www.amazon.in/")
        driver.forward()
        driver.save_screenshot('facebook.png')
        screenshot = Image.open('facebook.png')
        screenshot.show()
        driver.maximize_window()
        title = driver.title
        print(title)
        time.sleep(4)
        driver.close()


if __name__ == "__main__":
    b=Browers
    b.browers()