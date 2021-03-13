from pages.strona_glowna import HMenu
from pages.hamburger import HamburgerMenuClicks
from PageObjectsLocators import HamburgerMenuResults
from tests.main_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestHamburgerMenu(BaseTest):
    """
    Test menu hamburger
    """
    
    def setUp(self):
        super().setUp()
        sg = HMenu(self.driver)
    
    @unittest.skip
    def test_mapa(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_mapa()
        assert EC.element_to_be_clickable(HamburgerMenuResults.WYBOR_WOJEWODZTWA)
    
    @unittest.skip
    def test_plakat(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_plakat()
        assert EC.element_to_be_clickable(HamburgerMenuResults.NAZWA_STACJI)
    
    @unittest.skip
    def test_utrudnienia(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_utrudnienia()
        assert EC.element_to_be_clickable(HamburgerMenuResults.NAZWA_STACJI1)
    
    @unittest.skip
    def test_poradnik(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_poradnik()
        assert EC.element_to_be_clickable(HamburgerMenuResults.HELP_INPT)
    
    def test_mobilka(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_mobilka()
        assert EC.text_to_be_present_in_element(HamburgerMenuResults.POBIERZ_APP, "Pobierz aplikację mobilną na swoją platformę:") is False
    
    @unittest.skip
    def test_kontakt(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_kontakt()
        assert EC.element_to_be_clickable(HamburgerMenuResults.FORMULARZ_KONTAKTOWY_BTN)
        sg.hamburger_menu()

    @unittest.skip
    def test_szukanie_poloczen(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_kontakt()
        hm.click_polaczenia()

    @unittest.skip
    def test_close(self):
        hm = HamburgerMenuClicks(self.driver)
        hm.click_close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
