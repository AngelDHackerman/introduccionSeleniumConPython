from time import sleep
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class NavigationTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('https://google.com/')

  def test_browser_navigation(self):
    driver = self.driver

    search_field = driver.find_element(By.NAME, 'q')
    search_field.clear() # limpiamos lo que pueda estar en la barra de busqueda
    search_field('platzi') # pasamos que queremos buscar en google
    search_field.submit() # damos "click" en el boton de buscar

    driver.back()   # ? mueve hacia atras del historial
    sleep(3)    # espera por 3 segundos antes de pasar a la siguente linea
    driver.forward() # ? mueve hacia adelante
    sleep(3)    # espera por 3 segundos antes de pasar a la siguente linea
    driver.refresh() # ? refresca la pagina
    sleep(3)    # espera por 3 segundos antes de pasar a la siguente linea

  
  def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
  unittest.main(verbosity= 2)