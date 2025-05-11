import random
//1

for i in range(2,22,2):
	print(i)

for i in range(3,22,2)
	print(i)


//2
inicio = int(input("Introduce el primer número: "))

fin = int(input("Introduce el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio  # Intercambiar valores si están en orden inverso
suma = 0

for numero in range(inicio + 1, fin):
    suma += numero

print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")

//3
suma_total = 0
print("Introduce números enteros para sumarlos. Introduce 0 para terminar.")
while True:
    numero = int(input("Ingresa un número: "))
    
    if numero == 0:
        break  # Salir del bucle si el número es 0

    suma_total += numero
print(f"La suma total de los números ingresados es: {suma_total}")

//4
# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Adivina el número entre 0 y 9!")

while True:
    intento = int(input("Introduce tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! El número era {numero_secreto}.")
        print(f"Lo lograste en {intentos} intento(s).")
        break
    else:
        print("No es correcto. Intenta de nuevo.")
//5

print("Números pares del 100 al 0 en orden decreciente:")
for numero in range(100, -1, -2):  # Desde 100 hasta 0, saltando de 2 en 2
    print(numero)

//6

limite = int(input("Introduce un número entero positivo: "))

# Validar que el número sea positivo
if limite <= 0:
    print("Por favor, introduce un número entero mayor que 0.")
else:
    suma = 0
    for numero in range(0, limite):  # Excluye el número límite
        suma += numero

    print(f"La suma de los números entre 0 y {limite} (excluyendo {limite}) es: {suma}")

//7

# Puedes cambiar esta cantidad para probar con menos números
CANTIDAD_NUMEROS = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Introduce {CANTIDAD_NUMEROS} números enteros:")

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i+1}: "))
    
    # Par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impar = 1
        impares += 1

    # Positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # Los ceros no se cuentan como positivos ni negativos

# Mostrar resultados
print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

//8

CANTIDAD_NUMEROS = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Introduce {CANTIDAD_NUMEROS} números enteros:")
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impar = 1
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

//9
CANTIDAD_NUMEROS = 100
suma_total = 0
print(f"Introduce {CANTIDAD_NUMEROS} números enteros:")
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i+1}: "))
    suma_total += numero
media = suma_total / CANTIDAD_NUMEROS
print(f"\nLa media de los {CANTIDAD_NUMEROS} números es: {media}")

//10

numero = input("Ingresa un número entero: ")
if numero.startswith('-'):
    numero_invertido = '-' + numero[:0:-1]
else:
    numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")
