from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class RegisterNewUser(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= './chromedriver')
    driver = self.driver
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://demo-store.seleniumacademy.com')

  def test_new_user(self):
    driver = self.driver
    driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()  # ? click(), para abrir el log in de la pagina como si fuera un click humano
    driver.find_element(By.LINK_TEXT, 'Log In').click() # ? By.LINK_TEXT hace que se seleccione el texto indicado como link, en este caso el link es Log In

    create_account_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
    self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled()) # todo: .is_displayed() muestra si el boton esta visible y .is_enabled() muestra si esta habilitado, si esto es verdadero el siguiente paso es darle click
    create_account_button.click()

    self.assertEqual('Create New Customer Account', driver.title) # ? Esto verifica si el titulo de la ventana es igual al titulo de la ventana de nuestro driver. 

    first_name = driver.find_element(By.ID, 'firstname')
    middle_name = driver.find_element(By.ID, 'middlename') 
    last_name = driver.find_element(By.ID, 'lastname')
    email_address = driver.find_element(By.ID, 'email_address') 
    news_letter_subscription = driver.find_element(By.ID, 'is_subscribed')
    password = driver.find_element(By.ID, 'password')
    confirm_password = driver.find_element(By.ID, 'confirmation')
    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

  def tearDown(self):
    self.driver.implicitly_wait(3)
    self.driver.close()

if __name__ == '__main__':
  unittest.main(verbosity= 2)
