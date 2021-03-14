from pages.main_page import MainPage
from PageObjectsLocators import HamburgerMenu, SearchPage, BottomMenu, SiecRozkladObjects
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HMenu(MainPage):
    """
    Hamburger menu
    """
    def _verify_page(self):
        #weryfikacj czy to poprawna strona
        assert "Wyszukiwarka rozkładu jazdy pociągów PKP PLK S.A. - Portal Pasażera - PKP Polskie Linie Kolejowe S.A." in self.driver.title
        
    def hamburger_menu(self):
        #kliknięcie hamburger menu
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*SearchPage.POLITYKA_PRYWATNOSCI).click()
        element = wait.until(EC.element_to_be_clickable(HamburgerMenu.MENU_BTN))
        element.click()

class SearchForm(MainPage):
    """
    Formularz wyszukiwania połączeń
    """
    def _verify_page(self):
        #weryfikacj czy to poprawna strona
        assert "Wyszukiwarka rozkładu jazdy pociągów PKP PLK S.A. - Portal Pasażera - PKP Polskie Linie Kolejowe S.A." in self.driver.title
        
    
    def search_form(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*SearchPage.POLITYKA_PRYWATNOSCI).click()
        element = wait.until(EC.element_to_be_clickable(SearchPage.WYJAZD_INPT))
        element.click()

class SieciowyRozkladJazdy(MainPage):
    
    def _verify_page(self):
        #weryfikacj czy to poprawna strona
        assert "Wyszukiwarka rozkładu jazdy pociągów PKP PLK S.A. - Portal Pasażera - PKP Polskie Linie Kolejowe S.A." in self.driver.title

    def zaladuj_sieciowy_rozklad(self, rodzaj):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(BottomMenu.SIECIOWY_ROZKLAD))
        self.driver.find_element(*BottomMenu.SIECIOWY_ROZKLAD).click()
        if rodzaj == 1:
            wait.until(EC.element_to_be_clickable(SiecRozkladObjects.WEDLUG_STACJI))
            self.driver.find_element(*SiecRozkladObjects.WEDLUG_STACJI).click()
        elif rodzaj == 2:
            wait.until(EC.element_to_be_clickable(SiecRozkladObjects.WEDLUG_LINI))
            self.driver.find_element(*SiecRozkladObjects.WEDLUG_LINI).click()
        elif rodzaj == 3:
            wait.until(EC.element_to_be_clickable(SiecRozkladObjects.WEDLUG_TABLICY))
            self.driver.find_element(*SiecRozkladObjects.WEDLUG_TABLICY).click()
        else:
            "ups mamy błąd"
        
