import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

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
        driver.implicitly_wait(5)

    def test_search_text_field(self):
        dsearch_field = self.driver.find_element(By.ID, "search")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)