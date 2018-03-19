# -*- coding: utf-8 -*-
import telebot
import constants




# -*- coding: utf-8 -*-
import telebot
import constants
import os

import sys
import logging

import pypyodbc

#cursor.execute(mySQLQuery)
#infobase = cursor.fetchall()
#print(infobase)


AllMember = ['Воздержались','1.Котик Л-303Б','2.Щенок С-201А','3.Птичка Л-101Б','4.Медведь С-413В'] ##//ДОБАВЛЯТЬ//
Field_Vote = 0 # Проголосовал или нет

bot = telebot.TeleBot(constants.token) #объект бот



@bot.message_handler(commands=['start','help'])
def handle_start(message):

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Меню')
    user_markup.row('Узнать кто сейчас выступает')
    user_markup.row('Голосовать за участников!')
    user_markup.row('Текущие состояние голосования!')
    user_markup.row('Информация о Боте.')

    # _______________________Конектица к базе данных
    mySQLServer = "eu-cdbr-west-02.cleardb.net"
    myDatabase = "heroku_7d29c9f1038ad30"
    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=' + mySQLServer + ';' 'Database=' + myDatabase + ';' 'uid=b596427b83010e;''pwd=ea86f59b;')
    # ______________________________________________
    cursor = connection.cursor()
    cursor.execute("SELECT UsersID FROM heroku_7d29c9f1038ad30.springvoting WHERE UsersID = '2'")   # добавление запроса
    #connection.commit()  # если добавляешь
    results = cursor.fetchall()
    print(results)
    connection.close()
    # ________________________________________________закрытие бд
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_menu(message):
    global AllMember
    global Field_Vote
    if message.text == 'Информация о Боте.':
       bot.send_message(message.from_user.id, "Бот создан для СтудВесны Стоматологического и Лечебного Факультета.")
    elif message.text == 'Меню':
       articleKeyboard = telebot.types.InlineKeyboardMarkup(4)
       info_members = telebot.types.InlineKeyboardButton('Информация об участниках', callback_data="hm_1")
       info_of_spring = telebot.types.InlineKeyboardButton('Информация об СтудВесне', callback_data="hm_2")
       info_org = telebot.types.InlineKeyboardButton('Организаторы', callback_data="hm_3")
       info_sud = telebot.types.InlineKeyboardButton('Судьи', callback_data="hm_4")
       articleKeyboard.row(info_members)
       articleKeyboard.row(info_of_spring)
       articleKeyboard.row(info_org, info_sud)
       bot.send_message(message.from_user.id, "Что вы хотите узнать?", reply_markup=articleKeyboard)
       print('вызвано меню')
       #//ДОБАВЛЯТЬ ИНФОРМАЦИЮ//____________________
    elif message.text == 'Голосовать за участников!':
            VoteMemberKey = telebot.types.InlineKeyboardMarkup(4)
            memb_1 = telebot.types.InlineKeyboardButton('1.Котик Л-303Б', callback_data="memVot_1")
            memb_2 = telebot.types.InlineKeyboardButton('2.Щенок С-201А', callback_data="memVot_2")
            memb_3 = telebot.types.InlineKeyboardButton('3.Птичка Л-101Б', callback_data="memVot_3")
            memb_4 = telebot.types.InlineKeyboardButton('4.Медведь С-413В', callback_data="memVot_4")
            VoteMemberKey.row( memb_1)
            VoteMemberKey.row( memb_2)
            VoteMemberKey.row( memb_3)
            VoteMemberKey.row( memb_4)
            bot.send_message(message.from_user.id, "За кого отдадите свой голос?", reply_markup=VoteMemberKey)
    elif message.text == 'Текущие состояние голосования!':
        # _______________________КОЛИЧЕСТВО ПОЛЕ Vote
        mySQLServer = "DESKTOP-02AVU8U\SQLEXPRESS"
        myDatabase = "SpringVoting"
        connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=' + mySQLServer + ';' 'Database=' + myDatabase + ';')
        # ______________________________________________
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM SpringVoting.dbo.UsersVote group by Vote ")  # добавление запроса
        results = cursor.fetchall()
        print(results)
        Field_Vote = int(len(results))
        connection.close()
        if int(len(results)) < 1:
            bot.send_message(message.from_user.id, "Пока никто не проголосовал!")
        else:
            # _______________________Конектица ВЫВОДИТ СОСТОЯНИЕ ГОЛОСОВАНИЯ
            mySQLServer = "DESKTOP-02AVU8U\SQLEXPRESS"
            myDatabase = "SpringVoting"
            connection = pypyodbc.connect('Driver={SQL Server};'
                                          'Server=' + mySQLServer + ';' 'Database=' + myDatabase + ';')
            # ______________________________________________
            cursor = connection.cursor()
            cursor.execute("Select Vote, count(*) from SpringVoting.dbo.UsersVote group by Vote")  # добавление запроса
            results = cursor.fetchall()
            print(results)

            for number in range(Field_Vote):
                bot.send_message(message.from_user.id,  "" + str(AllMember[number]) + " : " + str(int(results[number][1])-1) + "")

            connection.close()


@bot.callback_query_handler(func=lambda k: True)
def menu_members(k):
     if k.data == "hm_1":
        MembersKeybord = telebot.types.InlineKeyboardMarkup(4)
        mem_1 = telebot.types.InlineKeyboardButton('Котик Л-303Б', callback_data="cqh_1")
        mem_2 = telebot.types.InlineKeyboardButton('Щенок С-201А', callback_data="cqh_2")
        mem_3 = telebot.types.InlineKeyboardButton('Птичка Л-101Б', callback_data="cqh_3")
        mem_4 = telebot.types.InlineKeyboardButton('Медведь С-413В', callback_data="cqh_4")
        MembersKeybord.row(mem_1)
        MembersKeybord.row(mem_2)
        MembersKeybord.row(mem_3)
        MembersKeybord.row(mem_4)
        bot.send_message(k.from_user.id, "О ком вы хотите узнать?", reply_markup=MembersKeybord)
     elif k.data == "cqh_1":
         bot.send_message(k.from_user.id, "Котик Л-303Б. Поёт песенку Мяу-Мяу как ваши дела.")
         directory = 'C:/Users/denis/PycharmProjects/String_BSMU_Bot/photo'
         img = open(directory + '/' + 'cat.jpg', 'rb')
         bot.send_chat_action(k.from_user.id, 'upload_photo')
         bot.send_photo(k.from_user.id, img)
     elif k.data == "cqh_2":
         bot.send_message(k.from_user.id, "Щенок С-201А Поёт песню Гав-Гав. Весёлый и жизнерадостный чувак всем мир.")
         directory = 'C:/Users/denis/PycharmProjects/String_BSMU_Bot/photo'
         img = open(directory + '/' + 'dog.jpeg', 'rb')
         bot.send_chat_action(k.from_user.id, 'upload_photo')
         bot.send_photo(k.from_user.id, img)
     elif k.data == "cqh_3":
         bot.send_message(k.from_user.id, "Птичка Л-101Б. Танец неичгео такой но можно было и лучше, а так сойдет.")
         directory = 'C:/Users/denis/PycharmProjects/String_BSMU_Bot/photo'
         img = open(directory + '/' + 'bird.jpg', 'rb')
         bot.send_chat_action(k.from_user.id, 'upload_photo')
         bot.send_photo(k.from_user.id, img)
     elif k.data == "cqh_4":
         bot.send_message(k.from_user.id, "Медведь С-413В с танцем который поразит всех, лучше вам это увидеть, чем услышать.")
         directory = 'C:/Users/denis/PycharmProjects/String_BSMU_Bot/photo'
         img = open(directory + '/' + 'beer.jpg', 'rb')
         bot.send_chat_action(k.from_user.id, 'upload_photo')
         bot.send_photo(k.from_user.id, img)

     elif k.data == "memVot_1":

            # _______________________Конектица к базе данных
            mySQLServer = "DESKTOP-02AVU8U\SQLEXPRESS"
            myDatabase = "SpringVoting"
            connection = pypyodbc.connect('Driver={SQL Server};'
                                          'Server=' + mySQLServer + ';' 'Database=' + myDatabase + ';')
            # ______________________________________________
            cursor = connection.cursor()
            cursor.execute("UPDATE SpringVoting.dbo.UsersVote SET Vote = '1' WHERE UsersID = '"+str(k.from_user.id)+"'")  # добавление запроса
            connection.commit()  # если добавляешь
            connection.close()
        # ________________________________________________закрытие бд
            bot.send_message(k.from_user.id, "Ваш голос учтён!")
     elif k.data == "memVot_2":
            # _______________________Конектица к базе данных
            mySQLServer = "DESKTOP-02AVU8U\SQLEXPRESS"
            myDatabase = "SpringVoting"
            connection = pypyodbc.connect('Driver={SQL Server};'
                                          'Server=' + mySQLServer + ';' 'Database=' + myDatabase + ';')
            # ______________________________________________
            cursor = connection.cursor()
            cursor.execute("UPDATE SpringVoting.dbo.UsersVote SET Vote = '2' WHERE UsersID = '"+str(k.from_user.id)+"'")  # добавление запроса
            connection.commit()  # если добавляешь
            connection.close()
        # ________________________________________________закрытие бд
            bot.send_message(k.from_user.id, "Ваш голос учтён!")



@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)


@bot.message_handler(content_types=['фото'])
def handle_text(message):
    if message.text == 'фото':

        directory = 'C:/Users/denis/PycharmProjects/String_BSMU_Bot/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory )
        for file in all_files_in_directory :
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

bot.polling(none_stop=True) #обработка функций

