#! /usr/bin/python3

mylist = ['Петя', 'Маша', 'Саша', 'Настя', 'Настя']

print(mylist)
print(mylist[:2])

print(mylist.index("Петя"))

mylist.sort()

print(mylist)
print(mylist.index("Петя"))

print ("Настя" in mylist)

my_numbers = [2,3,4,5,6,7]

print (my_numbers)
#print (type(my_numbers))

my_numbers.append("Python")
print (my_numbers)


print (my_numbers[0], my_numbers[len(my_numbers)-1])

# со ворого по четвертый 
print (my_numbers[1:4])

print (len(my_numbers))

print ('index of 6 is:' + str(my_numbers.index(6)))

my_numbers.remove("Python")

print (my_numbers)