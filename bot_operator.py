import telebot
import config

def send_message(message):
    operator = telebot.TeleBot(config.operator_token)
    operator.send_message(config.user_id1, message)
    operator.send_message(config.user_id2, message)

