def dividir_numeros():
    try:
        # 1. Solicitar datos al usuario
        print("--- Inicio de la División ---")
        num1_raw = input("Introduce el primer número (dividendo): ")
        num2_raw = input("Introduce el segundo número (divisor): ")
        
        # 2. Convertir entradas a enteros
        num1 = int(num1_raw)
        num2 = int(num2_raw)
        
        # 3. Realizar la división
        resultado = num1 / num2
        
        # 4. Mostrar el resultado
        print(f"El resultado es: {resultado}")
        return resultado

    except ValueError:
        # Se activa si el usuario mete letras o deja vacío
        print("Error: Debes introducir un número válido")
        
    except ZeroDivisionError:
        # Se activa si el usuario intenta dividir por 0
        print("Error: No es posible dividir entre cero")
        
    finally:
        # Este mensaje sale pase lo que pase
        print("Operación finalizada")

if __name__ == "__main__":
    dividir_numeros()