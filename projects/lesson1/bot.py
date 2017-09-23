import datetime
import ephem
from telegram.ext import Updater, CommandHandler,  MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
  updater = Updater("411056163:AAGC7UnsYLHTZk7ZcPbTNUfVwMBhaSen4rk")

  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", greet_user))
  dp.add_handler(CommandHandler("planet", constellation, pass_args = True))
  dp.add_handler(CommandHandler("wc", wc, pass_args = True))
  dp.add_handler(CommandHandler("calc", calc, pass_args = True))
  dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
  updater.start_polling()
  updater.idle()

def greet_user(bot, update):
  text = 'Вызван /start'
  print(text)
  update.message.reply_text(text)



def constellation(bot, update, args):
  planets = {
    'марс': ephem.Mars,
    'венера' : ephem.Venus,
    'юпитер' : ephem.Jupiter,
    'меркурий' : ephem.Mercury,
    'сатурн' : ephem.Saturn,
    'уран' : ephem.Uranus,
    'нептун' : ephem.Neptune
  }

  user_text = update.message.text
  if len(args) > 0:
        user_text = args[0].lower()
        now = datetime.datetime.now()
        planet = planets.get(user_text)
        if planet:
          answer = ephem.constellation(planet(str(now)))
          update.message.reply_text(answer[1])
        else:
          update.message.reply_text('Это такая планета?')
  else:
    update.message.reply_text('Надо ввести  название планеты!')



def wc(bot, update, args):
  if len(args) > 0:
    update.message.reply_text('Слов в такой фразе: {}'.format(args, len(args)))
  else:
    update.message.reply_text('Нужно ввести фразу!')


def calc(bot, update, args):
  if len(args) > 0:
    cmd = ''.join(args)
    answer = None
    try:
      if cmd.find('+') != -1:
        args_list = cmd.split('+')
        if len(args_list) == 2:
            answer = int(args_list[0]) + int(args_list[1])
      elif cmd.find('-') != -1:
        args_list = cmd.split('-')
        if len(args_list) == 2:
            answer = int(args_list[0]) - int(args_list[1])
      elif cmd.find('/') != -1:
        args_list = cmd.split('/')
        if len(args_list) == 2:
            try:
                answer = int(args_list[0]) / int(args_list[1])
            except ZeroDivisionError:
                answer = 'На ноль не делим!'
      elif cmd.find('*') != -1:
        args_list = cmd.split('*')
        if len(args_list) == 2:
            answer = int(args_list[0]) * int(args_list[1])
      else:
        answer = 'Так не считают'
      if answer == None:
        answer = 'Два числа нужно!'
    except (ValueError, TypeError):
      answer = 'Это мы не посчитаем' 
    update.message.reply_text(str(answer))
  else:
    update.message.reply_text('Так мы вообще ничего не посчитаем!')


def talk_to_me(bot, update):
  user_text = update.message.text 
  print(user_text)
  update.message.reply_text(user_text)    


main()