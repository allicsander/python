#!/usr/bin/python3

# def cut_cake(parts):
#   try:
#     return 1/parts
#   except ZeroDivisionError:
#   	return 'С ума посходили'

# print(cut_cake(5)) 
# print(cut_cake(0))  	







def ask_user():
	while True:
		try:
		  if "Хорошо"== input("Как дела?\n"):
			  break
		except KeyboardInterrupt:
			print("\nit's time to stop. it's not OK")
			break
        



ask_user()



