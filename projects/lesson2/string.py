#! /usr/bin/python3

def str_cmp(first_string, second_string):
	first_string_length, second_string_length = len(first_string), len(second_string)
	if first_string == second_string:
	  return 1
	elif first_string != second_string and first_string_length > second_string_length and second_string != "learn":
	  return 2
	elif first_string != second_string and second_string == "learn":
	  return 3  
	else:
		return 4


print (str_cmp('qwerty', 'qwerty'))		
print (str_cmp('qwerty', 'qwer4y'))		
print (str_cmp('qwertyqwerty', 'qwer4y'))		
print (str_cmp('qwerty', 'learn'))		
print (str_cmp('qwerty', 'learn'))	