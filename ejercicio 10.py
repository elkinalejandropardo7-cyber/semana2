suma = 0
contador = 0

nota = float(input("Ingrese una nota (-1 para terminar): "))

while nota != -1:
    suma += nota
    contador += 1
    nota = float(input("Ingrese una nota (-1 para terminar): "))

if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)
else:
    print("No se ingresaron notas.")