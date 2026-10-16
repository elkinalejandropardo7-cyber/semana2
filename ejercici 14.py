def generar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def main():
    try:
        n = int(input("Ingrese la cantidad de términos (N) que desea visualizar: "))
        if n <= 0:
            print("Por favor, ingrese un número entero mayor que 0.")
        else:
            resultado = generar_fibonacci(n)
            print(", ".join(map(str, resultado)))
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()