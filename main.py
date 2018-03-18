# -*- coding: utf-8 -*-
import telebot
import constants





bot = telebot.TeleBot("589935777:AAHYS__Ii5o90oKbNJWoF9oeilBTbruKh2g") #объект бот



@bot.message_handler(commands=['start','help'])
def handle_start(message):

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Меню')
    user_markup.row('Узнать кто сейчас выступает')
    user_markup.row('Голосовать за участников!')
    user_markup.row('Текущие состояние голосования!')
    user_markup.row('Информация о Боте.')

    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)



bot.polling(none_stop=True) #обработка функций

