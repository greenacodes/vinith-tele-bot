import os
import telebot

VINI = "5096203460:AAHqA0-BLCIv9IimbzASaXRJRaV9eozNAWw"
bot = telebot.TeleBot(VINI)


@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "HEY iam a bot...")


@bot.message_handler(commands=['hello'])
def greet(message):
    bot.reply_to(message, "hy there!")


@bot.message_handler(commands=['Age'])
def greet(message):
    bot.reply_to(message, "I was made on 25 JAN 2022")


# @bot.message_handler(commands=['❤'])
def greet(message):
    bot.reply_to(message, "Laddu😘")


@bot.message_handler(commands=['Name'])
def greet(message):
    bot.reply_to(message, "Programmer")


@bot.message_handler(commands=['Likes'])
def greet(message):
    bot.reply_to(message, "Coding , Hacking")


@bot.message_handler(commands=['Education'])
def greet(message):
    bot.reply_to(message, "Diploma in CSE at warangal")


@bot.message_handler(commands=['Love'])
def greet(message):
    bot.reply_to(message, "Yes, I ALWAYS LOVE YOU ❤")



    
@bot.message_handler(commands=['Instagram'])
def greet(message):
    bot.reply_to(message, "http://www.instagram.com/vinithreddybanda/")
    
@bot.message_handler(commands=['Linkedin'])
def greet(message):
    bot.reply_to(message, "https://www.linkedin.com/in/vinith-reddy-banda-4aa52122a")
    
 


bot.polling()
