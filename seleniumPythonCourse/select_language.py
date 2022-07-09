from lib2to3.pgen2 import driver
from select import select
from typing_extensions import Self
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

# * By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class LanguageOptions(unittest, unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demp-store.seleniumacademy.com')

  def test_select_language(self):
    pass

  
  # def tearDown(self):
  #   self.driver.quit()  # cierra la ventana para evitar el consumo de recursos


if __name__ == '__main__':
  unittest.main(verbosity = 2) # verbosity = 2 indica el nivel de detalle que la consola nos regresara.