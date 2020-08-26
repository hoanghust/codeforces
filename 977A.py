# Wrong subtraction
# by hoanghust

inputs = input()
inputs = inputs.split()

for num, input_ in enumerate(inputs):
	inputs[num] = int(input_)

n = inputs[0]
k = inputs[1]
for i in range(k):
	if n%10==0:
		n = int(n/10)
	else:
		n=n-1
print(n)