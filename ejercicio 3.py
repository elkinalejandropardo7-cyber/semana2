clave_correcta = 1234
intentos = 0

while intentos < 3:
    clave = int(input("Ingrese la contraseña: "))

    if clave == clave_correcta:
        print("Acceso concedido")
        break
    else:
        intentos = intentos + 1
        print("Contraseña incorrecta")

if intentos == 3 and clave != clave_correcta:
    print("Cuenta bloqueada")