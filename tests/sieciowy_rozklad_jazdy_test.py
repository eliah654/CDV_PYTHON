from pages.sieciowy_rozklad_jazdy import SieciowyRozkladJazdyOperacje
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
        sg = SearchForm(self.driver)
        sg.search_form()
    
    @data(*open_file("DDT_data4a.csv"))
    @unpack
    def wedlug_stacji_test(self, stacja, liczbawyszukiwan, nrtablicy1, nrtablicy2, nrtablicy3, nrtablicy4, nrtablicy5):
        
        sjr = SieciowyRozkladJazdyOperacje(self.driver)
        sjr.podaj_stacje(stacja)
        

    @data(*open_file("DDT_data4b.csv"))
    @unpack
    def wedlug_lini_test(self, nrlini, liczbawyszukiwan, nrtablicy1, nrtablicy2, nrtablicy3, nrtablicy4, nrtablicy5):
        pass

    @data(*open_file("DDT_data4c.csv"))
    @unpack
    def wedlug_tablicy_test(self, nrtablicy,nazwatablicy):
        pass

    "Sieciowy rozkład jazdy - Według stacji - Wybór stacji - Portal Pasażera - PKP Polskie Linie Kolejowe S.A."
    "Sieciowy rozkład jazdy - Według linii - Wybór linii - Portal Pasażera - PKP Polskie Linie Kolejowe S."
    "Sieciowy rozkład jazdy - Według tablicy - Wybór tablicy - Portal Pasażera - PKP Polskie Linie Kolejowe S.A."