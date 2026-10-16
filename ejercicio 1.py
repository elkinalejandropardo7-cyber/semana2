while True :
        print("---bienvenido al menu---")
        print("1. Consulta")
        print("2. Registrar")
        print("3. Salir")
        
        respuesta = int( input("seleccione una opcion"))
        if respuesta ==1 :
            print("Usted selecciono Consulta")
        elif respuesta ==2 :
            print("Usted selecciono Registrar")
        elif respuesta ==3 :
            print("Usted selecciono Salir")
            break
        else :
            print("opcion equivocado")