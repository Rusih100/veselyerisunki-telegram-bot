import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('TOKEN TELEGRAM')

bot_command_dict = {
    "/start": "Запуск бота",
    "/menu": "Вызов главного меню"
}


def main_menu(message=None, call=None):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="📅 Рассписание занятий", callback_data="inquiry_menu"),
        InlineKeyboardButton(text="📍 Адрес", callback_data="address_menu"),
        InlineKeyboardButton(text="🌐 Социальные сети", callback_data="social_network_menu"),
        InlineKeyboardButton(text="☎️ Связаться с нами", callback_data="contact_menu"),
        InlineKeyboardButton(text="ℹ️ О нас", callback_data="about_menu"),
        row_width=2
    )
    text = f"Чем мы можем вам помочь? 😌"

    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=keyboard)
    except AttributeError:
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)


def inquiry_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="🎨 ИЗО", callback_data='inquiry_art'),
        InlineKeyboardButton(text="🎓 Подготовка в школе", callback_data='inquiry_school'),
        InlineKeyboardButton(text="🧶 Куклы и вязание", callback_data='inquiry_knitting'),
        InlineKeyboardButton(text="⬅️ Назад", callback_data='back_main'),
        row_width=1
    )
    text = f"📅 Рассписание занятий"

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=keyboard)


def inquiry_art_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=f'back_inquiry_from_art'),
        row_width=1
    )
    text = [
        f"🎨 ИЗО (15 000 тг - 4 занятия)",

        f"5-7 лет\n"
        f"Четверг с 13:00-16:00\n"
        f"Суббота с 14:00-17:00",

        f"8-11 лет\n"
        f"Суббота с 14:00-17:00",

        f"12-17 лет\n" 
        f"Вторник с 10:00-13:00\n" 
        f"Четверг с 10:00-13:00\n"
        f"Суббота с 10:00-13:00\n"
        ]
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    for index in range(len(text) - 1):
        bot.send_message(chat_id=call.message.chat.id, text=text[index])
    bot.send_message(chat_id=call.message.chat.id, text=text[-1], reply_markup=keyboard)


def inquiry_school_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="⬅️ Назад", callback_data='back_inquiry_from_school'),
        row_width=1
    )
    text = [
        f"🎓 Подготовка к школе (26 000 тг - 12 занятий по 3 часа)",

        f"1 группа\n" 
        f"Вторник, четверг, пятница\n"
        f"10:00-13:00",

        f"2 группа\n" 
        f"Понедельник, среда, пятница\n"
        f"16:00-19:00"
    ]
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    for index in range(len(text) - 1):
        bot.send_message(chat_id=call.message.chat.id, text=text[index])
    bot.send_message(chat_id=call.message.chat.id, text=text[-1], reply_markup=keyboard)


def inquiry_knitting_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="⬅️ Назад", callback_data='back_inquiry_from_knitting'),
        row_width=1
    )
    text = [
        f"🧶 Куклы и вязание (10 000 тг - 4 занятия)",

        f"1 группа\n"
        f"Суббота\n"
        f"10:00-12:00",

        f"2 группа\n"
        f"Суббота\n"
        f"12:00-14:00"
    ]
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    for index in range(len(text) - 1):
        bot.send_message(chat_id=call.message.chat.id, text=text[index])
    bot.send_message(chat_id=call.message.chat.id, text=text[-1], reply_markup=keyboard)


def address_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=f'back_main_from_gps'),
        row_width=1
    )
    text = f"📍 Адрес \n\n" \
           f"Казахстан, город Нур-Султан, Валиханова 1"

    longitude = 71.439622
    latitude = 51.162236

    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    bot.send_location(chat_id=call.message.chat.id, longitude=longitude, latitude=latitude)
    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=keyboard)


def social_network_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="🌅 Instagram", url='https://www.instagram.com/veselyerisunki/'),
        InlineKeyboardButton(text="📞 WhatsApp", url='https://wa.me/77011238930'),
        InlineKeyboardButton(text="⬅️ Назад", callback_data='back_main'),
        row_width=1
    )
    text = f"🌐 Социальные сети"

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=keyboard)


def contact_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="⬅️ Назад", callback_data='back_main_from_contact'),
        row_width=1
    )
    text = [
        f"☎️ Связаться с нами",
        f"+77011238930",
        f"+77026908105"
    ]
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    for index in range(len(text) - 1):
        bot.send_message(chat_id=call.message.chat.id, text=text[index])
    bot.send_message(chat_id=call.message.chat.id, text=text[-1], reply_markup=keyboard)


def about_menu(call):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="⬅️ Назад", callback_data='back_main'),
        row_width=1
    )
    text = f"ℹ️ О нас \n\n" \
           f"«Веселые рисунки» - это не просто детская студия  развития, это место, " \
           f"где внимательно и с любовью относятся к каждому ребенку.\n\n" \
           f"Мы начали свою уникальную историю с 2007 года ☀ \n\n" \
           f"Мы быстро росли, развивались и вскоре, в нашей студии  ребята могли уже не " \
           f"только рисовать, но уже  вязать, вышивать, читать, писать, лепить. Вообщем, началась " \
           f"у нас совсем другая жизнь - яркая и удивительная. И мы даже глазом не успели моргнуть, как, дети в " \
           f"нашей студии подросли и стали такими прекрасными и талантливыми ребятами."

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=keyboard)


def remove_message(call, n=1):
    message_id = call.message.id - 1
    for i in range(n):
        bot.delete_message(chat_id=call.message.chat.id, message_id=(message_id - i))


def transition_func(call):
    func_call = call.data.split()[0]
    transition_dict = {
        "back_main_from_gps": (main_menu, 1),
        "back_main_from_contact": (main_menu, 2),
        "back_inquiry_from_art": (inquiry_menu, 3),
        "back_inquiry_from_school": (inquiry_menu, 2),
        "back_inquiry_from_knitting": (inquiry_menu, 2)
    }
    remove_message(call, transition_dict[func_call][1])
    transition_dict[func_call][0](call=call)


@bot.message_handler(commands=['start'])
def command_start(message):
    user_name = message.from_user.first_name
    text_list = [
        f"Добрый день, {user_name}! 😊",
        f"Вас приветствует детская студия \n'Веселые рисунки'! ☀️"
    ]
    for text in text_list:
        bot.send_message(message.from_user.id, text=text)

    command_menu(message=message)


@bot.message_handler(commands=['menu'])
def command_menu(message):
    main_menu(message=message)


@bot.message_handler(commands=['help'])
def command_help(message):
    text = f"Список команд: \n"
    for key, value in bot_command_dict.items():
        text += f"{key} - {value} \n"
    bot.send_message(message.from_user.id, text)


@bot.message_handler(content_types=['text'])
def text_message_log(message):
    text = f"{message.message_id} - {message.from_user.first_name} - {message.text}"
    print(text)


@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    func_call = call.data.split()[0]

    callback_dict = {
        # Кнопки главного меню:
        "inquiry_menu": inquiry_menu,
        "address_menu": address_menu,
        "social_network_menu": social_network_menu,
        "contact_menu": contact_menu,
        "about_menu": about_menu,

        "back_main": main_menu,
        "back_main_from_gps": transition_func,
        "back_main_from_contact": transition_func,

        # Кнопки меню рассписания:
        "inquiry_art": inquiry_art_menu,
        "inquiry_school": inquiry_school_menu,
        "inquiry_knitting": inquiry_school_menu,

        "back_inquiry": inquiry_menu,
        "back_inquiry_from_art": transition_func,
        "back_inquiry_from_school": transition_func,
        "back_inquiry_from_knitting": transition_func,
    }

    if func_call in callback_dict:
        callback_dict[func_call](call=call)


bot.polling(none_stop=True)


