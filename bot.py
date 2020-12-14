# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import nltk
from datetime import datetime
import telegrambot.imagesearch as search
from telebot import apihelper
import telegrambot.utils as utils
import csv
import random
import re
import os
import requests


TOKEN = '###'
bot = telebot.TeleBot(TOKEN)
user = bot.get_me()


@bot.message_handler(commands=['start'])
def welcome(message):
    f = message.from_user.first_name
    bot.send_message(message.chat.id, u'Привет, {}! Я умный робот. Меня разработали, чтобы помогать клиентам детейлинг центра. Я смогу рассказать тебе о наших услугах, дать рекомендации по детейлингу для твоего авто по одному лишь фото. Ещё я могу играть в разные весёлые игры и давать полезные советы для твоего автомобиля.\n📌Если кнопочное меню скрыто, нажми иконку 🎛 в правом нижнем углу'.format(f))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('📑Посмотреть список услуг', '📸Консультация по фото')
    markup.row('📍Наши контакты','🔥Мои советы и игры')
    bot.send_message(message.chat.id, "Чем я могу Вам помочь?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer_b(call):
    mi3 = types.InlineKeyboardMarkup(row_width=1)
    it1 = types.InlineKeyboardButton(text='🛎Заказать услугу', callback_data='telephone')
    mi3.add(it1)

    mi4 = types.InlineKeyboardMarkup(row_width=1)
    it1_1 = types.InlineKeyboardButton(text='📲Оставить номер', callback_data='add_telephone')
    mi4.add(it1_1)

    if call.data == 'add_telephone':
        bot.send_message(call.message.chat.id, 'Пожалуйста, напишите свой номер')

    if call.data == 'price':
        bot.send_message(call.message.chat.id, 'Вот наш прайс...')

    if call.data == 'telephone':
        bot.send_message(call.message.chat.id, 'Вот наш номер:. Будем ждать вашего звонка!\nИли, если вам удобно, - оставьте свой номер, и мы вам перезвоним', reply_markup=mi4)

    if call.data == 'detejlign_mojka':
        bot.send_message(call.message.chat.id, 'Детейлинг мойка\nДетейлинг-мойка поможет вашему автомобилю выглядеть так, будто он только сошёл с конвейера.\nВиды мойки в детейлинг центре «Автопример»:\nМойка двухфазная — это бесконтактная мойка, ручная мойка и чистка ковров.\nМойка трёхфазная — это бесконтактная мойка, ручная мойка, консервант ЛКП и чистка ковров.\nНано-мойка — это бесконтактная мойка, ручная мойка нано-шампунем и чистка ковров.\nМойка техническая — это бесконтактная мойка, ручная мойка, удаление битума, металлических вкраплений и чистка ковров. Проводится перед полировкой, для лучшего результата используется автоскраб или глина.\nДетейлинг-мойка — это бесконтактная мойка, ручная мойка, удаление битума, металлических вкраплений, мойка проёмов, чистка ковров, пылесос салона, влажная уборка, чистка стекол и чернение резины.\nМойка двигателя — это мойка с использованием специального диэлектрического средства. На сегодняшний день один из самых безопасных методов по очистке подкапотного пространства. В процессе мойки также применяется консервант, который продлевает срок эксплуатации автомобиля.\nЧистка подвески — это чистка всей площади подвески или отдельных её элементов.\nСтоимость услуг – на фото\nБолее подробные цены можно узнать, просто позвонив нам по телефону +7 910 561-82-73.')
        bot.send_photo(call.message.chat.id, photo=open(r'price\5_1.jpg', 'rb')
                       )
        bot.send_photo(call.message.chat.id, photo=open(r'price\5_2.jpg', 'rb'),
                       reply_markup=mi3)

    if call.data == 'shumoizolyaciya_salona':
        bot.send_message(call.message.chat.id, 'Шумоизоляция\nИспользование материалов премиум-класса для максимального поглощения шумов – передвигайтесь с комфортом и слушайте любимую музыку.\nСтоимость услуг можно узнать, просто позвонив нам по телефону +7 910 561-82-73.', reply_markup=mi3)

    if call.data == 'nanesenie_keramiki':
        bot.send_message(call.message.chat.id, 'Керамическое покрытие\nКерамическое покрытие придаёт автомобилю зеркальный блеск, сохраняет насыщенность цвета и защищает лакокрасочное покрытие.\nСтоимость услуг – на фото\nБолее подробные цены можно узнать, просто позвонив нам по телефону +7 910 561-82-73.')
        bot.send_photo(call.message.chat.id, photo=open(r'price\1.jpg', 'rb'),
                       reply_markup=mi3)

    if call.data == 'polirovka':
        bot.send_message(call.message.chat.id, 'Полировка\nКачественная полировка лакокрасочного покрытия и фар улучшает внешний вид автомобиля, избавляет от мелких потёртостей, придаёт блеск. Исходя из состояния лакокрасочного покрытия, мы проведём либо лёгкую полировку, либо восстановительную.\nСтоимость услуг – на фото\nБолее подробные цены можно узнать, просто позвонив нам по телефону +7 910 561-82-73.')
        bot.send_photo(call.message.chat.id, photo=open(r'price\4.jpg', 'rb'),
                       reply_markup=mi3)

    if call.data == 'ximchistka':
        bot.send_message(call.message.chat.id, 'Химчистка салона\nБережная химчистка салона с использованием профессиональной автохимии. А также озонирование — избавление от микробов и бактерий. \nСтоимость услуг – на фото\nБолее подробные цены можно узнать, просто позвонив нам по телефону +7 910 561-82-73.')
        bot.send_photo(call.message.chat.id, photo=open(r'price\3.jpg', 'rb'),
                       reply_markup=mi3)

    if call.data == 'udal':
        bot.send_message(call.message.chat.id, 'Удаление вмятин\nУдаление вмятин без покраски. Мы устраняем вмятины любой сложности. Работа проводится с применением специализированного оборудования, либо клеевым способом.\nСтоимость услуги – от 1000 ₽\nБолее точную цену можно узнать, просто позвонив нам по телефону +7 910 561-82-73.', reply_markup=mi3)

    if call.data == 'antirain':
        bot.send_message(call.message.chat.id, 'Антидождь\nОбработка стёкол составом для создания гидрофобного эффекта. После нанесения вода будет быстро стекать.\nСтоимость услуги – от 500 ₽ для лобового стекла и от 1500 ₽ – для передней полусферы\nБолее подробные цены можно узнать, просто позвонив нам по телефону +7 910 561-82-73.', reply_markup=mi3)

    if call.data == 'avtoatel':
        bot.send_message(call.message.chat.id, 'Автоателье\nЗамена обивки салона: перетяжка потолка, сидений, дверных карт, торпеды и руля. Чаще всего, мы используем в работе кожу и экокожу – практичные и безопасные материалы.\nСтоимость услуг можно узнать, просто позвонив нам по телефону +7 910 561-82-73.', reply_markup=mi3)

    if call.data == 'antigravijnaya_plyonka':
        bot.send_message(call.message.chat.id, 'Бронирование плёнкой\nБронированная плёнка для защиты лакокрасочного покрытия от мелких повреждений, сколов и царапин. Обладает гидрофобным эффектом, что позволяет автомобилю дольше оставаться чистым.\nСтоимость услуг – на фото\nБолее подробные цены можно узнать, просто позвонив нам по телефону +7 910 561-82-73.')
        bot.send_photo(call.message.chat.id, photo=open(r'C:\Users\Alexander\Desktop\ФОТО\price\2.jpg', 'rb'), reply_markup=mi3)

    if call.data == 'lajfhak_avto':
        bot.send_message(call.message.chat.id, utils.sovet())

    if call.data == 'game_marka_avto':
        dict_photo = utils.photo()
        text_true = dict_photo['true'].capitalize()
        text_false1 = dict_photo['false1'].capitalize()
        text_false2 = dict_photo['false2'].capitalize()
        text_false3 = dict_photo['false3'].capitalize()
        mi6 = types.InlineKeyboardMarkup(row_width=2)
        it1_6 = types.InlineKeyboardButton(text=text_true, callback_data='text_true')
        it2_6 = types.InlineKeyboardButton(text=text_false1, callback_data='text_false1')
        it3_6 = types.InlineKeyboardButton(text=text_false2, callback_data='text_false2')
        it4_6 = types.InlineKeyboardButton(text=text_false3, callback_data='text_false3')
        mi6add = [it1_6, it2_6, it3_6, it4_6]
        random.shuffle(mi6add)
        mi6.add(*mi6add)
        bot.send_message(call.message.chat.id, 'Автомобиль какой марки представлен на фото?')
        bot.send_photo(call.message.chat.id, dict_photo['img'], reply_markup=mi6)

    if call.data == 'text_true':
        mi7 = types.InlineKeyboardMarkup(row_width=1)
        it1_7 = types.InlineKeyboardButton(text='Следующий вопрос➡', callback_data='game_marka_avto')
        mi7.add(it1_7)
        bot.send_message(call.message.chat.id, '✅Верно!', reply_markup=mi7)

    if call.data == 'text_false1':
        bot.send_message(call.message.chat.id, 'Неверно ❌')
    if call.data == 'text_false2':
        bot.send_message(call.message.chat.id, 'Неверно ❌')
    if call.data == 'text_false3':
        bot.send_message(call.message.chat.id, 'Неверно ❌')


@bot.message_handler(content_types=['text'])
def dialog(message):
    tel = re.findall(r"\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}", message.text)
    mi2 = types.InlineKeyboardMarkup(row_width=1)
    it1 = types.InlineKeyboardButton(text='🚿Детейлигн мойка', callback_data='detejlign_mojka')
    it2 = types.InlineKeyboardButton(text='🔇Шумоизоляция салона', callback_data='shumoizolyaciya_salona')
    it3 = types.InlineKeyboardButton(text='💎Нанесение керамики', callback_data='nanesenie_keramiki')
    it4 = types.InlineKeyboardButton(text='💫Полировка', callback_data='polirovka')
    it5 = types.InlineKeyboardButton(text='🧼Химчистка салона', callback_data='ximchistka')
    it6 = types.InlineKeyboardButton(text='☀Антидождь', callback_data='antirain')
    it7 = types.InlineKeyboardButton(text='🧷Автоателье', callback_data='avtoatel')
    it8 = types.InlineKeyboardButton(text='🛠Удаление вмятин', callback_data='udal')
    it10 = types.InlineKeyboardButton(text='🛡Антигравийная плёнка', callback_data='antigravijnaya_plyonka')
    mi2.add(it1, it2, it3, it4, it5, it6, it7, it8, it10)

    mi5 = types.InlineKeyboardMarkup(row_width=1)
    it1_5 = types.InlineKeyboardButton(text='Полезный лайфхак для авто', callback_data='lajfhak_avto')
    it3_5 = types.InlineKeyboardButton(text='Игра: угадай марку авто', callback_data='game_marka_avto')

    mi5.add(it1_5, it3_5)

    if message.text == '📸Консультация по фото':
        bot.send_message(message.chat.id, 'Хорошо, пришли фото, и я скажу, какие услуги детейлинга необходимы твоему автомобилю')

    if message.text == '📑Посмотреть список услуг':
        bot.send_message(message.chat.id,
                         'Вот список наших услуг.\nПожалуйста, выберите услугу, и я расскажу вам о ней подробнее.', reply_markup=mi2)

    if message.text == '🔥Мои советы и игры':
        bot.send_message(message.chat.id, '🤖Я рад, что ты нажал на эту кнопку, ведь я очень люблю общаться с людьми и помогать им!\nИтак, с чего начнём?', reply_markup=mi5)
        # bot.register_next_step_handler(message, text_app)

    if message.text == '📍Наши контакты':
        bot.send_message(message.chat.id, 'Наш детейлинг центр находится по адресу: .\nНаш номер: ')

    if tel:
        bot.send_message(message.chat.id, 'Спасибо! Когда вам лучше позвонить?')
        bot.register_next_step_handler(message, time)


def text_app(message):
    s = utils.text_gen(message.text)
    bot.send_message(message.chat.id, s)


def time(message):
    time_z = message.text
    bot.send_message(message.chat.id, 'Хорошо. Позвоним вам ' + str(time_z).lower())


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    try:
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = '/photo/' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Так, сейчас проанализирую это фото")
        bot.send_message(message.chat.id, 'Одну секунду')
        pred = search.yasearch(src)
        if str(pred) != 'Не могу понять, что на фото :(':
            pred1 = 'Ух ты, это же ' + str(pred)
        else:
            pred1 = str(pred)
        bot.send_message(message.chat.id, pred1)

        mi = types.InlineKeyboardMarkup(row_width=1)
        it1 = types.InlineKeyboardButton(text='🛎Заказать услуги', callback_data='telephone')
        it2 = types.InlineKeyboardButton(text='💳Узнать стоимость услуг', callback_data='price')
        mi.add(it1, it2)

        uslugi = ['✔Детейлинг-мойка\n', '✔Нанесение бронированной плёнки\n', '✔Нанесение керамики\n',
                  '✔Полировка кузова\n', '✔Полировка фар\n', '✔Нанесение антидождя\n',
                  '✔Детейлинг-чистка подвески\n', '✔Химчистка и озонирование салона\n']
        uslugi_r = random.sample(uslugi, k=3)
        uslugi_r = ''.join(uslugi_r)
        bot.send_message(message.chat.id, 'Я думаю, ему необходимы следующие услуги: \n' + str(uslugi_r),
                         reply_markup=mi)

    except Exception as e:
        bot.reply_to(message, 'Похоже, произошла какая-то ошибка. Попробуй написать мне ещё раз')


bot.polling(none_stop=True)
