from pages.main_page import MainPage
from PageObjectsLocators import HamburgerMenu, SearchPage, BottomMenu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HMenu(MainPage):
    """
    Hamburger menu
    """

    def _verify_page(self):
        get_title = self.driver.title
        assert "Wyszukiwarka rozkładu jazdy pociągów PKP PLK S.A. - Portal Pasażera - PKP Polskie Linie Kolejowe S.A." in get_title
        
    def hamburger_menu(self):
        #kliknięcie hamburger menu
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*SearchPage.POLITYKA_PRYWATNOSCI).click()
        wait.until(EC.element_to_be_clickable(HamburgerMenu.MENU_BTN))
        self.driver.find_element(*HamburgerMenu.MENU_BTN).click()

class SearchForm(MainPage):
    """
    Formularz wyszukiwania połączeń
    """
    def _verify_page(self):
        get_title = self.driver.title
        assert "Wyszukiwarka rozkładu jazdy pociągów PKP PLK S.A. - Portal Pasażera - PKP Polskie Linie Kolejowe S.A." in get_title
        
    
    def search_form(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*SearchPage.POLITYKA_PRYWATNOSCI).click()
        wait.until(EC.element_to_be_clickable(SearchPage.WYJAZD_INPT))
        self.driver.find_element(*SearchPage.WYJAZD_INPT).click()

class SieciowyRozkladJazdy(MainPage):
    
    def _verify_page(self):

        assert "Wyszukiwarka rozkładu jazdy pociągów PKP PLK S.A. - Portal Pasażera - PKP Polskie Linie Kolejowe S.A." in self.driver.title

    def zaladuj_sieciowy_rozklad(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(BottomMenu.SIECIOWY_ROZKLAD))
        self.driver.find_element(*SearchPage.POLITYKA_PRYWATNOSCI).click()
        self.driver.find_element(*BottomMenu.SIECIOWY_ROZKLAD).click()
        

