#!/usr/bin/python3

# while True:
#   user_say = input('Скажи что-нибудь: ')
#   if user_say == 'Пока':
#     print('Ну пока')
#     break
#   else:
#     print('Сам ты {}'.format(user_say))



my_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


while True:
  if my_names.pop() == "Валера":
  	print("Валера нашелся!")
  	break

