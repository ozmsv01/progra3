print ("______________________________________")
print("Lista - sumar todos")
print ("______________________________________")
#solicitar un numero final de la lista
num1=int(input("Ingrese un numero hasta 100: "))

#crea la lista desde 1 hasta el $num1
lista = list(range(1, num1+1))

#Calcular la suma
resutado=sum(lista)

#imprimir el resultado
print(f"La suma de la lista hasta {num1} es {resutado}")















