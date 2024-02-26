import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
with open('setting.txt', 'r') as setting:
    settings = setting.readlines()
chrome_options = Options()
chrome_options.add_argument ("--no-sandbox")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
#bot.send_message(-4132338664, 'dvdv')
#bot.send_message(637485048, 'dvdv')
driver = webdriver.Chrome(options=chrome_options)
url = 'https://app.whales.market/'
driver.maximize_window()
driver.get(url)
time.sleep(1)
pyautogui.moveTo(int(settings[4].split(':')[1].split(',')[0]), int(settings[4].split(':')[1].split(',')[1]))
pyautogui.click()
time.sleep(10)