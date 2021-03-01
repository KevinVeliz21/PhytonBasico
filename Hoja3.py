#A) Escribir un programa que almacene la cadena de caracteres contraseña en una variable, ingresada por el usuario, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
L = "Phyto"
password =""
while password != L:
    password = input("Introduzca la contraseña correcta: ")
print("Contraseña correcta")


#B)
n = input("¿Nombre? ")
gender = input("¿Cuál es tu sexo  M o F? ")
if (gender == "M" and n.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)