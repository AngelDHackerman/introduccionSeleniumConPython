from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchTest2 import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)


smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
  "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs) # **kwargs agregando un numero arbitrario de paramentros (pueden ser uno o varios parametros)
runner.run(smoke_test)