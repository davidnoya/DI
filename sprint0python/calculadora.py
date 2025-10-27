from operaciones import suma, resta, multiplicacion, division

def main():
    while True:
        try:
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
        except ValueError:
            print("Introduce dos números válidos.")
            continue

        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            print("Resultado: " + str(suma(num1, num2)))
        elif opcion == "2":
            print("Resultado: " + str(resta(num1, num2)))
        elif opcion == "3":
            print("Resultado: " + str(multiplicacion(num1, num2)))
        elif opcion == "4":
            print("Resultado: " + str(division(num1, num2)))
        else:
            print("Opción no válida.")

        continuar = input("¿Quieres hacer otra operación? (s/n): ")
        if continuar != "s":
            print("Fin del programa")
            break

if __name__ == "__main__":
    main()
