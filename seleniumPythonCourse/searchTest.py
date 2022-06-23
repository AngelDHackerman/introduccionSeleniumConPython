import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# * By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service

class Search(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s = Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(5) # ? hace que espere 5 segundos

    def test_search_text_field(self):
      search_field = self.driver.find_element(By.ID, "search") # ID "search" viene de la pagina web que queremos testear.

    def test_search_text_field_by_name(self):
      search_field = self.driver.find_element(By.NAME, "q")

    def test_search_text_field_class_name(self):
      search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def tearDown(self):
        self.driver.quit() # cierra la ventana para evitar el consumo de recursos

if __name__ == '__main__':
    unittest.main(verbosity = 2)