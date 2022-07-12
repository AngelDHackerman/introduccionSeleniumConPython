import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait  # todo: esto nos permite usar las expected conditions. 
from selenium.webdriver.support import expected_conditions as EC # todo: esto nos permite usar las expected conditions. 

class ExplicitWaitTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    self.driver.get('http://demo-store.seleniumacademy.com')

  def test_account_link(self):
    WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, 'select-language').get_attribute('lenght') == '3')

    account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT'))) 
    account.click()

  def test_create_new_customer(self):
    self.driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()

    my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.LINK_TEXT, 'My account'))
    my_account.click()

    create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(By.LINK_TEXT, 'CREATE AN ACCOUNT'))
    create_account_button.click()

    WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

  def tearDown(self):
    self.driver.quit() # cierra la ventana para evitar el consumo de recursos

if __name__ == '__main__':
  unittest.main(verbosity = 2) # verbosity = 2 indica el nivel de detalle que la consola nos regresara.