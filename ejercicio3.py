def suma_digitos_potencia(base, exponente):
    resultado = base ** exponente
    suma = sum(int(digito) for digito in str(resultado))
    return suma

def main():
    while True:
        try:
            base = int(input("Ingrese la base (entero positivo): "))
            exponente = int(input("Ingrese el exponente (entero positivo): "))
            
            if base < 0 or exponente < 0:
                print("Error: ambos valores deben ser enteros positivos. Intente de nuevo.\n")
            else:
                suma = suma_digitos_potencia(base, exponente)
                print(f"{base}^{exponente} = {base ** exponente}")
                print(f"La suma de los dígitos del resultado es: {suma}")
                break
        except ValueError:
            print("Error: debe ingresar valores numéricos enteros válidos. Intente de nuevo.\n")

main()
