# A. Hulk
# by hoanghust

n = int(input())

str1 = "that I love"
str2 = "that I hate"

ls = ["I", "hate", "it"]
index = 2

if n >= 2:
    for i in range(n-1):
        if i % 2 == 0:
            ls.insert(index, str1)
        else:
            ls.insert(index, str2)   
        index += 1  

result = " ".join(ls)
print(result)   
