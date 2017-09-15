#!/usr/bin/python3

def answer(question):
	answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	return answers.get(question).lower()


print(answer("привет"))
print(answer("как дела"))
print(answer("пока"))
print(answer("hola"))