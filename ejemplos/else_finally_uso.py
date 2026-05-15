try:
    archivo = open("prueba.txt", "w")
    archivo.write("Escribiendo datos de prueba...")
except IOError:
    print("Error al manejar el archivo.")
else:
    print("El archivo se escribió correctamente.")
finally:
    archivo.close()
    print("Archivo cerrado y recursos liberados.")