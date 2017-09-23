wc =0
with open('referat.txt', 'r', encoding='utf-8') as f:
  for line in f:
  	wc += len(line.split())
  	print(line)
print ("\n\nСлов в тексте: " + str(wc) +"\n")