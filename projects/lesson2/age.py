#! /usr/bin/python3

age = input("Введите ваш возрас: ")

age = int(age)

if age < 7:
  print ("В детский сад")
elif age < 17:
  print ("В школу")
elif age < 22:
  print ("В ВУЗ")
else:
  print ("На работу")