# Translation
# by hoanghust

s = input()
t = input()
t_reverse = ""

for i in range(len(t)):
		t_reverse += t[-1-i]

if s == t_reverse:
	print("YES")
else:
	print("NO")