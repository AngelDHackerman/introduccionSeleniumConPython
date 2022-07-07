from itertools import product
import unittest # ? Esto nos da un reporte de las pruebas en la consola.
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# * By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service

class SearchTests(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s = Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("https://demo.onestepcheckout.com/") # sujeto de pruebas
        driver.maximize_window()
        driver.implicitly_wait(5) # ? hace que espere 5 segundos

    def test_search_tee(self):
      driver = self.driver
      search_field = driver.find_element_by_class_name('q')
      search_field.clear()

      search_field.send_keys('tee')
      search_field.submit()

    def test_search_salt_shaker(self):
      driver = self.driver
      search_field = driver.find_element(By.NAME, 'q')

      search_field.send_keys('salt shaker')
      search_field.submit()

      products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
      self.assertEqual(1, len(products))

    def tearDown(self):
      self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2) # verbosity = 2 indica el nivel de detalle que la consola nos regresara.