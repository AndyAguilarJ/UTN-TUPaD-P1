from statistics import mode, median, mean
from random import randint
//1
edad = int(input("Ingrese su edad:"))
if edad > 18:
	print("Es mayor de edad")
//2
nota = int(input("Ingrese nota:"))
if edad >= 6:
	print("Aprodado")
else:
	print("Desaprobado")

//3
num = float(input("Ingrese un numero:"))
div = num % 2
if div != 0:
	print("numero no par")
else:
	print("numero par")

//4
edad = int(input("Ingrese su edad: "))
if edad < 12:
	print("Es menor de 12")
elif edad > 12 and edad < 18:
	print("Es adolecente")
elif edad >= 18 and edad < 30:
	print("Es adulto joven")
else:
	print("mayor")
//5
contraseña = input("Ingrese su contraseña(entre 8 y 14 caracteres): ")
if len(contraseña) < 8 or len(contraseña) > 14:
	print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
	print("Ha ingresado una contraseña correcta")
//6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
	print("Sin sesgo (simétrica)")
else:
    print("No se puede determinar un sesgo claro.")
//7
string_user = input("ingrese una frase o palabra")

ultima_letra = string_user[-1].lower()

return ultima_letra if ultima_letra in 'aeiou' else palabra
//8
nombre = input("ingrese su nombre: ")
seleccion = int(input("ingrese un numero entre el 1 y el 3(1: mayusculas, 2:minusculas, 3:capitalizado): "))

if seleccion == 1:
	return nombre.upper()
elif seleccion == 2:
	return nombre.lower()
elif seleccion == 3:
	return nombre.title()
else:
	("selecion erronea")
//9 
magnitud = float(input("ingrese la magnitud del terremoto: "))


if magnitud < 0:
    return "no puede ser negativo el valor"
elif magnitud <= 3:
	return "Muy leve (imperceptible)"
elif magnitud < 4 or magnitud >= 3:
    return "Leve (ligeramente perceptible)"
elif magnitud < 5 or magnitud >= 6:
    return "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud < 6 or magnitud >= 7:
    return "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud < 7 magnitud >= 8:
    return "Muy Fuerte (puede causar daños significativos)"
else:
    return "seleccion erronea"

//10
hemisferio = input("Ingrese el hemisferio (N/S): ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if not (1 <= mes <= 12 and 1 <= dia <= 31):
        return "Error: Mes o día inválido"
    
    # Determinar la estación según el hemisferio
    if hemisferio.upper() == 'N':
        # Hemisferio Norte
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            return "Invierno"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            return "Verano"
        else:
            return "Otoño"
    elif hemisferio.upper() == 'S':
        # Hemisferio Sur (invierte las estaciones)
        if (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            return "Invierno"
        elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
            return "Primavera"
        elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            return "Verano"
        else:
            return "Otoño"
    else:
        return "Error: Hemisferio debe ser 'N' o 'S'"


