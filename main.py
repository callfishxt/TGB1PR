import telebot
import random
viclist = ['Молодец','Поздраляю','Умничка','Везунчик','Вы стеклодув','Любитель стекла','Каратель викторин']
funlist = ['Почему стекольные заводы всегда заняты? Потому что им всегда есть что гранить!',
           'Что скажет стеколомойщик, когда его спросят, как дела на заводе? Нам все в руки!',
           'Почему стекольные заводы никогда не скучают? Потому что у них всегда есть окна к похвале!',
           'Какой стекольный завод самый занятой? Тот, где люди в очереди стоят, чтобы разбить окно!',
           'Почему на стекольных заводах всегда тихо? Потому что стеклографии не звучат громко!',
           'Как называют завод, где производят бутылки? Стекловкусообразие!',
           'Что произойдет, если стекольщик на заводе долго не спит? Он начнет видеть окна возле каждого предмета!',
           'Как стекольные заводы поднимают настройку своих работников? Им показывают прозрачные слайды!',
           'Зачем стекольным заводам экстрасенсы? Чтобы заранее видеть, сколько окон им нужно производить!',
           'Когда на стекольных заводах наступает новый год, они празднуют разбитием бутылок и украшением окон!',
           "Почему стекольный завод всегда приносит прибыль? Потому что они всегда имеют чашку успеха!",
            "Какой самый популярный подарок на свадьбу стекольщикам? Очевидно, стеклянные сюрпризы!",
            "Зачем стеклоход ходит вокруг стекольного завода? Он ищет свою прозрачную любовь!",
            "Почему стеклодувы такие хорошие рассказчики? Потому что они всегда говорят правду в глаза!",
            "Как называют танцы на стекле? Стеклянные шары!",
            "Какой фильм любят смотреть на стекольных заводах? Стекло (Glass)!",
            "Почему стекло всегда спокойное? Потому что оно никогда не теряет своего хладнокровия!"
]

from telebot import types
qvestmode = False
bot = telebot.TeleBot()
def SetOff(bool):
    bool = False
def SetOn(bool):
    bool = True
@bot.message_handler(commands=['start','s'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}, Я чат бот ажур стиль, ты можешь увидеть снизу экрана,кнопки, нажимайте на них чтобы задавать вопросы и многое другое)',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Поздороваться":
        bot.send_message(message.chat.id, text="Привет! Я чат бот ажур стиль, ты можешь увидеть снизу экрана кнопки, нажимайте на них чтобы задавать вопросы и многое другое)")
    elif message.text == "❓ Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Викторина 💎")
        btn2 = types.KeyboardButton("Что я могу 🤖")
        btn3 = types.KeyboardButton("Обо Всем 🌃")
        btn4 = types.KeyboardButton("Шутки про стеклозавод 🤡")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3,btn4, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Шутки про стеклозавод 🤡":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Еще Одну Шутку!")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, back)
        bot.send_message(message.chat.id, "Окей вот и шутка:\n" + '<b>'+funlist[random.randrange(0,16)]+"</b>", reply_markup=markup,parse_mode='html')


    elif message.text == "Еще Одну Шутку!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Еще Одну Шутку!")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, back)
        bot.send_message(message.chat.id, "Окей вот и шутка:\n" + '<b>' + funlist[random.randrange(0, 16)] + "</b>",
                         reply_markup=markup, parse_mode='html')


    elif message.text == "Викторина 💎":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Бутылки стеклянные")
        button2 = types.KeyboardButton("Банки стеклянные")
        button3 = types.KeyboardButton("Любые")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button2, button1, button3, back)
        bot.send_message(message.chat.id,"Привет , {0.first_name}! \nРад видеть тебя в викторине!\nИтак, не будем же ждать, к первому вопросу.".format(message.from_user, bot.get_me()))
        bot.send_message(message.chat.id, "Вопрос №1:\nЧто принимаем?",reply_markup=markup)
    elif message.text == "Любые" :
        bot.send_message(message.chat.id,'Неправильно, попробуй еще раз!')
    elif message.text == "Банки стеклянные":
        bot.send_message(message.chat.id,'Неправильно, попробуй еще раз!')
    elif message.text == "Бутылки стеклянные":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Хрусталь целая")
        button2 = types.KeyboardButton("Хрусталь битая")
        button3 = types.KeyboardButton("Любые из предложенных")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)] + ', следующий вопрос №2!')
        bot.send_message(message.chat.id, 'Что из этого мы также принимаем!',reply_markup=markup)
    elif message.text == "Любые из предложенных" :
        bot.send_message(message.chat.id,'Неправильно, попробуй еще раз!')
    elif message.text == "Хрусталь битая":
        bot.send_message(message.chat.id,'Неправильно, попробуй еще раз!')
    elif message.text == "Хрусталь целая":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Синие и прозрачные стеклянные")
        button2 = types.KeyboardButton("Пластиковые,стеклянные")
        button3 = types.KeyboardButton("Железные и стеклянные")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button2, button1, button3, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+', следующий вопрос №3!')
        bot.send_message(message.chat.id, 'какие бутылки принимаем?', reply_markup=markup)
    elif message.text == "Железные и стеклянные":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "Пластиковые,стеклянные":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "Синие и прозрачные стеклянные":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Нисколько, даром")
        button2 = types.KeyboardButton("мало")
        button3 = types.KeyboardButton("много всего")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button2, button1, button3, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+', следующий вопрос №4!')
        bot.send_message(message.chat.id, 'Сколько платят за сдачу стекла?', reply_markup=markup)
    elif message.text == "мало":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "много всего":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")

    elif message.text == "Что я могу 🤖":
        bot.send_message(message.chat.id, text="Я - чат бот Ажур Стиль могу все что вы попросите!\nНапример если хотите я могу вам рассказать про стекло и когда были первые очки, если интересно тогда переходи в вопросы и выбери пункт обо всем! И узнай много вестей")

    elif message.text == "Нисколько, даром":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("мячи")
        button2 = types.KeyboardButton("деревянные игрушки")
        button3 = types.KeyboardButton("елочные игрушки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button2, button1, button3, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+', следующий вопрос №5!')
        bot.send_message(message.chat.id, 'Что изготавливают из бутылочного стекла?', reply_markup=markup)

    elif message.text == "мячи":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "деревянные игрушки":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")

    elif message.text == "елочные игрушки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("785")
        button2 = types.KeyboardButton("1088")
        button3 = types.KeyboardButton("2137")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button2, button1, button3, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)] + ', следующий вопрос №6!')
        bot.send_message(message.chat.id, 'При какой температуре плавится жидкое стекло?', reply_markup=markup)

    elif message.text == "785":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "2137":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")

    elif message.text == "1088":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("красный")
        button2 = types.KeyboardButton("голубой")
        button3 = types.KeyboardButton("синий")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button2, button1, button3, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+', следующий вопрос №7!')
        bot.send_message(message.chat.id, 'Какой цвет самого дорогого стекла?', reply_markup=markup)

    elif message.text == "голубой":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "синий":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "красный":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1451г")
        button2 = types.KeyboardButton("1673г")
        button3 = types.KeyboardButton("1342г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button3, button2, button1, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+', следующий вопрос №8!')
        bot.send_message(message.chat.id, 'Когда изобрели очки для коррекции зрения?', reply_markup=markup)

    elif message.text == "1673г":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "1342г":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")

    elif message.text == "1451г":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1876г")
        button2 = types.KeyboardButton("2004г")
        button3 = types.KeyboardButton("1903г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button3, button2, button1, back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+', следующий вопрос №9!')
        bot.send_message(message.chat.id, 'когда было изобретено Небьющееся стекло?', reply_markup=markup)
    elif message.text == "2004г":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "1876г":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")

    elif message.text == "1903г":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("металлы")
        button2 = types.KeyboardButton("краски")
        button3 = types.KeyboardButton("красители")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button3, button2, button1, back)
        bot.send_message(message.chat.id, 'Итак! Это последний вопрос викторины')
        bot.send_message(message.chat.id, 'что используют для окраски стекла?', reply_markup=markup)
    elif message.text == "краски":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "красители":
        bot.send_message(message.chat.id, text="Неправильно, попробуй еще раз!")
    elif message.text == "металлы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, viclist[random.randrange(0,6)]+'! Вы прошли эту викторину о стекле !', reply_markup=markup)


    elif message.text == "Обо Всем 🌃":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        btn1 = types.KeyboardButton("Что принимают стекольные фабрики?")
        btn2 = types.KeyboardButton("Что изготавливают стекольные фабрики?")
        btn3 = types.KeyboardButton("Когда изобрели?")
        markup.add(btn1,btn2,btn3,back)
        bot.send_message(message.chat.id, text="Здесь вы можете узнать все и ответы на викторину в том числе!",parse_mode='html',reply_markup=markup)

    elif message.text == "Когда изобрели?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Обо Всем 🌃")
        button2 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="О первых очках коррекции зрения: В 1451 году в Германии Nikolaus Kuzanski наладил производство вогнутых линз"
                                               ", которые имели тонкий центр линзы и толстый край и использовались для коррекции близорукости. "
                                               "Первые оправы для очков Первые оправы для очков изготавливались из дерева, свинца или меди.\n\nНебьющееся стекло "
                                               "было изобретено случайно. В 1903 году французский химик Эдуард Бенедиктус нечаянно уронил колбу, заполненную"
                                               "нитроцеллюлозой. Стекло треснуло, но не разлетелось на мелкие кусочки.\n\nТак как ученые считают эти находки древнейшими, "
                                               "то на вопрос, когда появилось стекло, они отвечают – около 12 тысяч лет назад. Именно столько лет насчитывает существование "
                                               "голубых и зеленых украшений из числа египетских археологических находок.\nОтвечая на вопрос, откуда появилось стекло, ученые сделали вывод, что это "
                                               "произошло примерно 55 веков назад, на территории Древнего Египта и Месопотамии. Первыми предметами из стекла были небольшие шарики правильной формы", reply_markup=markup)
    elif message.text == "Что изготавливают стекольные фабрики?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Обо Всем 🌃")
        button2 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="\nОснову стекольной промышленности в России представляют пять крупных заводов, специализирующихся "
                                               "на производстве листового стекла. На их долю приходится более 90% всего выпускаемого в стране объема. \n\n"
                                               "Листовое стекло производится из кварцевого песка, кальцинированной соды, доломита и различных примесей. \n\n"
                                               "Продукция заводов востребована в строительстве, машиностроении, производстве мебели, торгового и медицинского"
                                               "оборудования, бытовой техники. Статистика отрасли показывает ежегодный рост производства в пределах 15%. \n\nНовым "
                                               "перспективным направлением стекольной промышленности, в котором занято свыше 50 профильных предприятий, называют "
                                               "промышленную переработку, включающую в себя изготовление стеклопакетов, закаливание и армирование стекла, производство "
                                               "триплекса. \n\nСтекольные заводы реализуют готовую продукцию следующих типов: стекло листовое, закаленное, матовое, цветное, "
                                               "узорчатое, армированное, многослойное, огнеупорное, а также стеклопакеты и стеклянные блоки "
                                               "\n\nСтекольные фабрики изготавливают елочные игрушки, многие украшение, посуду, дверные стекла и очень большое количество "
                                               "товаров на заказ!", reply_markup=markup)
    elif message.text == "Что принимают стекольные фабрики?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Обо Всем 🌃")
        button2 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id,
                         text="\n\nПереработкой стекла занимаются стеклоперерабатывающие заводы. В отличие от переработки пластика, эта система налажена и успешно работает уже долгие годы. \n\nВ стране работают десятки предприятий, которые перерабатывают стекло и превращают его в новые изделия. Поэтому дело за каждым – сдавать стекло на переработку довольно просто. \n\nНайти ближайший пункт приёма стеклотары в своём городе можно здесь."
"\n\nВ контейнеры для вторсырья или пункты приёма стеклотары можно отнести бутылки от напитков, банки из-под консервов или детского питания, а также различные пузырьки. Тара может быть прозрачная, зелёная или коричневая."
"\n\nНа переработку можно сдать и листовое стекло, которое осталось при замене окон. Однако его принимают только в компании «Стеклобой»: листовое стекло надо оставить у контейнера."
"\n\nПрежде чем сдать стекло, его надо ополоснуть от остатков содержимого и снять с тары крышку. Этикетку отрывать не нужно.Так-же можно сдавать целую хрусталь в наши Стеклозаводы!"
"\n\nПри этом вместе со стеклом нельзя сдавать на переработку:"
"\n\nкерамическую и стеклянную посуду (бокалы, стаканы, кружки, тарелки);\nочки или линзы;\nавтомобильное стекло;\nкрышки от сковородок и кастрюль;\nлампочки;\nзеркала;"
"\nхрусталь.", reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")







bot.polling(none_stop=True)
