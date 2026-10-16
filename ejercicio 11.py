n = int(input("Ingrese un numero entero positivo: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("El factorial es:", factorial)