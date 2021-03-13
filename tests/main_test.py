import unittest
from selenium import webdriver
from time import sleep


class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome() #webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://portalpasazera.pl")


    def tearDown(self):
        sleep(2)
        self.driver.quit()
