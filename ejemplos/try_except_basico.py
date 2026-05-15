try:
    numero = int(input("Introduce un numero para dividir 100: "))
    print(f"Resultado: {100 / numero}")
except ValueError:
    print("Error: ¡Eso no es un numero!")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")