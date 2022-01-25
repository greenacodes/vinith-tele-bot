import os

import telebot

VINI = "5090152545:AAEu4gt5cgPwDi7VRFVzJmZZBPyzskzOn2M"

bot = telebot.TeleBot(VINI)





@bot.message_handler(commands=['command1'])

def greet(message):

  bot.reply_to(message,"HEY iam a bot...")





@bot.message_handler(commands=['command2'])

def greet(message):

  bot.reply_to(message,"hy there!")





@bot.message_handler(commands=['command3'])

def greet(message):

  bot.reply_to(message,"I was created on 25 JAN 2022")





@bot.message_handler(commands=['command4'])

def greet(message):

  bot.reply_to(message," I love Laddu😘")









@bot.message_handler(commands=['command5'])

def greet(message):

  bot.reply_to(message,"Hey Iam a Programmer")







@bot.message_handler(commands=['command6'])

def greet(message):

  bot.reply_to(message,"I love Coding , Hacking")





@bot.message_handler(commands=['command7'])

def greet(message):

  bot.reply_to(message,"diploma in CSE at warangal")





@bot.message_handler(commands=['command8'])

def greet(message):

  bot.reply_to(message,"Yes, I ALWAYS LOVE YOU ❤")





@bot.message_handler(commands=['command9'])

def greet(message):

  bot.reply_to(message,"A girl who can create a tele bot")



@bot.message_handler(commands=['command9'])

def greet(message):

  bot.reply_to(message,"A girl who can create a tele bot")



bot.polling()
