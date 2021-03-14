from pages.main_page import MainPage
from PageObjectsLocators import SiecRozkladObjects
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SieciowyRozkladJazdyOperacje(MainPage):
    
    def rodzaj_sieciowego_rozkladu_jazdy(self, rodzaj):
        
        if rodzaj == 1:
            if not EC.element_to_be_clickable(SiecRozkladObjects.WEDLUG_STACJI_FIELD):
                self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI).click()
        elif rodzaj == 2:
            if not EC.element_to_be_clickable(SiecRozkladObjects.WEDLUG_LINI_FIELD):
                self.driver.find_element(*SiecRozkladObjects.WEDLUG_LINI).click()
        elif rodzaj == 3:
            if not EC.element_to_be_clickable(SiecRozkladObjects.WEDLUG_TABLICY_FIELD):
                self.driver.find_element(*SiecRozkladObjects.WEDLUG_TABLICY).click()
        else:
            "ups mamy błąd"
    
    def podaj_stacje(self, stacja):
        
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI_FIELD)
        element.send_keys(stacja)
        sleep(1)
        element.send_keys(Keys.ENTER)
        
    def rozklad_stacje_resultat(self):
        resultat = []
        resultat.append(self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI_RESULTAT1))
        resultat.append(self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI_RESULTAT2))
        resultat.append(self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI_RESULTAT3))
        return resultat
    
    def podaj_linie(self, nrlini):
        
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_LINI_FIELD)
        element.send_keys(nrlini)
        element.send_keys(Keys.ENTER)
    
    def podaj_numer_tablicy(self, nrtablicy):
        
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_TABLICY_FIELD)
        element.send_keys(nrtablicy)
        element.send_keys(Keys.ENTER)
