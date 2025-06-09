def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero no negativo: "))
            if numero < 0:
                print("Error: el número debe ser no negativo. Intente de nuevo.\n")
            else:
                fact = factorial(numero)
                print(f"El factorial de {numero} es: {fact}")
                break  # Salir del bucle si todo fue correcto
        except ValueError:
            print("Error: debe ingresar un número entero válido. Intente de nuevo.\n")

main()
