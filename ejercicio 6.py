while True:
    Tipo = input("Ingrese su tipo de documento (CC, TI, CE): ")
    if Tipo == "CC":
        print("Seleccionaste Cédula de Ciudadanía")
        break
    elif Tipo == "TI":
        print("Seleccionaste Tarjeta de Identidad")
        break
    elif Tipo == "CE":
        print("Seleccionaste Cédula de Extranjería")
        break
    else:
        print("Opción equivocada, intente de nuevo")