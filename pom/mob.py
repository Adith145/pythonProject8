import time
import unittest
from html_test_report import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from mobsearch.searchmob import test_ama
from selenium.webdriver.common.action_chains import ActionChains


# class DemoImplicitWait():
class Testsample(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\seleniumwebdriver\chromedriver.exe")
        #time.sleep(3)

    def test_amazon(self):
        action = ActionChains(self.driver)
        self.driver.implicitly_wait(40)
        self.driver.get("https://www.amazon.in")
        titleOfWebPage = self.driver.title
        self.assertNotEqual("Amazon", titleOfWebPage, "PASSED")
        # seconds

        #self.driver.save_screenshot(r"C:\Users\Admin\OneDrive\Desktop\screenschot\homepage1.png")
        self.driver.maximize_window()

        # capture the title of the page
        amazon = self.driver.title
        # time.sleep(4)
        a =self.driver.find_element(by=By.XPATH, value=" //input[@id='twotabsearchtextbox']")
        action.scroll_to_element(a)
        a.send_keys("oneplus Mobile under 30000")

      #  self.driver.save_screenshot(r"C:\Users\Admin\OneDrive\Desktop\screenschot\search MOBILE.png")
        time.sleep(4)
        cls = test_ama(self.driver)
        cls.amazon_nav_click()
        self.driver.implicitly_wait(5)
        cls.amazon_feature_click()
        self.driver.implicitly_wait(5)
        cls.amazon_sort_click()
        time.sleep(4)
        cls.script_do()

        # time.sleep(4)
    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()