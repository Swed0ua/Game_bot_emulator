import sys
import asyncio
import config
import config2
from bot_operator_scr import *
import config_scr
import os
import sys
import telebot
import tempfile
import psutil
import subprocess
from config import user_id1, user_id2
import pyautogui
from time import sleep
from bot_operator import send_message
from pywinauto import Application
import numpy as np
# from PIL import ImageGrab
import pyscreenshot as ImageGrab
import cv2
# import easyocr
import os
import pytesseract
from PIL import Image, ImageEnhance
from bot_operator import send_message
# from bot_operator2 import send_message2
import os
import telebot
import tempfile
import time

bot = telebot.TeleBot(config.operator_token)
bot2 = telebot.TeleBot(config2.operator_token)

open_window = r"C:\Users\allo_\PycharmProjects\hero\images\777.png"
full_window = r"C:\Users\allo_\PycharmProjects\hero\images\full.png"
app_icon = r"C:\Users\allo_\PycharmProjects\hero\images\app_icon_1.png"
guild = r"C:\Users\allo_\PycharmProjects\hero\images\guild_1.png"
dungeon = r"C:\Users\allo_\PycharmProjects\hero\images\dungeon_2.png"
vboi = r"C:\Users\allo_\PycharmProjects\hero\images\vboi_1.png"
napastj = r"C:\Users\allo_\PycharmProjects\hero\images\napastj_1.png"
autoboi = r"C:\Users\allo_\PycharmProjects\hero\images\autoboi_1.png"
ok_button = r"C:\Users\allo_\PycharmProjects\hero\images\ok_1.png"
activate = r"C:\Users\allo_\PycharmProjects\hero\images\activate_1.png"
zabratj = r"C:\Users\allo_\PycharmProjects\hero\images\zabratj_1.png"
mertv = r"C:\Users\allo_\PycharmProjects\hero\images\mertv_1.png"
victory = r"C:\Users\allo_\PycharmProjects\hero\images\victory.png"
close = r"C:\Users\allo_\PycharmProjects\hero\images\close.png"
back = r"C:\Users\allo_\PycharmProjects\hero\images\back.png"
check_kom = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\check_kom.png"
check_reklama = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\reklama2,reklama1,reklama,reklama3.png"
# check_reklama = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\reklama1.png"


# корординатор картинок для нападения на вид титанов
pr1 = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\1.png"
pr2 = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\2.png"
pr3 = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\3.png"
pr4 = r"C:\Users\allo_\PycharmProjects\hero\images\2_komn\4.png"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open('image.png')
filename = 'image.png'


def stop_program():
    # закрывает эмулятор
    for proc in psutil.process_iter():
        if proc.name() == 'Nox.exe':
            proc.terminate()
    # sys.exit()


def check_off():
    # проверка на выключение бота
    with open('data.txt', "r") as file:
        data = file.read()
        if data == "off":
            print("Бот и Эмулятор остановлены/закрыты по вашей команде")
            send_message("Бот и Эмулятор остановлены/закрыты по вашей команде")
            for proc in psutil.process_iter():
                if proc.name() == 'Nox.exe':
                    proc.terminate()
            sys.exit()
        else:
            pass


def check_rek():
    # проверяет на наличие рекламы
    try:
        check = pyautogui.locateOnScreen(check_reklama)
        if check:
            with open("data.txt", 'w') as f:
                f.write("off")
            print("Выскочила рекалама, Бот и Эмулятор остановлены/закрыты, запустите бота")
            send_message("Выскочила рекалама, Бот и Эмулятор остановлены/закрыты, запустите бота")

    except:
        pass


def start_app():
    # запускает эмулятор и игру
    check_off()
    button1 = pyautogui.locateOnScreen(app_icon, confidence=0.7)
    sleep(1)
    pyautogui.doubleClick(button1)
    print("Хроники Хаоса запущены")
    send_message("Хроники Хаоса запущены")
    sleep(20)
    check_off()
    button = pyautogui.locateOnScreen(open_window, confidence=0.8)
    pyautogui.click(button)
    button = pyautogui.locateOnScreen(full_window, confidence=0.8)
    pyautogui.click(button)

    print("Раскрываем окно на весь экран, ждем загрузуки эмулятора..")
    send_message("Раскрываем окно на весь экран, ждем загрузуки эмулятора..")

    """Ожидание появления элемента на экране"""
    print("Ждем появления элемента - Гильдия")
    send_message("Ждем появления элемента - Гильдия")
    r = None
    count = 1000
    def seson_update():
        exec
        
    while r is None:
        check_off()
        count -= 1
        r = pyautogui.locateOnScreen(guild, confidence=0.8)
        if count == 0:
            print("Ошибка при запуске эмулятора с игрой..")
            send_message("Ошибка при запуске эмулятора с игрой..")
            break
        else:
            if r != None:
                print("Переходим в Гильдию")
                send_message("Переходим в Гильдию")
                button2 = pyautogui.locateOnScreen(guild, confidence=0.8)
                pyautogui.click(button2)
            else:
                continue

    print("Ждем появления элемента - Подземелье")
    send_message("Ждем появления элемента - Подземелье")
    r2 = None
    count = 1000
    while r2 is None:
        check_off()
        count -= 1
        r2 = pyautogui.locateOnScreen(dungeon, confidence=0.8)
        if count == 0:
            print("Ошибка при запуске эмулятора с игрой..")
            send_message("Ошибка при запуске эмулятора с игрой..")
            break
        else:
            if r2 != None:
                print("Переходим в Подземелье")
                send_message("Переходим в Подземелье")
                button3: object = pyautogui.locateOnScreen(dungeon, confidence=0.7)
                pyautogui.click(button3)
            else:
                continue

# обявляет переменную в которую будет записыватся время последнего действия бота, если нет никакого действия 30с бот перезапускается. сразу передается +60с это фора для времени запуска бота
last_time = time.time() + 60
event_click_count = 0


def floor():
    def restart_floor():
        # перезапускает бота если нет никакого действия 30с
        global last_time
        sleep(1)
        stop_program()
        sleep(5)
        start_app()
        sleep(5)
        last_time = time.time() + 60
        floor()

    def check_photos():
        ## проверка на рекламу и ошибки
        img_link = r'C:\Users\allo_\PycharmProjects\hero\images\photos'
        images = os.listdir(img_link)
        for img in images:
            r = pyautogui.locateOnScreen(img_link + f'\\{img}', confidence=0.8)
            if r:
                print("Замечена реклама / ошибка, эмулятор перезапускается")
                send_message("Замечена реклама / ошибка, эмулятор перезапускается")
                send_message('Источник перезагрузки - ' + img)
                restart_floor()

    def add_event_click():
        # записывает действия в счетчик
        global last_time
        global event_click_count

        last_time = time.time()
        event_click_count += 1

    def check_event_time():
        # проверка на отсутствия действий (30сек)
        global last_time
        time_now = time.time()
        if time_now - last_time > 30:
            print("Игра остановилась (возможно из за промаха по кнопке), эмулятор перезапускается")
            send_message("Игра остановилась (возможно из за промаха по кнопке), эмулятор перезапускается")
            restart_floor()

    room_count = 0

    while True:
        # общий цикл игры
        check_off()
        check_rek()
        check_event_time()

        r3 = None
        count = 25
        while r3 is None:
            # цикл на проверку кнопки в бой или кнопки забрать (сохранение уровня)
            check_off()
            check_event_time()
            count -= 1
            r3 = pyautogui.locateOnScreen(vboi, confidence=0.7)

            def check_activate():
                button7 = pyautogui.locateOnScreen(activate, confidence=0.7)
                if button7 != None:
                    pyautogui.click(button7)
                    sleep(2)
                    print("Нажатие на кнопку Забрать (сохранение уровня)")
                    button10 = pyautogui.locateOnScreen(zabratj, confidence=0.7)
                    pyautogui.click(button10)

            if r3 != None:
                print("В Бой🏴‍☠️!")
                send_message("В Бой🏴‍☠️!")
                button3 = pyautogui.locateOnScreen(vboi, confidence=0.7)
                add_event_click()
                pyautogui.click(button3)



                sleep(0.1)
                # button10: object = pyautogui.locateOnScreen(vboi, confidence=0.7)
                # pyautogui.click(button10)

                # Проверка на попадание по кнопке в Бой
                btn_check = pyautogui.locateOnScreen(vboi, confidence=0.5)
                if btn_check != None:
                    sleep(0.5)
                    btn_check = pyautogui.locateOnScreen(vboi, confidence=0.7)
                    print('NONER *****************************************************')
                    pyautogui.click(btn_check)


            else:
                check_activate()

        # считывание комната ординарная или двойная
        type_komnata = None
        r3 = None
        count = 5
        while r3 is None:
            check_rek()
            check_event_time()
            check_off()
            count -= 1
            r3 = pyautogui.locateOnScreen(check_kom)
            if count == 0:
                print("❷")
                send_message("двойная❷")
                type_komnata = 2
                #  если комната одинарная
                break
            else:
                if r3 != None:
                    print("❶")
                    send_message("одинарная❶")
                    type_komnata = 1

                    break
                else:
                    continue

        # Если комната двойная
        if type_komnata > 1:
            check_status = 1
            while True:
                check_rek()
                check_off()
                check_event_time()

                r3 = None
                count = 2
                while r3 is None:
                    check_rek()
                    check_off()
                    count -= 1
                    r3 = pyautogui.locateCenterOnScreen(pr1)
                    if count == 0:
                        print("...❌❌❌")
                        send_message("...❌❌❌")
                        break

                    else:
                        if r3 != None:
                            print("🏥 '.")
                            send_message("🏥 '.")
                            item1 = str(r3)
                            item2 = item1.split(",")
                            itemX = item2[0]
                            itemY = item2[1]
                            itemX2 = ''.join([i for i in itemX if i.isdigit()])
                            itemY2 = ''.join([i for i in itemY if i.isdigit()])
                            itemX2 = int(itemX2)
                            itemY2 = int(itemY2)
                            itemY2 = itemY2 + 155
                            # sleep(0.2)
                            pyautogui.click(x=itemX2, y=itemY2)
                            check_status = 0

                            break
                        else:
                            continue

                if check_status == 0:
                    break
                else:
                    pass

                r3 = None
                count = 2
                while r3 is None:
                    check_rek()
                    check_off()
                    check_event_time()
                    count -= 1
                    r3 = pyautogui.locateCenterOnScreen(pr2)
                    if count == 0:
                        print("...❌🔵")
                        send_message("...❌🔵")
                        break
                    else:
                        if r3 != None:
                            print("...🔵")
                            send_message("...🔵 ")
                            item1 = str(r3)
                            item2 = item1.split(",")
                            itemX = item2[0]
                            itemY = item2[1]
                            itemX2 = ''.join([i for i in itemX if i.isdigit()])
                            itemY2 = ''.join([i for i in itemY if i.isdigit()])
                            itemX2 = int(itemX2)
                            itemY2 = int(itemY2)
                            itemY2 = itemY2 + 155
                            # sleep(0.2)
                            pyautogui.click(x=itemX2, y=itemY2)
                            check_status = 0

                            break
                        else:
                            continue

                if check_status == 0:
                    break
                else:
                    pass

                r3 = None
                count = 2
                while r3 is None:
                    check_rek()
                    check_off()
                    check_event_time()
                    count -= 1
                    r3 = pyautogui.locateCenterOnScreen(pr3)
                    if count == 0:
                        print("...❌🔴")
                        send_message("...❌🔴 ")
                        break
                    else:
                        if r3 != None:
                            print("...🔴 ")
                            send_message("...🔴 ")
                            item1 = str(r3)
                            item2 = item1.split(",")
                            itemX = item2[0]
                            itemY = item2[1]
                            itemX2 = ''.join([i for i in itemX if i.isdigit()])
                            itemY2 = ''.join([i for i in itemY if i.isdigit()])
                            itemX2 = int(itemX2)
                            itemY2 = int(itemY2)
                            itemY2 = itemY2 + 155
                            # sleep(0.2)
                            pyautogui.click(x=itemX2, y=itemY2)
                            check_status = 0



                if check_status == 0:
                    break
                else:
                    pass

            # кнопка Автобой
            sleep(1)

            pyautogui.click(x=1540, y=886)

            # Считывание Все ли Титаны живы
            r100 = None
            count = 8
            while r100 is None:
                check_rek()
                check_off()
                check_event_time()
                count -= 1
                r100 = pyautogui.locateOnScreen(mertv, confidence=0.7)
                if count == 0:
                    print("️ВЫЖИЛИ ВСЕ,ИДЁМ ДАЛЬШЕ....2....❷")
                    send_message("ВЫЖИЛИ ВСЕ, ИДЁМ ДАЛЬШЕ ...2.....❷")
                    pyautogui.click(x=1317, y=897)
                    break
                else:
                    if r100 != None:
                        print(
                            "Один ТИТАН † - ВНИМАНИЕ (выбете ручное управление, кнопка назад - нажата) эмулятор закрыт")
                        send_message(
                            "Один ТИТАН † - ВНИМАНИЕ (берите ручное управление, кнопка назад - нажата) эмулятор закрыт")
                        path = tempfile.gettempdir() + 'screenshot.png'
                        screenshot = ImageGrab.grab()
                        screenshot.save(path, 'PNG')
                        bot.send_photo(user_id1, open(path, 'rb'))
                        bot.send_photo(user_id2, open(path, 'rb'))
                        # нажимаем назад
                        pyautogui.keyDown('ESC')
                        sleep(2)
                        button = pyautogui.locateOnScreen(back, confidence=0.7)
                        pyautogui.click(button)
                        button = pyautogui.locateOnScreen(back, confidence=0.7)
                        pyautogui.click(button)
                        for proc in psutil.process_iter():
                            if proc.name() == 'Nox.exe':
                                proc.terminate()
                        sys.exit()
                    else:
                        continue

        # Если комната ординарная
        else:
            # Нажимаем кнопку ОК
            pyautogui.click(x=946, y=853)


            # НАЖАТЬ КНОПКУ АВТОБОЙ

            #sleep(1)

            pyautogui.doubleClick(x=1540, y=886, interval=0.1)

            # Считывание Все ли Титаны живы
            r100 = None
            count = 8
            while r100 is None:
                check_rek()
                check_off()
                check_event_time()

                count -= 1
                r100 = pyautogui.locateOnScreen(mertv, confidence=0.7)
                if count == 0:
                    print("ВЫЖИЛИ ВСЕ,ИДЁМ ДАЛЬШЕ ....1....❶")
                    send_message("️ВЫЖИЛИ ВСЕ,ИДЁМ ДАЛЬШЕ...1....❶")
                    pyautogui.click(x=1317, y=897)
                    break
                else:
                    if r100 != None:
                        print(
                            "Один ТИТАН †☠️ - ВНИМАНИЕ (берите ручное управление, кнопка назад - нажата) эмулятор закрыт")
                        send_message(
                            "Один ТИТАН †☠️ - ВНИМАНИЕ (берите ручное управление, кнопка назад - нажата) эмулятор закрыт")
                        path = tempfile.gettempdir() + 'screenshot.png'
                        screenshot = ImageGrab.grab()
                        screenshot.save(path, 'PNG')
                        bot.send_photo(user_id1, open(path, 'rb'))
                        bot.send_photo(user_id2, open(path, 'rb'))
                        bot2.send_photo(config2.user_id1, open(path, 'rb'))
                        bot2.send_photo(config2.user_id2, open(path, 'rb'))
                        # нажимаем назад
                        pyautogui.keyDown('ESC')
                        sleep(2)
                        button = pyautogui.locateOnScreen(back, confidence=0.7)
                        pyautogui.click(button)
                        button = pyautogui.locateOnScreen(back, confidence=0.7)
                        pyautogui.click(button)

                        for proc in psutil.process_iter():
                            if proc.name() == 'Nox.exe':
                                proc.terminate()
                        sys.exit()
                    else:
                        continue
        check_photos()


if __name__ == "__main__":
    check_rek()
    check_off()
    start_app()
    floor()
