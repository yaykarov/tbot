import telebot
from telebot import types

bot = telebot.TeleBot('5177442169:AAEYhRptsZytItX_19pMXgE_8ADVaFzMOvQ')
@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

if __name__ == "__main__":
	bot.infinity_polling()