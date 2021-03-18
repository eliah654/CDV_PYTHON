import HtmlTestRunner
import unittest
from tests.hamburger_test import TestHamburgerMenu
from tests.search_page_test import TrainConnectionsTest
from tests.sieciowy_rozklad_jazdy_test import SieciowyRozkladJazyTest
import os

dir = os.getcwd()

hamburger_tests = unittest.TestLoader().loadTestsFromTestCase(TestHamburgerMenu)
search_tests = unittest.TestLoader().loadTestsFromTestCase(TrainConnectionsTest)
siec_test = unittest.TestLoader().loadTestsFromTestCase(SieciowyRozkladJazyTest)

test_suite = unittest.TestSuite([hamburger_tests, search_tests, siec_test])


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
