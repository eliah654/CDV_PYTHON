from pages.strona_glowna import HMenu
from pages.hamburger import HamburgerMenuClicks
from PageObjectsLocators import HamburgerMenuResults, HamburgerMenu, SearchPage
from tests.main_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
import unittest
from time import sleep


class TestHamburgerMenu(BaseTest):
    """
    Test menu hamburger
    """
    
    def setUp(self):
        super().setUp()
        sg = HMenu(self.driver)
        sg.hamburger_menu()
       
    def test_mapa(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_mapa()
        sleep(1)
        assert EC.element_to_be_clickable(HamburgerMenuResults.WYBOR_WOJEWODZTWA)
    
    def test_plakat(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_plakat()
        sleep(1)
        assert EC.element_to_be_clickable(HamburgerMenuResults.NAZWA_STACJI)
    
    def test_utrudnienia(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_utrudnienia()
        sleep(1)
        assert EC.element_to_be_clickable(HamburgerMenuResults.NAZWA_STACJI1)
    
    def test_poradnik(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_poradnik()
        sleep(1)
        assert EC.element_to_be_clickable(HamburgerMenuResults.HELP_INPT)
    
    def test_mobilka(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_mobilka()
        sleep(1)
        assert EC.text_to_be_present_in_element(HamburgerMenuResults.POBIERZ_APP, "Pobierz aplikację mobilną na swoją platformę:")
    
    def test_kontakt(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_kontakt()
        sleep(1)
        assert EC.element_to_be_clickable(HamburgerMenuResults.FORMULARZ_KONTAKTOWY_BTN)
    
    def test_szukanie_poloczen(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_kontakt()
        sleep(2)
        hm.click_hmenu()
        sleep(2)
        hm.click_polaczenia()
        sleep(2)
        assert EC.element_to_be_clickable(SearchPage.SZUKAJ_BTN)
    
    def test_close(self):
        hm = HamburgerMenuClicks(self.driver)
        sleep(1)
        hm.click_close()
        sleep(1)
        assert EC.element_to_be_clickable(HamburgerMenu.MENU_POLACZENIA)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
