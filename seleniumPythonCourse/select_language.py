from lib2to3.pgen2 import driver
from select import select
from typing_extensions import Self
import unittest
from selenium import webdriver

# * By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# todo: Con esto podemos selecionar los lenguajes 
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest, unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com')

  def test_select_language(self):
    exp_options = ['English', 'French', 'German'] # idiomas que tiene nuestra pagina de pruebas
    act_options = [] # aqui vamos a guardar las opciones que eligamos cuando las estemos testeando

    select_language = Select(self.driver.find_element(By.ID, 'select-language')) # ? aqui seleccionamos el lenguaje que queremos

    self.assertEqual(3, len(select_language.options)) # ? Aqui validamos que select_language efectivamente tiene 3 optiones 

    for option in select_language.options:
      act_options.append(option.text)

    self.assertEqual(exp_options, act_options) # * valida que las opciones que escribimos en exp_options sean iguales a las que agregamos en act_options

    self.assertEqual('English', select_language.first_selected_option.text) # * Asi verificamos que el lenguaje por defecto en la pagina es el ingles.

    select_language.select_by_visible_text('German') # Seleccionamos el lenguaje para que sea el aleman
    self.assertTrue('store=german' in self.driver.current_url) # ? validamos que la pagina este efectivamente en aleman.

    select_language = Select(self.driver.find_element(By.ID, 'select-language'))
    select_language.select_by_index(0) # * aqui regresamos la pagina a ingles, [0] porque ingles es el primero en la lista.
  
  # def tearDown(self):
  #   self.driver.quit()  # cierra la ventana para evitar el consumo de recursos


if __name__ == '__main__':
  unittest.main(verbosity = 2) # verbosity = 2 indica el nivel de detalle que la consola nos regresara.