from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class test_ama:
    def __init__(self, driver):
        self.driver = driver
        self.nav_button = "//input[@id='nav-search-submit-button']"
        self.featured = " //span[contains(text(),'Featured')]"
        self.select = "//a[@id='s-result-sort-select_4']"

    def amazon_nav_click(self):
        self.driver.find_element(by=By.XPATH, value=self.nav_button).click()

    def amazon_feature_click(self):
        self.driver.find_element(by=By.XPATH, value=" //span[contains(text(),'Featured')]").click()

    def amazon_sort_click(self):
        self.driver.find_element(by=By.XPATH, value=self.select).click()

    def script_do(self):
        self.driver.execute_script("alert('search successfully');")
        time.sleep(4)

        self.driver.switch_to.alert.dismiss()
        print("end of file writting")
