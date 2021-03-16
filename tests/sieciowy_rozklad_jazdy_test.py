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

    @unittest.skip
    @data(*open_file("DDT_data4b.csv"))
    @unpack
    def test_wedlug_stacji(self, stacja, liczbawyszukiwan, nrtablicy1, nrtablicy2, nrtablicy3, nrtablicy4, nrtablicy5):
        wst = SieciowyRozkladJazdyOperacje(self.driver)
        wst.podaj_stacje(stacja)
        sleep(5)
        
        assert wst.rozklad_stacje_rezultat(1) == liczbawyszukiwan

        if nrtablicy1 != "0":
            assert nrtablicy1 in wst.rozklad_stacje_rezultat(2)
        if nrtablicy2 != "0":
            assert nrtablicy2 in wst.rozklad_stacje_rezultat(3)
        if nrtablicy3 != "0":
            assert nrtablicy3 in wst.rozklad_stacje_rezultat(4)
        if nrtablicy4 != "0":
            assert nrtablicy4 in wst.rozklad_stacje_rezultat(5)
        if nrtablicy5 != "0":
            assert nrtablicy5 in wst.rozklad_stacje_rezultat(6)

    @unittest.skip
    @data(*open_file("DDT_data4a.csv"))
    @unpack
    def test_wedlug_lini(self, nrlini, liczbawyszukiwan, nrtablicy1, nrtablicy2, nrtablicy3, nrtablicy4, nrtablicy5):
        sleep(2)
        wst = SieciowyRozkladJazdyOperacje(self.driver)
        wst.podaj_linie(nrlini)
        sleep(5)
    
        assert wst.rozklad_stacje_rezultat(1) == liczbawyszukiwan
    
        if nrtablicy1 != "0":
            assert nrtablicy1 in wst.rozklad_stacje_rezultat(2)
        if nrtablicy2 != "0":
            assert nrtablicy2 in wst.rozklad_stacje_rezultat(3)
        if nrtablicy3 != "0":
            assert nrtablicy3 in wst.rozklad_stacje_rezultat(4)
        if nrtablicy4 != "0":
            assert nrtablicy4 in wst.rozklad_stacje_rezultat(5)
        if nrtablicy5 != "0":
            assert nrtablicy5 in wst.rozklad_stacje_rezultat(6)

    
    @data(*open_file("DDT_data4c.csv"))
    @unpack
    def test_wedlug_tablicy(self, nrtablicy, nazwatablicy):
        sleep(2)
        wst = SieciowyRozkladJazdyOperacje(self.driver)
        wst.podaj_numer_tablicy(nrtablicy)
        sleep(5)
        
        assert nrtablicy in wst.rozklad_stacje_rezultat(7)
        stacje = wst.rozklad_stacje_rezultat(8).replace('\n', ' ')
        assert nazwatablicy in stacje


if __name__ == "__main__":
    unittest.main(verbosity=2)