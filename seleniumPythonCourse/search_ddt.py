from lib2to3.pgen2 import driver
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

class SearchDDT(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= "./chromedriver")
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com')

  def test_search_ddt(sefl):
    pass

  def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
  unittest.main(verbosity= 2)