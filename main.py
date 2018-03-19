
import telebot
import os
import pypyodbc

#AllMember = ['Воздержались','1.Котик Л-303Б','2.Щенок С-201А','3.Птичка Л-101Б','4.Медведь С-413В'] ##//ДОБАВЛЯТЬ//
#Field_Vote = 0 # Проголосовал или нет

bot = telebot.TeleBot("589935777:AAHYS__Ii5o90oKbNJWoF9oeilBTbruKh2g") #объект бот



@bot.message_handler(commands=['start','help'])
def handle_start(message):

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Меню')
    user_markup.row('Узнать кто сейчас выступает')
    user_markup.row('Голосовать за участников!')
    user_markup.row('Текущие состояние голосования!')
    user_markup.row('Информация о Боте.')
    """
    # _______________________Конектица к базе данных
    mySQLServer = "eu-cdbr-west-02.cleardb.net"
    myDatabase = "heroku_7d29c9f1038ad30"
    connection = pypyodbc.connect('Driver={ODBC Driver 13 for SQL Server}; Server=' + mySQLServer + '; Database=' + myDatabase + '; UID=b596427b83010e; PWD=ea86f59b;')
    # ______________________________________________
    cursor = connection.cursor()
    cursor.execute("SELECT UsersID FROM heroku_7d29c9f1038ad30.springvoting WHERE UsersID = '2'")   # добавление запроса
    #connection.commit()  # если добавляешь
    results = cursor.fetchall()
    print(results)
    connection.close()
    # ________________________________________________закрытие бд
    """
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)




bot.polling(none_stop=True) #обработка функций

