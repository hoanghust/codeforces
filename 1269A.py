# A. Equation
# by hoanghust

n = int(input())
if n >= 1 and n <= pow(10,7):
    a = 9*n
    b = 8*n
    if a >= 2 and a <= pow(10,9) and b >= 2 and b <= pow(10,9):
        print(a,b)

