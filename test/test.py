# Base Imports
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Other imports
import time
import unittest

# Sleep for a few to give thigs time to get started
time.sleep(5)


class Selenium(unittest.TestCase):
    
    # Basic setup for the unit tests
    def setUp(self):
        self.chrome = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.chrome.implicitly_wait(20)

        self.firefox = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        self.firefox.implicitly_wait(20)
    
    # Tear down the unit tests and ensure that both browsers are quit properly
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
