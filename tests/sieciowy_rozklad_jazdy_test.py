from pages.sieciowy_rozklad_jazdy import SieciowyRozkladJazdyOperacje
from pages.strona_glowna import SieciowyRozkladJazdy
from tests.main_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as ActC
from time import sleep
import unittest
import csv
from ddt import ddt, data, unpack


@ddt
class SieciowyRozkladJazyTest(BaseTest):
    
    def open_file(file_name):
        rows = []
        data_file = open(file_name, 'rt')
        reader = csv.reader(data_file)
        next(reader, None)
        for row in reader:
            rows.append(row)
        data_file.close()
        return rows
    
    def setUp(self):
        super().setUp()
        sg = SieciowyRozkladJazdy(self.driver)
        sg.zaladuj_sieciowy_rozklad()
    
    @data(*open_file("DDT_data4b.csv"))
    @unpack
    def test_wedlug_stacji(self, stacja, liczbawyszukiwan, nrtablicy1, nrtablicy2, nrtablicy3, nrtablicy4, nrtablicy5):
        wst = SieciowyRozkladJazdyOperacje(self.driver)
        #wst.rodzaj_sieciowego_rozkladu_jazdy(1)
        wst.podaj_stacje(stacja)
        sleep(5)
        wyniki_weryfikacja = wst.rozklad_stacje_resultat()
        print(wyniki_weryfikacja)
        print(EC.text_to_be_present_in_element(wyniki_weryfikacja[0]))

    @unittest.skip
    @data(*open_file("DDT_data4a.csv"))
    @unpack
    def test_wedlug_lini(self, nrlini, liczbawyszukiwan, nrtablicy1, nrtablicy2, nrtablicy3, nrtablicy4, nrtablicy5):
        pass

    @unittest.skip
    @data(*open_file("DDT_data4c.csv"))
    @unpack
    def test_wedlug_tablicy(self, nrtablicy,nazwatablicy):
        pass

"""
    "Sieciowy rozkład jazdy - Według stacji - Wybór stacji - Portal Pasażera - PKP Polskie Linie Kolejowe S.A."
    "Sieciowy rozkład jazdy - Według linii - Wybór linii - Portal Pasażera - PKP Polskie Linie Kolejowe S."
    "Sieciowy rozkład jazdy - Według tablicy - Wybór tablicy - Portal Pasażera - PKP Polskie Linie Kolejowe S.A."
"""

if __name__ == "__main__":
    unittest.main(verbosity=2)