#!/usr/bin/python3

def get_summ(one, two, delimeter = '@'):
	return str(one) + delimeter + str(two)

# my_summ = get_summ(12, 18)
# print(my_summ)

# my_summ = get_summ("Hello", " World")
# print(my_summ)


my_summ = get_summ("Hello", 25, delimeter ='+')
print(my_summ)

	