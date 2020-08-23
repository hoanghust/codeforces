# A. Coins
# by hoanghust

inputs = input()
inputs = inputs.split()
for i, input_ in enumerate(inputs):
    inputs[i] = int(input_)

max_coin = inputs[0]
sum_coins = inputs[1]

sum_tmp = 0
remainder = sum_coins - sum_tmp
count = 0

while sum_tmp < sum_coins:
    count += int(remainder/max_coin)
    remainder = remainder % max_coin
    sum_tmp = sum_coins - remainder
    max_coin -= 1
    
print(count)
