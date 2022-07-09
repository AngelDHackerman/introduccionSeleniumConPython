from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By # Nos permite selectionar los elementos por "id", "name", etc de manera mas facil. Recibe 2 parametros (By.name, 'nameOfItem')


class CompareProducts(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com')

  def test_compare_products_removal_alert(self):
    driver = self.driver
    search_field = driver.find_element(By.NAME, 'q')
    search_field.clear()  # todo: con esto eliminamos lo que este escrito en el input de busqueda

    search_field.send_keys('tee') # todo: Aqui le pasamos lo que queremos escribir en el input de busqueda
    search_field.submit() # se envia lo que buscabamos 

    driver.find_element(By.CLASS_NAME, 'link-compare').click() # selecionamos la opcion de 'comparar' las camisas en nuestra pagina
    driver.find_element(By.LINK_TEXT, 'Clear All').click() # Limpiamos las comparaciones que hizo la pagina 

    alert = driver._switch_to.alert  # ? Cambianos la atencion del navegador al alert
    alert_text = alert.text

    # Aqui validamos que el texto que le pasamos sea igual al texto que nos muestra el alert en la pagina.
    self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

    alert.accept() # todo: aceptamos lo que nos muestre la alerta


if __name__ == '__main__':
  unittest.main(verbosity= 2) # verbosity es el nivel de detalle que queremos que nos devuelva la consola. 
