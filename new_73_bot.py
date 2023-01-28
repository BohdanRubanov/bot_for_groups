import all_words
import telebot 
import random
bot = telebot.TeleBot("5871931662:AAHDs_T94N2aJON8ahbaeHoXRWeggF2qQ-w")   
all_words_list = all_words.all_words_list1.split()
all_words_list_bot = all_words.all_bot_words.split(",")
b = []
bot_flag = False
bot_conversation = False

# def default_test(message):
#     nick = message.from_user.username
#     bot.send_message(message.chat.id, f"@{nick}")
# bot.send_message(735386924, "Задай команду '/start', щоб почати роботу")
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]

CrossesOrToe = ["0", "X"]


playerSymbol = CrossesOrToe[random.randint(0, 1)]


botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"


# lose/win

winbool = False
drowbool = False
losebool = False
def clear():
    global gameGround
    gameGround = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]


def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        global losebool
        losebool = True

def draw(cell1, cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9):
    if (cell1 == botSymbol or cell1 == playerSymbol) and (cell2 == botSymbol or cell2 == playerSymbol) and (cell3 == botSymbol or cell3 == playerSymbol) and (cell4 == botSymbol or cell4 == playerSymbol) and (cell5 == botSymbol or cell5 == playerSymbol) and (cell6 == botSymbol or cell6 == playerSymbol) and (cell7 == botSymbol or cell7 == playerSymbol) and (cell8 == botSymbol or cell8 == playerSymbol) and (cell9 == botSymbol or cell9 == playerSymbol):
        global drowbool
        drowbool =True
# def main(message):
#     if message.text == "Старт":
# bt1 = telebot.types.KeyboardButton("Позвать")
# bt2 = telebot.types.KeyboardButton("Кто нажмёт тот гей")
# bt3 = telebot.types.KeyboardButton("На случай ссоры")
# bt4 = telebot.types.KeyboardButton("Казино")
# bt5 = telebot.types.KeyboardButton("Анекдот")
# markup = telebot.types.ReplyKeyboardMarkup()
# markup.add(bt1)
# markup.add(bt2)
# markup.add(bt3)
# markup.add(bt4)
# markup.add(bt5)
# @bot.message_handler(commands=['start'])
# def bot_start(message):
#     # сообщение которое отправляет программа нашемо боту по id
#     bot.send_message(message.chat.id, "Дарова")
#     # print(message.chat.id)
    # bot.register_next_step_handler(message, press_play)
# @bot.message_handler(content_types= ["text"])
@bot.message_handler(commands=['call'])

def call(message):
    nick = bot.get_chat_administrators(message.chat.id)
    for i in nick:    
        # print(i.user)  
        # print(mention)
        if i.user.username == None:
            # print(mention)
            mention = f"[{i.user.first_name}](tg://user?id={i.user.id})" 
            # user1 = bot.get_chat_member(message.chat.id, i.user.id)
            # print(user1)
            bot.send_message(message.chat.id, mention, parse_mode = "markdown")
        else:
            bot.send_message(message.chat.id, f"@{i.user.username}")

    # if message.text == "Казино":
    #     # menu_bar2 = telebot.types.ReplyKeyboardMarkup()
    #     # bt_num_bet = telebot.types.KeyboardButton("Скинул")
    #     # menu_bar2.add(bt_num_bet)
    #     bot.send_message(message.chat.id, "Ставку кидай на карту 4149499805473913")
    #     bot.register_next_step_handler(message, choose_num) 

@bot.message_handler(commands=['kazino'])
def kazino_1(message):
        menu_bar = telebot.types.InlineKeyboardMarkup()
        # menu_bar2 = telebot.types.InlineKeyboardButton()
        bt_num_bet = telebot.types.InlineKeyboardButton("Скинул(а)?(только честно отвечай)", callback_data='Скинул?')
        menu_bar.add(bt_num_bet)
        bot.send_message(message.chat.id, "Ставку кидай на карту 4149499805473913", reply_markup=menu_bar)
        bot.register_next_step_handler(message, choose_num) 
def choose_num(message):
    if "Да" in message.text or "Скинул" in message.text or "Ага" in message.text or "да" in message.text or "скинул" in message.text or "ага" in message.text:
            menu_bar1 = telebot.types.InlineKeyboardMarkup()
            number = random.randint(1, 3)
            bt_num1 = telebot.types.InlineKeyboardButton("1", callback_data='1')
            bt_num2 = telebot.types.InlineKeyboardButton("2", callback_data='2')
            bt_num3 = telebot.types.InlineKeyboardButton("3", callback_data='3')
            menu_bar1.add(bt_num1)
            menu_bar1.add(bt_num2)
            menu_bar1.add(bt_num3)
            bot.send_message(message.chat.id, "Угадай число от 1 до 3 которое я загадал (надо написать число в чат)", reply_markup=menu_bar1)
            bot.register_next_step_handler(message, kazino, number)
def kazino(message, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, "Угадал(а), но деньги не отдам")
    else:
        if message.text != "Казино":
            bot.send_message(message.chat.id, "Не в этот раз")
@bot.message_handler(commands=['math_test'])
def start_test(message):
    bot.send_message(message.chat.id, "Тебе делать нечего?")
    bot.register_next_step_handler(message, math_test) 
def math_test(message):
    if "Да" in message.text or "Нечего" in message.text or "Ага" in message.text or "да" in message.text or "нечего" in message.text or "ага" in message.text:
        # test_symbol = "+"
        menu_bar_test = telebot.types.InlineKeyboardMarkup()
        number1 = random.randint(1, 200)
        number2 = random.randint(1, 200)
        operation = random.randint(1, 2)
        if operation == 1:
            test_symbol = "+"
        if operation == 2:
            test_symbol = "-"
        # if operation == 3:
        #     test_symbol = "*"
        # if operation == 4:
        #     test_symbol = ":"
        bt_num_test = telebot.types.InlineKeyboardButton(f"{number1} {test_symbol} {number2}", callback_data='1')
        menu_bar_test.add(bt_num_test)
        bot.send_message(message.chat.id, "Ну ок")
        bot.send_message(message.chat.id, "Тогда решай пример", reply_markup=menu_bar_test)
        bot.register_next_step_handler(message, right_answer, number1, number2, test_symbol)
def right_answer(message, num1, num2, sym):
    # print(num1,num2,sym)
    if sym == "+":
        # print(num1,num2,sym)
        if message.text == str(num1 + num2):
            # print(num1,num2,sym)
            bot.send_message(message.chat.id, "Ну правильно")
        else:
            bot.send_message(message.chat.id, "Неа")
    elif sym == "-":
        if message.text == str(num1 - num2):
            bot.send_message(message.chat.id, "Ну правильно")
        else:
            bot.send_message(message.chat.id, "Неа")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
@bot.message_handler(commands=['cross_zero'])
def cross_zero(message):
    clear()
    bot.send_message(message.chat.id, "Жоские крестики нолики(в разработке)")
    item = {}
    global markup
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    i = 0
    for i in range(9):
        item[i] = telebot.types.InlineKeyboardButton(gameGround[i], callback_data=str(i))
    markup.row(item[0], item[1], item[2])
    markup.row(item[3], item[4], item[5])
    markup.row(item[6], item[7], item[8])
    bot.send_message(message.chat.id, "Ну что, ходи давай", reply_markup=markup)

@bot.callback_query_handler(func= lambda call: True)
def processing_callback(call):
    # print(gameGround)
    item = {}
    if call.message:
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
            # print(randomCell, "111111111")
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
            # print(randomCell, "2222222")
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol
            # print(randomCell)
            # print(randomCell, "333333333333")
        for i in range(9):
            if call.data == str(i):
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol
            win(gameGround[0], gameGround[1], gameGround[2])
            win(gameGround[0], gameGround[4], gameGround[8])
            win(gameGround[0], gameGround[3], gameGround[6])
            win(gameGround[1], gameGround[4], gameGround[7])
            win(gameGround[2], gameGround[5], gameGround[8])
            win(gameGround[2], gameGround[4], gameGround[6])
            win(gameGround[3], gameGround[4], gameGround[5])
            win(gameGround[6], gameGround[7], gameGround[8])
            
            lose(gameGround[0], gameGround[1], gameGround[2])
            lose(gameGround[0], gameGround[4], gameGround[8])
            lose(gameGround[0], gameGround[3], gameGround[6])
            lose(gameGround[1], gameGround[4], gameGround[7])
            lose(gameGround[2], gameGround[5], gameGround[8])
            lose(gameGround[2], gameGround[4], gameGround[6])
            lose(gameGround[3], gameGround[4], gameGround[5])
            lose(gameGround[6], gameGround[7], gameGround[8])
            
            draw(gameGround[0], gameGround[1], gameGround[2],
                 gameGround[3], gameGround[4], gameGround[5],
                 gameGround[6], gameGround[7], gameGround[8])
            item[i] = telebot.types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

   
        global  markup
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        bot.send_message(call.message.chat.id, "Твой ход", reply_markup=markup)
        global winbool
        global losebool
        global drowbool
        if winbool and not losebool and not drowbool:
            clear()
            bot.send_message(call.message.chat.id, "Повезло")

            winbool = False
        if losebool and not winbool and not drowbool:
            clear()
            bot.send_message(call.message.chat.id, "Изи")
            losebool = False
        if drowbool and not losebool and not drowbool:
            clear()
            bot.send_message(call.message.chat.id, "Ничья")
            drowbool = False

            losebool = False
    # print(gameGround)




















@bot.message_handler(commands=['words'])
def change_word_flag(message):
    bot.send_message(message.chat.id, 'Пиши слово')
    global bot_flag
    bot_flag = True
    # print(bot_flag)
    
@bot.message_handler(commands=['conversation'])
def conversation(message):
    bot.send_message(message.chat.id, 'Привет красавчик или красотка')
    global bot_conversation
    bot_conversation = True
    
    
    
    
@bot.message_handler(content_types= ["text"])
    # print(11111111)
def bot_word(message):
    global bot_flag
    global bot_conversation
    if bot_flag:
        # print(11111111111)
        user_city = str(message.text) # пользователь начинает первый и вводит город
        # print(user_city)
        if user_city.lower() == 'стоп': 
            bot.send_message(message.chat.id, 'Я выиграл') # остановка игры 
            bot_flag = False
            b.clear()
        else:
            try:
                for i in all_words_list:
                    # print(i)
                    if i[0].lower() == user_city[-1].lower():
                        #  print(i) 
                         b.append(i) # перебираем все города в списке, если первая буква города из списка равна последней букве введеного пользователем города мы добавляем этот город в список
                        #  print(b)
                    elif user_city[-1].lower() == 'ь' or user_city[-1].lower() == 'ъ' or user_city[-1].lower() == 'й' or user_city[-1].lower() == 'ы' or user_city[-1].lower() == 'ё': 
                         if i[0].lower() == user_city[-2].lower(): 
                            b.append(i) # если город заканчивается на ь,й,ъ,ы сравниваем первую букву с предпоследней
                gorod = random.choice(b) # из полученного списка выбираем рандомом одно подходящее слово
                # print(gorod)
                bot.send_message(message.chat.id, gorod)
                b.clear() # очищаем список 
            except:
                bot.send_message(message.chat.id, "Не в этот раз")
    if not bot_flag and bot_conversation:
        # bot.send_message(message.chat.id, "Митя с др")
            bot_text = random.choice(all_words_list_bot)
            bot.send_message(message.chat.id, bot_text)



bot.polling(none_stop=True)