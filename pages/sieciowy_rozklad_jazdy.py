from pages.main_page import MainPage
from PageObjectsLocators import SiecRozkladObjects, BottomMenu
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC


class SieciowyRozkladJazdyOperacje(MainPage):

    def podaj_stacje(self, stacja):
        
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI_FIELD)
        element.send_keys(stacja)
        element.send_keys(Keys.ENTER)
    
    def podaj_linie(self, nrlini):
        
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_LINI_FIELD)
        element.send_keys(nrlini)
        element.send_keys(Keys.ENTER)
    
    def podaj_numer_tablicy(self, nrtablicy):
        
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_TABLICY_FIELD)
        element.send_keys(nrtablicy)
        element.send_keys(Keys.ENTER)
    
    

