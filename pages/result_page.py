from pages.main_page import MainPage
from PageObjectsLocators import ResultsPage
from selenium.webdriver.common.keys import Keys

class ResultPageClicks(MainPage):
    
    def check_pociag(self, ifnazwa, pociag):

        if int(ifnazwa) == 1:
            nazwa_pociagu = self.driver.find_element_by_xpath("//span[contains(text(),'" + pociag + "')]")
            return nazwa_pociagu
        elif int(ifnazwa) == 0:
            nazwa_pociagu = self.driver.find_element_by_xpath("//p[contains(text(),'" + pociag + "')]")
            return nazwa_pociagu
        elif int(ifnazwa) == 2:
            nazwa_pociagu = self.driver.find_element_by_xpath("// div[ @class ='search-results__item row abt-focusable search-results__item--expanded'] // div[@ class ='col-9 col-12--phone relative'] // div[@ class ='row row-station box--flex block-phone'] // div[@ class ='col-3 col-12--phone inline-center box--flex--column'] // p[@ class ='item-label'][contains(text(), 'osobowy')]")
            return nazwa_pociagu

    def check_numer_pociagu(self, numer):
        ret_xpath = self.driver.find_element_by_xpath("//p[contains(text(),'" + numer + "')]")
        return ret_xpath


    def clcik_przesiadki(self, poziom):
        
        if poziom == 1:
            element = self.driver.find_element(*ResultsPage.PRZESIADKI1_BTN)
            element.click()
        elif poziom == 2:
            element = self.driver.find_element(*ResultsPage.PRZESIADKI2_BTN)
            element.click()
        elif poziom == 3:
            element = self.driver.find_element(*ResultsPage.PRZESIADKI3_BTN)
            element.click()
        elif poziom == 4:
            element = self.driver.find_element(*ResultsPage.PRZESIADKI4_BTN)
            element.click()
        elif poziom == 5:
            element = self.driver.find_element(*ResultsPage.PRZESIADKI5_BTN)
            element.click()
    
    def check_nazwa_numer(self, ifnazwa, pociag, numer):
        cnn = ResultPageClicks(self.driver)
        nazwa_numer = [cnn.check_pociag(ifnazwa, pociag), cnn.check_numer_pociagu(numer)]
        return nazwa_numer
    
    def verification(self, ifnazwa, pociag, numer):
        numer_nazwa = self.check_nazwa_numer(ifnazwa, pociag, numer)
        assert numer_nazwa[0] != Exception
        assert numer_nazwa[1] != Exception
        return "OK"

    def check_przesiadki(self, pociag, numer, ifnazwa, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C):
    
        sprawdzenie = []
        # pierwszy pociąg
        assert self.verification(ifnazwa, pociag, numer) == "OK"
        sprawdzenie.append("OK")
        # drugi pociąg
        if prze1A != "0":
            assert self.verification(prze1C, prze1A, prze1B) == "OK"
            sprawdzenie.append("OK")
    
        # trzeci pociąg
        elif prze2A != "0":
            assert self.verification(prze2C, prze2A, prze2B) == "OK"
            sprawdzenie.append("OK")
    
        # czwarty pociąg
        elif prze3A != "0":
            assert self.verification(prze3C, prze3A, prze3B) == "OK"
            sprawdzenie.append("OK")
    
        # piąty pociąg
        elif prze4A != "0":
            assert self.verification(prze4C, prze4A, prze4B) == "OK"
            sprawdzenie.append("OK")
    
        else:
            sprawdzenie.append("NOT")
    
        return sprawdzenie
        
    def brak_polaczenia(self):
        pass
    