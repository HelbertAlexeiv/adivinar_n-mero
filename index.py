from random import randrange

print("Adivina el número")
num_user = int(input("Ingrese un número: "))
num_random = randrange(1, 1000, 2)
print(num_random)

while num_user != num_random:
    
    if num_user < num_random:
        print("El número es más grande")
    else: 
        print("El número es más pequeño")
    
    num_user = int(input("Ingrese un número: "))

print("Felicidades adivinaste el número")
