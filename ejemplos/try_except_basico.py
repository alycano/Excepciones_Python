try:
    numero = int(input("Introduce un número para dividir 100: "))
    print(f"Resultado: {100 / numero}")
except ValueError:
    print("Error: ¡Eso no es un número!")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")