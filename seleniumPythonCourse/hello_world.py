import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWord(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path = './chromedriver') # traemos el driver para hacer las pruebas con Chrome
    driver = cls.driver
    driver.implicitly_wait(10) # hace que el programa espere 10 seg entre cada accion.

  def test_hello_world(self):
    driver = self.driver
    driver.get('https://www.platzi.com')

  def test_visit_wikipedia(self):
    self.driver.get('https://www.wikipedia.org')

  @classmethod
  def tearDown(cls):
    cls.driver.quit() # Esto cierra la ventana para evitar el uso de recursos. 

if __name__ == "__name__":
  unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))