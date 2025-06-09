def decimal_a_binario(n):
    binario = ""
    if n == 0:
        return "0"
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero < 0:
                print("Error: el número debe ser positivo. Intente de nuevo.\n")
            else:
                binario = decimal_a_binario(numero)
                print(f"El número {numero} en binario es: {binario}")
                break
        except ValueError:
            print("Error: debe ingresar un número entero válido. Intente de nuevo.\n")

main()
