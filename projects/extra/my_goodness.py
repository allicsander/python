# print("Hello, World!")

a, b = 70, 1
if a < b:
	print('a ({}) is less than b ({})'.format(a, b))
else:
	print('a ({}) is not less than b ({})'.format(a, b))


print("yes" if a < b else "no")


# loops

fh = open("lines.txt")
for line in fh.readlines():
  print(line, end="")


# functions 
def isprime(n):
	for n in range(1, n):
		print(n)


isprime(15)

