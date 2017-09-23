#! /usr/bin/python3

age = int(input("Введите ваш возрас: "))

if age < 7:
  print ("В детский сад")
elif age < 17:
  print ("В школу")
elif age < 22:
  print ("В ВУЗ")
else:
  print ("На работу")