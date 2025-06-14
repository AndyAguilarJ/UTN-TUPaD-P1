def factorial(n):
    if n == 0 or n == 1:
        return n
    else: 
        return n * factorial(n-1)
    
    for i in range(n):
        print(f"Factorial de {i} es: {factorial(i)}")


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    return base * potencia(base, exponente - 1)

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    # Si es par, agrego 0 al final
    if n % 2 == 0:
        return decimal_a_binario(n // 2) + "0"
    # Si es impar, agrego 1 al final
    return decimal_a_binario(n // 2) + "1"

def es_palindromo(palabra):
    # Casos base
    if len(palabra) <= 1:
        return True
    
    # Si los caracteres en los extremos son diferentes, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    
    # Recursión con la palabra sin los extremos
    return es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    if numero < 10:
        return 1 if numero == digito else 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

if __name__ == "__main__":
    n = 5
    factorial(n)
    print(f"Factoriales desde 1 hasta {n}:")
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")
    
    num = 10
    fibonacci(num)
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci(i)}")

    base = 2
    exp = 4
    potencia(base,exp)
    print(f"{base}^{exp} = {potencia(base, exp)}")

    num = 10
    print(f"Número decimal: {num}")
    print(f"Representación binaria: {decimal_a_binario(num)}")

    palabras = ["ana", "python", "radar", "oso", "refer"]
    print("Verificación de palíndromos:")
    for palabra in palabras:
        print(f"'{palabra}': {es_palindromo(palabra)}")

    numeros = [1234, 9, 305, 1000]
    print("Suma de dígitos:")
    for num in numeros:
        print(f"Suma de dígitos de {num}: {suma_digitos(num)}")

    ejemplos = [
    (12233421, 2),
    (5555, 5),
    (123456, 7)
    ]
    print("Conteo de dígitos específicos:")
    for numero, digito in ejemplos:
        print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")


