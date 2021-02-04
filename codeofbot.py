import telebot
from telebot import types
import constants


bot = telebot.TeleBot(constants.token)


#Приветствие#

@bot.message_handler(commands=['start'])
def main(message):
    gi = bot.send_message(message.chat.id, 'Привет, меня зовут БуФи и я хочу тебе помочь!'
                          + message.from_user.first_name + ", напечатай /choose ")
    bot.register_next_step_handler(gi, bofi)

#keyboard#
@bot.message_handler(commands=['choose'])
def bofi(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/Книги')
    itembtn2 = types.KeyboardButton('/Фильмы')
    itembtn3 = types.KeyboardButton('/Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "А ну-ка,  "
                     + message.from_user.first_name
                     + ", выберите, что же вы хотели увидеть?", reply_markup=markup)



@bot.message_handler(commands=["Фильмы"])
def user_reg(message):
       markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
       itembtn1 = types.KeyboardButton('/Драмы')
       itembtn2 = types.KeyboardButton('/Мультфильмы')
       itembtn3 = types.KeyboardButton('/Боевики')
       itembtn4 = types.KeyboardButton('/Фэнтези')
       itembtn7 = types.KeyboardButton('/Комедия')
       markup.add(itembtn1, itembtn2, itembtn3, itembtn4,itembtn7)
       msg = bot.send_message(message.chat.id, 'Выберите жанр', reply_markup=markup)

@bot.message_handler(commands=["Книги"])
def user_reg(message):
       markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
       itembtn1 = types.KeyboardButton('/Казахская литература')
       itembtn2 = types.KeyboardButton('/Психология')
       itembtn3 = types.KeyboardButton('/Романы')
       itembtn4 = types.KeyboardButton('/Детская литература')
       itembtn5 = types.KeyboardButton('/Современная проза')
       markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
       msg = bot.send_message(message.chat.id, 'Выберите жанр', reply_markup=markup)


@bot.message_handler(commands=['Драмы'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
    msg = bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Мультфильмы'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=9))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=10))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Боевики'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=11))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=12))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=13))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=14))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=15))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Комедия'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=16))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=17))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=18))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=19))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=20))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Фэнтези'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=21))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=22))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=23))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=24))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=25))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)


@bot.message_handler(commands=['Казахская литература'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=26))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=27))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=28))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=29))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=30))
    msg = bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Психология'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=31))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=32))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=33))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=34))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=35))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Наука'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=36))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=37))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=38))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=39))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=40))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Детская литература'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=41))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=42))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=43))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=44))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=45))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.message_handler(commands=['Современная проза'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Один', callback_data=46))
    markup.add(telebot.types.InlineKeyboardButton(text='Два', callback_data=47))
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=48))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=49))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=50))
    msg=bot.send_message(message.chat.id, text="Выберите цифру от одного до пяти", reply_markup=markup)
    bot.register_next_step_handler(msg, query_handler)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    answer = ''
    "self.data = call.data"
    if call.data == "1":
        answer = 'https://t.me/NEWcinemaHd2019/1506'
    elif call.data== "2":
        answer = 'https://t.me/NEWcinemaHd2019/1421'
    elif call.data == "3":
        answer = 'https://t.me/NEWcinemaHd2019/1401'
    elif call.data == "4":
        answer = 'https://t.me/NEWcinemaHd2019/1393'
    elif call.data == "5":
        answer = 'https://t.me/NEWcinemaHd2019/1391'
    elif call.data == "7":
        answer = 'https://t.me/NEWcinemaHd2019/1368'
    elif call.data == "7":
        answer = 'https://t.me/NEWcinemaHd2019/42'
    elif call.data == "8":
        answer = 'https://t.me/NEWcinemaHd2019/54'
    elif call.data == "9":
        answer = 'https://t.me/NEWcinemaHd2019/1334'
    elif call.data == "10":
        answer = 'https://t.me/NEWcinemaHd2019/72'
    elif call.data == "11":
        answer = 'https://t.me/NEWcinemaHd2019/24'
    elif call.data == "12":
        answer = 'https://t.me/NEWcinemaHd2019/1476'
    elif call.data == "13":
        answer = 'https://t.me/NEWcinemaHd2019/1461'
    elif call.data == "14":
        answer = 'https://t.me/NEWcinemaHd2019/1455'
    elif call.data == "15":
        answer = 'https://t.me/NEWcinemaHd2019/1436'
    elif call.data == "16":
        answer = 'https://t.me/NEWcinemaHd2019/1416'
    elif call.data == "17":
        answer = 'https://t.me/NEWcinemaHd2019/1357'
    elif call.data == "18":
        answer = 'https://t.me/NEWcinemaHd2019/218'
    elif call.data == "19":
        answer = 'https://t.me/NEWcinemaHd2019/1472'
    elif call.data == "20":
        answer = 'https://t.me/NEWcinemaHd2019/1445'
    elif call.data == "21":
        answer = 'https://t.me/NEWcinemaHd2019/1470'
    elif call.data == "22":
        answer = 'https://t.me/NEWcinemaHd2019/1407'
    elif call.data == "23":
        answer = 'https://t.me/NEWcinemaHd2019/1389'
    elif call.data == "24":
        answer = 'https://t.me/NEWcinemaHd2019/1358'
    elif call.data == "25":
        answer = 'https://t.me/NEWcinemaHd2019/1237'
    elif call.data == "26":
        answer = 'https://t.me/bookbotstome/2'
    elif call.data == "27":
        answer = 'https://t.me/bookbotstome/4'
    elif call.data == "28":
        answer = 'https://t.me/bookbotstome/5'
    elif call.data == "29":
        answer = 'https://t.me/bookbotstome/6'
    elif call.data == "30":
        answer = 'https://t.me/bookbotstome/14'
    elif call.data == "31":
        answer = 'https://t.me/bookbotstome/8'
    elif call.data == "32":
        answer = 'https://t.me/bookbotstome/11'
    elif call.data == "33":
        answer = 'https://t.me/bookbotstome/13'
    elif call.data == "34":
        answer = 'https://t.me/bookbotstome/16'
    elif call.data == "35":
        answer = 'https://t.me/bookbotstome/25'
    elif call.data == "36":
        answer = 'https://t.me/bookbotstome/17'
    elif call.data == "37":
        answer = 'https://t.me/science_and_engineering_books/20'
    elif call.data == "38":
        answer = 'https://t.me/booksScience/1432'
    elif call.data == "39":
        answer = 'https://t.me/booksScience/1430'
    elif call.data == "40":
        answer = 'https://t.me/booksScience/1416'
    elif call.data == "41":
        answer = 'https://t.me/luchshee_detyam/120'
    elif call.data == "42":
        answer = 'https://t.me/luchshee_detyam/118'
    elif call.data == "43":
        answer = 'https://t.me/luchshee_detyam/98'
    elif call.data == "44":
        answer = 'https://t.me/luchshee_detyam/92'
    elif call.data == "45":
        answer = 'https://t.me/luchshee_detyam/87'
    elif call.data == "46":
        answer = 'https://t.me/bookbotstome/22'
    elif call.data == "47":
        answer = 'https://t.me/bookbotstome/19'
    elif call.data == "48":
        answer = 'https://t.me/bookbotstome/22'
    elif call.data == "49":
        answer = 'https://t.me/bookbotstome/21'
    elif call.data == "50":
        answer = 'https://t.me/bookbotstome/18'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
bot.polling()
