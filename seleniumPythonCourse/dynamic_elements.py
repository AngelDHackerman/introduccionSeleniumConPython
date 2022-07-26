from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unittest

class DynamicElements(unittest.TestCase):

  # alistamos el webDriver y le pasamos la direccion URL a testear
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= "./chromedriver")
    driver = self.driver
    driver.get("http://the-internet.herokuapp.com")  # https://the-internet.herokuapp.com/disappearing_elements
    driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

  # Aqui hacemos las pruebas automatizadas
  def test_name_elements(self):
    driver = self.driver

    options = []
    menu = 5 
    tries = 1

    while len(options) < 5:
      options.clear()

      for i in range(menu):
        try:
          option_name = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
          options.append(option_name.text)
          print(options)
        except:
          print(f'Option number {i + 1} is NOT FOUND')
          tries += 1
          driver.refresh()

    print(f'Finished in {tries} tries')

  # Se cierra el programa para no consumir demasiados recurso
  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)