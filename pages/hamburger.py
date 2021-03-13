from pages.main_page import MainPage
from PageObjectsLocators import HamburgerMenu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HamburgerMenuClicks(MainPage):
    
    def _verify_page(self):
        hmenu = WebDriverWait(self.driver, 5)
        hmenu.until(EC.element_to_be_clickable(HamburgerMenu.MENU_WHOLE))
    
    
    def click_polaczenia(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_POLACZENIA)
        element.click()

    def click_mapa(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_MAPA)
        element.click()
        
    def click_plakat(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_PLAKAT)
        element.click()
        
    def click_utrudnienia(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_UTRUDNIENIA)
        element.click()
        
    def click_poradnik(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_PORADNIK)
        element.click()
        
    def click_mobilka(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_MOBILKA)
        element.click()
        
    def click_kontakt(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_KONTAKT)
        element.click()
        
    def click_close(self):
        element = self.driver.find_element(*HamburgerMenu.MENU_CLOSE)
        element.click()