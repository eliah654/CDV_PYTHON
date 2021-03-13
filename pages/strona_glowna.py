from pages.main_page import MainPage
from PageObjectsLocators import HamburgerMenu, SearchPage
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
