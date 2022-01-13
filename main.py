from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from config import USERNAME, PASSWORD, PATH
from time import sleep
import random

class AutoWriter:
	def __init__(self):
		self.i = int(input('Write a count your friend: '))
		self.message = input('Write a message: ')
		service = Service(PATH)
		options = webdriver.ChromeOptions()
		self.driver = webdriver.Chrome(
			service=service,
			options=options
		)
		self.driver.get('https://www.instagram.com/')
		self.username = USERNAME
		self.password = PASSWORD

	def auto_login(self):
		sleep(5)

		user_input = self.driver.find_element(By.NAME, 'username')
		user_input.clear()
		user_input.send_keys(self.username)
		sleep(3)

		pass_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
		pass_input.clear()
		sleep(3)
		pass_input.send_keys(self.password)
		sleep(5)
		pass_input.send_keys(Keys.ENTER)
		sleep(5)

		close_tabs = self.driver.find_element(By.CSS_SELECTOR, 'button[class="sqdOP yWX7d    y3zKF     "]')
		close_tabs.click()
		sleep(5)

		try:
			notify_tabs = self.driver.find_element(By.CSS_SELECTOR, 'button[class="aOOlW   HoLwm "]')
			notify_tabs.click()
			sleep(5)
		except Exception as ex:
			print(ex)


	def auto_writemessage(self):
		open_messenger = self.driver.find_element(By.CSS_SELECTOR, 'a[class="xWeGp"]')
		open_messenger.click()
		sleep(5)

		subject = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="         DPiy6    qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              "]')
		subject[random.randint(0, self.i)].click()
		sleep(3)

		message = self.driver.find_element(By.TAG_NAME, 'textarea')
		message.clear()
		message.send_keys(self.message)
		sleep(3)

		send_button = self.driver.find_element(By.CSS_SELECTOR, 'div[class="             qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm                                        JI_ht                                                                      "]> button[class="sqdOP yWX7d    y3zKF     "]')
		send_button.click()
		sleep(10)

	def run(self):
		print('Starting...')
		self.auto_login()
		self.auto_writemessage()


if __name__ == '__main__':
	app = AutoWriter()
	app.run()
