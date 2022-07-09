import unittest # ? Esto nos da un reporte de las pruebas en la consola.
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
        driver.get("https://demo.onestepcheckout.com/") # sujeto de pruebas
        driver.maximize_window()
        driver.implicitly_wait(5) # ? hace que espere 5 segundos

    def test_search_text_field(self):
      search_field = self.driver.find_element(By.ID, "search") # ID "search" viene de la pagina web que queremos testear.

    def test_search_text_field_by_name(self):
      search_field = self.driver.find_element(By.NAME, "q") # 'q' es el nombre de la etiqueta que estamos testeando

    def test_search_text_field_class_name(self):
      search_field = self.driver.find_element(By.CLASS_NAME, "input-text") 

    def test_search_button_enabled(self):
      button = self.driver.find_element(By.CLASS_NAME, "button")

    def test_count_of_promo_images(self): # ? contara el numero de fotos en el banner de promo
      banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
      banners = banner_list.find_elements(By.TAG_NAME, 'img') # ? cuenta los tags "img" dentro del banner "promos'"
      self.assertEqual(3, len(banners)) # ? verifica si son 3 las imagenes del banner comparado con el largo del banner

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(By.XPATH,"//*[@id='top']/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img")

    def test_shopping_cart (self):
      shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")

    def tearDown(self):
      self.driver.quit() # cierra la ventana para evitar el consumo de recursos

if __name__ == '__main__':
  unittest.main(verbosity = 2) # verbosity = 2 indica el nivel de detalle que la consola nos regresara.