from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class DynamicControls(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= "./chromedriver")
    driver = self.driver
    driver.get("http://the-internet.herokuapp.com")
    driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()  # le damos click al enlace que dice: Dynamic Controls

  def test_dynamic_controls(self):
    pass

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main(verbosity= 2)