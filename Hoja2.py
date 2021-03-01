#a)
n= int(input("Altura del triangulo:  "))
for i in range(n):
    for j in range(i+1):
         print("*", end="")
    print("")


#b)
n = int(input("Numero : "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")