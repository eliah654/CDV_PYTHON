from pages.search_page import SearchFormClicks
from pages.strona_glowna import SearchForm
from pages.result_page import ResultPageClicks
from tests.main_test import BaseTest
from PageObjectsLocators import ResultsPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as ActC
from time import sleep
import unittest
import csv
from ddt import ddt, data, unpack
import os


def open_file(file_name):
    rows = []
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(THIS_FOLDER, file_name)
    data_file = open(file_path, 'rt')
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    data_file.close()
    return rows


@ddt
class TrainConnectionsTest(BaseTest):
    """
    Test wyszukiwania połączeń
    """

    def setUp(self):
        super().setUp()
        sg = SearchForm(self.driver)
        sg.search_form()
    
    @data(*open_file("DDT_data.csv"))
    @unpack
    def test_search_ddt(self, godzinka, dzien, wyjazd, przyjazd, pociag, numer, ifnazwa):
        
        fc = SearchFormClicks(self.driver)
        fc.set_houer(godzinka)
        fc.set_date(dzien)
        fc.wyjazd_z(wyjazd)
        fc.przyjazd_do(przyjazd)
        sleep(1)
        fc.polaczenia_bezposrednie()
        sleep(1)
        fc.click_szukaj()
        
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(ResultsPage.NOWE_WYSZUKIWANIE_BT))
        tytul = self.driver.title
        if tytul.startswith("Wyniki wyszukiwania"):
            nazwa_pociagu = ResultPageClicks.check_pociag(ifnazwa, pociag)
            numer_pociagu = ResultPageClicks.check_numer_pociagu(numer)
            assert numer in numer_pociagu.text
            assert pociag in nazwa_pociagu.text
    
    @data(*open_file("DDT_data2.csv"))
    @unpack
    def test_search_ddt2(self, godzinka, dzien, wyjazd, przyjazd, pociag, numer, ifnazwa, przesiadki, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C):
        
        fc = SearchFormClicks(self.driver)
        fc.set_houer(godzinka)
        fc.set_date(dzien)
        fc.wyjazd_z(wyjazd)
        fc.przyjazd_do(przyjazd)
        sleep(1)
        fc.click_szukaj()
        
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(ResultsPage.NOWE_WYSZUKIWANIE_BT))
        tytul = self.driver.title
        if tytul.startswith("Wyniki wyszukiwania"):
            
            if int(przesiadki) == 1:
                if EC.element_to_be_clickable(ResultsPage.PRZESIADKI1_BTN):
                    rp = ResultPageClicks(self.driver)
                    rp.clcik_przesiadki(1)
                    sleep(7)
                    
                    wynik = [rp.check_przesiadki(pociag, numer, ifnazwa, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C)]
                    
                    assert wynik[0][1] == "OK"
                    assert wynik[0][1] == "OK"
            
            elif int(przesiadki) == 2:
                if EC.element_to_be_clickable(ResultsPage.PRZESIADKI2_BTN):
                    sleep(5)
                    action_on_element = ActC(self.driver)
                    action_on_element.move_to_element(self.driver.find_element(*ResultsPage.PRZESIADKI2_BTN)).perform()
                    rp = ResultPageClicks(self.driver)
                    rp.clcik_przesiadki(2)
                    sleep(6)
                    wynik = [rp.check_przesiadki(pociag, numer, ifnazwa, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C)]
                    
                    assert wynik[0][1] == "OK"
                    assert wynik[0][1] == "OK"
            
            elif int(przesiadki) == 3:
                if EC.element_to_be_clickable(ResultsPage.PRZESIADKI3_BTN):
                    sleep(5)
                    action_on_element = ActC(self.driver)
                    action_on_element.move_to_element(self.driver.find_element(*ResultsPage.PRZESIADKI3_BTN)).perform()
                    rp = ResultPageClicks(self.driver)
                    rp.clcik_przesiadki(3)
                    sleep(5)
                    wynik = [rp.check_przesiadki(pociag, numer, ifnazwa, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C)]
                    
                    assert wynik[0][1] == "OK"
                    assert wynik[0][1] == "OK"
            
            elif int(przesiadki) == 4:
                if EC.element_to_be_clickable(ResultsPage.PRZESIADKI4_BTN):
                    sleep(5)
                    action_on_element = ActC(self.driver)
                    action_on_element.move_to_element(self.driver.find_element(*ResultsPage.PRZESIADKI4_BTN)).perform()
                    rp = ResultPageClicks(self.driver)
                    rp.clcik_przesiadki(4)
                    sleep(5)
                    wynik = [rp.check_przesiadki(pociag, numer, ifnazwa, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C)]
                    
                    assert wynik[0][1] == "OK"
                    assert wynik[0][1] == "OK"
            
            elif int(przesiadki) == 5:
                
                if EC.element_to_be_clickable(ResultsPage.PRZESIADKI5_BTN):
                    sleep(5)
                    action_on_element = ActC(self.driver)
                    action_on_element.move_to_element(self.driver.find_element(*ResultsPage.PRZESIADKI5_BTN)).perform()
                    
                    rp = ResultPageClicks(self.driver)
                    rp.clcik_przesiadki(5)
                    sleep(5)
                    wynik = [rp.check_przesiadki(pociag, numer, ifnazwa, prze1A, prze1B, prze1C, prze2A, prze2B, prze2C, prze3A, prze3B, prze3C, prze4A, prze4B, prze4C)]
                    
                    assert wynik[0][1] == "OK"
                    assert wynik[0][1] == "OK"
            
            else:
                print("nie ma takiego pociągu")
    
    @data(*open_file("DDT_data3.csv"))
    @unpack
    def test_search_ddt(self, godzinka, dzien, wyjazd, przyjazd):
        fc = SearchFormClicks(self.driver)
        fc.set_houer(godzinka)
        fc.set_date(dzien)
        fc.wyjazd_z(wyjazd)
        fc.przyjazd_do(przyjazd)
        sleep(1)
        fc.polaczenia_bezposrednie()
        sleep(1)
        fc.click_szukaj()
        sleep(5)
        element = self.driver.find_element(*ResultsPage.BRAK_POLACZENIA)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(verbosity=2)
