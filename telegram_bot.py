import googletrans
from googletrans import Translator
import telebot

bot = telebot.TeleBot("You Token")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! , How can I help you?")


@bot.message_handler(commands=['translate', 'Translate'])
def echo_msg(message):
    bot.register_next_step_handler(message, callback=extract_msg)


def extract_msg(message):
    translator = Translator()
    lang = translator.detect(message.text)
    if lang.lang == 'th':
        translator = Translator()
        result = translator.translate(message.text, src='th', dest='en')
        bot.reply_to(message, result.text)
    else:
        translator = Translator()
        result = translator.translate(message.text, src='en', dest='th')
        bot.reply_to(message, result.text)


bot.polling()
