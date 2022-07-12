from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class AddRemoveElements(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

  def test_add_remove(self):
    pass

  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main(verbosity= 2)