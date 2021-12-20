import os
import telebot
from telebot import types

# Токент бота
TOKEN = '5026643977:AAHXaXR3EwkVKYZ2Hv1lubUc_iz6n61ty60'

HELLO = "Wanna find spotify of best rock bands? Let's start."
HELP = "This bot was created in order to find the best rock bands on spotify"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itmbtn1 = telebot.types.KeyboardButton('QUEEN')
    itmbtn2 = telebot.types.KeyboardButton('RHCP')
    itmbtn3 = telebot.types.KeyboardButton('Green Day')
    markup.add(itmbtn1, itmbtn2, itmbtn3)
    bot.send_message(message.chat.id, HELLO, reply_markup=markup)

@bot.message_handler(commands='help')
def send_help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(content_types='text')
def text(message):
    if message.text == 'QUEEN':
        photo = open('..\QUEEN.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d?si=sWOhOszfSnK8pZ1ZDMewVA')
    elif message.text == 'RHCP':
        photo = open('..\RHCP.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://open.spotify.com/artist/0L8ExT028jH3ddEcZwqJJ5?si=0WqTkcOHQsOlPZANgID_9A')
    elif message.text == 'Green Day':
        photo = open('..\Green Day.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://open.spotify.com/artist/7oPftvlwr6VrsViSDV7fJY?si=ZNVkwFC2QAeGJ5zfmiE6-Q')

bot.infinity_polling()