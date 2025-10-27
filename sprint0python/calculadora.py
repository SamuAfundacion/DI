from sprint0python import operaciones

def calculadora():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Debes introducir números válidos.")
            continue

        while True:
            print("=" * 40)
            print("\nEscoge una operación")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Salir")
            print("=" * 40)

            try:
                opcion = int(input("Elige la operación (1/2/3/4/5): "))
            except ValueError:
                print("Debes introducir un número del 1 al 5.")
                continue

            if opcion == 1:
                resultado = operaciones.suma(num1, num2)
            elif opcion == 2:
                resultado = operaciones.resta(num1, num2)
            elif opcion == 3:
                resultado = operaciones.multiplicacion(num1, num2)
            elif opcion == 4:
                resultado = operaciones.division(num1, num2)
            elif opcion == 5:
                break
            else:
                print("Opción no válida.")
                continue

            print(f"\n -- El resultado es: {resultado}\n")

        while True:
            seguir = input("\n¿Quieres introducir nuevos números? (S/N): ").strip().lower()
            if seguir in ("s", "n"):
                break
            else:
                print("Introduce 'S' o 'N'.")

        if seguir == "n":
            print("Hasta pronto!")
            break


if __name__ == "__main__":
    calculadora()
