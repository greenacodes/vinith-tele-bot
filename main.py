import os
import telebot
from keep_alive import keep_alive
VINI = "5096203460:AAHqA0-BLCIv9IimbzASaXRJRaV9eozNAWw"
bot = telebot.TeleBot(VINI)


@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "HEY iam a bot...")


@bot.message_handler(commands=['hello'])
def greet(message):
    bot.reply_to(message, "hy there!")


@bot.message_handler(commands=['age'])
def greet(message):
    bot.reply_to(message, "I was made on 25 JAN 2022")


# @bot.message_handler(commands=['laddu'])
def greet(message):
    bot.reply_to(message, "Laddu😘")


@bot.message_handler(commands=['name'])
def greet(message):
    bot.reply_to(message, "Programmer")


@bot.message_handler(commands=['likes'])
def greet(message):
    bot.reply_to(message, " I ❤ Coding")


@bot.message_handler(commands=['education'])
def greet(message):
    bot.reply_to(message, "Diploma in CSE at warangal")


@bot.message_handler(commands=['love'])
def greet(message):
    bot.reply_to(message, "Yes, I ALWAYS LOVE YOU ❤")



    
@bot.message_handler(commands=['instagram'])
def greet(message):
    bot.reply_to(message, "http://www.instagram.com/vinithreddybanda/")
    
@bot.message_handler(commands=['linkedin'])
def greet(message):
    bot.reply_to(message, "https://www.linkedin.com/in/vinith-reddy-banda-4aa52122a")
    
 
keep_alive()

bot.polling()
