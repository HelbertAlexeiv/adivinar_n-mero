# Ejercicio Adivina el número 
Hacer un programa que genere un número aleatorio sin un rango en concreto

## Análisis:
Usando la libreria random se genera un número aleatorio, este número será comparado con uno introducido por el usuario, esta es la condicion para que salga del bucle si la condicion no se cumple 
se evalua que tan cerca esta el usurio de adivinar el número.

## Diseño:
![diagrama](diagrama_adivina_número.png)

## Construccion
```python
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
```
