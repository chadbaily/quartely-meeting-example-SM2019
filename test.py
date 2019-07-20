# Base Imports
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Other imports
import time
import unittest

# Sleep for a few to give thigs time to get started
time.sleep(5)


class Selenium(unittest.TestCase):
    # def setUp(self):
    #     # Create a new instance of the Firefox driver
    #     self.driver = webdriver.Remote(
    #         desired_capabilities=DesiredCapabilities.CHROME,
    #         command_executor="http://hub:4444/wd/hub"
    #     )

    #     self.driver.implicitly_wait(20)

    # def test_CBT(self):
    #     self.driver.get(
    #         'http://crossbrowsertesting.github.io/selenium_example_page.html')
    #     self.assertEqual("Selenium Test Example Page", self.driver.title)
    #     self.test_result = 'pass'
    #     self.driver.quit()
    def setUp(self):
        self.chrome = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.chrome.implicitly_wait(20)

        self.firefox = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        self.firefox.implicitly_wait(20)
    
    def tearDown(self):
        self.chrome.quit()
        self.firefox.quit()

    def test_Chrome(self):
        self.chrome.get('https://www.google.com')
        title = self.chrome.title
        self.assertEqual(title, 'Google')

    def test_FireFox(self):
        self.firefox.get('https://www.google.com')
        title = self.firefox.title
        self.assertEqual(title, 'Google')


if __name__ == '__main__':
    unittest.main()
