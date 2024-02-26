from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import telebot
with open('setting.txt', 'r') as setting:
    settings = setting.readlines()
bot = telebot.TeleBot('6748506826:AAGveR40uvujvbPillxDBFE0Qdy43aKHB58')
chrome_options = Options()
chrome_options.add_argument ("--no-sandbox")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)
url = 'https://app.whales.market/'
driver.get(url)
driver.maximize_window()
sell = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div[2]')
buy = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div[1]')
b1 = '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[8]/button'
b2 = '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[9]/button'
#bot.send_message(5894748201, 'dvdv')
N = 0
def find_coin(coin):
    q = 1
    while True:
        element = driver.find_element(By.XPATH, f'/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[{q}]').text.split('\n')[0]
        if element.replace('\n', '') != coin.replace('\n', ''):
            q += 1
        else:
            driver.find_element(By.XPATH,
                                          f'/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[{q}]').click()
def sell_(coin, price_sell):
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[8]/button').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[9]/button').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[9]/button').click()
    except:
        pass
    time.sleep(3)
    sell.click()
    time.sleep(2)
    find_coin(coin)
    time.sleep(1)
    n = 1
    dictionary = {}
    while True:
        try:
            element = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]/div/div[2]/div[1]/div[1]/div/div').text
            href = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]').get_attribute('href')
            n += 1
            dictionary.update({href: element.replace('\n/Token', '').replace('$', '')})
        except:
            break
    with open('used.txt', 'r') as file:
        data = file.readlines()
    dictionary = {k: v for k, v in dictionary.items() if float(v) >= price_sell}
    for used_key in data:
        used_key = used_key.strip()
        if used_key.replace('\n', '') in dictionary:
            del dictionary[used_key]
    with open('used.txt', 'a') as file:
        for key in dictionary.keys():
            file.write(f"{key}\n")
    if dictionary:
        dict_text = "\n".join(f"{key}: {value}" for key, value in dictionary.items())
        print(dict_text)
        bot.send_message(5894748201, f'Продаж {coin}\n{dict_text}')


def buy_(coin, price_buy):
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[8]/button').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[9]/button').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[9]/button').click()
    except:
        pass
    time.sleep(3)
    buy.click()
    time.sleep(2)
    find_coin(coin)
    time.sleep(1)
    n = 1
    dictionary = {}
    while True:
        try:
            element = driver.find_element(By.XPATH,
                                          f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]/div/div[2]/div[1]/div[1]/div/div').text
            href = driver.find_element(By.XPATH,
                                       f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]').get_attribute(
                'href')
            n += 1
            dictionary.update({href: element.replace('\n/Token', '').replace('$', '')})
        except:
            break
    with open('used.txt', 'r') as file:
        data = file.readlines()
    dictionary = {k: v for k, v in dictionary.items() if float(v) <= price_buy}
    for used_key in data:
        used_key = used_key.strip()
        if used_key.replace('\n', '') in dictionary:
            del dictionary[used_key]
    with open('used.txt', 'a') as file:
        for key in dictionary.keys():
            file.write(f"{key}\n")
    if dictionary:
        dict_text = "\n".join(f"{key}: {value}" for key, value in dictionary.items())
        print(dict_text)
        bot.send_message(5894748201, f'Купівля: {coin}\n{dict_text}')

n = 0
while True:
    for x in range(len(settings[2].split(':')[1].split(','))):
        sell_(settings[2].split(':')[1].split(',')[x].split('\n')[0], float(settings[0].split(':')[1].split(',')[x]))
        time.sleep(3)
        buy_(settings[2].split(':')[1].split(',')[x].split('\n')[0], float(settings[1].split(':')[1].split(',')[x]))
        n+=1
        if int(settings[3].split(':')[1]) != 0 and n%int(settings[3].split(':')[1]) == 0:
            bot.send_message(5894748201, f'Цикл№{n}')
