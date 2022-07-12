import unittest
from selenium import webdriver

class ExplicitWaitTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    self.driver.get('http://demo-store.seleniumacademy.com')

  def test_account_link(self):
    pass

  def test_create_new_customer(self):
    pass

  def tearDown(self):
    self.driver.quit() # cierra la ventana para evitar el consumo de recursos

if __name__ == '__main__':
  unittest.main(verbosity = 2) # verbosity = 2 indica el nivel de detalle que la consola nos regresara.