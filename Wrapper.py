from SeleniumUsingPython.Interview import *
from selenium.webdriver.common.by import By


class Wrapper():

    def __init__(self, driver):
        self.driver = driver


    def getByLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        if locatorType == "xpath":
            return By.XPATH
        if locatorType == "css":
            return By.CSS_SELECTOR
        if locatorType == "classname":
            return By.CLASS_NAME
        else:
            print("LocatorType " + str(locatorType) + "not correct supported")


    def getElement(self,locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByLocatorType(locatorType)
            element = self.driver.find_element_by(byType, locator)
            print("Element Found")
        except:
            print("Element Not Found")


    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False
