import os
import time
from selenium import  webdriver
from SeleniumUsingPython.Interview.Wrapper import *
from SeleniumUsingPython.webdriver.common.by import By
from selenium.webdriver.support.select import Select



driverLocation = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation);
# driver = webdriver.firefox

class Controller():

    def test(self):

        wrap = Wrapper(driver)

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        elementExist = wrap.isElementPresent("name", By.ID)
        print(str(elementExist))




oController = Controller()
oController.test()