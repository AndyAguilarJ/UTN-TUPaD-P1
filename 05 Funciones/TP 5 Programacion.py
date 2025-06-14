import math

# 1. Hola mundo
def imprimir_hola_mundo():
	print("hola mundo")

# 2. Saludo
def saludar_usuario(nombre):
	print("hola ", nombre)

# 3. Info personal
def informacion_personal(nombre, apellido, edad, residencia):
	
	print("soy " + nombre +" " + apellido + " tengo "+ edad + " años y vivo en" + residencia)

# 4. Área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida"
    return (suma, resta, multiplicacion, division)

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# PROGRAMA PRINCIPAL
def main():
    # Punto 4
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

    # Punto 5
    segundos = int(input("\nIngrese la cantidad de segundos: "))
    print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

    # Punto 6
    numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # Punto 7
    a = float(input("\nIngrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = operaciones_basicas(a, b)
    print(f"Suma: {resultado[0]}")
    print(f"Resta: {resultado[1]}")
    print(f"Multiplicación: {resultado[2]}")
    print(f"División: {resultado[3]}")

    # Punto 8
    peso = float(input("\nIngrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")

    # Punto 9
    celsius = float(input("\nIngrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}")

    # Punto 10
    num1 = float(input("\nIngrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio es: {promedio:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
