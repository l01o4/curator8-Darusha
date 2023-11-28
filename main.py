import telebot

bot = telebot.TeleBot('6974693729:AAGj6BK_dAIaKgVZkj8XT_wzsAbcE0M4h7I')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Мяу, я бот-абормот! Помурчим о жизни?', parse_mode='Markdown')


@bot.message_handler(commands=['cat'])
def main(message):
    bot.send_message(message.chat.id, '''
╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈
┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈
┈┃┃╱▔▔▔  ▏╱▋▋╮┈
┈┃╰▏┃╱╭╮┃╱╱  ╱╱▆┃┈
┈╰━▏┗━╰╯┗━╱╱╱ ╰┻┫┈
┈┈┈▏┏┳━━━━▏┏┳━━╯┈
┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈
 ''', parse_mode='Markdown')


@bot.message_handler(commands=['meow'])
def main(message):
    bot.send_message(message.chat.id, '_люблю тебя)_', parse_mode='Markdown')


bot.infinity_polling()