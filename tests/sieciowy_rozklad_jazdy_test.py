from pages.sieciowy_rozklad_jazdy import SieciowyRozkladJazdyOperacje
from pages.strona_glowna import SieciowyRozkladJazdy
from tests.main_test import BaseTest
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
class SieciowyRozkladJazyTest(BaseTest):

    def setUp(self):
        super().setUp()
        sg = SieciowyRozkladJazdy(self.driver)
        sg.zaladuj_sieciowy_rozklad()
    
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
    
    def test_error_message_verification1(self):
        wst = SieciowyRozkladJazdyOperacje(self.driver)
        wst.podaj_stacje("sodjfuhno")
        sleep(2)

        assert "Wpisana nazwa stacji jest nieprawidłowa. Prosimy o zwrócenie uwagi na poprawną pisownię." in wst.rozklad_stacje_rezultat(9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
