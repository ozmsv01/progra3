# Definir la función para calcular el número
def positivo_negativo(num):
    # Verificamos si el número es positivo, negativo o cero
    if num > 0:
        return ("El número es positivo")
    elif num < 0:
        return ("El número es negativo")
    else:
        return ("El número es 0")

# Solicitar el número al usuario
num = int(input("Introduce un número para calcular: "))
# Mostrar el resultado llamando a la función
print(f"El {num} es {positivo_negativo(num)}")

