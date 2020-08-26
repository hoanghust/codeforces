# A. Word
# by hoanghust

s = input()
lowercase_num = 0
uppercase_num =0

for letter in s:
	if letter.islower():
		lowercase_num += 1
	else:
		uppercase_num += 1
		
if lowercase_num >= uppercase_num:
	s = s.lower()
else:
	s = s.upper()
	
print(s)
	
		