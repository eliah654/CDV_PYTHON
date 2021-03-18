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
    
    def rozklad_stacje_rezultat(self, result_object):
        resultat = "t"
        if result_object == 1:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT1).text
        elif result_object == 2:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT2).text
        elif result_object == 3:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT3).text
        elif result_object == 4:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT4).text
        elif result_object == 5:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT5).text
        elif result_object == 6:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT6).text
        elif result_object == 7:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT7).text
        elif result_object == 8:
            resultat = self.driver.find_element(*SiecRozkladObjects.OBJECT_RESULTAT8).text
        elif result_object == 9:
            resultat = self.driver.find_element(*SiecRozkladObjects.ERROR_MESSAGE1).text
        return resultat
    
    def podaj_linie(self, nrlini):
        self.driver.find_element(*SiecRozkladObjects.WEDLUG_LINI).click()
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_LINI_FIELD)
        if EC.element_to_be_clickable(element):
            element.send_keys(nrlini)
            sleep(2)
            element.send_keys(Keys.ENTER)
    
    def podaj_numer_tablicy(self, nrtablicy):
        self.driver.find_element(*SiecRozkladObjects.WEDLUG_TABLICY).click()
        element = self.driver.find_element(*SiecRozkladObjects.WEDLUG_TABLICY_FIELD)
        if EC.element_to_be_clickable(element):
            element.send_keys(nrtablicy)
            sleep(1)
            element.send_keys(Keys.ENTER)
