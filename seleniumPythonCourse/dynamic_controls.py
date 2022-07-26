from lib2to3.pgen2 import driver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ? Esto es para hacer las esperas entre eventos
from selenium.webdriver.support import expected_conditions as EC 
from selenium import webdriver

class DynamicControls(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= "./chromedriver")
    driver = self.driver
    driver.get("http://the-internet.herokuapp.com")
    driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()  # le damos click al enlace que dice: Dynamic Controls

  def test_dynamic_controls(self):
    driver = self.driver

    checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
    checkbox.click()  # damos click al checkbox

    remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
    remove_add_button.click()

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))  # ? Esperara 15seg hasta que el elemento sea clicable de nuevo
    remove_add_button.click()

    enable_disable_button = driver.find_element(By.CSS_SELECTOR, '#input-example > button')  # click al boton de enable / disable
    enable_disable_button.click()  # click al boton de enable / disable

    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))  # ? Esperara 15seg hasta que el elemento sea clicable de nuevo

    text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
    text_area.send_keys('Platzi')  # todo: asi es como se envian los textos desde selenium

    enable_disable_button.click()  # volvemos a deshabilitar el input


  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)