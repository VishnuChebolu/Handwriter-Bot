import telebot
import os
from dotenv import load_dotenv
import pywhatkit



load_dotenv()

api = os.getenv('API_KEY')
bot = telebot.TeleBot(api)

#comments
@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Send some random text, I'll convert it into handwriting'''
    bot.reply_to(message, msg)

@bot.message_handler(commands = ['help'])
def greet(message):
    msg = ''' This is a handwriter bot\nSend some random text, I'll convert it into handwriting'''
    bot.reply_to(message, msg)

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.reply_to(message, "Converting to Handwriting, wait for sometime :)")
    pywhatkit.text_to_handwriting(message.text,"text1.png")
    bot.send_photo(message.chat.id, photo=open('text1.png', 'rb'))

if __name__ == '__main__':
    bot.polling() 