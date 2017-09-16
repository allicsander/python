#!/usr/bin/python3

# while True:
#   user_say = input('Скажи что-нибудь: ')
#   if user_say == 'Пока':
#     print('Ну пока')
#     break
#   else:
#     print('Сам ты {}'.format(user_say))



def find_person(name):
  while True:
    if my_names.pop() == name:
  	  print("{} нашелся!".format(name))
  	  break

my_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


find_person("Вася")

def ask_user():
	while True:
		if "Хорошо"== input("Как дела?\n"):
			break

ask_user()

