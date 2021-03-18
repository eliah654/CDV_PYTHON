from pages.main_page import MainPage
from PageObjectsLocators import SearchPage
from selenium.webdriver.common.keys import Keys


class SearchFormClicks(MainPage):
    """
    Wypełnianie formularza wyszukiwania połączeń
    """
    
    def clear_field(self, linkDoPola):
        linkDoPola.send_keys(Keys.LEFT_CONTROL, 'a')
        linkDoPola.send_keys(Keys.BACKSPACE)
    
    def wyjazd_z(self, miasto):
        element = self.driver.find_element(*SearchPage.WYJAZD_INPT)
        element.send_keys(miasto)
    
    def przyjazd_do(self, miasto):
        element = self.driver.find_element(*SearchPage.PRZYJAZD_INPT)
        element.send_keys(miasto)
    
    def set_date(self, dmy):
        element = self.driver.find_element(*SearchPage.DATA_INP)
        element.click()
        self.clear_field(element)
        element.send_keys(dmy)
    
    def set_houer(self, godzinah):
        element = self.driver.find_element(*SearchPage.GODZINA_INP)
        element.click()
        self.clear_field(element)
        element.send_keys(godzinah)
    
    def polaczenia_bezposrednie(self):
        element = self.driver.find_element(*SearchPage.POLACZENIA_BEZPOSREDNIE_CB)
        element.click()
    
    def click_szukaj(self):
        element = self.driver.find_element(*SearchPage.SZUKAJ_BTN)
        element.click()
    
    def wiecej_szukaj_open(self):
        element = self.driver.find_element(*SearchPage.WIECJE_OPCJI_WYSZUKIWANIA)
        element.click()
    
    def wiecej_szukaj_close(self):
        element = self.driver.find_element(*SearchPage.ZAMKNIJ_OPCJE_WYSZUKIWANIA)
        element.click()
