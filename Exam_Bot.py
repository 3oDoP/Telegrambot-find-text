import telebot
bot = telebot.TeleBot('TOKEN') #Add you Telegram Bot token
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Write a question or part of a question, and I'll try to find an answer to it. You need to write without dots, but with commas and dashes (if there are any).")
@bot.message_handler()
def get_user_text(message):
    with open('YOU FILE WITH ANSWER.txt', 'r', encoding='utf-8') as file: #Specify the path to the file .txt , end each answer with the characters <****>
        text = file.read()
        s1 = str(message.text)
        if s1 in text:
            indexes = text.index(s1)
            indexes2 = text.index('****', indexes)
            super = text[indexes:indexes2]
            if len(super) > 4096:
                for x in range(0, len(super),4096):
                    bot.send_message(message.chat.id, super[x:x + 4096])
            else:
                bot.send_message(message.chat.id, super)
        else:
            bot.send_message(message.chat.id, "You wrote the question incorrectly, you need to write with a capital letter, as accurately as possible, with dots, dashes and commas")
            bot.send_message(message.chat.id,"Example: Market infrastructure is a set of legal forms mediating the movement of goods and services, acts of purchase and sale, or a set of institutions, systems, services, enterprises serving the market and performing certain functions to ensure the normal mode of its functioning.")
bot.polling(none_stop=True)