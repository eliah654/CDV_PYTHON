import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://portalpasazera.pl")
       
      

    def tearDown(self):
        sleep(2)
        self.driver.quit()
