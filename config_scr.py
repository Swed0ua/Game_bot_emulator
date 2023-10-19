import telebot
import config2

def send_message2(message):
    operator = telebot.TeleBot(config2.operator_token)
    operator.send_message(config2.user_id1, message)
    operator.send_message(config2.user_id2, message)

