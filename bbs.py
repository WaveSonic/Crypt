from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import datetime
import threading
from selenium import webdriver
import traceback
from selenium.webdriver.common.action_chains import ActionChains
import telebot
import pyautogui
with open('setting.txt', 'r') as setting:
    settings = setting.readlines()
bot = telebot.TeleBot('6748506826:AAGveR40uvujvbPillxDBFE0Qdy43aKHB58')
chrome_options = Options()
chrome_options.add_argument ("--no-sandbox")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
#bot.send_message(-4132338664, 'dvdv')
#bot.send_message(637485048, 'dvdv')
driver = webdriver.Chrome(options=chrome_options)
url = 'https://app.whales.market/'
driver.get(url)
driver.maximize_window()

def t1(coin, price):
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div[1]').click()
    time.sleep(2)
    def find_coin(coin):
            q = 0
            table = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div')
            while True:
                try:
                    element_by_name = table.find_element(By.XPATH, f".//*[contains(text(), '{coin}')]")
                    element_by_name.click()
                    time.sleep(2)
                    break
                except:
                    pyautogui.moveTo(int(settings[4].split(':')[1].split(',')[0]), int(settings[4].split(':')[1].split(',')[1]))
                    pyautogui.click()
                    time.sleep(1)
                    continue


    def create(coin, price_buy):
        n = 1
        dictionary = {}
        NN = 0
        while True:
            try:
                time.sleep(0.7)
                element = driver.find_element(By.XPATH,
                                              f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]/div/div[2]/div[1]/div[1]/div/div').text
                href = driver.find_element(By.XPATH,
                                           f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]').get_attribute(
                    'href')
                n += 1
                NN += 1
                dictionary.update({href: element.replace('\n/Token', '').replace('$', '')})
                if NN >= 5:
                    break
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
            bot.send_message(637485048, f'Купівля: {coin}\n{dict_text}')

    try:
        find_coin(coin)
        create(coin, price)
    except Exception as e:
        error_traceback = traceback.format_exc()  # Зберігаємо трасування помилки як рядок
        error_message = f'Потік Купівля {coin}, Зруйновано\n{error_traceback}'
        bot.send_message(637485048, error_message[:4047])

def t2(coin, price):
    driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div[2]').click()
    time.sleep(2)
    def find_coin(coin):
            q = 0
            table = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div')
            while True:
                try:
                    element_by_name = table.find_element(By.XPATH, f".//*[contains(text(), '{coin}')]")
                    element_by_name.click()
                    time.sleep(2)
                    break
                except:
                    pyautogui.moveTo(int(settings[4].split(':')[1].split(',')[0]),
                                     int(settings[4].split(':')[1].split(',')[1]))
                    pyautogui.click()
                    time.sleep(1)
                    continue

    def create(coin, price_buy):
        n = 1
        NN = 0
        dictionary = {}
        while True:
            time.sleep(0.7)
            try:
                element = driver.find_element(By.XPATH,
                                              f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]/div/div[2]/div[1]/div[1]/div/div').text
                href = driver.find_element(By.XPATH,
                                           f'//*[@id="__next"]/main/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div/div/a[{n}]').get_attribute(
                    'href')
                n += 1
                dictionary.update({href: element.replace('\n/Token', '').replace('$', '')})
                if NN >= 5:
                    break
            except:
                break
        with open('used.txt', 'r') as file:
            data = file.readlines()
        dictionary = {k: v for k, v in dictionary.items() if float(v) >= price_buy}
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
            bot.send_message(637485048, f'Продаж: {coin}\n{dict_text}')
    try:
        find_coin(coin)
        create(coin, price)
    except Exception as e:
        error_traceback = traceback.format_exc()  # Зберігаємо трасування помилки як рядок
        error_message = f'Потік Продаж {coin}, Зруйновано\n{error_traceback}'
        bot.send_message(637485048, error_message[:4047])
def main_1():
    COUNT = 0
    while True:
        now = datetime.datetime.now()
        for x in range(len(settings[2].replace('\n', '').split(':')[1].split(','))):
            t1(settings[2].replace('\n', '').split(':')[1].split(',')[x], float(settings[1].replace('\n', '').split(':')[1].split(',')[x]))
            t2(settings[2].replace('\n', '').split(':')[1].split(',')[x], float(settings[0].replace('\n', '').split(':')[1].split(',')[x]))
        print(datetime.datetime.now() - now)
        COUNT += 1
        if COUNT%int(settings[3].split(":")[1]) == 0:
            bot.send_message(637485048, f"Цикл: {COUNT}")

def main_2():
    bot = telebot.TeleBot('6748506826:AAGveR40uvujvbPillxDBFE0Qdy43aKHB58')
    @bot.message_handler(func=lambda message: True)
    def start(message):
        if message.text == 'Hello':
            bot.send_message(message.chat.id, message.text)

    bot.polling(none_stop=True)


thr1 = threading.Thread(target=main_1)
thr2 = threading.Thread(target=main_2)

thr1.start()
thr2.start()